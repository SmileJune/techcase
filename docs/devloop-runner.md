# DevLoop Local Runner

This document describes the mini PC runner that continues an approved DevLoop PR
with Codex CLI.

## Flow

1. DevLoop creates an idea Issue.
2. A human comments `/ai approve`.
3. GitHub Actions creates an `ai/issue-*` scaffold PR.
4. A human comments `/ai implement` on the Issue.
5. The mini PC runner detects the command.
6. The runner checks out the matching PR branch locally.
7. The runner invokes `codex exec` with `--sandbox workspace-write`.
8. The runner can commit and push changes back to the same PR branch.

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
  `/ai implement`.
- `DEVLOOP_CODEX_MODEL`: optional Codex model override.
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

## Mark Existing Commands

Before enabling a timer on a repository that already has `/ai implement`
comments, mark the current commands as processed so the runner only handles new
commands:

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

- The runner only responds to `/ai implement`, not `/ai approve`.
- The runner records processed `/ai implement` comment ids in a local state file
  so a systemd timer does not repeat the same implementation command.
- The runner uses `codex exec --sandbox workspace-write`.
- The runner refuses to commit changes under `.github/workflows/`, `infra/`,
  and `apps/backend/alembic/`.
- The runner does not merge PRs.
- The runner does not push to `main`; it pushes only to the existing
  `ai/issue-*` PR branch.
