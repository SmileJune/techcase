from __future__ import annotations

import re
from dataclasses import dataclass

from sqlalchemy import delete, select
from sqlalchemy.orm import joinedload

from app.db.session import SessionLocal
from app.keywords.dictionaries import KEYWORD_RULES, KeywordRule
from app.models.article import Article
from app.models.article_keyword import ArticleKeyword

MATCHED_BY = "dictionary_v1"
TITLE_ONLY_ALIASES = {
    "Go": ("go",),
}


@dataclass(frozen=True)
class ExtractedKeyword:
    keyword: str
    keyword_type: str
    confidence: float


def extract_keywords(article: Article) -> list[ExtractedKeyword]:
    text_parts = [
        ("title", article.title or ""),
        ("summary", article.summary or ""),
        ("content", article.content_text or ""),
    ]
    extracted: dict[tuple[str, str], ExtractedKeyword] = {}

    for rule in KEYWORD_RULES:
        for field_name, text in text_parts:
            if not text:
                continue

            if matches_rule(text, rule):
                key = (rule.keyword, rule.keyword_type)
                confidence = confidence_for_field(field_name)
                previous = extracted.get(key)
                if previous is None or previous.confidence < confidence:
                    extracted[key] = ExtractedKeyword(
                        keyword=rule.keyword,
                        keyword_type=rule.keyword_type,
                        confidence=confidence,
                    )

            if field_name == "title" and matches_title_only_alias(text, rule):
                key = (rule.keyword, rule.keyword_type)
                previous = extracted.get(key)
                if previous is None or previous.confidence < 0.95:
                    extracted[key] = ExtractedKeyword(
                        keyword=rule.keyword,
                        keyword_type=rule.keyword_type,
                        confidence=0.95,
                    )

    return sorted(extracted.values(), key=lambda item: (item.keyword_type, item.keyword))


def matches_rule(text: str, rule: KeywordRule) -> bool:
    normalized_text = normalize_text(text)
    return any(contains_alias(normalized_text, alias) for alias in rule.aliases)


def matches_title_only_alias(text: str, rule: KeywordRule) -> bool:
    normalized_text = normalize_text(text)
    return any(
        contains_alias(normalized_text, alias)
        for alias in TITLE_ONLY_ALIASES.get(rule.keyword, ())
    )


def normalize_text(value: str) -> str:
    return re.sub(r"\s+", " ", value.casefold())


def contains_alias(text: str, alias: str) -> bool:
    normalized_alias = normalize_text(alias)
    pattern = rf"(?<![a-z0-9]){re.escape(normalized_alias)}(?![a-z0-9])"
    return re.search(pattern, text) is not None


def confidence_for_field(field_name: str) -> float:
    if field_name == "title":
        return 0.95
    if field_name == "summary":
        return 0.85
    return 0.75


def replace_article_keywords(article: Article, extracted_keywords: list[ExtractedKeyword]) -> None:
    article.keywords = [
        keyword for keyword in article.keywords if keyword.matched_by != MATCHED_BY
    ]
    article.keywords.extend(
        ArticleKeyword(
            keyword=keyword.keyword,
            keyword_type=keyword.keyword_type,
            confidence=keyword.confidence,
            matched_by=MATCHED_BY,
        )
        for keyword in extracted_keywords
    )


def extract_all_keywords() -> tuple[int, int]:
    with SessionLocal() as db:
        db.execute(delete(ArticleKeyword).where(ArticleKeyword.matched_by == MATCHED_BY))
        articles = list(
            db.scalars(
                select(Article)
                .options(joinedload(Article.keywords))
                .order_by(Article.published_at.desc().nullslast())
            )
            .unique()
            .all()
        )

        keyword_count = 0
        for article in articles:
            extracted_keywords = extract_keywords(article)
            replace_article_keywords(article, extracted_keywords)
            keyword_count += len(extracted_keywords)

        db.commit()
        return len(articles), keyword_count


def main() -> None:
    article_count, keyword_count = extract_all_keywords()
    print(f"Extracted keywords: articles={article_count}, keywords={keyword_count}")


if __name__ == "__main__":
    main()
