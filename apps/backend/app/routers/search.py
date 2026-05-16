from fastapi import APIRouter, Query

from app.search.service import search_articles as search_article_documents

router = APIRouter(tags=["search"])


@router.get("/search")
def search_articles(q: str = Query(default="", description="Search query")) -> dict[str, object]:
    return search_article_documents(q)
