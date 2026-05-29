#!/usr/bin/env python3
"""Create a DevLoop product improvement idea as a GitHub Issue.

Modes:
- manual: read a human/Codex-drafted idea from DEVLOOP_IDEA_* variables.
- api: ask one low-cost OpenAI model call for one safe, small idea.

The script uses only the Python standard library so GitHub Actions can run it
without installing repository dependencies.
"""

from __future__ import annotations

import hashlib
import json
import os
import sys
import textwrap
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
GITHUB_API = "https://api.github.com"
OPENAI_API = "https://api.openai.com/v1/chat/completions"
PROMPT_PATH = ROOT / "scripts" / "ai" / "prompts" / "unified_employee.md"
IDEA_FIELDS = ("title", "problem", "rationale", "scope", "non_goals", "risks", "validation")
DEFAULT_CONTEXT_FILES = (
    "PRODUCT.md",
    "README.md",
    "AI_POLICY.md",
    "AGENTS.md",
    "docs/development.md",
    "docs/architecture.md",
    "docs/search-design.md",
    "docs/search-evaluation.md",
    "docs/source-collection-strategy.md",
    "docs/scheduler.md",
    "docs/devloop-runner.md",
)
FORBIDDEN_SCOPE_TERMS = (
    "authentication",
    "authorization",
    "login",
    "permission",
    "billing",
    "payment",
    "subscription",
    "database migration",
    "db migration",
    "alembic",
    "terraform apply",
    "terraform import",
    "terraform state",
    "infrastructure provisioning",
    "production deployment",
    "deployment configuration",
    "secret",
    "secrets",
    "automatic merge",
    "auto merge",
    "main branch push",
)


def env(name: str, default: str | None = None) -> str | None:
    value = os.environ.get(name)
    if value is None or value == "":
        return default
    return value


def require_env(name: str) -> str:
    value = env(name)
    if not value:
        raise RuntimeError(f"{name} is required.")
    return value.strip()


def load_env_file_if_needed() -> None:
    if env("OPENAI_API_KEY"):
        return

    env_file = ROOT / env("DEVLOOP_ENV_FILE", ".env.devloop")
    if not env_file.exists():
        return

    for line in env_file.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or "=" not in stripped:
            continue
        key, value = stripped.split("=", 1)
        key = key.strip()
        if key == "OPENAI_API_KEY" and not env(key):
            os.environ[key] = value.strip().strip('"').strip("'")


def github_request(
    method: str,
    path: str,
    token: str,
    payload: dict[str, Any] | None = None,
) -> dict[str, Any] | list[Any]:
    data = None if payload is None else json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(
        f"{GITHUB_API}{path}",
        data=data,
        method=method,
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "X-GitHub-Api-Version": "2022-11-28",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            raw = response.read().decode("utf-8")
            return {} if not raw else json.loads(raw)
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"GitHub API {method} {path} failed: HTTP {exc.code}: {body}") from exc


def openai_request(payload: dict[str, Any]) -> dict[str, Any]:
    load_env_file_if_needed()
    api_key = require_env("OPENAI_API_KEY")
    request = urllib.request.Request(
        OPENAI_API,
        data=json.dumps(payload).encode("utf-8"),
        method="POST",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"OpenAI API request failed: HTTP {exc.code}: {body}") from exc


def read_limited_file(path: Path, max_chars: int) -> str:
    text = path.read_text(encoding="utf-8", errors="replace")
    if len(text) <= max_chars:
        return text
    return text[:max_chars] + "\n\n[truncated]\n"


def read_repo_context() -> str:
    total_limit = int(env("DEVLOOP_MAX_CONTEXT_CHARS", "26000"))
    per_file_limit = int(env("DEVLOOP_MAX_CONTEXT_FILE_CHARS", "6000"))
    configured = env("DEVLOOP_CONTEXT_FILES")
    files = (
        tuple(part.strip() for part in configured.split(",") if part.strip())
        if configured
        else DEFAULT_CONTEXT_FILES
    )

    sections: list[str] = []
    used = 0
    for relative in files:
        path = ROOT / relative
        if not path.exists() or not path.is_file():
            continue

        text = read_limited_file(path, per_file_limit)
        section = f"--- {relative} ---\n{text.strip()}\n"
        remaining = total_limit - used
        if remaining <= 0:
            break
        if len(section) > remaining:
            section = section[:remaining] + "\n\n[context truncated]\n"
        sections.append(section)
        used += len(section)

    if not sections:
        raise RuntimeError("No repository context files were found.")
    return "\n".join(sections)


def manual_idea_from_env() -> dict[str, str]:
    env_names = {
        "title": "DEVLOOP_IDEA_TITLE",
        "problem": "DEVLOOP_IDEA_PROBLEM",
        "rationale": "DEVLOOP_IDEA_RATIONALE",
        "scope": "DEVLOOP_IDEA_SCOPE",
        "non_goals": "DEVLOOP_IDEA_NON_GOALS",
        "risks": "DEVLOOP_IDEA_RISKS",
        "validation": "DEVLOOP_IDEA_VALIDATION",
    }
    return {field: require_env(env_name) for field, env_name in env_names.items()}


def list_recent_devloop_issues(repo: str | None, token: str | None) -> list[dict[str, Any]]:
    if not repo or not token:
        return []

    limit = int(env("DEVLOOP_RECENT_ISSUE_LIMIT", "10"))
    query = urllib.parse.urlencode(
        {
            "state": "all",
            "labels": "devloop,ai-proposed",
            "per_page": str(limit),
            "sort": "created",
            "direction": "desc",
        }
    )
    result = github_request("GET", f"/repos/{repo}/issues?{query}", token)
    if not isinstance(result, list):
        raise RuntimeError("Unexpected GitHub issues response.")
    return [issue for issue in result if "pull_request" not in issue]


def recent_issue_context(issues: list[dict[str, Any]]) -> str:
    if not issues:
        return "No previous DevLoop proposals were available."

    lines = []
    for issue in issues:
        body = str(issue.get("body") or "")
        excerpt = " ".join(body.split())[:500]
        lines.append(
            "\n".join(
                [
                    f"- #{issue.get('number')} ({issue.get('state')}): {issue.get('title')}",
                    f"  excerpt: {excerpt}",
                ]
            )
        )
    return "\n".join(lines)


def api_idea(recent_context: str) -> dict[str, str]:
    prompt = PROMPT_PATH.read_text(encoding="utf-8")
    context = read_repo_context()
    model = env("OPENAI_MODEL", "gpt-4.1-mini")
    response = openai_request(
        {
            "model": model,
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "Return only valid JSON. Propose one small, safe, high-leverage "
                        "DevLoop idea. Do not propose forbidden changes. Write every "
                        "JSON field value in Korean, except product names, file paths, "
                        "commands, and technical keywords that are normally written in English."
                    ),
                },
                {
                    "role": "user",
                    "content": textwrap.dedent(
                        f"""
                        {prompt}

                        Repository context:

                        {context}

                        Recent DevLoop proposals that must not be repeated or closely paraphrased:

                        {recent_context}

                        Return a JSON object with exactly these string fields:
                        title, problem, rationale, scope, non_goals, risks, validation.
                        All field values must be written in Korean. Keep the title concise.
                        """
                    ).strip(),
                },
            ],
            "response_format": {"type": "json_object"},
            "temperature": 0.3,
            "max_completion_tokens": int(env("DEVLOOP_MAX_OUTPUT_TOKENS", "900")),
        }
    )
    content = response["choices"][0]["message"]["content"]
    return validate_idea(json.loads(content))


def validate_idea(idea: dict[str, Any]) -> dict[str, str]:
    normalized = {field: str(idea.get(field, "")).strip() for field in IDEA_FIELDS}
    missing = [field for field, value in normalized.items() if not value]
    if missing:
        raise RuntimeError(f"Idea is missing required fields: {', '.join(missing)}")

    risky_scope = " ".join([normalized["title"], normalized["scope"]]).lower()
    found = [term for term in FORBIDDEN_SCOPE_TERMS if term in risky_scope]
    if found:
        raise RuntimeError(f"Idea appears to touch forbidden scope: {', '.join(found)}")

    return normalized


def load_idea(recent_context: str) -> dict[str, str]:
    mode = env("DEVLOOP_PROPOSAL_MODE", "api").lower()
    if mode == "manual":
        return validate_idea(manual_idea_from_env())
    if mode == "api":
        return api_idea(recent_context)
    raise RuntimeError("DEVLOOP_PROPOSAL_MODE must be 'manual' or 'api'.")


def build_issue_body(idea: dict[str, str]) -> str:
    fields = {
        "문제": idea["problem"],
        "지금 필요한 이유": idea["rationale"],
        "제안 범위": idea["scope"],
        "하지 않을 일": idea["non_goals"],
        "위험 요소 / 가드레일": idea["risks"],
        "검증 방법": idea["validation"],
    }
    fingerprint_source = "\n".join([idea["title"], idea["problem"], idea["scope"]])
    fingerprint = hashlib.sha256(fingerprint_source.encode("utf-8")).hexdigest()[:12]

    sections = []
    for heading, value in fields.items():
        sections.append(f"## {heading}\n\n{value.strip()}")
    sections.append(
        textwrap.dedent(
            f"""
            ## 승인 방법

            이 아이디어를 진행하려면 이슈 댓글에 정확히 `/ai approve`를 남겨주세요.
            승인 후 DevLoop가 `ai/` 브랜치와 PR scaffold를 생성합니다.

            DevLoop fingerprint: `{fingerprint}`
            """
        ).strip()
    )
    return "\n\n".join(sections)


def search_existing_issue(repo: str, token: str, fingerprint: str) -> str | None:
    query = urllib.parse.urlencode(
        {
            "q": f"repo:{repo} is:issue {fingerprint}",
            "per_page": "1",
        }
    )
    request = urllib.request.Request(
        f"{GITHUB_API}/search/issues?{query}",
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "X-GitHub-Api-Version": "2022-11-28",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            result = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"GitHub issue search failed: HTTP {exc.code}: {body}") from exc

    items = result.get("items", [])
    if not items:
        return None
    return str(items[0].get("html_url"))


def ensure_label(repo: str, token: str, name: str, color: str, description: str) -> None:
    encoded_name = urllib.parse.quote(name, safe="")
    try:
        github_request("GET", f"/repos/{repo}/labels/{encoded_name}", token)
        return
    except RuntimeError as exc:
        if "HTTP 404" not in str(exc):
            raise

    github_request(
        "POST",
        f"/repos/{repo}/labels",
        token,
        {
            "name": name,
            "color": color,
            "description": description,
        },
    )


def main() -> int:
    dry_run = env("DEVLOOP_DRY_RUN", "false").lower() == "true"
    repo = env("GITHUB_REPOSITORY")
    token = env("GITHUB_TOKEN") or env("GH_TOKEN")
    recent_context = recent_issue_context(list_recent_devloop_issues(repo, token))
    idea = load_idea(recent_context)
    title = f"[DevLoop] {idea['title']}"
    body = build_issue_body(idea)
    fingerprint = body.rsplit("`", 2)[1]

    if dry_run:
        print(json.dumps({"title": title, "body": body}, ensure_ascii=False, indent=2))
        return 0

    repo = require_env("GITHUB_REPOSITORY")
    token = env("GITHUB_TOKEN") or env("GH_TOKEN")
    if not token:
        raise RuntimeError("GITHUB_TOKEN or GH_TOKEN is required.")

    existing = search_existing_issue(repo, token, fingerprint)
    if existing:
        print(f"Matching DevLoop issue already exists: {existing}")
        return 0

    ensure_label(repo, token, "devloop", "5319e7", "Managed by the DevLoop MVP workflow.")
    ensure_label(repo, token, "ai-proposed", "1d76db", "AI-proposed idea awaiting human review.")

    issue = github_request(
        "POST",
        f"/repos/{repo}/issues",
        token,
        {
            "title": title,
            "body": body,
            "labels": ["devloop", "ai-proposed"],
        },
    )
    print(f"Created DevLoop idea issue: {issue.get('html_url')}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)
