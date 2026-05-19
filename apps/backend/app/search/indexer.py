from datetime import UTC, datetime

from elasticsearch import helpers
from sqlalchemy import select
from sqlalchemy.orm import joinedload

from app.db.session import SessionLocal
from app.models.article import Article
from app.search.client import get_elasticsearch_client
from app.search.documents import article_to_document
from app.search.indexes import ARTICLES_INDEX, ARTICLES_INDEX_SETTINGS


def ensure_articles_index() -> None:
    client = get_elasticsearch_client()
    if client.indices.exists(index=ARTICLES_INDEX):
        client.indices.put_mapping(
            index=ARTICLES_INDEX,
            properties=ARTICLES_INDEX_SETTINGS["mappings"]["properties"],
        )
        return

    client.indices.create(index=ARTICLES_INDEX, **ARTICLES_INDEX_SETTINGS)


def reset_articles_index() -> None:
    client = get_elasticsearch_client()
    if client.indices.exists(index=ARTICLES_INDEX):
        client.indices.delete(index=ARTICLES_INDEX)

    client.indices.create(index=ARTICLES_INDEX, **ARTICLES_INDEX_SETTINGS)


def article_actions(articles: list[Article]) -> list[dict[str, object]]:
    return [
        {
            "_op_type": "index",
            "_index": ARTICLES_INDEX,
            "_id": str(article.id),
            "_source": article_to_document(article),
        }
        for article in articles
    ]


def reindex_articles() -> int:
    reset_articles_index()
    client = get_elasticsearch_client()

    with SessionLocal() as db:
        articles = list(
            db.scalars(
                select(Article)
                .options(
                    joinedload(Article.source),
                    joinedload(Article.keywords),
                    joinedload(Article.summaries),
                )
                .order_by(Article.published_at.desc().nullslast())
            )
            .unique()
            .all()
        )

        if not articles:
            return 0

        helpers.bulk(client, article_actions(articles))
        indexed_at = datetime.now(UTC)
        for article in articles:
            article.indexed_at = indexed_at

        db.commit()

    return len(articles)


def main() -> None:
    indexed_count = reindex_articles()
    print(f"Indexed articles: {indexed_count}")


if __name__ == "__main__":
    main()
