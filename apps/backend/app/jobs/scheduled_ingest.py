from __future__ import annotations

import argparse
from dataclasses import dataclass
from datetime import UTC, datetime

from app.config import get_settings
from app.crawler.rss import CrawlSummary, crawl_enabled_sources
from app.keywords.extractor import extract_all_keywords
from app.search.indexer import reindex_articles
from app.search.suggestions import reindex_suggestions
from app.summaries.generator import DEFAULT_PROMPT_VERSION, generate_summaries


@dataclass(frozen=True)
class ScheduledIngestResult:
    crawl_summaries: list[CrawlSummary]
    keyword_article_count: int
    keyword_count: int
    selected_summary_count: int
    generated_summary_count: int
    failed_summary_count: int
    indexed_count: int
    suggestion_indexed_count: int


def run_scheduled_ingest(
    *,
    source_slug: str | None,
    source_limit: int | None,
    summary_limit: int,
    skip_llm: bool,
    prompt_version: str,
    model: str,
) -> ScheduledIngestResult:
    started_at = datetime.now(UTC)
    crawl_summaries = crawl_enabled_sources(limit=source_limit, source_slug=source_slug)
    changed_article_count = sum(
        summary.created_count + summary.updated_count for summary in crawl_summaries
    )

    if changed_article_count == 0:
        return ScheduledIngestResult(
            crawl_summaries=crawl_summaries,
            keyword_article_count=0,
            keyword_count=0,
            selected_summary_count=0,
            generated_summary_count=0,
            failed_summary_count=0,
            indexed_count=0,
            suggestion_indexed_count=0,
        )

    keyword_article_count, keyword_count = extract_all_keywords()

    selected_summary_count = 0
    generated_summary_count = 0
    failed_summary_count = 0
    created_article_count = sum(summary.created_count for summary in crawl_summaries)

    if not skip_llm and created_article_count > 0 and summary_limit > 0:
        selected_summary_count, generated_summary_count, failed_summary_count = (
            generate_summaries(
                limit=summary_limit,
                source_slug=source_slug,
                dry_run=False,
                force=False,
                prompt_version=prompt_version,
                model=model,
                created_after=started_at,
            )
        )

    indexed_count = reindex_articles()
    suggestion_indexed_count = reindex_suggestions()

    return ScheduledIngestResult(
        crawl_summaries=crawl_summaries,
        keyword_article_count=keyword_article_count,
        keyword_count=keyword_count,
        selected_summary_count=selected_summary_count,
        generated_summary_count=generated_summary_count,
        failed_summary_count=failed_summary_count,
        indexed_count=indexed_count,
        suggestion_indexed_count=suggestion_indexed_count,
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Crawl RSS sources and enrich newly created articles for scheduled runs."
    )
    parser.add_argument("--source", dest="source_slug", help="Run one source slug only.")
    parser.add_argument("--source-limit", type=int, help="Limit number of RSS sources.")
    parser.add_argument(
        "--summary-limit",
        type=int,
        default=20,
        help="Maximum number of newly created articles to summarize.",
    )
    parser.add_argument("--skip-llm", action="store_true", help="Skip LLM summary generation.")
    parser.add_argument("--prompt-version", default=DEFAULT_PROMPT_VERSION)
    parser.add_argument("--model", default=get_settings().openai_model)
    return parser.parse_args()


def print_result(result: ScheduledIngestResult) -> None:
    print("Scheduled ingest completed")

    for summary in result.crawl_summaries:
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

    print(
        "Post process: "
        f"keyword_articles={result.keyword_article_count}, "
        f"keywords={result.keyword_count}, "
        f"summary_selected={result.selected_summary_count}, "
        f"summary_generated={result.generated_summary_count}, "
        f"summary_failed={result.failed_summary_count}, "
        f"indexed={result.indexed_count}, "
        f"suggestions_indexed={result.suggestion_indexed_count}"
    )


def main() -> None:
    args = parse_args()
    result = run_scheduled_ingest(
        source_slug=args.source_slug,
        source_limit=args.source_limit,
        summary_limit=args.summary_limit,
        skip_llm=args.skip_llm,
        prompt_version=args.prompt_version,
        model=args.model,
    )
    print_result(result)


if __name__ == "__main__":
    main()
