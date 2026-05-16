ARTICLES_INDEX = "articles"

ARTICLES_INDEX_SETTINGS = {
    "settings": {
        "number_of_shards": 1,
        "number_of_replicas": 0,
        "analysis": {
            "normalizer": {
                "lowercase_normalizer": {
                    "type": "custom",
                    "filter": ["lowercase"],
                }
            }
        },
    },
    "mappings": {
        "dynamic": "strict",
        "properties": {
            "id": {"type": "keyword"},
            "title": {"type": "text"},
            "url": {"type": "keyword"},
            "company": {"type": "keyword", "normalizer": "lowercase_normalizer"},
            "source": {"type": "keyword", "normalizer": "lowercase_normalizer"},
            "sourceSlug": {"type": "keyword"},
            "publishedAt": {"type": "date"},
            "summary": {"type": "text"},
            "caseSummary": {"type": "text"},
            "caseProblem": {"type": "text"},
            "caseSolution": {"type": "text"},
            "content": {"type": "text"},
            "technologies": {"type": "keyword", "normalizer": "lowercase_normalizer"},
            "architectureKeywords": {"type": "keyword", "normalizer": "lowercase_normalizer"},
            "problemKeywords": {"type": "keyword", "normalizer": "lowercase_normalizer"},
        },
    },
}
