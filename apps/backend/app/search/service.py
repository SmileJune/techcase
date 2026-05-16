from typing import Any

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
        query={
            "multi_match": {
                "query": normalized_query,
                "fields": SEARCH_FIELDS,
                "type": "best_fields",
                "operator": "and",
            }
        },
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

