# AI_POLICY.md

This policy defines the safe operating boundary for the DevLoop MVP in this
repository.

## Goal

The DevLoop MVP lets one unified AI employee propose product improvement ideas
as GitHub Issues. A human approves which Issues may advance to a PR.

## Current MVP Boundary

Allowed:

- Create GitHub Issues containing AI-proposed product improvement ideas.
- Generate one low-cost AI idea per manually triggered proposal workflow run.
- Detect human approval comments on those Issues.
- Create an `ai/` branch after approval.
- Open a PR scaffold for the approved idea.
- Add documentation-only planning artifacts for the approved idea.
- Detect `/ai implement` through a local mini PC runner.
- Run Codex CLI locally on an approved `ai/issue-*` PR branch.
- Use manual proposal mode when a human wants to provide a Codex-drafted idea
  instead of spending API credits.

Not allowed:

- Automatic merge.
- Direct push to `main`.
- Service code changes without a later explicit human request.
- Authentication or authorization changes.
- Payment or billing changes.
- Database migrations.
- Infrastructure or deployment configuration changes.
- Secret creation, rotation, or disclosure.
- OpenAI API calls from the approved implementation workflow.
- More than one AI-generated idea per proposal workflow run.
- Local runner commits without a human `/ai implement` command.
- Local runner pushes to `main`.

## Required GitHub Configuration

Secrets:

- `OPENAI_API_KEY`: DevLoop-only OpenAI API key used by the proposal workflow
  when `proposal_mode=api`.

Repository variables:

- `OPENAI_MODEL`: Optional model for proposal generation. Defaults to
  `gpt-4.1-mini` when unset.
- `DEVLOOP_APPROVERS`: Optional comma-separated GitHub usernames allowed to
  approve ideas. If unset, GitHub author association must be `OWNER`, `MEMBER`,
  or `COLLABORATOR`.

## Required GitHub Actions Permissions

The proposal workflow needs:

```yaml
permissions:
  contents: read
  issues: write
```

The approved implementation workflow needs:

```yaml
permissions:
  contents: write
  issues: write
  pull-requests: write
```

## Approval Signal

The implementation workflow only responds to Issue comments whose trimmed body is:

```text
/ai approve
```

The Issue must also carry the `devloop` and `ai-proposed` labels.

## Implementation Signal

The local mini PC runner only continues implementation after a human comments:

```text
/ai implement
```

The runner should work on the existing `ai/issue-*` PR branch and must not merge
the PR.

## Human Review Expectations

Before approving an Issue, verify that:

- The idea fits `PRODUCT.md`.
- The proposed scope is small and reviewable.
- The idea does not touch forbidden areas.
- The validation plan is concrete.
- The requested result can be reviewed in a PR before any merge.
