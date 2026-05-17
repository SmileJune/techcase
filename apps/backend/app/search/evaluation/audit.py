from __future__ import annotations

import argparse
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from app.search.evaluation.evaluator import (
    average,
    evaluate_query,
    format_score,
    load_dataset,
)
from app.search.service import search_articles

DEFAULT_OUTPUT_PATH = Path(__file__).parents[5] / "docs" / "search-audit-report.md"
TOP_K_AUDIT = 10
DETAIL_COUNT = 3


def build_audit_report(output_path: Path = DEFAULT_OUTPUT_PATH) -> None:
    dataset = load_dataset()
    query_cases = dataset["queries"]
    scores = [evaluate_query(query_case) for query_case in query_cases]
    score_by_id = {score.query_id: score for score in scores}

    lines = [
        "# Search Audit Report",
        "",
        f"Generated at: {datetime.now(UTC).isoformat()}",
        "",
        "## Summary",
        "",
        f"- queries: {len(query_cases)}",
        f"- average precision@5: {format_score(average(score.precision_at_5 for score in scores))}",
        f"- average recall@10: {format_score(average(score.recall_at_10 for score in scores))}",
        f"- average mrr: {format_score(average(score.mrr for score in scores))}",
        f"- average ndcg@10: {format_score(average(score.ndcg_at_10 for score in scores))}",
        "",
        "## Query Audits",
        "",
    ]

    for query_case in query_cases:
        score = score_by_id[query_case["id"]]
        search_result = search_articles(query_case["query"], size=TOP_K_AUDIT)
        expected_by_url = {
            expected["url"]: expected for expected in query_case["expectedResults"]
        }

        lines.extend(query_section(query_case, score, search_result, expected_by_url))

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(f"Wrote search audit report: {output_path}")


def query_section(
    query_case: dict[str, Any],
    score: Any,
    search_result: dict[str, Any],
    expected_by_url: dict[str, dict[str, Any]],
) -> list[str]:
    lines = [
        f"### {query_case['id']} - `{query_case['query']}`",
        "",
        f"- category: {query_case['category']}",
        f"- intent: {query_case.get('intent', '')}",
        f"- total results: {search_result['total']}",
        f"- precision@5: {format_score(score.precision_at_5)}",
        f"- recall@10: {format_score(score.recall_at_10)}",
        f"- mrr: {format_score(score.mrr)}",
        f"- ndcg@10: {format_score(score.ndcg_at_10)}",
        "",
        "#### Expected URLs",
        "",
    ]

    for expected in expected_by_url.values():
        lines.append(
            f"- relevance {expected['relevance']}: "
            f"[{escape_markdown(expected['title'])}]({expected['url']})"
        )

    lines.extend(
        [
            "",
            "#### Top Results",
            "",
            "| Rank | Match | Title | Source | Score | Keywords |",
            "|---:|---|---|---|---:|---|",
        ]
    )

    for rank, item in enumerate(search_result["items"], start=1):
        expected = expected_by_url.get(item["url"])
        match = f"expected:{expected['relevance']}" if expected else "-"
        source = f"{item['company']} / {item['source']}"
        keywords = ", ".join(top_keywords(item))
        lines.append(
            "| "
            f"{rank} | "
            f"{match} | "
            f"[{escape_markdown(item['title'])}]({item['url']}) | "
            f"{escape_markdown(source)} | "
            f"{item['score']:.2f} | "
            f"{escape_markdown(keywords)} |"
        )

    lines.extend(
        [
            "",
            "#### Top Result Details",
            "",
        ]
    )

    for rank, item in enumerate(search_result["items"][:DETAIL_COUNT], start=1):
        lines.extend(result_detail(rank, item, expected_by_url))

    lines.append("")
    return lines


def result_detail(
    rank: int, item: dict[str, Any], expected_by_url: dict[str, dict[str, Any]]
) -> list[str]:
    expected = expected_by_url.get(item["url"])
    match = f"expected relevance {expected['relevance']}" if expected else "not expected"
    highlights = highlight_snippets(item.get("highlights", {}))

    lines = [
        f"##### {rank}. {item['title']}",
        "",
        f"- match: {match}",
        f"- source: {item['company']} / {item['source']}",
        f"- url: {item['url']}",
        f"- technologies: {', '.join(item.get('technologies', [])) or '-'}",
        f"- problem keywords: {', '.join(item.get('problemKeywords', [])) or '-'}",
        f"- case summary: {clean_inline(item.get('caseSummary') or item.get('summary') or '-')}",
    ]

    if item.get("caseProblem"):
        lines.append(f"- problem: {clean_inline(item['caseProblem'])}")

    if item.get("caseSolution"):
        lines.append(f"- solution: {clean_inline(item['caseSolution'])}")

    if highlights:
        lines.extend(["", "Highlights:", ""])
        lines.extend([f"- {snippet}" for snippet in highlights])

    lines.append("")
    return lines


def top_keywords(item: dict[str, Any]) -> list[str]:
    keywords = [
        *item.get("technologies", []),
        *item.get("problemKeywords", []),
        *item.get("architectureKeywords", []),
    ]
    return unique(keywords)[:6]


def highlight_snippets(highlights: dict[str, list[str]]) -> list[str]:
    snippets = []
    for field in ["title", "caseSummary", "caseProblem", "caseSolution", "summary", "content"]:
        for snippet in highlights.get(field, [])[:2]:
            snippets.append(f"{field}: {clean_inline(snippet)}")

    return snippets[:6]


def unique(values: list[str]) -> list[str]:
    seen = set()
    result = []
    for value in values:
        normalized = value.casefold()
        if normalized in seen:
            continue

        seen.add(normalized)
        result.append(value)

    return result


def clean_inline(value: str) -> str:
    return " ".join(value.replace("<em>", "**").replace("</em>", "**").split())


def escape_markdown(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate a Markdown search audit report.")
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT_PATH,
        help="Markdown report output path.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    build_audit_report(output_path=args.output)


if __name__ == "__main__":
    main()
