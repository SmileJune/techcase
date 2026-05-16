from collections import defaultdict
from typing import Any

from app.models.article import Article

KEYWORD_FIELD_BY_TYPE = {
    "technology": "technologies",
    "aws_service": "technologies",
    "architecture": "architectureKeywords",
    "problem": "problemKeywords",
}


def article_to_document(article: Article) -> dict[str, Any]:
    keyword_fields: dict[str, list[str]] = defaultdict(list)

    for keyword in article.keywords:
        field = KEYWORD_FIELD_BY_TYPE.get(keyword.keyword_type)
        if field:
            keyword_fields[field].append(keyword.keyword)

    return {
        "id": str(article.id),
        "title": article.title,
        "url": article.url,
        "company": article.source.company_name,
        "source": article.source.name,
        "sourceSlug": article.source.slug,
        "publishedAt": article.published_at.isoformat() if article.published_at else None,
        "summary": article.summary,
        "content": article.content_text,
        "technologies": sorted(set(keyword_fields["technologies"])),
        "architectureKeywords": sorted(set(keyword_fields["architectureKeywords"])),
        "problemKeywords": sorted(set(keyword_fields["problemKeywords"])),
    }

