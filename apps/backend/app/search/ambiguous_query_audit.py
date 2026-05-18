from __future__ import annotations

import argparse
from dataclasses import dataclass

from app.search.service import expand_query, matched_rule_keywords, search_articles
from app.search.suggestions import suggest

DEFAULT_QUERIES = [
    "next",
    "go",
    "golang",
    "spring",
    "node",
    "ai",
    "r",
]


@dataclass(frozen=True)
class TopResult:
    title: str
    source: str
    score: float
    technologies: list[str]


@dataclass(frozen=True)
class AmbiguousQueryAuditResult:
    query: str
    expanded_query: str
    matched_keywords: list[str]
    total: int
    top_results: list[TopResult]
    suggestion_labels: list[str]


def audit_ambiguous_queries(
    queries: list[str],
    *,
    top_size: int,
    suggestion_size: int,
) -> list[AmbiguousQueryAuditResult]:
    return [
        audit_ambiguous_query(
            query=query,
            top_size=top_size,
            suggestion_size=suggestion_size,
        )
        for query in queries
    ]


def audit_ambiguous_query(
    *,
    query: str,
    top_size: int,
    suggestion_size: int,
) -> AmbiguousQueryAuditResult:
    search_result = search_articles(query, size=top_size)
    suggestion_result = suggest(query[:suggestion_size])

    return AmbiguousQueryAuditResult(
        query=query,
        expanded_query=expand_query(query),
        matched_keywords=matched_rule_keywords(query),
        total=search_result["total"],
        top_results=[top_result(item) for item in search_result["items"]],
        suggestion_labels=[item["label"] for item in suggestion_result["items"]],
    )


def top_result(item: dict) -> TopResult:
    return TopResult(
        title=item["title"],
        source=f"{item['company']} / {item['source']}",
        score=item["score"],
        technologies=item.get("technologies", []),
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Inspect short or ambiguous search queries before adding aliases."
    )
    parser.add_argument(
        "queries",
        nargs="*",
        default=DEFAULT_QUERIES,
        help="Queries to inspect. Defaults to common ambiguous technology terms.",
    )
    parser.add_argument("--top-size", type=int, default=5)
    parser.add_argument("--suggestion-prefix-size", type=int, default=3)
    return parser.parse_args()


def print_audit(results: list[AmbiguousQueryAuditResult]) -> None:
    print("Ambiguous query audit")

    for result in results:
        print()
        print(f"## {result.query}")
        print(f"- total: {result.total}")
        print(f"- expanded: {result.expanded_query}")
        print(f"- matched keywords: {', '.join(result.matched_keywords) or '-'}")
        print(f"- suggestions: {', '.join(result.suggestion_labels) or '-'}")
        print("- top results:")

        for index, item in enumerate(result.top_results, start=1):
            technologies = ", ".join(item.technologies) or "-"
            print(
                f"  {index}. {item.title} "
                f"({item.source}, score={item.score:.2f}, technologies={technologies})"
            )


def main() -> None:
    args = parse_args()
    results = audit_ambiguous_queries(
        args.queries,
        top_size=args.top_size,
        suggestion_size=args.suggestion_prefix_size,
    )
    print_audit(results)


if __name__ == "__main__":
    main()
