from fastapi import APIRouter, Query

from app.search.suggestions import suggest as suggest_search_terms

router = APIRouter()


@router.get("/suggest")
def suggest(q: str = Query(default="", description="Autocomplete query")) -> dict[str, object]:
    return suggest_search_terms(q)
