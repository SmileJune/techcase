#!/usr/bin/env python3
"""Create a branch and PR scaffold for an approved DevLoop idea Issue."""

from __future__ import annotations

import base64
import json
import os
import re
import sys
import textwrap
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any


GITHUB_API = "https://api.github.com"
APPROVAL_COMMAND = "/ai approve"


def env(name: str, default: str | None = None) -> str | None:
    value = os.environ.get(name)
    if value is None or value == "":
        return default
    return value


def load_event() -> dict[str, Any]:
    event_path = env("GITHUB_EVENT_PATH")
    if not event_path:
        raise RuntimeError("GITHUB_EVENT_PATH is required.")
    return json.loads(Path(event_path).read_text(encoding="utf-8"))


def github_request(
    method: str,
    path: str,
    token: str,
    payload: dict[str, Any] | None = None,
    ok_statuses: set[int] | None = None,
) -> dict[str, Any] | list[Any]:
    ok_statuses = ok_statuses or {200, 201}
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
            if response.status not in ok_statuses:
                raise RuntimeError(f"Unexpected HTTP status {response.status} for {method} {path}")
            return {} if not raw else json.loads(raw)
    except urllib.error.HTTPError as exc:
        if exc.code in ok_statuses:
            return {}
        body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"GitHub API {method} {path} failed: HTTP {exc.code}: {body}") from exc


def is_allowed_approver(event: dict[str, Any]) -> bool:
    allowed_users = {
        user.strip().lower()
        for user in env("DEVLOOP_APPROVERS", "").split(",")
        if user.strip()
    }
    commenter = event["comment"]["user"]["login"].lower()
    if allowed_users:
        return commenter in allowed_users
    return event["comment"].get("author_association") in {"OWNER", "MEMBER", "COLLABORATOR"}


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", value.lower()).strip("-")
    return slug[:48] or "idea"


def issue_has_required_labels(issue: dict[str, Any]) -> bool:
    labels = {label["name"] for label in issue.get("labels", [])}
    return {"devloop", "ai-proposed"}.issubset(labels)


def get_default_branch(repo: str, token: str) -> tuple[str, str]:
    repo_data = github_request("GET", f"/repos/{repo}", token)
    default_branch = str(repo_data["default_branch"])
    ref = github_request("GET", f"/repos/{repo}/git/ref/heads/{default_branch}", token)
    sha = str(ref["object"]["sha"])
    return default_branch, sha


def ensure_branch(repo: str, token: str, branch: str, base_sha: str) -> None:
    try:
        github_request("GET", f"/repos/{repo}/git/ref/heads/{branch}", token)
        print(f"Branch already exists: {branch}")
        return
    except RuntimeError as exc:
        if "HTTP 404" not in str(exc):
            raise

    github_request(
        "POST",
        f"/repos/{repo}/git/refs",
        token,
        {
            "ref": f"refs/heads/{branch}",
            "sha": base_sha,
        },
    )
    print(f"Created branch: {branch}")


def create_plan_file(repo: str, token: str, branch: str, issue: dict[str, Any]) -> str:
    number = issue["number"]
    title = issue["title"]
    body = issue.get("body") or ""
    path = f"docs/ai-ideas/issue-{number}.md"
    content = textwrap.dedent(
        f"""
        # DevLoop 아이디어 #{number}: {title}

        이 파일은 GitHub Issue에서 사람이 승인한 뒤 생성된 PR scaffold입니다.
        의도적으로 실제 서비스 코드는 수정하지 않습니다.

        ## 승인된 이슈

        - 이슈: #{number}
        - 제목: {title}

        ## 원본 제안

        {body}

        ## 구현 메모

        - 승인된 범위 안에서만 변경합니다.
        - 인증, 결제, 데이터베이스 마이그레이션, 인프라는 건드리지 않습니다.
        - 자동 머지는 활성화하지 않습니다.
        - 사람 리뷰를 요청하기 전에 검증 메모를 남깁니다.
        """
    ).strip() + "\n"

    encoded = base64.b64encode(content.encode("utf-8")).decode("ascii")
    payload = {
        "message": f"Add DevLoop scaffold for issue #{number}",
        "content": encoded,
        "branch": branch,
    }
    try:
        existing = github_request("GET", f"/repos/{repo}/contents/{path}?ref={branch}", token)
        if isinstance(existing, dict) and existing.get("sha"):
            print(f"Plan file already exists: {path}")
            return path
    except RuntimeError as exc:
        if "HTTP 404" not in str(exc):
            raise

    github_request(
        "PUT",
        f"/repos/{repo}/contents/{path}",
        token,
        payload,
    )
    return path


def find_existing_pr(repo: str, token: str, branch: str) -> str | None:
    owner = repo.split("/", 1)[0]
    query_path = f"/repos/{repo}/pulls?head={owner}:{branch}&state=open&per_page=1"
    pulls = github_request("GET", query_path, token)
    if isinstance(pulls, list) and pulls:
        return str(pulls[0].get("html_url"))
    return None


def create_pr(repo: str, token: str, base: str, branch: str, issue: dict[str, Any], plan_path: str) -> str:
    existing = find_existing_pr(repo, token, branch)
    if existing:
        return existing

    number = issue["number"]
    pr = github_request(
        "POST",
        f"/repos/{repo}/pulls",
        token,
        {
            "title": f"[DevLoop] 승인된 아이디어 #{number} scaffold",
            "head": branch,
            "base": base,
            "body": textwrap.dedent(
                f"""
                ## 승인된 아이디어

                Refs #{number}

                ## 변경 사항

                - 승인된 아이디어에 대한 문서 전용 PR scaffold로 `{plan_path}`를 추가했습니다.

                ## 의도적으로 제외한 것

                - 실제 서비스 코드 변경은 없습니다.
                - 자동 머지는 없습니다.
                - 인증, 결제, 데이터베이스 마이그레이션, 인프라 변경은 없습니다.

                ## 검증

                - 이 PR이 승인된 scaffold만 포함하는지 확인합니다.
                - 후속 구현이 `AI_POLICY.md` 범위 안에 있는지 확인합니다.
                """
            ).strip(),
        },
    )
    return str(pr.get("html_url"))


def comment_on_issue(repo: str, token: str, issue_number: int, body: str) -> None:
    github_request(
        "POST",
        f"/repos/{repo}/issues/{issue_number}/comments",
        token,
        {"body": body},
    )


def main() -> int:
    repo = env("GITHUB_REPOSITORY")
    token = env("GITHUB_TOKEN")
    if not repo:
        raise RuntimeError("GITHUB_REPOSITORY is required.")
    if not token:
        raise RuntimeError("GITHUB_TOKEN is required.")

    event = load_event()
    issue = event.get("issue") or {}
    comment = event.get("comment") or {}

    if "pull_request" in issue:
        print("Ignoring PR comment.")
        return 0
    if (comment.get("body") or "").strip() != APPROVAL_COMMAND:
        print("Ignoring comment without approval command.")
        return 0
    if not is_allowed_approver(event):
        raise RuntimeError("Comment author is not allowed to approve DevLoop ideas.")

    issue_number = int(issue["number"])
    issue = github_request("GET", f"/repos/{repo}/issues/{issue_number}", token)
    if not issue_has_required_labels(issue):
        raise RuntimeError("Issue must have both 'devloop' and 'ai-proposed' labels.")

    base_branch, base_sha = get_default_branch(repo, token)
    branch = f"ai/issue-{issue_number}-{slugify(issue['title'])}"
    ensure_branch(repo, token, branch, base_sha)
    plan_path = create_plan_file(repo, token, branch, issue)
    pr_url = create_pr(repo, token, base_branch, branch, issue, plan_path)

    comment_on_issue(
        repo,
        token,
        issue_number,
        f"DevLoop가 승인된 아이디어의 PR scaffold를 생성했습니다: {pr_url}",
    )
    print(f"Created or found PR: {pr_url}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)
