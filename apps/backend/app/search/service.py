import re
from typing import Any

from app.keywords.dictionaries import KEYWORD_RULES, KeywordRule
from app.search.client import get_elasticsearch_client
from app.search.indexes import ARTICLES_INDEX

SEARCH_FIELDS = [
    "technologies^5",
    "title^4",
    "architectureKeywords^3",
    "problemKeywords^3",
    "summary^2",
    "content",
]


def search_articles(query: str, size: int = 20) -> dict[str, Any]:
    client = get_elasticsearch_client()
    normalized_query = query.strip()

    if not normalized_query:
        return {"query": query, "total": 0, "items": []}

    response = client.search(
        index=ARTICLES_INDEX,
        size=size,
        query=build_search_query(normalized_query),
        highlight={
            "fields": {
                "title": {},
                "summary": {},
                "content": {"fragment_size": 160, "number_of_fragments": 2},
            }
        },
    )

    hits = response["hits"]["hits"]
    total = response["hits"]["total"]
    total_value = total["value"] if isinstance(total, dict) else total

    return {
        "query": query,
        "total": total_value,
        "items": [hit_to_item(hit) for hit in hits],
    }


def build_search_query(query: str) -> dict[str, Any]:
    expanded_query = expand_query(query)
    exact_query = multi_match_query(query, operator="and", boost=4)

    if expanded_query == query:
        return exact_query

    return {
        "bool": {
            "should": [
                exact_query,
                multi_match_query(expanded_query, operator="or", boost=2),
            ],
            "minimum_should_match": 1,
        }
    }


def multi_match_query(query: str, operator: str, boost: int) -> dict[str, Any]:
    return {
        "multi_match": {
            "query": query,
            "fields": SEARCH_FIELDS,
            "type": "best_fields",
            "operator": operator,
            "boost": boost,
        }
    }


def expand_query(query: str) -> str:
    normalized_query = normalize_text(query)
    expanded_terms = []

    for rule in KEYWORD_RULES:
        if not matches_rule(normalized_query, rule):
            continue

        matched_non_ascii_alias = next(
            (
                alias
                for alias in rule.aliases
                if has_non_ascii(alias) and contains_alias(normalized_query, alias)
            ),
            None,
        )
        if matched_non_ascii_alias is None:
            continue

        search_alias = first_ascii_alias(rule)
        if search_alias and search_alias.casefold() not in normalized_query:
            expanded_terms.append(search_alias)

    if not expanded_terms:
        return query

    return " ".join([query, *sorted(set(expanded_terms))])


def matches_rule(normalized_query: str, rule: KeywordRule) -> bool:
    return any(contains_alias(normalized_query, alias) for alias in rule.aliases)


def first_ascii_alias(rule: KeywordRule) -> str | None:
    return next((alias for alias in rule.aliases if not has_non_ascii(alias)), None)


def has_non_ascii(value: str) -> bool:
    return any(ord(character) > 127 for character in value)


def normalize_text(value: str) -> str:
    return re.sub(r"\s+", " ", value.casefold())


def contains_alias(text: str, alias: str) -> bool:
    normalized_alias = normalize_text(alias)
    pattern = rf"(?<![a-z0-9]){re.escape(normalized_alias)}(?![a-z0-9])"
    return re.search(pattern, text) is not None


def hit_to_item(hit: dict[str, Any]) -> dict[str, Any]:
    source = hit["_source"]
    return {
        "id": source["id"],
        "title": source["title"],
        "url": source["url"],
        "company": source["company"],
        "source": source["source"],
        "sourceSlug": source["sourceSlug"],
        "publishedAt": source.get("publishedAt"),
        "summary": source.get("summary"),
        "score": hit["_score"],
        "technologies": source.get("technologies", []),
        "architectureKeywords": source.get("architectureKeywords", []),
        "problemKeywords": source.get("problemKeywords", []),
        "highlights": hit.get("highlight", {}),
    }
