# TechCase Backend

FastAPI backend for TechCase.

Initial responsibilities:

- Search API
- PostgreSQL access
- Elasticsearch access
- RSS crawler commands
- Indexing commands

## Local Development

```bash
uv sync
uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Health check:

```bash
curl http://localhost:8000/health
```

## Database Migrations

Run the latest Alembic migrations:

```bash
uv run alembic upgrade head
```

Show migration history:

```bash
uv run alembic history
```

## Seed Data

Insert or update the initial AWS RSS sources:

```bash
uv run python -m app.seeds.seed_sources
```

## RSS Crawler

Crawl enabled RSS sources and upsert articles:

```bash
uv run python -m app.crawler.rss
```
