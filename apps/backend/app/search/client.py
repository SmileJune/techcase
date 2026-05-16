from functools import lru_cache

from elasticsearch import Elasticsearch

from app.config import get_settings


@lru_cache
def get_elasticsearch_client() -> Elasticsearch:
    settings = get_settings()
    return Elasticsearch(settings.elasticsearch_url)

