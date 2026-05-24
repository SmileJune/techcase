# TechCase Web

Next.js frontend for TechCase.

The MVP starts as a static export so it can be deployed to S3 and CloudFront.

## Local Development

```bash
pnpm install
pnpm --dir apps/web dev
```

## Build

```bash
pnpm --dir apps/web build
```

The generated static output will be written to `apps/web/out`.

## Search Result Highlights

Search result cards render Elasticsearch highlight snippets from the API response
with `<em>` markers visually emphasized in the title, summary, case problem, case
solution, and evidence details. Keyword chips also highlight matches when the API
returns `matchedKeywords`, or when a keyword appears in highlighted snippets.

Manual validation:

1. Start the backend API and web app locally.
2. Search for a technology or architecture term such as `Lambda` or
   `event-driven`.
3. Confirm the result card shows highlighted title or summary text and visually
   emphasizes matching technology, problem, or architecture keyword chips when
   matching evidence is present in the response.
