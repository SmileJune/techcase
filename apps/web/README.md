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

