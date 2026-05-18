from __future__ import annotations

import argparse
from dataclasses import dataclass

from app.search.service import (
    QUERY_ONLY_KEYWORD_ALIASES,
    expand_query,
    matched_rule_keywords,
    search_articles,
)
from app.search.suggestions import suggest


@dataclass(frozen=True)
class AliasAuditResult:
    alias: str
    keyword: str
    expanded_query: str
    matched_keywords: list[str]
    top_result_count: int
    top_keyword_count: int
    suggestion_prefix: str
    suggestion_labels: list[str]

    @property
    def matched(self) -> bool:
        return self.keyword in self.matched_keywords

    @property
    def ranked(self) -> bool:
        return self.top_keyword_count > 0

    @property
    def suggested(self) -> bool:
        return self.keyword in self.suggestion_labels

    @property
    def passed(self) -> bool:
        return self.matched and self.ranked and self.suggested


def audit_query_aliases(*, top_size: int, suggest_prefix_size: int) -> list[AliasAuditResult]:
    return [
        audit_query_alias(
            alias=alias,
            keyword=keyword,
            top_size=top_size,
            suggest_prefix_size=suggest_prefix_size,
        )
        for alias, keyword in sorted(QUERY_ONLY_KEYWORD_ALIASES.items())
    ]


def audit_query_alias(
    *,
    alias: str,
    keyword: str,
    top_size: int,
    suggest_prefix_size: int,
) -> AliasAuditResult:
    search_result = search_articles(alias, size=top_size)
    top_items = search_result["items"]
    suggestion_prefix = alias[:suggest_prefix_size]
    suggestion_result = suggest(suggestion_prefix)

    return AliasAuditResult(
        alias=alias,
        keyword=keyword,
        expanded_query=expand_query(alias),
        matched_keywords=matched_rule_keywords(alias),
        top_result_count=len(top_items),
        top_keyword_count=count_items_with_keyword(top_items, keyword),
        suggestion_prefix=suggestion_prefix,
        suggestion_labels=[item["label"] for item in suggestion_result["items"]],
    )


def count_items_with_keyword(items: list[dict], keyword: str) -> int:
    normalized_keyword = keyword.casefold()
    count = 0

    for item in items:
        technologies = [value.casefold() for value in item.get("technologies", [])]
        if normalized_keyword in technologies:
            count += 1

    return count


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check query-only aliases against search ranking and suggestions."
    )
    parser.add_argument("--top-size", type=int, default=5)
    parser.add_argument("--suggest-prefix-size", type=int, default=3)
    return parser.parse_args()


def print_audit(results: list[AliasAuditResult]) -> None:
    if not results:
        print("No query-only aliases configured.")
        return

    print("Query-only alias audit")
    print()
    print(
        f"{'status':<6} {'alias':<12} {'keyword':<18} "
        f"{'matched':<8} {'top':<7} {'suggest':<8}"
    )
    print("-" * 72)

    for result in results:
        status = "PASS" if result.passed else "FAIL"
        matched = "yes" if result.matched else "no"
        top = f"{result.top_keyword_count}/{result.top_result_count}"
        suggested = "yes" if result.suggested else "no"
        print(
            f"{status:<6} {result.alias:<12} {result.keyword:<18} "
            f"{matched:<8} {top:<7} {suggested:<8}"
        )
        print(f"  expanded: {result.expanded_query}")
        print(
            f"  suggestions({result.suggestion_prefix}): "
            f"{', '.join(result.suggestion_labels) or '-'}"
        )


def main() -> None:
    args = parse_args()
    results = audit_query_aliases(
        top_size=args.top_size,
        suggest_prefix_size=args.suggest_prefix_size,
    )
    print_audit(results)

    if any(not result.passed for result in results):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
