#!/usr/bin/env python3
"""Local DevLoop runner for mini PC based Codex CLI implementation.

This runner watches DevLoop Issues for a human `/ai implement` command, checks
out the matching `ai/issue-*` PR branch, and can run `codex exec` locally.

It is intentionally conservative:
- default mode is dry-run
- it refuses to run on a dirty workspace
- commit and push are separate explicit flags
- forbidden path changes block commit/push
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import tempfile
import textwrap
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any


GITHUB_API = "https://api.github.com"
IMPLEMENT_COMMAND = "/ai implement"
START_MARKER = "<!-- devloop-runner:start -->"
DONE_MARKER = "<!-- devloop-runner:done -->"
FORBIDDEN_PATH_PREFIXES = (
    ".github/workflows/",
    "infra/",
    "apps/backend/alembic/",
)
FORBIDDEN_PATH_NAMES = (
    "alembic.ini",
    "terraform.tfvars",
    "terraform.tfvars.json",
)


@dataclass(frozen=True)
class Candidate:
    issue: dict[str, Any]
    command_comment: dict[str, Any]
    pull_request: dict[str, Any]


def env(name: str, default: str | None = None) -> str | None:
    value = os.environ.get(name)
    if value is None or value == "":
        return default
    return value


def run_command(
    args: list[str],
    cwd: Path,
    check: bool = True,
    capture_output: bool = True,
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        args,
        cwd=cwd,
        check=check,
        capture_output=capture_output,
        text=True,
    )


class GitHubClient:
    def __init__(self, repo: str, token: str) -> None:
        self.repo = repo
        self.token = token

    def request(
        self,
        method: str,
        path: str,
        payload: dict[str, Any] | None = None,
    ) -> dict[str, Any] | list[Any]:
        data = None if payload is None else json.dumps(payload).encode("utf-8")
        request = urllib.request.Request(
            f"{GITHUB_API}{path}",
            data=data,
            method=method,
            headers={
                "Accept": "application/vnd.github+json",
                "Authorization": f"Bearer {self.token}",
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

    def list_open_devloop_issues(self) -> list[dict[str, Any]]:
        query = urllib.parse.urlencode(
            {
                "state": "open",
                "labels": "devloop,ai-proposed",
                "per_page": "100",
            }
        )
        result = self.request("GET", f"/repos/{self.repo}/issues?{query}")
        if not isinstance(result, list):
            raise RuntimeError("Unexpected GitHub issues response.")
        return [issue for issue in result if "pull_request" not in issue]

    def list_comments(self, issue_number: int) -> list[dict[str, Any]]:
        result = self.request(
            "GET",
            f"/repos/{self.repo}/issues/{issue_number}/comments?per_page=100",
        )
        if not isinstance(result, list):
            raise RuntimeError("Unexpected GitHub comments response.")
        return result

    def list_open_pull_requests(self) -> list[dict[str, Any]]:
        result = self.request("GET", f"/repos/{self.repo}/pulls?state=open&per_page=100")
        if not isinstance(result, list):
            raise RuntimeError("Unexpected GitHub pulls response.")
        return result

    def comment(self, issue_number: int, body: str) -> None:
        self.request(
            "POST",
            f"/repos/{self.repo}/issues/{issue_number}/comments",
            {"body": body},
        )


def is_allowed_approver(comment: dict[str, Any]) -> bool:
    allowed_users = {
        user.strip().lower()
        for user in env("DEVLOOP_APPROVERS", "").split(",")
        if user.strip()
    }
    commenter = comment["user"]["login"].lower()
    if allowed_users:
        return commenter in allowed_users
    return comment.get("author_association") in {"OWNER", "MEMBER", "COLLABORATOR"}


def last_implement_command(comments: list[dict[str, Any]]) -> dict[str, Any] | None:
    matching = [
        comment
        for comment in comments
        if (comment.get("body") or "").strip() == IMPLEMENT_COMMAND and is_allowed_approver(comment)
    ]
    return matching[-1] if matching else None


def has_runner_marker_after(comments: list[dict[str, Any]], marker: str, created_at: str) -> bool:
    return any(
        marker in (comment.get("body") or "") and comment.get("created_at", "") > created_at
        for comment in comments
    )


def find_issue_pr(issue_number: int, pulls: list[dict[str, Any]]) -> dict[str, Any] | None:
    prefix = f"ai/issue-{issue_number}"
    for pull in pulls:
        head = pull.get("head") or {}
        branch = str(head.get("ref") or "")
        if branch == prefix or branch.startswith(f"{prefix}-"):
            return pull
    return None


def find_candidates(client: GitHubClient, force: bool = False) -> list[Candidate]:
    pulls = client.list_open_pull_requests()
    candidates: list[Candidate] = []
    for issue in client.list_open_devloop_issues():
        issue_number = int(issue["number"])
        comments = client.list_comments(issue_number)
        command = last_implement_command(comments)
        if not command:
            continue

        if not force and (
            has_runner_marker_after(comments, START_MARKER, command["created_at"])
            or has_runner_marker_after(comments, DONE_MARKER, command["created_at"])
        ):
            continue

        pull = find_issue_pr(issue_number, pulls)
        if not pull:
            continue
        candidates.append(Candidate(issue=issue, command_comment=command, pull_request=pull))
    return candidates


def assert_clean_workspace(workspace: Path) -> None:
    result = run_command(["git", "status", "--porcelain"], cwd=workspace)
    if result.stdout.strip():
        raise RuntimeError(
            "Workspace is dirty. Use a dedicated mini PC clone or commit/stash local changes first."
        )


def checkout_branch(workspace: Path, branch: str) -> None:
    run_command(
        ["git", "fetch", "origin", f"+refs/heads/{branch}:refs/remotes/origin/{branch}"],
        cwd=workspace,
        capture_output=False,
    )
    run_command(["git", "checkout", "-B", branch, f"origin/{branch}"], cwd=workspace, capture_output=False)
    run_command(["git", "pull", "--ff-only", "origin", branch], cwd=workspace, capture_output=False)


def changed_files(workspace: Path) -> list[str]:
    result = run_command(["git", "diff", "--name-only"], cwd=workspace)
    staged = run_command(["git", "diff", "--cached", "--name-only"], cwd=workspace)
    files = set(result.stdout.splitlines()) | set(staged.stdout.splitlines())
    return sorted(file for file in files if file)


def forbidden_changed_files(files: list[str]) -> list[str]:
    forbidden = []
    for file in files:
        if file in FORBIDDEN_PATH_NAMES or any(file.startswith(prefix) for prefix in FORBIDDEN_PATH_PREFIXES):
            forbidden.append(file)
    return forbidden


def plan_path_for_issue(workspace: Path, issue_number: int) -> Path:
    return workspace / "docs" / "ai-ideas" / f"issue-{issue_number}.md"


def build_codex_prompt(issue_number: int, plan_path: Path) -> str:
    return textwrap.dedent(
        f"""
        `AI_POLICY.md`, `AGENTS.md`, and `{plan_path.relative_to(plan_path.parents[2])}`를 읽고
        승인된 DevLoop 아이디어 #{issue_number}를 실제 구현해줘.

        필수 제약:
        - 현재 브랜치에서만 작업한다.
        - 승인된 범위 밖으로 확장하지 않는다.
        - 인증, 인가, 결제, 데이터베이스 마이그레이션, 인프라 설정은 변경하지 않는다.
        - 자동 머지나 main 직접 push는 하지 않는다.
        - 구현 후 관련 테스트나 정적 검사를 실행한다.
        - 커밋이나 push는 하지 않는다. 변경과 검증 결과만 남긴다.
        """
    ).strip()


def run_codex(workspace: Path, issue_number: int, model: str | None) -> Path:
    plan_path = plan_path_for_issue(workspace, issue_number)
    if not plan_path.exists():
        raise RuntimeError(f"Expected scaffold file does not exist: {plan_path}")

    output_dir = Path(tempfile.mkdtemp(prefix="devloop-codex-"))
    output_path = output_dir / f"issue-{issue_number}-last-message.md"
    command = [
        "codex",
        "exec",
        "--sandbox",
        "workspace-write",
        "--cd",
        str(workspace),
        "--output-last-message",
        str(output_path),
    ]
    if model:
        command.extend(["--model", model])
    command.append(build_codex_prompt(issue_number, plan_path))
    run_command(command, cwd=workspace, capture_output=False)
    return output_path


def commit_and_push(workspace: Path, issue_number: int, branch: str, push: bool) -> str:
    files = changed_files(workspace)
    if not files:
        return "No changes were produced by Codex."

    forbidden = forbidden_changed_files(files)
    if forbidden:
        raise RuntimeError(
            "Codex changed forbidden paths; refusing to commit: " + ", ".join(forbidden)
        )

    run_command(["git", "add", "-A"], cwd=workspace, capture_output=False)
    run_command(["git", "commit", "-m", f"Implement DevLoop idea #{issue_number}"], cwd=workspace)
    if push:
        run_command(["git", "push", "origin", f"HEAD:{branch}"], cwd=workspace, capture_output=False)
        return f"Committed and pushed changes to `{branch}`."
    return "Committed changes locally. Push was skipped."


def process_candidate(
    client: GitHubClient,
    candidate: Candidate,
    workspace: Path,
    execute_codex: bool,
    commit: bool,
    push: bool,
    model: str | None,
) -> None:
    issue_number = int(candidate.issue["number"])
    branch = str((candidate.pull_request.get("head") or {}).get("ref"))
    pr_url = str(candidate.pull_request.get("html_url"))

    if not execute_codex:
        print(f"[dry-run] Would implement issue #{issue_number} on {branch}: {pr_url}")
        return

    assert_clean_workspace(workspace)
    client.comment(
        issue_number,
        textwrap.dedent(
            f"""
            {START_MARKER}
            DevLoop runner가 미니 PC에서 구현을 시작합니다.

            - PR: {pr_url}
            - 브랜치: `{branch}`
            """
        ).strip(),
    )
    checkout_branch(workspace, branch)
    output_path = run_codex(workspace, issue_number, model)
    files = changed_files(workspace)

    if commit:
        result = commit_and_push(workspace, issue_number, branch, push)
    else:
        result = "Codex 실행은 완료했지만 commit 옵션이 꺼져 있어 커밋하지 않았습니다."

    file_lines = "\n".join(f"- `{file}`" for file in files) if files else "- 변경 파일 없음"
    client.comment(
        issue_number,
        textwrap.dedent(
            f"""
            {DONE_MARKER}
            DevLoop runner 실행이 완료되었습니다.

            - PR: {pr_url}
            - 브랜치: `{branch}`
            - 결과: {result}
            - Codex 마지막 메시지: `{output_path}`

            변경 파일:
            {file_lines}
            """
        ).strip(),
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the local DevLoop Codex CLI runner.")
    parser.add_argument("--repo", default=env("GITHUB_REPOSITORY"))
    parser.add_argument("--workspace", default=env("DEVLOOP_WORKSPACE", os.getcwd()))
    parser.add_argument("--interval", type=int, default=int(env("DEVLOOP_RUNNER_INTERVAL", "300")))
    parser.add_argument("--once", action="store_true")
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--execute-codex", action="store_true")
    parser.add_argument("--commit", action="store_true")
    parser.add_argument("--push", action="store_true")
    parser.add_argument("--model", default=env("DEVLOOP_CODEX_MODEL"))
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not args.repo:
        raise RuntimeError("GITHUB_REPOSITORY or --repo is required.")
    token = env("GITHUB_TOKEN") or env("GH_TOKEN")
    if not token:
        raise RuntimeError("GITHUB_TOKEN, GH_TOKEN, or equivalent local runner token is required.")

    workspace = Path(args.workspace).resolve()
    client = GitHubClient(args.repo, token)

    while True:
        candidates = find_candidates(client, force=args.force)
        if not candidates:
            print("No approved DevLoop implementation commands found.")
        for candidate in candidates:
            process_candidate(
                client=client,
                candidate=candidate,
                workspace=workspace,
                execute_codex=args.execute_codex,
                commit=args.commit,
                push=args.push,
                model=args.model,
            )

        if args.once:
            break
        time.sleep(args.interval)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)
