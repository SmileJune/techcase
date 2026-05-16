import re
from typing import Any

from app.keywords.dictionaries import KEYWORD_RULES, KeywordRule
from app.search.client import get_elasticsearch_client
from app.search.indexes import ARTICLES_INDEX

SEARCH_FIELDS = [
    "technologies^5",
    "title^4",
    "caseSummary^4",
    "architectureKeywords^3",
    "problemKeywords^3",
    "caseProblem^3",
    "caseSolution^3",
    "summary^2",
    "content",
]

FUZZY_SEARCH_FIELDS = [
    "title^3",
    "caseSummary^3",
    "caseProblem^2",
    "caseSolution^2",
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
                "caseSummary": {},
                "caseProblem": {},
                "caseSolution": {},
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
    matched_keywords = matched_rule_keywords(query)
    should_queries = [
        multi_match_query(query, operator="and", boost=4),
        phrase_match_query(query),
        keyword_terms_query(matched_keywords),
    ]

    if matched_keywords:
        should_queries.append(canonical_keyword_match_query(matched_keywords))

    if expanded_query != query:
        should_queries.append(multi_match_query(expanded_query, operator="or", boost=2))

    if has_ascii_letter(query) and not matched_keywords:
        should_queries.append(fuzzy_match_query(query))

    return {
        "bool": {
            "should": should_queries,
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


def canonical_keyword_match_query(keywords: list[str]) -> dict[str, Any]:
    return {
        "bool": {
            "should": [
                {
                    "multi_match": {
                        "query": keyword,
                        "fields": [
                            "technologies^8",
                            "title^6",
                            "caseSummary^5",
                            "caseProblem^4",
                            "caseSolution^4",
                            "architectureKeywords^4",
                            "problemKeywords^4",
                            "summary^3",
                            "content",
                        ],
                        "type": "phrase",
                        "slop": 1,
                        "boost": 5,
                    }
                }
                for keyword in keywords
            ],
            "minimum_should_match": 1,
        }
    }


def fuzzy_match_query(query: str) -> dict[str, Any]:
    return {
        "multi_match": {
            "query": query,
            "fields": FUZZY_SEARCH_FIELDS,
            "type": "best_fields",
            "operator": "or",
            "fuzziness": "AUTO",
            "prefix_length": 2,
            "max_expansions": 30,
            "boost": 0.6,
        }
    }


def phrase_match_query(query: str) -> dict[str, Any]:
    return {
        "multi_match": {
            "query": query,
            "fields": [
                "title^6",
                "caseSummary^4",
                "caseProblem^4",
                "caseSolution^3",
                "summary^3",
                "content",
            ],
            "type": "phrase",
            "slop": 1,
            "boost": 3,
        }
    }


def keyword_terms_query(keywords: list[str]) -> dict[str, Any]:
    if not keywords:
        return {"match_none": {}}

    term_values = sorted({keyword for keyword in keywords} | {keyword.casefold() for keyword in keywords})

    return {
        "bool": {
            "should": [
                {"terms": {"technologies": term_values, "boost": 8}},
                {"terms": {"architectureKeywords": term_values, "boost": 7}},
                {"terms": {"problemKeywords": term_values, "boost": 7}},
            ],
            "minimum_should_match": 1,
        }
    }


def matched_rule_keywords(query: str) -> list[str]:
    normalized_query = normalize_text(query)
    return sorted(
        {rule.keyword for rule in KEYWORD_RULES if matches_rule(normalized_query, rule)}
    )


def expand_query(query: str) -> str:
    normalized_query = normalize_text(query)
    expanded_terms = []

    for rule in KEYWORD_RULES:
        if not matches_rule(normalized_query, rule):
            continue

        search_alias = first_ascii_alias(rule)
        if search_alias and search_alias.casefold() not in normalized_query:
            expanded_terms.append(search_alias)

    if not expanded_terms:
        return query

    return " ".join([query, *sorted(set(expanded_terms))])


def matches_rule(normalized_query: str, rule: KeywordRule) -> bool:
    return any(contains_alias(normalized_query, alias) for alias in rule.aliases) or any(
        fuzzy_contains_alias(normalized_query, alias) for alias in rule.aliases
    )


def first_ascii_alias(rule: KeywordRule) -> str | None:
    return next((alias for alias in rule.aliases if not has_non_ascii(alias)), None)


def has_non_ascii(value: str) -> bool:
    return any(ord(character) > 127 for character in value)


def has_ascii_letter(value: str) -> bool:
    return any(("a" <= character <= "z") or ("A" <= character <= "Z") for character in value)


def normalize_text(value: str) -> str:
    return re.sub(r"\s+", " ", value.casefold())


def contains_alias(text: str, alias: str) -> bool:
    normalized_alias = normalize_text(alias)
    pattern = rf"(?<![a-z0-9]){re.escape(normalized_alias)}(?![a-z0-9])"
    return re.search(pattern, text) is not None


def fuzzy_contains_alias(text: str, alias: str) -> bool:
    if has_non_ascii(alias) or not has_ascii_letter(text):
        return False

    compact_query = compact_ascii(text)
    compact_alias = compact_ascii(alias)

    if len(compact_query) < 6 or len(compact_alias) < 6:
        return False

    max_distance = 1 if len(compact_alias) < 10 else 2
    return levenshtein_distance_at_most(compact_query, compact_alias, max_distance)


def compact_ascii(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.casefold())


def levenshtein_distance_at_most(left: str, right: str, max_distance: int) -> bool:
    if abs(len(left) - len(right)) > max_distance:
        return False

    previous_row = list(range(len(right) + 1))

    for left_index, left_character in enumerate(left, start=1):
        current_row = [left_index]
        row_minimum = current_row[0]

        for right_index, right_character in enumerate(right, start=1):
            insertion_cost = current_row[right_index - 1] + 1
            deletion_cost = previous_row[right_index] + 1
            substitution_cost = previous_row[right_index - 1] + (
                0 if left_character == right_character else 1
            )
            cost = min(insertion_cost, deletion_cost, substitution_cost)
            current_row.append(cost)
            row_minimum = min(row_minimum, cost)

        if row_minimum > max_distance:
            return False

        previous_row = current_row

    return previous_row[-1] <= max_distance


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
        "caseSummary": source.get("caseSummary"),
        "caseProblem": source.get("caseProblem"),
        "caseSolution": source.get("caseSolution"),
        "contentType": source.get("contentType"),
        "score": hit["_score"],
        "technologies": source.get("technologies", []),
        "architectureKeywords": source.get("architectureKeywords", []),
        "problemKeywords": source.get("problemKeywords", []),
        "highlights": hit.get("highlight", {}),
    }
