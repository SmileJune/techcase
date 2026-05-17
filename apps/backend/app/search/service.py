import re
from typing import Any, Literal

from app.keywords.dictionaries import KEYWORD_RULES, KeywordRule
from app.search.client import get_elasticsearch_client
from app.search.indexes import ARTICLES_INDEX

SearchSort = Literal["relevance", "latest"]
KEYWORD_LABEL_BY_NORMALIZED = {rule.keyword.casefold(): rule.keyword for rule in KEYWORD_RULES}
GENERIC_FACET_VALUES = {
    "java",
    "search",
    "observability",
}
CONTENT_TYPE_RANKING_WEIGHTS = {
    "technical_case": 30,
    "engineering_story": 15,
    "tutorial": 8,
}

FACET_AGGREGATIONS = {
    "sources": {
        "terms": {"field": "sourceSlug", "size": 18},
        "aggs": {
            "sample": {
                "top_hits": {
                    "size": 1,
                    "_source": ["company", "source", "sourceSlug"],
                }
            }
        },
    },
    "technologies": {"terms": {"field": "technologies", "size": 32}},
    "problemKeywords": {"terms": {"field": "problemKeywords", "size": 18}},
    "contentTypes": {"terms": {"field": "contentType", "size": 10}},
}

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


def search_articles(
    query: str,
    size: int = 20,
    sort: SearchSort = "relevance",
    sources: list[str] | None = None,
    technologies: list[str] | None = None,
    problem_keywords: list[str] | None = None,
    content_types: list[str] | None = None,
) -> dict[str, Any]:
    client = get_elasticsearch_client()
    normalized_query = query.strip()
    filters = normalize_filters(
        sources=sources,
        technologies=technologies,
        problem_keywords=problem_keywords,
        content_types=content_types,
    )

    if not normalized_query:
        return empty_search_response(query, sort, filters)

    response = client.search(
        index=ARTICLES_INDEX,
        size=size,
        query=build_filtered_search_query(normalized_query, filters),
        sort=build_sort(sort),
        aggs=FACET_AGGREGATIONS,
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
        "sort": sort,
        "filters": filters,
        "facets": parse_facets(response.get("aggregations", {}), normalized_query),
        "total": total_value,
        "items": [hit_to_item(hit) for hit in hits],
    }


def empty_search_response(
    query: str, sort: SearchSort, filters: dict[str, list[str]]
) -> dict[str, Any]:
    return {
        "query": query,
        "sort": sort,
        "filters": filters,
        "facets": empty_facets(),
        "total": 0,
        "items": [],
    }


def normalize_filters(
    sources: list[str] | None,
    technologies: list[str] | None,
    problem_keywords: list[str] | None,
    content_types: list[str] | None,
) -> dict[str, list[str]]:
    return {
        "sources": clean_values(sources),
        "technologies": clean_values(technologies),
        "problemKeywords": clean_values(problem_keywords),
        "contentTypes": clean_values(content_types),
    }


def clean_values(values: list[str] | None) -> list[str]:
    if not values:
        return []

    cleaned_values = []
    seen = set()
    for value in values:
        cleaned = value.strip()
        normalized = cleaned.casefold()
        if not cleaned or normalized in seen:
            continue

        seen.add(normalized)
        cleaned_values.append(cleaned)

    return cleaned_values


def build_filtered_search_query(query: str, filters: dict[str, list[str]]) -> dict[str, Any]:
    filter_clauses = build_filter_clauses(filters)

    if not filter_clauses:
        return build_search_query(query)

    return {
        "bool": {
            "must": [build_search_query(query)],
            "filter": filter_clauses,
        }
    }


def build_filter_clauses(filters: dict[str, list[str]]) -> list[dict[str, Any]]:
    clauses = []

    if filters["sources"]:
        clauses.append({"terms": {"sourceSlug": filters["sources"]}})

    if filters["technologies"]:
        clauses.append({"terms": {"technologies": term_values(filters["technologies"])}})

    if filters["problemKeywords"]:
        clauses.append({"terms": {"problemKeywords": term_values(filters["problemKeywords"])}})

    if filters["contentTypes"]:
        clauses.append({"terms": {"contentType": term_values(filters["contentTypes"])}})

    return clauses


def term_values(values: list[str]) -> list[str]:
    return sorted({value for value in values} | {value.casefold() for value in values})


def empty_facets() -> dict[str, list[dict[str, Any]]]:
    return {
        "sources": [],
        "technologies": [],
        "problemKeywords": [],
        "contentTypes": [],
    }


def parse_facets(
    aggregations: dict[str, Any], query: str = ""
) -> dict[str, list[dict[str, Any]]]:
    if not aggregations:
        return empty_facets()

    matched_keywords = matched_rule_keywords(query)

    return {
        "sources": parse_source_facets(aggregations.get("sources", {})),
        "technologies": parse_term_facets(
            aggregations.get("technologies", {}),
            matched_keywords=matched_keywords,
            limit=12,
        ),
        "problemKeywords": parse_term_facets(
            aggregations.get("problemKeywords", {}),
            matched_keywords=matched_keywords,
            limit=10,
        ),
        "contentTypes": parse_content_type_facets(aggregations.get("contentTypes", {})),
    }


def parse_source_facets(aggregation: dict[str, Any]) -> list[dict[str, Any]]:
    facets = []
    for bucket in aggregation.get("buckets", []):
        sample_hits = bucket.get("sample", {}).get("hits", {}).get("hits", [])
        source = sample_hits[0].get("_source", {}) if sample_hits else {}
        facets.append(
            {
                "value": bucket["key"],
                "label": source_facet_label(source, bucket["key"]),
                "count": bucket["doc_count"],
            }
        )

    return facets


def source_facet_label(source: dict[str, Any], fallback: str) -> str:
    company = source.get("company")
    source_name = source.get("source")

    if company == "AWS" and source_name:
        return source_name

    return company or source_name or fallback


def parse_term_facets(
    aggregation: dict[str, Any], matched_keywords: list[str], limit: int
) -> list[dict[str, Any]]:
    facets = []
    matched_values = {keyword.casefold() for keyword in matched_keywords}

    for bucket in aggregation.get("buckets", []):
        value = bucket["key"]
        label = keyword_label(value)
        is_recommended = value.casefold() in matched_values or label.casefold() in matched_values
        facets.append(
            {
                "value": bucket["key"],
                "label": label,
                "count": bucket["doc_count"],
                "isRecommended": is_recommended,
            }
        )

    return sorted(facets, key=facet_sort_key)[:limit]


def facet_sort_key(facet: dict[str, Any]) -> tuple[int, int, int, str]:
    value = str(facet["value"]).casefold()
    is_generic = value in GENERIC_FACET_VALUES

    return (
        0 if facet.get("isRecommended") else 1,
        1 if is_generic else 0,
        -int(facet["count"]),
        str(facet["label"]).casefold(),
    )


def keyword_label(value: str) -> str:
    return KEYWORD_LABEL_BY_NORMALIZED.get(value.casefold(), value)


def parse_content_type_facets(aggregation: dict[str, Any]) -> list[dict[str, Any]]:
    return [
        {
            "value": bucket["key"],
            "label": content_type_label(bucket["key"]),
            "count": bucket["doc_count"],
        }
        for bucket in aggregation.get("buckets", [])
    ]


def content_type_label(value: str) -> str:
    labels = {
        "technical_case": "기술 사례",
        "engineering_story": "엔지니어링 스토리",
        "tutorial": "튜토리얼",
        "release_note": "릴리스",
        "event": "이벤트",
        "recruiting": "채용",
        "interview": "인터뷰",
        "news": "뉴스",
        "other": "기타",
    }

    return labels.get(value, value)


def build_sort(sort: SearchSort) -> list[dict[str, Any]] | None:
    if sort == "latest":
        return [
            {"publishedAt": {"order": "desc", "missing": "_last"}},
            {"_score": {"order": "desc"}},
        ]

    return None


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

    base_query = {
        "bool": {
            "should": should_queries,
            "minimum_should_match": 1,
        }
    }

    return apply_content_type_ranking(base_query)


def apply_content_type_ranking(query: dict[str, Any]) -> dict[str, Any]:
    return {
        "function_score": {
            "query": query,
            "functions": [
                {
                    "filter": {"term": {"contentType": content_type}},
                    "weight": weight,
                }
                for content_type, weight in CONTENT_TYPE_RANKING_WEIGHTS.items()
            ],
            "score_mode": "sum",
            "boost_mode": "sum",
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

    term_values = sorted(
        {keyword for keyword in keywords} | {keyword.casefold() for keyword in keywords}
    )

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
