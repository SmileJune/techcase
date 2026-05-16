from dataclasses import dataclass
from datetime import UTC, datetime
from email.utils import parsedate_to_datetime
from typing import Any

import feedparser
import httpx
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.models.article import Article
from app.models.crawl_run import CrawlRun
from app.models.source import Source


@dataclass(frozen=True)
class CrawlSummary:
    source_slug: str
    fetched_count: int
    created_count: int
    updated_count: int
    unchanged_count: int
    failed_count: int
    status: str


def parse_datetime(value: str | None) -> datetime | None:
    if not value:
        return None

    try:
        parsed = parsedate_to_datetime(value)
    except (TypeError, ValueError):
        return None

    if parsed.tzinfo is None:
        return parsed.replace(tzinfo=UTC)

    return parsed


def get_entry_value(entry: Any, key: str) -> Any:
    if isinstance(entry, dict):
        return entry.get(key)
    return getattr(entry, key, None)


def entry_url(entry: Any) -> str | None:
    link = get_entry_value(entry, "link")
    if isinstance(link, str) and link:
        return link
    return None


def entry_author(entry: Any) -> str | None:
    author = get_entry_value(entry, "author")
    if isinstance(author, str) and author:
        return author
    return None


def entry_summary(entry: Any) -> str | None:
    summary = get_entry_value(entry, "summary")
    if isinstance(summary, str) and summary:
        return summary

    description = get_entry_value(entry, "description")
    if isinstance(description, str) and description:
        return description

    return None


def entry_published_at(entry: Any) -> datetime | None:
    published = get_entry_value(entry, "published")
    if isinstance(published, str):
        return parse_datetime(published)

    updated = get_entry_value(entry, "updated")
    if isinstance(updated, str):
        return parse_datetime(updated)

    return None


def entry_raw_metadata(entry: Any) -> dict[str, Any]:
    if isinstance(entry, dict):
        return {
            "id": entry.get("id"),
            "guid": entry.get("guid"),
            "tags": entry.get("tags"),
            "published": entry.get("published"),
            "updated": entry.get("updated"),
        }

    return {}


def fetch_feed(feed_url: str) -> list[Any]:
    with httpx.Client(timeout=20.0, follow_redirects=True) as client:
        response = client.get(feed_url)
        response.raise_for_status()

    parsed = feedparser.parse(response.content)
    return list(parsed.entries)


def upsert_article(db: Session, source: Source, entry: Any, collected_at: datetime) -> str:
    url = entry_url(entry)
    title = get_entry_value(entry, "title")

    if not url or not isinstance(title, str) or not title:
        raise ValueError("RSS entry is missing required title or url")

    article = db.scalar(select(Article).where(Article.url == url))
    author = entry_author(entry)
    published_at = entry_published_at(entry)
    summary = entry_summary(entry)
    raw_metadata = entry_raw_metadata(entry)

    if article is None:
        article = Article(
            source_id=source.id,
            url=url,
            title=title,
            author=author,
            published_at=published_at,
            summary=summary,
            raw_metadata=raw_metadata,
            collected_at=collected_at,
        )
        db.add(article)
        return "created"

    changes = {
        "source_id": source.id,
        "title": title,
        "author": author,
        "published_at": published_at,
        "summary": summary,
        "raw_metadata": raw_metadata,
    }

    changed = False
    for field, value in changes.items():
        if getattr(article, field) != value:
            setattr(article, field, value)
            changed = True

    if not changed:
        return "unchanged"

    article.collected_at = collected_at
    return "updated"


def crawl_source(db: Session, source: Source) -> CrawlSummary:
    started_at = datetime.now(UTC)
    crawl_run = CrawlRun(source_id=source.id, status="running", started_at=started_at)
    db.add(crawl_run)
    db.flush()

    fetched_count = 0
    created_count = 0
    updated_count = 0
    unchanged_count = 0
    failed_count = 0
    error_message: str | None = None

    try:
        entries = fetch_feed(source.feed_url)
        fetched_count = len(entries)
        collected_at = datetime.now(UTC)

        for entry in entries:
            try:
                result = upsert_article(db, source, entry, collected_at)
                if result == "created":
                    created_count += 1
                elif result == "updated":
                    updated_count += 1
                else:
                    unchanged_count += 1
            except Exception:
                failed_count += 1

        status = "succeeded" if failed_count == 0 else "partial_failed"
    except Exception as exc:
        status = "failed"
        error_message = str(exc)

    crawl_run.status = status
    crawl_run.finished_at = datetime.now(UTC)
    crawl_run.fetched_count = fetched_count
    crawl_run.created_count = created_count
    crawl_run.updated_count = updated_count
    crawl_run.unchanged_count = unchanged_count
    crawl_run.failed_count = failed_count
    crawl_run.error_message = error_message
    crawl_run.metadata_json = {"feed_url": source.feed_url}

    return CrawlSummary(
        source_slug=source.slug,
        fetched_count=fetched_count,
        created_count=created_count,
        updated_count=updated_count,
        unchanged_count=unchanged_count,
        failed_count=failed_count,
        status=status,
    )


def crawl_enabled_sources(limit: int | None = None) -> list[CrawlSummary]:
    with SessionLocal() as db:
        statement = select(Source).where(Source.enabled.is_(True)).order_by(Source.slug)
        if limit is not None:
            statement = statement.limit(limit)

        sources = list(db.scalars(statement))
        summaries = [crawl_source(db, source) for source in sources]
        db.commit()

    return summaries


def main() -> None:
    summaries = crawl_enabled_sources()
    for summary in summaries:
        print(
            "Crawled "
            f"{summary.source_slug}: "
            f"status={summary.status}, "
            f"fetched={summary.fetched_count}, "
            f"created={summary.created_count}, "
            f"updated={summary.updated_count}, "
            f"unchanged={summary.unchanged_count}, "
            f"failed={summary.failed_count}"
        )


if __name__ == "__main__":
    main()
