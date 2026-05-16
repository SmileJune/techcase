from dataclasses import dataclass
from typing import Any

from elasticsearch import helpers
from sqlalchemy import func, select

from app.db.session import SessionLocal
from app.keywords.dictionaries import KEYWORD_RULES, KeywordRule
from app.models.article import Article
from app.models.article_keyword import ArticleKeyword
from app.models.source import Source
from app.search.client import get_elasticsearch_client
from app.search.indexes import SUGGESTIONS_INDEX, SUGGESTIONS_INDEX_SETTINGS


TYPE_BASE_WEIGHTS = {
    "aws_service": 130,
    "technology": 125,
    "architecture": 105,
    "problem": 100,
    "company": 80,
}

TYPE_LABELS = {
    "aws_service": "AWS 서비스",
    "technology": "기술",
    "architecture": "아키텍처",
    "problem": "문제 상황",
    "company": "회사",
}


@dataclass(frozen=True)
class SuggestionCandidate:
    id: str
    label: str
    type: str
    aliases: tuple[str, ...]
    article_count: int


def ensure_suggestions_index() -> None:
    client = get_elasticsearch_client()
    if client.indices.exists(index=SUGGESTIONS_INDEX):
        client.indices.put_mapping(
            index=SUGGESTIONS_INDEX,
            properties=SUGGESTIONS_INDEX_SETTINGS["mappings"]["properties"],
        )
        return

    client.indices.create(index=SUGGESTIONS_INDEX, **SUGGESTIONS_INDEX_SETTINGS)


def suggestion_actions(candidates: list[SuggestionCandidate]) -> list[dict[str, Any]]:
    return [
        {
            "_op_type": "index",
            "_index": SUGGESTIONS_INDEX,
            "_id": candidate.id,
            "_source": suggestion_document(candidate),
        }
        for candidate in candidates
    ]


def suggestion_document(candidate: SuggestionCandidate) -> dict[str, Any]:
    inputs = unique_values([candidate.label, *candidate.aliases])
    weight = TYPE_BASE_WEIGHTS.get(candidate.type, 50) + min(candidate.article_count, 50)

    return {
        "id": candidate.id,
        "label": candidate.label,
        "type": candidate.type,
        "description": TYPE_LABELS.get(candidate.type, candidate.type),
        "aliases": inputs,
        "articleCount": candidate.article_count,
        "suggest": {
            "input": inputs,
            "weight": weight,
        },
    }


def build_keyword_candidates(keyword_counts: dict[tuple[str, str], int]) -> list[SuggestionCandidate]:
    return [
        SuggestionCandidate(
            id=f"{rule.keyword_type}:{slugify_id(rule.keyword)}",
            label=rule.keyword,
            type=rule.keyword_type,
            aliases=rule.aliases,
            article_count=keyword_counts.get((rule.keyword_type, rule.keyword), 0),
        )
        for rule in KEYWORD_RULES
    ]


def build_company_candidates() -> list[SuggestionCandidate]:
    with SessionLocal() as db:
        rows = db.execute(
            select(Source.company_name, func.count(Article.id))
            .join(Article, Article.source_id == Source.id)
            .where(Source.enabled.is_(True))
            .group_by(Source.company_name)
            .order_by(Source.company_name)
        ).all()

    return [
        SuggestionCandidate(
            id=f"company:{slugify_id(company_name)}",
            label=company_name,
            type="company",
            aliases=(company_name,),
            article_count=int(source_count),
        )
        for company_name, source_count in rows
    ]


def keyword_counts() -> dict[tuple[str, str], int]:
    with SessionLocal() as db:
        rows = db.execute(
            select(
                ArticleKeyword.keyword_type,
                ArticleKeyword.keyword,
                func.count(ArticleKeyword.article_id.distinct()),
            ).group_by(ArticleKeyword.keyword_type, ArticleKeyword.keyword)
        ).all()

    return {
        (keyword_type, keyword): int(count)
        for keyword_type, keyword, count in rows
    }


def reindex_suggestions() -> int:
    ensure_suggestions_index()
    client = get_elasticsearch_client()
    candidates = [
        *build_keyword_candidates(keyword_counts()),
        *build_company_candidates(),
    ]

    if not candidates:
        return 0

    helpers.bulk(client, suggestion_actions(candidates))
    return len(candidates)


def suggest(query: str, size: int = 8) -> dict[str, Any]:
    normalized_query = query.strip()

    if not normalized_query:
        return {"query": query, "items": []}

    client = get_elasticsearch_client()
    response = client.search(
        index=SUGGESTIONS_INDEX,
        suggest={
            "techcase-suggest": {
                "prefix": normalized_query,
                "completion": {
                    "field": "suggest",
                    "size": size,
                    "skip_duplicates": True,
                    "fuzzy": {
                        "fuzziness": "AUTO",
                        "min_length": 4,
                        "prefix_length": 2,
                    },
                },
            }
        },
    )
    options = response["suggest"]["techcase-suggest"][0]["options"]

    return {
        "query": query,
        "items": [suggestion_hit_to_item(option) for option in options],
    }


def suggestion_hit_to_item(option: dict[str, Any]) -> dict[str, Any]:
    source = option["_source"]
    return {
        "id": source["id"],
        "label": source["label"],
        "type": source["type"],
        "description": source["description"],
        "aliases": source.get("aliases", []),
        "articleCount": source.get("articleCount", 0),
        "score": option["_score"],
    }


def unique_values(values: list[str]) -> list[str]:
    seen = set()
    result = []

    for value in values:
        normalized = value.strip()
        key = normalized.casefold()

        if not normalized or key in seen:
            continue

        seen.add(key)
        result.append(normalized)

    return result


def slugify_id(value: str) -> str:
    return "-".join(value.casefold().replace("/", " ").split())


def main() -> None:
    indexed_count = reindex_suggestions()
    print(f"Indexed suggestions: {indexed_count}")


if __name__ == "__main__":
    main()
