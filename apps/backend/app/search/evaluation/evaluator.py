from __future__ import annotations

import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from app.search.service import search_articles

DATASET_PATH = Path(__file__).with_name("queries.json")
TOP_K_PRECISION = 5
TOP_K_RECALL = 10
TOP_K_NDCG = 10


@dataclass(frozen=True)
class QueryScore:
    query_id: str
    query: str
    category: str
    total_results: int
    precision_at_5: float
    recall_at_10: float
    mrr: float
    ndcg_at_10: float


def load_dataset(path: Path = DATASET_PATH) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def evaluate_dataset() -> list[QueryScore]:
    dataset = load_dataset()
    return [evaluate_query(query_case) for query_case in dataset["queries"]]


def evaluate_query(query_case: dict[str, Any]) -> QueryScore:
    search_result = search_articles(query_case["query"], size=TOP_K_RECALL)
    result_urls = [item["url"] for item in search_result["items"]]
    relevance_by_url = {
        expected["url"]: expected["relevance"] for expected in query_case["expectedResults"]
    }

    precision = precision_at_k(result_urls, relevance_by_url, TOP_K_PRECISION)
    recall = recall_at_k(result_urls, relevance_by_url, TOP_K_RECALL)
    mrr = mean_reciprocal_rank(result_urls, relevance_by_url)
    ndcg = ndcg_at_k(result_urls, relevance_by_url, TOP_K_NDCG)

    return QueryScore(
        query_id=query_case["id"],
        query=query_case["query"],
        category=query_case["category"],
        total_results=search_result["total"],
        precision_at_5=precision,
        recall_at_10=recall,
        mrr=mrr,
        ndcg_at_10=ndcg,
    )


def precision_at_k(
    result_urls: list[str], relevance_by_url: dict[str, int], k: int
) -> float:
    if k == 0:
        return 0.0

    hits = count_hits(result_urls[:k], relevance_by_url)
    return hits / k


def recall_at_k(result_urls: list[str], relevance_by_url: dict[str, int], k: int) -> float:
    if not relevance_by_url:
        return 0.0

    hits = count_hits(result_urls[:k], relevance_by_url)
    return hits / len(relevance_by_url)


def mean_reciprocal_rank(result_urls: list[str], relevance_by_url: dict[str, int]) -> float:
    for index, url in enumerate(result_urls, start=1):
        if url in relevance_by_url:
            return 1 / index

    return 0.0


def ndcg_at_k(result_urls: list[str], relevance_by_url: dict[str, int], k: int) -> float:
    dcg = discounted_cumulative_gain(
        [relevance_by_url.get(url, 0) for url in result_urls[:k]]
    )
    ideal_relevances = sorted(relevance_by_url.values(), reverse=True)[:k]
    ideal_dcg = discounted_cumulative_gain(ideal_relevances)

    if ideal_dcg == 0:
        return 0.0

    return dcg / ideal_dcg


def discounted_cumulative_gain(relevances: list[int]) -> float:
    return sum(
        ((2**relevance) - 1) / math.log2(index + 1)
        for index, relevance in enumerate(relevances, start=1)
    )


def count_hits(result_urls: list[str], relevance_by_url: dict[str, int]) -> int:
    return sum(1 for url in result_urls if url in relevance_by_url)


def print_report(scores: list[QueryScore]) -> None:
    print("TechCase search evaluation")
    print()
    print(
        "query_id".ljust(38),
        "category".ljust(12),
        "total".rjust(5),
        "p@5".rjust(6),
        "r@10".rjust(6),
        "mrr".rjust(6),
        "ndcg@10".rjust(8),
    )
    print("-" * 90)

    for score in scores:
        print(
            score.query_id.ljust(38),
            score.category.ljust(12),
            str(score.total_results).rjust(5),
            format_score(score.precision_at_5).rjust(6),
            format_score(score.recall_at_10).rjust(6),
            format_score(score.mrr).rjust(6),
            format_score(score.ndcg_at_10).rjust(8),
        )

    print("-" * 90)
    print(
        "average".ljust(38),
        "".ljust(12),
        "".rjust(5),
        format_score(average(score.precision_at_5 for score in scores)).rjust(6),
        format_score(average(score.recall_at_10 for score in scores)).rjust(6),
        format_score(average(score.mrr for score in scores)).rjust(6),
        format_score(average(score.ndcg_at_10 for score in scores)).rjust(8),
    )


def average(values: Any) -> float:
    value_list = list(values)
    if not value_list:
        return 0.0

    return sum(value_list) / len(value_list)


def format_score(value: float) -> str:
    return f"{value:.3f}"


def main() -> None:
    scores = evaluate_dataset()
    print_report(scores)


if __name__ == "__main__":
    main()
