from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from app.search.service import search_articles

ROOT_DIR = Path(__file__).parents[5]
DATASET_PATH = Path(__file__).with_name("queries.json")
DEFAULT_JSON_OUTPUT_PATH = ROOT_DIR / "docs" / "search-evaluation-results.json"
DEFAULT_LOW_SCORE_OUTPUT_PATH = ROOT_DIR / "docs" / "search-evaluation-low-score.md"
TOP_K_PRECISION = 5
TOP_K_RECALL = 10
TOP_K_NDCG = 10
DEFAULT_MIN_PRECISION_AT_5 = 0.4
DEFAULT_MIN_RECALL_AT_10 = 0.8
DEFAULT_MIN_MRR = 0.5
DEFAULT_MIN_NDCG_AT_10 = 0.7


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
    expected_count: int
    top_results: list[dict[str, Any]]


def load_dataset(path: Path = DATASET_PATH) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def evaluate_dataset(path: Path = DATASET_PATH) -> list[QueryScore]:
    dataset = load_dataset(path)
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
        expected_count=len(relevance_by_url),
        top_results=[
            {
                "rank": index,
                "title": item["title"],
                "url": item["url"],
                "company": item["company"],
                "source": item["source"],
                "sourceSlug": item["sourceSlug"],
                "contentType": item.get("contentType"),
                "score": item.get("score"),
                "isExpected": item["url"] in relevance_by_url,
                "expectedRelevance": relevance_by_url.get(item["url"]),
            }
            for index, item in enumerate(search_result["items"], start=1)
        ],
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


def write_json_report(scores: list[QueryScore], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output = {
        "generatedAt": datetime.now(UTC).isoformat(),
        "summary": summary(scores),
        "queries": [score_to_json(score) for score in scores],
    }
    output_path.write_text(
        json.dumps(output, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def write_low_score_report(
    scores: list[QueryScore],
    output_path: Path,
    *,
    min_precision_at_5: float,
    min_recall_at_10: float,
    min_mrr: float,
    min_ndcg_at_10: float,
) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    low_scores = [
        (
            score,
            low_score_reasons(
                score,
                min_precision_at_5,
                min_recall_at_10,
                min_mrr,
                min_ndcg_at_10,
            ),
        )
        for score in scores
    ]
    low_scores = [(score, reasons) for score, reasons in low_scores if reasons]
    low_scores.sort(key=lambda item: (item[0].precision_at_5, item[0].ndcg_at_10, item[0].query_id))

    lines = [
        "# Search Evaluation Low Score Report",
        "",
        f"- generated at: {datetime.now(UTC).isoformat()}",
        f"- queries: {len(scores)}",
        f"- low score queries: {len(low_scores)}",
        (
            "- thresholds: "
            f"p@5>={min_precision_at_5}, "
            f"r@10>={min_recall_at_10}, "
            f"mrr>={min_mrr}, "
            f"ndcg@10>={min_ndcg_at_10}"
        ),
        "",
        "## Review Targets",
        "",
        "| query_id | query | category | total | p@5 | r@10 | mrr | ndcg@10 | reasons |",
        "| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |",
    ]

    for score, reasons in low_scores:
        lines.append(
            f"| {escape_markdown(score.query_id)} "
            f"| {escape_markdown(score.query)} "
            f"| {escape_markdown(score.category)} "
            f"| {score.total_results} "
            f"| {format_score(score.precision_at_5)} "
            f"| {format_score(score.recall_at_10)} "
            f"| {format_score(score.mrr)} "
            f"| {format_score(score.ndcg_at_10)} "
            f"| {escape_markdown(', '.join(reasons))} |"
        )

    lines.extend(["", "## Details", ""])

    for score, reasons in low_scores:
        lines.extend(low_score_detail(score, reasons))

    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def low_score_reasons(
    score: QueryScore,
    min_precision_at_5: float,
    min_recall_at_10: float,
    min_mrr: float,
    min_ndcg_at_10: float,
) -> list[str]:
    reasons = []
    if (
        can_reach_precision_threshold(
            score.expected_count, TOP_K_PRECISION, min_precision_at_5
        )
        and score.precision_at_5 < min_precision_at_5
    ):
        reasons.append("low_precision")
    if score.recall_at_10 < min_recall_at_10:
        reasons.append("low_recall")
    if score.mrr < min_mrr:
        reasons.append("low_mrr")
    if score.ndcg_at_10 < min_ndcg_at_10:
        reasons.append("low_ndcg")
    return reasons


def can_reach_precision_threshold(
    expected_count: int, k: int, threshold: float
) -> bool:
    if k <= 0:
        return False

    return min(expected_count, k) / k >= threshold


def low_score_detail(score: QueryScore, reasons: list[str]) -> list[str]:
    lines = [
        f"### {escape_markdown(score.query_id)}",
        "",
        f"- query: {escape_markdown(score.query)}",
        f"- category: {escape_markdown(score.category)}",
        f"- reasons: {escape_markdown(', '.join(reasons))}",
        (
            "- scores: "
            f"p@5={format_score(score.precision_at_5)}, "
            f"r@10={format_score(score.recall_at_10)}, "
            f"mrr={format_score(score.mrr)}, "
            f"ndcg@10={format_score(score.ndcg_at_10)}"
        ),
        "",
        "| rank | expected | title | company/source |",
        "| ---: | --- | --- | --- |",
    ]

    for item in score.top_results[:TOP_K_RECALL]:
        expected = (
            f"yes:{item['expectedRelevance']}" if item["isExpected"] else "-"
        )
        lines.append(
            f"| {item['rank']} "
            f"| {expected} "
            f"| [{escape_markdown(str(item['title']))}]({item['url']}) "
            f"| {escape_markdown(str(item['company']))} / {escape_markdown(str(item['source']))} |"
        )

    lines.append("")
    return lines


def summary(scores: list[QueryScore]) -> dict[str, Any]:
    return {
        "queryCount": len(scores),
        "averagePrecisionAt5": average(score.precision_at_5 for score in scores),
        "averageRecallAt10": average(score.recall_at_10 for score in scores),
        "averageMrr": average(score.mrr for score in scores),
        "averageNdcgAt10": average(score.ndcg_at_10 for score in scores),
    }


def score_to_json(score: QueryScore) -> dict[str, Any]:
    return {
        "queryId": score.query_id,
        "query": score.query,
        "category": score.category,
        "totalResults": score.total_results,
        "expectedCount": score.expected_count,
        "precisionAt5": score.precision_at_5,
        "recallAt10": score.recall_at_10,
        "mrr": score.mrr,
        "ndcgAt10": score.ndcg_at_10,
        "topResults": score.top_results,
    }


def average(values: Any) -> float:
    value_list = list(values)
    if not value_list:
        return 0.0

    return sum(value_list) / len(value_list)


def format_score(value: float) -> str:
    return f"{value:.3f}"


def escape_markdown(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Evaluate TechCase search quality.")
    parser.add_argument("--dataset", type=Path, default=DATASET_PATH)
    parser.add_argument("--json-output", type=Path, default=DEFAULT_JSON_OUTPUT_PATH)
    parser.add_argument("--low-score-output", type=Path, default=DEFAULT_LOW_SCORE_OUTPUT_PATH)
    parser.add_argument("--min-precision-at-5", type=float, default=DEFAULT_MIN_PRECISION_AT_5)
    parser.add_argument("--min-recall-at-10", type=float, default=DEFAULT_MIN_RECALL_AT_10)
    parser.add_argument("--min-mrr", type=float, default=DEFAULT_MIN_MRR)
    parser.add_argument("--min-ndcg-at-10", type=float, default=DEFAULT_MIN_NDCG_AT_10)
    parser.add_argument("--no-write", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    scores = evaluate_dataset(args.dataset)
    print_report(scores)
    if not args.no_write:
        write_json_report(scores, args.json_output)
        write_low_score_report(
            scores,
            args.low_score_output,
            min_precision_at_5=args.min_precision_at_5,
            min_recall_at_10=args.min_recall_at_10,
            min_mrr=args.min_mrr,
            min_ndcg_at_10=args.min_ndcg_at_10,
        )
        print()
        print(f"Wrote evaluation JSON: {args.json_output}")
        print(f"Wrote low score report: {args.low_score_output}")


if __name__ == "__main__":
    main()
