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
- `GITHUB_TOKEN` or `GH_TOKEN`: token for the local runner

Optional environment variables:

- `DEVLOOP_WORKSPACE`: path to the local clone. Defaults to the current
  directory.
- `DEVLOOP_RUNNER_INTERVAL`: polling interval in seconds. Defaults to `300`.
- `DEVLOOP_APPROVERS`: comma-separated GitHub usernames allowed to use
  `/ai implement`.
- `DEVLOOP_CODEX_MODEL`: optional Codex model override.

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

## Safety Notes

- The runner only responds to `/ai implement`, not `/ai approve`.
- The runner uses `codex exec --sandbox workspace-write`.
- The runner refuses to commit changes under `.github/workflows/`, `infra/`,
  and `apps/backend/alembic/`.
- The runner does not merge PRs.
- The runner does not push to `main`; it pushes only to the existing
  `ai/issue-*` PR branch.
