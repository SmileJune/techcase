from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from app.search.service import search_articles

ROOT_DIR = Path(__file__).parents[5]
DEFAULT_DATASET_PATH = Path(__file__).with_name("keyword_pool.json")
DEFAULT_REPORT_PATH = ROOT_DIR / "docs" / "search-keyword-probe-report.md"
DEFAULT_JSON_OUTPUT_PATH = ROOT_DIR / "docs" / "search-keyword-probe-results.json"
DEFAULT_TOP_SIZE = 5
BROAD_RESULT_THRESHOLD = 500


@dataclass(frozen=True)
class ProbeResult:
    query: dict[str, Any]
    total: int
    items: list[dict[str, Any]]
    diagnostics: list[str]


def load_keyword_pool(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def run_probe(dataset_path: Path, top_size: int, limit: int | None = None) -> list[ProbeResult]:
    dataset = load_keyword_pool(dataset_path)
    queries = dataset["queries"][:limit] if limit is not None else dataset["queries"]

    return [probe_query(query_case, top_size) for query_case in queries]


def probe_query(query_case: dict[str, Any], top_size: int) -> ProbeResult:
    search_result = search_articles(query_case["query"], size=top_size)
    items = search_result["items"]
    diagnostics = diagnose(query_case, search_result["total"], items)

    return ProbeResult(
        query=query_case,
        total=search_result["total"],
        items=items,
        diagnostics=diagnostics,
    )


def diagnose(query_case: dict[str, Any], total: int, items: list[dict[str, Any]]) -> list[str]:
    diagnostics: list[str] = []

    if total == 0:
        return ["no_results"]

    top_items = items[:DEFAULT_TOP_SIZE]
    if any(is_url_title(item) for item in top_items):
        diagnostics.append("url_title")

    if total >= BROAD_RESULT_THRESHOLD:
        if intent_match_count(query_case, top_items) < 3:
            diagnostics.append("broad_results")
        else:
            diagnostics.append("large_candidate_pool")

    if top_items and sum(1 for item in top_items if item.get("contentType") == "other") >= 3:
        diagnostics.append("other_dominant")

    if top_items and not has_intent_match(query_case, top_items):
        diagnostics.append("weak_intent_match")

    if top_items and not any(item.get("caseSummary") for item in top_items):
        diagnostics.append("missing_case_summary")

    if query_case["query"].strip() and not any(item.get("highlights") for item in top_items):
        diagnostics.append("no_highlights")

    source_counts = Counter(item.get("sourceSlug") for item in top_items)
    if top_items and source_counts.most_common(1)[0][1] >= 4:
        diagnostics.append("single_source_dominance")

    return diagnostics


def is_url_title(item: dict[str, Any]) -> bool:
    title = str(item.get("title") or "")
    url = str(item.get("url") or "")
    return title.startswith("http://") or title.startswith("https://") or title == url


def has_intent_match(query_case: dict[str, Any], items: list[dict[str, Any]]) -> bool:
    terms = intent_terms(query_case)
    if not terms:
        return True

    searchable_text = normalize_text(
        " ".join(item_search_text(item) for item in items)
    )
    return any(term in searchable_text for term in terms)


def intent_match_count(query_case: dict[str, Any], items: list[dict[str, Any]]) -> int:
    terms = intent_terms(query_case)
    if not terms:
        return len(items)

    return sum(
        1
        for item in items
        if any(term in normalize_text(item_search_text(item)) for term in terms)
    )


def intent_terms(query_case: dict[str, Any]) -> list[str]:
    raw_terms = [
        query_case.get("query", ""),
        *query_case.get("aliases", []),
        *query_case.get("intendedTerms", []),
    ]
    normalized_terms = []
    seen = set()
    for term in raw_terms:
        normalized = normalize_text(str(term))
        if not normalized or normalized in seen:
            continue

        seen.add(normalized)
        normalized_terms.append(normalized)

    return normalized_terms


def item_search_text(item: dict[str, Any]) -> str:
    values = [
        item.get("title"),
        item.get("company"),
        item.get("source"),
        item.get("summary"),
        item.get("caseSummary"),
        item.get("caseProblem"),
        item.get("caseSolution"),
        " ".join(item.get("technologies") or []),
        " ".join(item.get("architectureKeywords") or []),
        " ".join(item.get("problemKeywords") or []),
    ]
    highlights = item.get("highlights") or {}
    for snippets in highlights.values():
        values.extend(snippets)

    return " ".join(str(value) for value in values if value)


def normalize_text(value: str) -> str:
    return re.sub(r"\s+", " ", value.casefold()).strip()


def write_json_report(results: list[ProbeResult], output_path: Path, top_size: int) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output = {
        "generatedAt": datetime.now(UTC).isoformat(),
        "topSize": top_size,
        "summary": summarize(results),
        "queries": [result_to_json(result) for result in results],
    }
    output_path.write_text(
        json.dumps(output, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def write_markdown_report(results: list[ProbeResult], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    summary = summarize(results)
    diagnostics_summary = (
        ", ".join(
            f"{key}={value}" for key, value in summary["diagnostics"].items()
        )
        or "-"
    )
    lines = [
        "# Search Keyword Probe Report",
        "",
        f"- generated at: {datetime.now(UTC).isoformat()}",
        f"- queries: {summary['queryCount']}",
        f"- diagnostics: {diagnostics_summary}",
        "",
        "## Review Priority",
        "",
        "| priority | query | category | total | diagnostics | top result |",
        "| --- | --- | --- | ---: | --- | --- |",
    ]

    for result in sorted(results, key=review_sort_key):
        if not result.diagnostics:
            continue

        lines.append(result_summary_row(result))

    lines.extend(
        [
            "",
            "## All Query Results",
            "",
        ]
    )

    for result in results:
        lines.extend(query_section(result))

    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def summarize(results: list[ProbeResult]) -> dict[str, Any]:
    diagnostics = Counter(
        diagnostic for result in results for diagnostic in result.diagnostics
    )
    categories = Counter(str(result.query.get("category", "")) for result in results)
    priorities = Counter(str(result.query.get("priority", "")) for result in results)
    return {
        "queryCount": len(results),
        "diagnostics": dict(sorted(diagnostics.items())),
        "categories": dict(sorted(categories.items())),
        "priorities": dict(sorted(priorities.items())),
    }


def result_to_json(result: ProbeResult) -> dict[str, Any]:
    return {
        "query": result.query["query"],
        "category": result.query.get("category"),
        "priority": result.query.get("priority"),
        "intent": result.query.get("intent"),
        "total": result.total,
        "diagnostics": result.diagnostics,
        "topResults": [
            {
                "rank": index,
                "title": item.get("title"),
                "company": item.get("company"),
                "source": item.get("source"),
                "sourceSlug": item.get("sourceSlug"),
                "url": item.get("url"),
                "contentType": item.get("contentType"),
                "technologies": item.get("technologies"),
                "architectureKeywords": item.get("architectureKeywords"),
                "problemKeywords": item.get("problemKeywords"),
                "score": item.get("score"),
            }
            for index, item in enumerate(result.items, start=1)
        ],
    }


def review_sort_key(result: ProbeResult) -> tuple[int, str, str]:
    severity = 0
    if "no_results" in result.diagnostics or "url_title" in result.diagnostics:
        severity = 3
    elif "weak_intent_match" in result.diagnostics or "other_dominant" in result.diagnostics:
        severity = 2
    elif result.diagnostics:
        severity = 1

    priority_weight = {"high": 0, "medium": 1, "low": 2}.get(
        str(result.query.get("priority")), 3
    )
    return (-severity, str(priority_weight), str(result.query["query"]).casefold())


def result_summary_row(result: ProbeResult) -> str:
    top_item = result.items[0] if result.items else None
    top_result = "-"
    if top_item:
        top_result = (
            f"[{escape_markdown(str(top_item.get('title') or 'Untitled'))}]"
            f"({top_item.get('url')})"
        )

    return (
        f"| {escape_markdown(str(result.query.get('priority', '-')))} "
        f"| {escape_markdown(str(result.query['query']))} "
        f"| {escape_markdown(str(result.query.get('category', '-')))} "
        f"| {result.total} "
        f"| {escape_markdown(', '.join(result.diagnostics))} "
        f"| {top_result} |"
    )


def query_section(result: ProbeResult) -> list[str]:
    lines = [
        f"### {escape_markdown(str(result.query['query']))}",
        "",
        f"- category: {escape_markdown(str(result.query.get('category', '-')))}",
        f"- priority: {escape_markdown(str(result.query.get('priority', '-')))}",
        f"- total: {result.total}",
        f"- diagnostics: {escape_markdown(', '.join(result.diagnostics) or '-')}",
        f"- intent: {escape_markdown(str(result.query.get('intent', '-')))}",
        "",
        "| rank | title | company/source | content type | keywords |",
        "| ---: | --- | --- | --- | --- |",
    ]

    for index, item in enumerate(result.items, start=1):
        company = escape_markdown(str(item.get("company") or "-"))
        source = escape_markdown(str(item.get("source") or "-"))
        keywords = [
            *(item.get("technologies") or [])[:3],
            *(item.get("architectureKeywords") or [])[:2],
            *(item.get("problemKeywords") or [])[:2],
        ]
        lines.append(
            f"| {index} "
            f"| [{escape_markdown(str(item.get('title') or 'Untitled'))}]({item.get('url')}) "
            f"| {company} / {source} "
            f"| {escape_markdown(str(item.get('contentType') or '-'))} "
            f"| {escape_markdown(', '.join(keywords) or '-')} |"
        )

    lines.append("")
    return lines


def escape_markdown(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run broad keyword probes and generate a triage report."
    )
    parser.add_argument("--dataset", type=Path, default=DEFAULT_DATASET_PATH)
    parser.add_argument("--output", type=Path, default=DEFAULT_REPORT_PATH)
    parser.add_argument("--json-output", type=Path, default=DEFAULT_JSON_OUTPUT_PATH)
    parser.add_argument("--top-size", type=int, default=DEFAULT_TOP_SIZE)
    parser.add_argument("--limit", type=int)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    results = run_probe(args.dataset, args.top_size, args.limit)
    write_markdown_report(results, args.output)
    write_json_report(results, args.json_output, args.top_size)
    summary = summarize(results)
    print(
        "Keyword probe completed: "
        f"queries={summary['queryCount']}, "
        f"diagnostics={summary['diagnostics']}, "
        f"report={args.output}"
    )


if __name__ == "__main__":
    main()
