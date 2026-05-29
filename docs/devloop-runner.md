# DevLoop Local Runner

This document describes the mini PC runner that continues an approved DevLoop PR
with Codex CLI.

## Flow

1. DevLoop creates an idea Issue.
2. A human comments `/ai approve`.
3. GitHub Actions creates an `ai/issue-*` scaffold PR.
4. The mini PC runner sees `/ai approve` or `/ai implement` after the scaffold
   PR exists.
5. The mini PC runner detects the command.
6. The runner checks out the matching PR branch locally.
7. The runner invokes `codex exec` with `--sandbox workspace-write`.
8. The runner can commit and push changes back to the same PR branch.
9. A human can leave `/ai revise` feedback on the Issue or PR, and the runner
   adds a follow-up commit on the same PR branch.

After Codex finishes, the runner also updates the PR description with the actual
implementation summary, changed files, validation results, and any remaining
risk notes. This keeps the PR from looking like a scaffold-only change after
implementation commits have been added.

## Required Local Setup

Install and authenticate these on the mini PC:

- `git`
- `python3`
- `codex`
- GitHub credentials that can read Issues, comment on Issues, fetch branches,
  and push to the repository

Required environment variables:

- `GITHUB_REPOSITORY`: for example `SmileJune/techcase`

Optional but recommended:

- `GITHUB_TOKEN` or `GH_TOKEN`: token for the local runner. Without a token, the
  runner can read public Issues and PRs but cannot leave status comments.

Optional environment variables:

- `DEVLOOP_WORKSPACE`: path to the local clone. Defaults to the current
  directory.
- `DEVLOOP_RUNNER_INTERVAL`: polling interval in seconds. Defaults to `300`.
- `DEVLOOP_APPROVERS`: comma-separated GitHub usernames allowed to use
  implementation commands.
- `DEVLOOP_CODEX_MODEL`: optional Codex model override.
- `DEVLOOP_IMPLEMENT_COMMANDS`: comma-separated comment commands that trigger
  local implementation after a scaffold PR exists. Defaults to
  `/ai implement,/ai approve`.
- `DEVLOOP_REVISE_COMMAND`: optional feedback command override. Defaults to
  `/ai revise`.
- `CODEX_BIN`: optional full path to the Codex CLI executable. Useful for
  systemd, cron, or SSH non-interactive shells where `~/.local/bin` is not on
  `PATH`.
- `DEVLOOP_STATE_FILE`: optional path for the local processed-command state.
  Defaults to `~/.local/state/devloop/techcase-runner.json`.

Use a dedicated clone for the runner. The runner refuses to start work when the
workspace is dirty.

## Dry Run

Check what the runner would do without running Codex:

```bash
python3 scripts/devloop/runner.py \
  --repo SmileJune/techcase \
  --once
```

## Execute Without Commit

Run Codex locally, but leave changes uncommitted for manual inspection:

```bash
python3 scripts/devloop/runner.py \
  --repo SmileJune/techcase \
  --once \
  --execute-codex
```

## Execute And Push

Run Codex, commit the resulting allowed changes, and push to the existing PR
branch:

```bash
python3 scripts/devloop/runner.py \
  --repo SmileJune/techcase \
  --once \
  --execute-codex \
  --commit \
  --push
```

When execution completes, the runner expects the Codex final message to include
these sections:

```markdown
## 변경 요약
- What changed and what a reviewer should inspect.

## 검증
- Commands that were run and their results.

## 미실행/위험
- Checks that could not be run, residual risk, or human follow-up needed.
```

The runner copies those sections into the PR body and completion comment. If a
section is missing, the PR body records that gap explicitly so the missing
evidence is visible during review.

## Revise An Existing PR

Leave feedback on the original DevLoop Issue or on the matching scaffold PR:

```text
/ai revise
검색 평가 데이터는 좋은데 MySQL 쿼리가 너무 넓어서 relevance가 낮습니다.
MySQL 운영 성능 대신 더 구체적인 쿼리 2개로 나눠 주세요.
```

The runner will keep the existing PR branch, run Codex with the feedback, and
push a follow-up `Revise DevLoop idea #...` commit to the same PR.

## Mark Existing Commands

Before enabling a timer on a repository that already has `/ai implement`,
`/ai approve`, or `/ai revise` comments, mark the current commands as processed
so the runner only handles new commands:

```bash
python3 scripts/devloop/runner.py \
  --repo SmileJune/techcase \
  --once \
  --mark-existing
```

## Run Continuously With systemd

The repository includes user-service templates for the `home-1` mini PC:

- `scripts/devloop/home-1.service`
- `scripts/devloop/home-1.timer`

Install them into the user systemd directory:

```bash
mkdir -p ~/.config/systemd/user ~/.config/devloop
cp scripts/devloop/home-1.service ~/.config/systemd/user/techcase-devloop.service
cp scripts/devloop/home-1.timer ~/.config/systemd/user/techcase-devloop.timer
cp scripts/devloop/runner.py ~/.local/bin/techcase-devloop-runner.py
chmod +x ~/.local/bin/techcase-devloop-runner.py
cat > ~/.config/devloop/techcase.env <<'EOF'
GITHUB_REPOSITORY=SmileJune/techcase
DEVLOOP_WORKSPACE=/home/godhkekf24/devloop/techcase-runner
CODEX_BIN=/home/godhkekf24/.local/bin/codex
DEVLOOP_APPROVERS=SmileJune
# Optional. Defaults to /ai implement,/ai approve:
# DEVLOOP_IMPLEMENT_COMMANDS=/ai implement,/ai approve
# Optional. Add a fine-grained token if you want runner status comments:
# GH_TOKEN=github_pat_...
# Optional state file override:
# DEVLOOP_STATE_FILE=/home/godhkekf24/.local/state/devloop/techcase-runner.json
EOF
systemctl --user daemon-reload
python3 scripts/devloop/runner.py --repo SmileJune/techcase --once --mark-existing
systemctl --user enable --now techcase-devloop.timer
```

Check timer and logs:

```bash
systemctl --user status techcase-devloop.timer
journalctl --user -u techcase-devloop.service -n 100 --no-pager
```

## Safety Notes

- The runner only starts implementation after a matching scaffold PR exists.
  By default it accepts `/ai approve` and `/ai implement`; set
  `DEVLOOP_IMPLEMENT_COMMANDS=/ai implement` if implementation should require a
  second explicit command.
- The runner accepts `/ai revise` on the Issue or matching PR after the first
  PR exists, even if the original DevLoop Issue is already closed. Revision
  prompts explicitly preserve existing PR work and apply only the requested
  feedback.
- The runner records processed implementation command ids in a local state file
  so a systemd timer does not repeat the same command.
- The runner uses `codex exec --sandbox workspace-write`.
- The runner refuses to commit changes under `.github/workflows/`, `infra/`,
  and `apps/backend/alembic/`.
- After implementation, the runner rewrites the initial scaffold PR body so it
  reflects the actual diff and validation evidence instead of only saying that a
  scaffold was created.
- The runner does not merge PRs.
- The runner does not push to `main`; it pushes only to the existing
  `ai/issue-*` PR branch.

## Comment Shortcuts

GitHub does not currently support repository-defined slash-command autocomplete
inside Issue or PR comments. GitHub's built-in slash commands include
`/saved-replies`, which can insert saved replies from your user account.
Practical alternatives:

- Use browser or OS text replacement snippets such as `;revise` ->
  `/ai revise`.
- Use GitHub saved replies for common DevLoop commands, then type
  `/saved-replies` in the comment box and choose the saved reply.
- Keep the command examples in this document and paste them into comments.
