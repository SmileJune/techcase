from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import httpx
from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload

from app.config import get_settings
from app.db.session import SessionLocal
from app.models.article import Article
from app.models.article_summary import ArticleSummary
from app.models.source import Source

SUMMARY_TYPE = "case_summary"
DEFAULT_LANGUAGE = "ko"
DEFAULT_PROMPT_VERSION = "case-summary-v1"
PROMPT_PATH = Path(__file__).parent / "prompts" / "case_summary_v1.md"
MAX_CONTENT_CHARS = 12000
ALLOWED_CONTENT_TYPES = {
    "technical_case",
    "engineering_story",
    "tutorial",
    "release_note",
    "event",
    "recruiting",
    "interview",
    "news",
    "other",
}


@dataclass(frozen=True)
class SummaryRequest:
    article: Article
    prompt_version: str
    model: str


def load_prompt() -> str:
    return PROMPT_PATH.read_text(encoding="utf-8")


def select_target_articles(
    db: Session,
    *,
    limit: int,
    source_slug: str | None,
    prompt_version: str,
    force: bool,
) -> list[Article]:
    statement = (
        select(Article)
        .join(Source)
        .options(
            joinedload(Article.source),
            joinedload(Article.keywords),
            joinedload(Article.summaries),
        )
        .order_by(Article.published_at.desc().nullslast())
    )

    if source_slug:
        statement = statement.where(Source.slug == source_slug)

    articles = list(db.scalars(statement).unique().all())
    if not force:
        articles = [
            article
            for article in articles
            if not has_current_summary(article, prompt_version=prompt_version)
        ]

    return articles[:limit]


def has_current_summary(article: Article, *, prompt_version: str) -> bool:
    return any(
        summary.summary_type == SUMMARY_TYPE
        and summary.language == DEFAULT_LANGUAGE
        and summary.prompt_version == prompt_version
        for summary in article.summaries
    )


def build_user_content(article: Article) -> str:
    keyword_values = sorted(
        {keyword.keyword for keyword in article.keywords if keyword.keyword}
    )
    content = article.content_text or article.summary or ""
    clipped_content = content[:MAX_CONTENT_CHARS]

    return "\n".join(
        [
            f"Title: {article.title}",
            f"Company: {article.source.company_name}",
            f"Source: {article.source.name}",
            f"URL: {article.url}",
            f"Published at: {article.published_at.isoformat() if article.published_at else ''}",
            f"Existing keywords: {', '.join(keyword_values)}",
            f"RSS summary: {article.summary or ''}",
            "Content:",
            clipped_content,
        ]
    )


def call_openai_json(system_prompt: str, user_content: str, model: str) -> dict[str, Any]:
    settings = get_settings()
    if not settings.openai_api_key:
        raise RuntimeError("OPENAI_API_KEY is required unless --dry-run is used.")

    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_content},
        ],
        "response_format": {"type": "json_object"},
        "temperature": 0.2,
    }
    headers = {
        "Authorization": f"Bearer {settings.openai_api_key}",
        "Content-Type": "application/json",
    }

    with httpx.Client(timeout=60.0) as client:
        response = client.post(
            "https://api.openai.com/v1/chat/completions",
            headers=headers,
            json=payload,
        )
        response.raise_for_status()

    raw_response = response.json()
    content = raw_response["choices"][0]["message"]["content"]
    parsed = json.loads(content)
    parsed["_raw_openai_response"] = raw_response
    return parsed


def upsert_summary(
    db: Session,
    article: Article,
    *,
    parsed: dict[str, Any],
    prompt_version: str,
    model: str,
) -> None:
    summary = next(
        (
            item
            for item in article.summaries
            if item.summary_type == SUMMARY_TYPE
            and item.language == DEFAULT_LANGUAGE
            and item.prompt_version == prompt_version
        ),
        None,
    )

    if summary is None:
        summary = ArticleSummary(
            article_id=article.id,
            summary_type=SUMMARY_TYPE,
            language=DEFAULT_LANGUAGE,
            model=model,
            prompt_version=prompt_version,
            case_summary=parsed["case_summary"],
        )
        db.add(summary)

    summary.model = model
    summary.content_type = normalize_content_type(parsed.get("content_type"))
    summary.case_summary = parsed["case_summary"]
    summary.problem = parsed.get("problem")
    summary.solution = parsed.get("solution")
    summary.technologies = list_or_none(parsed.get("technologies"))
    summary.architecture_keywords = list_or_none(parsed.get("architecture_keywords"))
    summary.problem_keywords = list_or_none(parsed.get("problem_keywords"))
    summary.confidence = (
        float(parsed["confidence"]) if parsed.get("confidence") is not None else None
    )
    summary.raw_response = parsed.get("_raw_openai_response", parsed)


def normalize_content_type(value: Any) -> str:
    if not isinstance(value, str):
        return "other"

    normalized = value.strip().casefold()
    if normalized not in ALLOWED_CONTENT_TYPES:
        return "other"

    return normalized


def validate_summary_response(parsed: dict[str, Any]) -> None:
    if not isinstance(parsed.get("case_summary"), str) or not parsed["case_summary"].strip():
        raise ValueError("LLM response is missing case_summary")

    if parsed.get("confidence") is not None:
        confidence = float(parsed["confidence"])
        if confidence < 0 or confidence > 1:
            raise ValueError("LLM response confidence must be between 0 and 1")


def list_or_none(value: Any) -> list[str] | None:
    if not isinstance(value, list):
        return None

    return [str(item) for item in value if item]


def generate_summaries(
    *,
    limit: int,
    source_slug: str | None,
    dry_run: bool,
    force: bool,
    prompt_version: str,
    model: str,
) -> tuple[int, int, int]:
    system_prompt = load_prompt()
    generated_count = 0
    failed_count = 0

    with SessionLocal() as db:
        articles = select_target_articles(
            db,
            limit=limit,
            source_slug=source_slug,
            prompt_version=prompt_version,
            force=force,
        )

        for article in articles:
            user_content = build_user_content(article)
            if dry_run:
                print_dry_run(article, system_prompt, user_content)
                continue

            try:
                parsed = call_openai_json(system_prompt, user_content, model)
                validate_summary_response(parsed)
                upsert_summary(
                    db,
                    article,
                    parsed=parsed,
                    prompt_version=prompt_version,
                    model=model,
                )
                db.commit()
                generated_count += 1
                print(f"Generated summary: {article.title}")
            except Exception as exc:
                db.rollback()
                failed_count += 1
                print(f"Failed summary: {article.title} ({exc})")

    return len(articles), generated_count, failed_count


def print_dry_run(article: Article, system_prompt: str, user_content: str) -> None:
    print("=" * 80)
    print(f"Article: {article.title}")
    print(f"URL: {article.url}")
    print("-" * 80)
    print(system_prompt[:1200])
    print("-" * 80)
    print(user_content[:2000])


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate LLM case summaries for articles.")
    parser.add_argument("--limit", type=int, default=5)
    parser.add_argument("--source", dest="source_slug")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--prompt-version", default=DEFAULT_PROMPT_VERSION)
    parser.add_argument("--model", default=get_settings().openai_model)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    selected_count, generated_count, failed_count = generate_summaries(
        limit=args.limit,
        source_slug=args.source_slug,
        dry_run=args.dry_run,
        force=args.force,
        prompt_version=args.prompt_version,
        model=args.model,
    )
    print(
        "LLM summaries: "
        f"selected={selected_count}, generated={generated_count}, failed={failed_count}"
    )


if __name__ == "__main__":
    main()
