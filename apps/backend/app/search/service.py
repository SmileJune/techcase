import re
from typing import Any, Literal

from app.keywords.dictionaries import KEYWORD_RULES, KeywordRule
from app.search.client import get_elasticsearch_client
from app.search.indexes import ARTICLES_INDEX

SearchSort = Literal["relevance", "latest"]
KEYWORD_LABEL_BY_NORMALIZED = {rule.keyword.casefold(): rule.keyword for rule in KEYWORD_RULES}
QUERY_ONLY_KEYWORD_ALIASES = {
    "go": "Go",
    "next": "Next.js",
    "node": "Node.js",
}
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
    page: int = 1,
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

    effective_sort = "latest" if not normalized_query and sort == "relevance" else sort
    normalized_page = max(page, 1)
    offset = (normalized_page - 1) * size

    response = client.search(
        index=ARTICLES_INDEX,
        from_=offset,
        size=size,
        query=build_filtered_search_query(normalized_query, filters),
        sort=build_sort(effective_sort),
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
        "sort": effective_sort,
        "filters": filters,
        "facets": parse_facets(response.get("aggregations", {}), normalized_query),
        "total": total_value,
        "page": normalized_page,
        "pageSize": size,
        "totalPages": total_pages(total_value, size),
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
        "page": 1,
        "pageSize": 20,
        "totalPages": 0,
        "items": [],
    }


def total_pages(total: int, size: int) -> int:
    if total <= 0:
        return 0

    return (total + size - 1) // size


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
    base_query = build_search_query(query) if query else {"match_all": {}}

    if not filter_clauses:
        return base_query

    return {
        "bool": {
            "must": [base_query],
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
    if is_query_only_alias(query):
        return build_query_only_alias_search_query(query)

    expanded_query = expand_query(query)
    matched_keywords = matched_rule_keywords(query)
    term_keywords = term_match_keywords(query, matched_keywords)
    should_queries = [
        multi_match_query(query, operator="and", boost=4),
        phrase_match_query(query),
        keyword_terms_query(term_keywords),
        *intent_boost_queries(query, matched_keywords),
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


def build_query_only_alias_search_query(query: str) -> dict[str, Any]:
    expanded_query = expand_query(query)
    matched_keywords = matched_rule_keywords(query)
    should_queries = [
        keyword_terms_query(matched_keywords),
        canonical_keyword_match_query(matched_keywords),
        title_phrase_match_query(query),
    ]

    if expanded_query != query:
        should_queries.append(multi_match_query(expanded_query, operator="or", boost=1))

    base_query = {
        "bool": {
            "should": should_queries,
            "minimum_should_match": 1,
        }
    }

    return apply_content_type_ranking(base_query)


def is_query_only_alias(query: str) -> bool:
    return normalize_text(query) in QUERY_ONLY_KEYWORD_ALIASES


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


def title_phrase_match_query(query: str) -> dict[str, Any]:
    return {
        "multi_match": {
            "query": query,
            "fields": [
                "title^8",
                "summary^2",
            ],
            "type": "phrase",
            "slop": 1,
            "boost": 2,
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


def intent_boost_queries(query: str, matched_keywords: list[str]) -> list[dict[str, Any]]:
    normalized_query = normalize_text(query)
    normalized_keywords = {keyword.casefold() for keyword in matched_keywords}
    boosts: list[dict[str, Any]] = []

    if "apache kafka" in normalized_keywords and contains_any(
        normalized_query, ["검색", "search"]
    ):
        boosts.extend(search_kafka_intent_boost_queries())

    if contains_all(normalized_query, ["실시간", "검색"]) and contains_any(
        normalized_query, ["인덱싱", "색인", "indexing"]
    ):
        boosts.extend(realtime_search_indexing_boost_queries())

    if "search" in normalized_keywords and contains_any(
        normalized_query, ["개선", "품질", "quality", "relevance", "성능"]
    ):
        boosts.extend(search_quality_boost_queries())

    if "elasticsearch" in normalized_keywords and contains_any(
        normalized_query, ["인덱스", "index", "구조", "structure"]
    ):
        boosts.extend(elasticsearch_index_boost_queries())

    if "event-driven architecture" in normalized_keywords and contains_any(
        normalized_query, ["상품", "조회", "커머스", "commerce"]
    ):
        boosts.extend(event_driven_commerce_boost_queries())

    if "log platform" in normalized_keywords:
        boosts.extend(log_platform_boost_queries())

    return boosts


def search_kafka_intent_boost_queries() -> list[dict[str, Any]]:
    return [
        constant_score_boost(
            [title_phrase_filter("컬리 검색이 카프카")],
            boost=520,
        ),
        constant_score_boost(
            [title_phrase_filter("컬리 검색이 카프카를")],
            boost=620,
        ),
        constant_score_boost(
            [title_phrase_filter("검색플랫폼 연동기")],
            boost=500,
        ),
        constant_score_boost(
            [
                title_phrase_filter("이벤트 기반 적용 상품 조회 시스템"),
                keyword_field_terms_filter("technologies", ["Apache Kafka"]),
            ],
            boost=360,
        ),
        constant_score_boost(
            [
                keyword_field_terms_filter("technologies", ["Apache Kafka"]),
                text_phrase_filter("검색 시스템"),
            ],
            boost=160,
        ),
        constant_score_boost(
            [
                keyword_field_terms_filter("technologies", ["Apache Kafka"]),
                text_phrase_filter("검색 플랫폼"),
            ],
            boost=160,
        ),
        constant_score_boost(
            [
                keyword_field_terms_filter("technologies", ["Apache Kafka"]),
                text_phrase_filter("검색플랫폼"),
            ],
            boost=160,
        ),
        constant_score_boost(
            [
                keyword_field_terms_filter("technologies", ["Apache Kafka"]),
                text_phrase_filter("카프카 스트림즈"),
            ],
            boost=90,
        ),
    ]


def realtime_search_indexing_boost_queries() -> list[dict[str, Any]]:
    return [
        constant_score_boost(
            [title_phrase_filter("실시간 인덱싱")],
            boost=900,
        ),
        constant_score_boost(
            [title_phrase_filter("실시간 인덱싱을")],
            boost=700,
        ),
        constant_score_boost(
            [title_phrase_filter("인덱싱을 위한 Elasticsearch")],
            boost=700,
        ),
        constant_score_boost(
            [title_phrase_filter("검색플랫폼 연동기")],
            boost=220,
        ),
        constant_score_boost(
            [title_phrase_filter("컬리 검색이 카프카")],
            boost=180,
        ),
        constant_score_boost(
            [title_phrase_filter("컬리 검색이 카프카를")],
            boost=220,
        ),
        constant_score_boost(
            [title_phrase_filter("이벤트 기반 적용 상품 조회 시스템")],
            boost=180,
        ),
        constant_score_boost(
            [text_phrase_filter("실시간 인덱싱")],
            boost=180,
        ),
        constant_score_boost(
            [text_phrase_filter("실시간 검색")],
            boost=90,
        ),
        constant_score_boost(
            [
                keyword_field_terms_filter(
                    "technologies",
                    ["Elasticsearch", "Amazon OpenSearch Service", "search"],
                ),
                text_phrase_filter("인덱싱"),
            ],
            boost=180,
        ),
        constant_score_boost(
            [
                keyword_field_terms_filter(
                    "technologies",
                    ["Elasticsearch", "Amazon OpenSearch Service", "search"],
                ),
                text_phrase_filter("색인"),
            ],
            boost=180,
        ),
    ]


def search_quality_boost_queries() -> list[dict[str, Any]]:
    return [
        constant_score_boost(
            [title_phrase_filter("검색 성능 개선")],
            boost=460,
        ),
        constant_score_boost(
            [title_phrase_filter("검색 품질")],
            boost=420,
        ),
        constant_score_boost(
            [title_phrase_filter("search relevance")],
            boost=380,
        ),
        constant_score_boost(
            [title_phrase_filter("search architecture")],
            boost=260,
        ),
        constant_score_boost(
            [title_phrase_filter("Atlas Search 정렬이슈")],
            boost=260,
        ),
        constant_score_boost(
            [text_phrase_filter("검색 성능 개선")],
            boost=180,
        ),
        constant_score_boost(
            [text_phrase_filter("검색 품질 개선")],
            boost=180,
        ),
        constant_score_boost(
            [text_phrase_filter("search relevance")],
            boost=160,
        ),
    ]


def elasticsearch_index_boost_queries() -> list[dict[str, Any]]:
    return [
        constant_score_boost(
            [title_phrase_filter("Elasticsearch 인덱스 구조")],
            boost=680,
        ),
        constant_score_boost(
            [title_phrase_filter("실시간 인덱싱을 위한 Elasticsearch")],
            boost=560,
        ),
        constant_score_boost(
            [title_phrase_filter("Elasticsearch 병렬 테스트")],
            boost=180,
        ),
        constant_score_boost(
            [text_phrase_filter("Elasticsearch 인덱스 구조")],
            boost=220,
        ),
        constant_score_boost(
            [text_phrase_filter("검색 성능 개선")],
            boost=160,
        ),
    ]


def event_driven_commerce_boost_queries() -> list[dict[str, Any]]:
    return [
        constant_score_boost(
            [title_phrase_filter("이벤트 기반 적용 상품 조회 시스템")],
            boost=720,
        ),
        constant_score_boost(
            [title_phrase_filter("배민스토어에 이벤트 기반 아키텍처")],
            boost=320,
        ),
        constant_score_boost(
            [title_phrase_filter("이벤트 기반 통합 알림 플랫폼")],
            boost=420,
        ),
        constant_score_boost(
            [
                text_phrase_filter("상품 조회"),
                text_phrase_filter("이벤트 기반"),
            ],
            boost=260,
        ),
        constant_score_boost(
            [
                keyword_field_terms_filter(
                    "architectureKeywords", ["event-driven architecture"]
                ),
                text_phrase_filter("상품"),
            ],
            boost=160,
        ),
    ]


def log_platform_boost_queries() -> list[dict[str, Any]]:
    return [
        constant_score_boost(
            [title_phrase_filter("로그 파이프라인")],
            boost=360,
        ),
        constant_score_boost(
            [title_phrase_filter("로그를 ClickStack으로 실시간 처리")],
            boost=340,
        ),
        constant_score_boost(
            [title_phrase_filter("지능형 로그 파이프라인")],
            boost=320,
        ),
        constant_score_boost(
            [title_phrase_filter("로그 데이터로 유저 이해")],
            boost=260,
        ),
        constant_score_boost(
            [title_phrase_filter("로그를 기록")],
            boost=180,
        ),
        constant_score_boost(
            [text_phrase_filter("로깅 플랫폼")],
            boost=220,
        ),
        constant_score_boost(
            [text_phrase_filter("로그 파이프라인")],
            boost=180,
        ),
        constant_score_boost(
            [text_phrase_filter("로그 플랫폼")],
            boost=140,
        ),
        constant_score_boost(
            [text_phrase_filter("로그 시스템")],
            boost=100,
        ),
    ]


def constant_score_boost(filters: list[dict[str, Any]], boost: int) -> dict[str, Any]:
    return {
        "constant_score": {
            "filter": {"bool": {"must": filters}},
            "boost": boost,
        }
    }


def keyword_field_terms_filter(field: str, values: list[str]) -> dict[str, Any]:
    return {"terms": {field: term_values(values)}}


def text_phrase_filter(phrase: str) -> dict[str, Any]:
    return {
        "multi_match": {
            "query": phrase,
            "fields": [
                "title^5",
                "caseSummary^4",
                "caseProblem^3",
                "caseSolution^3",
                "summary^2",
                "content",
            ],
            "type": "phrase",
            "slop": 1,
        }
    }


def title_phrase_filter(phrase: str) -> dict[str, Any]:
    return {
        "match_phrase": {
            "title": {
                "query": phrase,
                "slop": 1,
            }
        }
    }


def contains_all(text: str, terms: list[str]) -> bool:
    return all(term in text for term in terms)


def contains_any(text: str, terms: list[str]) -> bool:
    return any(term in text for term in terms)


def matched_rule_keywords(query: str) -> list[str]:
    normalized_query = normalize_text(query)
    matched_keywords = {
        rule.keyword for rule in KEYWORD_RULES if matches_rule(normalized_query, rule)
    }

    query_only_keyword = QUERY_ONLY_KEYWORD_ALIASES.get(normalized_query)
    if query_only_keyword:
        matched_keywords.add(query_only_keyword)

    return sorted(matched_keywords)


def term_match_keywords(query: str, keywords: list[str]) -> list[str]:
    if is_single_token_query(query):
        return keywords

    return [keyword for keyword in keywords if keyword.casefold() not in GENERIC_FACET_VALUES]


def is_single_token_query(query: str) -> bool:
    return len(normalize_text(query).split()) == 1


def expand_query(query: str) -> str:
    normalized_query = normalize_text(query)
    expanded_terms = []

    for rule in KEYWORD_RULES:
        if not matches_rule(normalized_query, rule) and not matches_query_only_alias(
            normalized_query, rule
        ):
            continue

        search_alias = first_ascii_alias(rule)
        if search_alias and search_alias.casefold() not in normalized_query:
            expanded_terms.append(search_alias)

    if not expanded_terms:
        return query

    return " ".join([query, *sorted(set(expanded_terms))])


def matches_query_only_alias(normalized_query: str, rule: KeywordRule) -> bool:
    return QUERY_ONLY_KEYWORD_ALIASES.get(normalized_query) == rule.keyword


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
