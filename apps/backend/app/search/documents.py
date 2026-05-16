from collections import defaultdict
from typing import Any

from app.models.article import Article
from app.models.article_summary import ArticleSummary

KEYWORD_FIELD_BY_TYPE = {
    "technology": "technologies",
    "aws_service": "technologies",
    "architecture": "architectureKeywords",
    "problem": "problemKeywords",
}


def article_to_document(article: Article) -> dict[str, Any]:
    keyword_fields: dict[str, list[str]] = defaultdict(list)
    case_summary = latest_case_summary(article)

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
        "caseSummary": case_summary.case_summary if case_summary else None,
        "caseProblem": case_summary.problem if case_summary else None,
        "caseSolution": case_summary.solution if case_summary else None,
        "content": article.content_text,
        "technologies": sorted(set(keyword_fields["technologies"])),
        "architectureKeywords": sorted(set(keyword_fields["architectureKeywords"])),
        "problemKeywords": sorted(set(keyword_fields["problemKeywords"])),
    }


def latest_case_summary(article: Article) -> ArticleSummary | None:
    summaries = [
        summary for summary in article.summaries if summary.summary_type == "case_summary"
    ]
    if not summaries:
        return None

    return max(summaries, key=lambda summary: summary.updated_at or summary.created_at)
