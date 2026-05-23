# AGENTS.md

This repository allows AI-assisted development only inside the guardrails below.

## Repository Context

TechCase is a product for discovering practical technology adoption examples
from trusted engineering blogs. Read these files before proposing or planning
work:

- `README.md`
- `PRODUCT.md`
- `AI_POLICY.md`
- Relevant files under `docs/`

## DevLoop MVP Flow

1. A human manually runs the proposal workflow.
2. In `api` mode, one unified AI employee proposes exactly one small idea.
3. In `manual` mode, the workflow records the human-supplied draft.
4. The workflow records the idea as a GitHub Issue.
5. A human reviews the Issue.
6. A human approves by adding an Issue comment containing exactly:

   ```text
   /ai approve
   ```

7. Only after approval may AI create a branch and PR.
8. The MVP implementation creates a PR scaffold only. It must not change service
   code automatically.

## Hard Rules

- Do not push directly to `main`.
- Do not implement automatic merge.
- Do not modify authentication, authorization, payment, billing, database
  migrations, or infrastructure settings.
- Do not change production configuration or secrets.
- Do not make broad refactors unless explicitly requested by a human.
- Keep AI-generated PRs small, reviewable, and easy to revert.
- Do not call the OpenAI API from the approved implementation workflow.

## Branch and PR Rules

- AI branches must use the prefix `ai/`.
- AI PRs must reference the approved Issue.
- AI PRs must describe:
  - What was approved.
  - What changed.
  - What was intentionally left out.
  - How a human can validate the result.

## Approval Rules

- The approval signal is a GitHub Issue comment containing `/ai approve`.
- The workflow should only act on Issues labeled for DevLoop proposals.
- Optional repository variable `DEVLOOP_APPROVERS` can restrict who may approve.
  Use a comma-separated list of GitHub usernames.

## Suggested Agent Behavior

- Prefer documentation, tests, and narrow workflow improvements before product
  code changes.
- Use existing project conventions.
- Explain uncertainty in PR descriptions.
- Stop when a requested change would violate `AI_POLICY.md`.
