# PRODUCT.md

This file gives AI agents enough product context to propose useful ideas without
guessing the direction of the service.

## Product

- Name: TechCase
- One-line definition: A technical case search service that helps developers find
  real-world adoption examples from trusted company and official engineering
  blogs.
- Current stage: MVP

## Target Users

- Developers evaluating a new technology stack.
- Engineers investigating production issues or architecture options.
- Technical leads comparing practical adoption cases across companies.

## Core Problem

Developers can find official docs and tutorials easily, but it is hard to find
credible real-world examples that explain why a company adopted a technology,
what problem it solved, and how it fit into the surrounding architecture.

## Product Principles

- Prioritize trusted company and official engineering blogs.
- Prefer practical technology adoption context over generic tutorials.
- Make search useful for technology names, problem contexts, architecture terms,
  companies, and technology combinations.
- Keep the experience focused on fast discovery and comparison of real cases.

## Current Product Surface

- Web app: `apps/web`
- Backend/API/crawler/search: `apps/backend`
- Infrastructure: `infra`
- Product and engineering docs: `README.md`, `docs/`

## Near-Term Improvement Areas

DevLoop improvement ideas should focus on low-risk product or developer workflow
improvements first, such as:

- Search quality evaluation and observability.
- Result explanation, snippets, and relevance signals.
- Source quality, deduplication, and metadata clarity.
- Documentation and onboarding for maintainers.
- Small UX improvements that do not require auth, billing, migrations, or
  infrastructure changes.

## Out of Scope for DevLoop MVP

AI agents must not propose or implement changes that require:

- Authentication or authorization changes.
- Payment, billing, or subscription logic.
- Database migrations or destructive data changes.
- Infrastructure provisioning or production deployment changes.
- Direct pushes to `main`.
- Automatic merge behavior.

## Idea Quality Bar

Every proposed idea should include:

- A concise title.
- The user or maintainer problem it addresses.
- Why the idea fits TechCase now.
- A small, reviewable implementation scope.
- Clear non-goals and risk notes.
- Suggested validation steps.
