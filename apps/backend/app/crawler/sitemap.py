import argparse
import re
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from datetime import UTC, datetime
from email.utils import parsedate_to_datetime
from typing import Any
from urllib.parse import urlparse

import httpx
from bs4 import BeautifulSoup
from readability import Document
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.crawler.rss import CRAWLER_USER_AGENT, clean_feed_text
from app.db.session import SessionLocal
from app.models.article import Article
from app.models.crawl_run import CrawlRun
from app.models.source import Source

SITEMAP_NAMESPACE = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
ARTICLE_PATH_PATTERN = re.compile(r"/\d+/?$")
SOURCE_ARTICLE_PATH_PATTERNS = {
    "gmarket-tech-blog": re.compile(r"/\d+/?$"),
    "upstage-blog": re.compile(r"/blog/ko/[^/]+/?$"),
}


@dataclass(frozen=True)
class SitemapEntry:
    url: str
    lastmod: str | None = None


@dataclass(frozen=True)
class SitemapCrawlSummary:
    source_slug: str
    fetched_count: int
    created_count: int
    updated_count: int
    unchanged_count: int
    failed_count: int
    status: str


def parse_sitemap(xml_text: str) -> list[SitemapEntry]:
    root = ET.fromstring(xml_text)
    entries: list[SitemapEntry] = []

    for url_node in root.findall("sm:url", SITEMAP_NAMESPACE):
        loc_node = url_node.find("sm:loc", SITEMAP_NAMESPACE)
        if loc_node is None or not loc_node.text:
            continue

        lastmod_node = url_node.find("sm:lastmod", SITEMAP_NAMESPACE)
        lastmod = None
        if lastmod_node is not None and lastmod_node.text:
            lastmod = lastmod_node.text.strip()

        entries.append(SitemapEntry(url=loc_node.text.strip(), lastmod=lastmod))

    return entries


def fetch_sitemap_entries(sitemap_url: str) -> list[SitemapEntry]:
    headers = {
        "User-Agent": CRAWLER_USER_AGENT,
        "Accept": "application/xml, text/xml, */*",
    }
    with httpx.Client(timeout=20.0, follow_redirects=True, headers=headers) as client:
        return fetch_sitemap_entries_with_client(client, sitemap_url)


def fetch_sitemap_entries_with_client(client: httpx.Client, sitemap_url: str) -> list[SitemapEntry]:
    response = client.get(sitemap_url)
    response.raise_for_status()

    root = ET.fromstring(response.text)
    nested_sitemaps = root.findall("sm:sitemap/sm:loc", SITEMAP_NAMESPACE)
    if not nested_sitemaps:
        return parse_sitemap(response.text)

    entries: list[SitemapEntry] = []
    for sitemap_node in nested_sitemaps:
        if sitemap_node.text:
            entries.extend(fetch_sitemap_entries_with_client(client, sitemap_node.text.strip()))
    return entries


def is_article_url(source: Source, url: str) -> bool:
    source_host = urlparse(source.site_url or "").netloc
    parsed = urlparse(url)
    if source_host and parsed.netloc != source_host:
        return False

    pattern = SOURCE_ARTICLE_PATH_PATTERNS.get(source.slug, ARTICLE_PATH_PATTERN)
    return bool(pattern.search(parsed.path))


def parse_datetime(value: str | None) -> datetime | None:
    if not value:
        return None

    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        pass

    try:
        parsed = parsedate_to_datetime(value)
    except (TypeError, ValueError):
        return None

    if parsed.tzinfo is None:
        return parsed.replace(tzinfo=UTC)
    return parsed


def meta_content(soup: BeautifulSoup, *selectors: tuple[str, str]) -> str | None:
    for attr, value in selectors:
        node = soup.find("meta", attrs={attr: value})
        content = node.get("content") if node else None
        if isinstance(content, str) and content.strip():
            return content.strip()
    return None


def clean_title(value: str | None) -> str | None:
    if not value:
        return None
    return re.sub(r"\s+", " ", value).strip()


def extract_article_payload(url: str, html: str, lastmod: str | None) -> dict[str, Any]:
    soup = BeautifulSoup(html, "html.parser")
    document = Document(html)
    readable_html = document.summary(html_partial=True)
    content_text = clean_feed_text(readable_html)

    title = clean_title(
        meta_content(soup, ("property", "og:title"), ("name", "twitter:title"))
        or document.short_title()
        or (soup.title.get_text(" ", strip=True) if soup.title else None)
    )
    if not title:
        title = url

    summary = clean_feed_text(
        meta_content(soup, ("property", "og:description"), ("name", "description")) or ""
    )
    published_at = parse_datetime(
        meta_content(
            soup,
            ("property", "article:published_time"),
            ("name", "article:published_time"),
            ("property", "og:updated_time"),
        )
        or lastmod
    )
    author = meta_content(soup, ("name", "author"), ("property", "article:author"))

    return {
        "url": url,
        "title": title,
        "author": author,
        "published_at": published_at,
        "summary": summary or None,
        "content_html": readable_html,
        "content_text": content_text or None,
        "raw_metadata": {
            "sitemap_lastmod": lastmod,
            "collection_strategy": "sitemap",
        },
    }


def fetch_article_payload(client: httpx.Client, entry: SitemapEntry) -> dict[str, Any]:
    response = client.get(entry.url)
    response.raise_for_status()
    return extract_article_payload(entry.url, response.text, entry.lastmod)


def upsert_article_payload(
    db: Session, source: Source, payload: dict[str, Any], collected_at: datetime
) -> str:
    article = db.scalar(select(Article).where(Article.url == payload["url"]))

    if article is None:
        article = Article(
            source_id=source.id,
            url=payload["url"],
            title=payload["title"],
            author=payload["author"],
            published_at=payload["published_at"],
            summary=payload["summary"],
            content_html=payload["content_html"],
            content_text=payload["content_text"],
            raw_metadata=payload["raw_metadata"],
            collected_at=collected_at,
        )
        db.add(article)
        return "created"

    changes = {
        "source_id": source.id,
        "title": payload["title"],
        "author": payload["author"],
        "published_at": payload["published_at"],
        "summary": payload["summary"],
        "content_html": payload["content_html"],
        "content_text": payload["content_text"],
        "raw_metadata": payload["raw_metadata"],
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


def crawl_sitemap_source(
    db: Session, source: Source, limit: int | None = None
) -> SitemapCrawlSummary:
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
        if source.collection_strategy != "sitemap":
            raise ValueError(
                f"Unsupported collection strategy for sitemap crawler: {source.collection_strategy}"
            )
        if not source.feed_url:
            raise ValueError("Sitemap source is missing feed_url")

        entries = []
        for entry in fetch_sitemap_entries(source.feed_url):
            if is_article_url(source, entry.url):
                entries.append(entry)
        if limit is not None:
            entries = entries[:limit]

        fetched_count = len(entries)
        collected_at = datetime.now(UTC)
        headers = {
            "User-Agent": CRAWLER_USER_AGENT,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        }
        with httpx.Client(timeout=20.0, follow_redirects=True, headers=headers) as client:
            for entry in entries:
                try:
                    payload = fetch_article_payload(client, entry)
                    result = upsert_article_payload(db, source, payload, collected_at)
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
        "sitemap_url": source.feed_url,
        "collection_strategy": source.collection_strategy,
        "content_strategy": source.content_strategy,
    }

    return SitemapCrawlSummary(
        source_slug=source.slug,
        fetched_count=fetched_count,
        created_count=created_count,
        updated_count=updated_count,
        unchanged_count=unchanged_count,
        failed_count=failed_count,
        status=status,
    )


def crawl_sitemap_sources(
    limit: int | None = None, source_slug: str | None = None
) -> list[SitemapCrawlSummary]:
    with SessionLocal() as db:
        statement = (
            select(Source)
            .where(Source.enabled.is_(True), Source.collection_strategy == "sitemap")
            .order_by(Source.slug)
        )
        if source_slug is not None:
            statement = statement.where(Source.slug == source_slug)

        sources = list(db.scalars(statement))
        summaries = [crawl_sitemap_source(db, source, limit=limit) for source in sources]
        db.commit()

    return summaries


def main() -> None:
    parser = argparse.ArgumentParser(description="Crawl enabled sitemap sources.")
    parser.add_argument("--source", dest="source_slug", help="Crawl a single source slug.")
    parser.add_argument("--limit", type=int, help="Limit number of article URLs per source.")
    args = parser.parse_args()

    summaries = crawl_sitemap_sources(limit=args.limit, source_slug=args.source_slug)
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
