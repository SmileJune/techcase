from typing import Annotated

from fastapi import APIRouter, Query

from app.search.service import SearchSort
from app.search.service import search_articles as search_article_documents

router = APIRouter(tags=["search"])


@router.get("/search")
def search_articles(
    q: Annotated[str, Query(description="Search query")] = "",
    sort: Annotated[SearchSort, Query(description="Search result sort order")] = "relevance",
    source: Annotated[list[str] | None, Query(description="Filter by source slug")] = None,
    technology: Annotated[list[str] | None, Query(description="Filter by technology")] = None,
    problem: Annotated[list[str] | None, Query(description="Filter by problem keyword")] = None,
    content_type: Annotated[list[str] | None, Query(description="Filter by content type")] = None,
) -> dict[str, object]:
    return search_article_documents(
        q,
        sort=sort,
        sources=source,
        technologies=technology,
        problem_keywords=problem,
        content_types=content_type,
    )
