from __future__ import annotations

import argparse
import re
from collections import defaultdict
from dataclasses import dataclass, field
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import joinedload

from app.db.session import SessionLocal
from app.keywords.dictionaries import KEYWORD_RULES
from app.models.article import Article
from app.models.article_summary import ArticleSummary
from app.models.source import Source


ACRONYM_PATTERN = re.compile(r"(?<![A-Za-z0-9])([A-Z][A-Z0-9+#.]{1,14})(?![A-Za-z0-9])")
TECH_TOKEN_PATTERN = re.compile(
    r"(?<![A-Za-z0-9])([A-Za-z][A-Za-z0-9]+(?:[.-][A-Za-z0-9]+)+)(?![A-Za-z0-9])"
)

STOPWORDS = {
    "AI",
    "API",
    "AWS",
    "CD",
    "CI",
    "CLI",
    "CPU",
    "DB",
    "DNS",
    "FROM",
    "FAQ",
    "HTTP",
    "HTTPS",
    "ID",
    "IDC",
    "IT",
    "IP",
    "JSON",
    "MVP",
    "OS",
    "PDF",
    "PM",
    "PC",
    "PR",
    "QA",
    "RSS",
    "SDK",
    "SQL",
    "SSL",
    "SELECT",
    "TCP",
    "TLS",
    "UI",
    "URL",
    "UX",
    "XML",
}


@dataclass
class CandidateStats:
    label: str
    articles: set[UUID] = field(default_factory=set)
    examples: list[str] = field(default_factory=list)
    sources: set[str] = field(default_factory=set)


def known_terms() -> set[str]:
    terms = set()

    for rule in KEYWORD_RULES:
        terms.add(normalize_candidate(rule.keyword))
        for alias in rule.aliases:
            terms.add(normalize_candidate(alias))

    with SessionLocal() as db:
        source_rows = db.execute(select(Source.company_name, Source.name)).all()

    for company_name, source_name in source_rows:
        terms.add(normalize_candidate(company_name))
        terms.add(normalize_candidate(source_name))

    return {term for term in terms if term}


def audit_suggestions(*, min_articles: int, limit: int) -> list[CandidateStats]:
    known = known_terms()
    candidates: dict[str, CandidateStats] = {}

    with SessionLocal() as db:
        articles = list(
            db.scalars(
                select(Article)
                .options(joinedload(Article.source), joinedload(Article.summaries))
                .order_by(Article.published_at.desc().nullslast())
            )
            .unique()
            .all()
        )

    for article in articles:
        text = "\n".join(
            [
                article.title or "",
                article.summary or "",
                article.content_text or "",
                *summary_text_parts(article.summaries),
            ]
        )

        for label in extract_candidate_labels(text, article.summaries):
            normalized = normalize_candidate(label)

            if not should_keep_candidate(label, normalized, known):
                continue

            stats = candidates.setdefault(normalized, CandidateStats(label=display_label(label)))
            stats.articles.add(article.id)
            stats.sources.add(article.source.name)

            if len(stats.examples) < 3:
                stats.examples.append(article.title)

    return sorted(
        (
            stats
            for stats in candidates.values()
            if len(stats.articles) >= min_articles
        ),
        key=lambda stats: (-len(stats.articles), stats.label.casefold()),
    )[:limit]


def summary_text_parts(summaries: list[ArticleSummary]) -> list[str]:
    parts: list[str] = []

    for summary in summaries:
        parts.extend(summary.technologies or [])
        parts.extend(summary.architecture_keywords or [])
        parts.extend(summary.problem_keywords or [])

    return parts


def extract_candidate_labels(text: str, summaries: list[ArticleSummary]) -> set[str]:
    labels = set()

    labels.update(match.group(1) for match in ACRONYM_PATTERN.finditer(text))
    labels.update(match.group(1) for match in TECH_TOKEN_PATTERN.finditer(text))

    for summary in summaries:
        labels.update(summary.technologies or [])

    return labels


def should_keep_candidate(label: str, normalized: str, known: set[str]) -> bool:
    if not normalized or normalized in known:
        return False

    if display_label(label).upper() in STOPWORDS:
        return False

    if ".com" in normalized or ".net" in normalized or ".org" in normalized:
        return False

    if len(normalized) < 2:
        return False

    return True


def normalize_candidate(value: str) -> str:
    return re.sub(r"[^a-z0-9+#.]+", "", value.casefold())


def display_label(value: str) -> str:
    return re.sub(r"\s+", " ", value.strip())


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Find repeated technology-like terms missing from suggestion rules."
    )
    parser.add_argument("--min-articles", type=int, default=3)
    parser.add_argument("--limit", type=int, default=30)
    return parser.parse_args()


def print_audit(candidates: list[CandidateStats]) -> None:
    if not candidates:
        print("No potential missing suggestions found.")
        return

    print("Potential missing suggestions")
    print()
    print(f"{'candidate':<28} {'articles':>8}  sources")
    print("-" * 72)

    for candidate in candidates:
        sources = ", ".join(sorted(candidate.sources)[:3])
        print(f"{candidate.label:<28} {len(candidate.articles):>8}  {sources}")
        for example in candidate.examples:
            print(f"  - {example}")


def main() -> None:
    args = parse_args()
    print_audit(audit_suggestions(min_articles=args.min_articles, limit=args.limit))


if __name__ == "__main__":
    main()
