from fastapi import APIRouter, Query

router = APIRouter(tags=["search"])


@router.get("/search")
def search_articles(q: str = Query(default="", description="Search query")) -> dict[str, object]:
    return {
        "query": q,
        "total": 0,
        "items": [],
    }

