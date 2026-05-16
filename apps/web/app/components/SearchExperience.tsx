"use client";

import { FormEvent, useState } from "react";

const quickSearches = [
  "Lambda",
  "EventBridge",
  "DynamoDB",
  "EKS",
  "event-driven",
  "cost optimization",
];

type SearchResultItem = {
  id: string;
  title: string;
  url: string;
  company: string;
  source: string;
  sourceSlug: string;
  publishedAt?: string | null;
  summary?: string | null;
  caseSummary?: string | null;
  caseProblem?: string | null;
  caseSolution?: string | null;
  contentType?: string | null;
  score: number;
  technologies: string[];
  architectureKeywords: string[];
  problemKeywords: string[];
  highlights: Record<string, string[]>;
};

type SearchResponse = {
  query: string;
  total: number;
  items: SearchResultItem[];
};

const apiBaseUrl = process.env.NEXT_PUBLIC_API_BASE_URL ?? "http://localhost:8000";

function stripHighlightTags(value: string): string {
  return value.replaceAll("<em>", "").replaceAll("</em>", "");
}

function formatDate(value?: string | null): string {
  if (!value) {
    return "날짜 없음";
  }

  return new Intl.DateTimeFormat("ko-KR", {
    year: "numeric",
    month: "short",
    day: "numeric",
  }).format(new Date(value));
}

function bestSnippet(item: SearchResultItem): string {
  if (item.caseSummary) {
    return item.caseSummary;
  }

  const highlight =
    item.highlights.caseSummary?.[0] ??
    item.highlights.summary?.[0] ??
    item.highlights.content?.[0] ??
    item.highlights.title?.[0];

  if (highlight) {
    return stripHighlightTags(highlight);
  }

  return item.caseSummary ?? item.summary ?? "요약 정보가 아직 없습니다.";
}

export function SearchExperience() {
  const [query, setQuery] = useState("");
  const [result, setResult] = useState<SearchResponse | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [errorMessage, setErrorMessage] = useState<string | null>(null);

  async function runSearch(nextQuery: string) {
    const trimmedQuery = nextQuery.trim();
    setQuery(nextQuery);

    if (!trimmedQuery) {
      setResult(null);
      setErrorMessage(null);
      return;
    }

    setIsLoading(true);
    setErrorMessage(null);

    try {
      const response = await fetch(
        `${apiBaseUrl}/api/search?q=${encodeURIComponent(trimmedQuery)}`,
      );

      if (!response.ok) {
        throw new Error(`검색 요청 실패: ${response.status}`);
      }

      const data = (await response.json()) as SearchResponse;
      setResult(data);
    } catch (error) {
      setResult(null);
      setErrorMessage(error instanceof Error ? error.message : "검색 중 오류가 발생했습니다.");
    } finally {
      setIsLoading(false);
    }
  }

  function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    void runSearch(query);
  }

  return (
    <section className="search-panel" aria-label="기술 사례 검색">
      <form className="search-row" onSubmit={handleSubmit}>
        <input
          className="search-input"
          name="q"
          placeholder="Lambda, EventBridge, migration, event-driven..."
          aria-label="검색어"
          value={query}
          onChange={(event) => setQuery(event.target.value)}
        />
        <button className="search-button" type="submit" disabled={isLoading}>
          {isLoading ? "검색 중" : "검색"}
        </button>
      </form>

      <div className="tag-list" aria-label="추천 검색어">
        {quickSearches.map((keyword) => (
          <button className="tag" type="button" key={keyword} onClick={() => void runSearch(keyword)}>
            {keyword}
          </button>
        ))}
      </div>

      <SearchState result={result} isLoading={isLoading} errorMessage={errorMessage} />
    </section>
  );
}

function SearchState({
  result,
  isLoading,
  errorMessage,
}: {
  result: SearchResponse | null;
  isLoading: boolean;
  errorMessage: string | null;
}) {
  if (isLoading) {
    return <p className="result-empty">검색 결과를 불러오는 중입니다.</p>;
  }

  if (errorMessage) {
    return <p className="result-error">{errorMessage}</p>;
  }

  if (!result) {
    return (
      <p className="result-empty">
        추천 검색어를 누르거나 직접 검색어를 입력해 AWS 기술 블로그 사례를 찾아보세요.
      </p>
    );
  }

  if (result.items.length === 0) {
    return <p className="result-empty">`{result.query}`에 대한 검색 결과가 없습니다.</p>;
  }

  return (
    <div className="results">
      <div className="result-summary">
        <strong>{result.total}</strong>개 사례를 찾았습니다.
      </div>
      <div className="result-list">
        {result.items.map((item) => (
          <article className="result-card" key={item.id}>
            <div className="result-meta">
              <span>{item.source}</span>
              <span>{formatDate(item.publishedAt)}</span>
            </div>
            <h2>
              <a href={item.url} target="_blank" rel="noreferrer">
                {item.title}
              </a>
            </h2>
            <p>{bestSnippet(item)}</p>
            <KeywordList item={item} />
          </article>
        ))}
      </div>
    </div>
  );
}

function KeywordList({ item }: { item: SearchResultItem }) {
  const keywords = [
    ...item.technologies,
    ...item.architectureKeywords,
    ...item.problemKeywords,
  ].slice(0, 8);

  if (keywords.length === 0) {
    return null;
  }

  return (
    <div className="result-keywords">
      {keywords.map((keyword) => (
        <span key={keyword}>{keyword}</span>
      ))}
    </div>
  );
}
