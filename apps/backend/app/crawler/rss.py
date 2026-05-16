import argparse
import html
import re
from dataclasses import dataclass
from datetime import UTC, datetime
from email.utils import parsedate_to_datetime
from typing import Any
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

import feedparser
import httpx
from bs4 import BeautifulSoup
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.models.article import Article
from app.models.crawl_run import CrawlRun
from app.models.source import Source

CRAWLER_USER_AGENT = (
    "TechCaseBot/0.1 "
    "(RSS crawler for technical case search; https://github.com/SmileJune/techcase)"
)
MAX_FEED_PAGES = 200
WORDPRESS_FOOTER_PATTERN = re.compile(r"\s*The post .+ first appeared on .+\.$", re.DOTALL)


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
        return clean_feed_text(summary)

    description = get_entry_value(entry, "description")
    if isinstance(description, str) and description:
        return clean_feed_text(description)

    return None


def entry_content_html(entry: Any) -> str | None:
    content = get_entry_value(entry, "content")
    if isinstance(content, list) and content:
        value = content[0].get("value") if isinstance(content[0], dict) else None
        if isinstance(value, str) and value:
            return value

    encoded = get_entry_value(entry, "content:encoded")
    if isinstance(encoded, str) and encoded:
        return encoded

    return None


def clean_feed_text(value: str) -> str:
    decoded = html.unescape(value)
    text = BeautifulSoup(decoded, "html.parser").get_text(" ", strip=True)
    text = html.unescape(text)
    text = WORDPRESS_FOOTER_PATTERN.sub("", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


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
    headers = {
        "User-Agent": CRAWLER_USER_AGENT,
        "Accept": "application/rss+xml, application/atom+xml, application/xml, text/xml, */*",
    }
    with httpx.Client(timeout=20.0, follow_redirects=True, headers=headers) as client:
        return fetch_feed_with_client(client, feed_url)


def fetch_feed_with_client(client: httpx.Client, feed_url: str) -> list[Any]:
    response = client.get(feed_url)
    response.raise_for_status()

    parsed = feedparser.parse(response.content)
    return list(parsed.entries)


def fetch_source_entries(source: Source) -> list[Any]:
    if source.collection_strategy != "rss":
        raise ValueError(
            f"Unsupported collection strategy for RSS crawler: {source.collection_strategy}"
        )

    if not source.feed_url:
        raise ValueError("RSS source is missing feed_url")

    if source.pagination_strategy == "none":
        return fetch_feed(source.feed_url)

    if source.pagination_strategy != "wordpress_paged":
        raise ValueError(f"Unsupported RSS pagination strategy: {source.pagination_strategy}")

    entries_by_url: dict[str, Any] = {}
    headers = {
        "User-Agent": CRAWLER_USER_AGENT,
        "Accept": "application/rss+xml, application/atom+xml, application/xml, text/xml, */*",
    }

    with httpx.Client(timeout=20.0, follow_redirects=True, headers=headers) as client:
        for page in range(1, MAX_FEED_PAGES + 1):
            try:
                page_entries = fetch_feed_with_client(
                    client, paginated_feed_url(source.feed_url, page)
                )
            except httpx.HTTPStatusError as exc:
                if exc.response.status_code == 404 and page > 1:
                    break
                raise

            if not page_entries:
                break

            new_entry_count = 0
            for entry in page_entries:
                url = entry_url(entry)
                if not url or url in entries_by_url:
                    continue

                entries_by_url[url] = entry
                new_entry_count += 1

            if new_entry_count == 0:
                break

    return list(entries_by_url.values())


def paginated_feed_url(feed_url: str, page: int) -> str:
    if page == 1:
        return feed_url

    parts = urlsplit(feed_url)
    query = dict(parse_qsl(parts.query, keep_blank_values=True))
    query["paged"] = str(page)
    return urlunsplit((parts.scheme, parts.netloc, parts.path, urlencode(query), parts.fragment))


def upsert_article(db: Session, source: Source, entry: Any, collected_at: datetime) -> str:
    url = entry_url(entry)
    title = get_entry_value(entry, "title")

    if not url or not isinstance(title, str) or not title:
        raise ValueError("RSS entry is missing required title or url")

    article = db.scalar(select(Article).where(Article.url == url))
    author = entry_author(entry)
    published_at = entry_published_at(entry)
    summary = entry_summary(entry)
    content_html = entry_content_html(entry)
    content_text = clean_feed_text(content_html) if content_html else None
    raw_metadata = entry_raw_metadata(entry)

    if article is None:
        article = Article(
            source_id=source.id,
            url=url,
            title=title,
            author=author,
            published_at=published_at,
            summary=summary,
            content_html=content_html,
            content_text=content_text,
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
        "content_html": content_html,
        "content_text": content_text,
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
        entries = fetch_source_entries(source)
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
    crawl_run.metadata_json = {
        "feed_url": source.feed_url,
        "collection_strategy": source.collection_strategy,
        "pagination_strategy": source.pagination_strategy,
        "content_strategy": source.content_strategy,
    }

    return CrawlSummary(
        source_slug=source.slug,
        fetched_count=fetched_count,
        created_count=created_count,
        updated_count=updated_count,
        unchanged_count=unchanged_count,
        failed_count=failed_count,
        status=status,
    )


def crawl_enabled_sources(
    limit: int | None = None, source_slug: str | None = None
) -> list[CrawlSummary]:
    with SessionLocal() as db:
        statement = (
            select(Source)
            .where(Source.enabled.is_(True), Source.collection_strategy == "rss")
            .order_by(Source.slug)
        )
        if source_slug is not None:
            statement = statement.where(Source.slug == source_slug)
        if limit is not None:
            statement = statement.limit(limit)

        sources = list(db.scalars(statement))
        summaries = [crawl_source(db, source) for source in sources]
        db.commit()

    return summaries


def main() -> None:
    parser = argparse.ArgumentParser(description="Crawl enabled RSS sources.")
    parser.add_argument("--source", dest="source_slug", help="Crawl a single source slug.")
    parser.add_argument("--limit", type=int, help="Limit number of sources to crawl.")
    args = parser.parse_args()

    summaries = crawl_enabled_sources(limit=args.limit, source_slug=args.source_slug)
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
