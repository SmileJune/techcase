"use client";

import { FormEvent, KeyboardEvent, useEffect, useRef, useState } from "react";
import type { CSSProperties } from "react";

const quickSearches = [
  "Lambda",
  "장애 대응",
  "RAG",
  "Flutter",
  "추천 모델",
  "비용 최적화",
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

type SuggestionItem = {
  id: string;
  label: string;
  type: string;
  description: string;
  aliases: string[];
  articleCount: number;
  score: number;
};

type SuggestResponse = {
  query: string;
  items: SuggestionItem[];
};

type CompanyLogo = {
  label: string;
  background: string;
  foreground: string;
  border?: string;
  imageSrc?: string;
};

type HighlightPart = {
  text: string;
  isHighlighted: boolean;
};

type MatchReason = {
  field: string;
  label: string;
  snippets: string[];
};

const apiBaseUrl = process.env.NEXT_PUBLIC_API_BASE_URL ?? "http://localhost:8000";

const companyLogos: Record<string, CompanyLogo> = {
  "29cm": { label: "29", background: "#111111", foreground: "#ffffff" },
  aws: { label: "AWS", background: "#232f3e", foreground: "#ff9900" },
  daangn: { label: "당근", background: "#ff6f0f", foreground: "#ffffff" },
  devsisters: { label: "DS", background: "#e72d2c", foreground: "#ffffff" },
  "gc company": { label: "GC", background: "#00a676", foreground: "#ffffff" },
  kakao: {
    label: "K",
    background: "#fee500",
    foreground: "#191919",
    border: "#dfc900",
    imageSrc: "/logos/kakao.png",
  },
  "kakao pay": { label: "PAY", background: "#ffeb00", foreground: "#111111", border: "#dfcf00" },
  kurly: { label: "K", background: "#5f0080", foreground: "#ffffff" },
  "ly corporation": { label: "LY", background: "#06c755", foreground: "#ffffff" },
  musinsa: { label: "M", background: "#000000", foreground: "#ffffff" },
  naver: {
    label: "N",
    background: "#ffffff",
    foreground: "#03c75a",
    border: "#d8e1dc",
    imageSrc: "/logos/naver.svg",
  },
  socar: { label: "SOCAR", background: "#00b8ff", foreground: "#ffffff" },
  toss: {
    label: "toss",
    background: "#ffffff",
    foreground: "#0064ff",
    border: "#d8e1dc",
    imageSrc: "/logos/toss.png",
  },
  "woowa brothers": { label: "배민", background: "#2ac1bc", foreground: "#ffffff" },
  yogiyo: { label: "Y", background: "#fa0050", foreground: "#ffffff" },
};

const highlightLabels: Record<string, string> = {
  title: "제목",
  caseSummary: "사례 요약",
  caseProblem: "문제",
  caseSolution: "해결",
  summary: "RSS 요약",
  content: "본문",
};

function stripHighlightTags(value: string): string {
  return value.replaceAll("<em>", "").replaceAll("</em>", "");
}

function splitHighlight(value: string): HighlightPart[] {
  return value.split(/(<em>|<\/em>)/).reduce(
    (state, part) => {
      if (part === "<em>") {
        state.isHighlighted = true;
        return state;
      }

      if (part === "</em>") {
        state.isHighlighted = false;
        return state;
      }

      if (part) {
        state.parts.push({ text: part, isHighlighted: state.isHighlighted });
      }

      return state;
    },
    { isHighlighted: false, parts: [] as HighlightPart[] },
  ).parts;
}

function firstHighlight(item: SearchResultItem, field: string): string | null {
  return item.highlights[field]?.[0] ?? null;
}

function highlightOrText(item: SearchResultItem, field: string, fallback?: string | null): string {
  return firstHighlight(item, field) ?? fallback ?? "";
}

function matchReasons(item: SearchResultItem): MatchReason[] {
  return Object.entries(highlightLabels)
    .flatMap(([field, label]) => {
      const snippets = item.highlights[field]?.slice(0, 2) ?? [];

      if (snippets.length === 0) {
        return [];
      }

      return [{ field, label, snippets }];
    })
    .slice(0, 4);
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

function formatContentType(value?: string | null): string | null {
  if (!value) {
    return null;
  }

  const labels: Record<string, string> = {
    technical_case: "기술 사례",
    engineering_story: "엔지니어링 스토리",
    tutorial: "튜토리얼",
    release_note: "릴리스",
    event: "이벤트",
    recruiting: "채용",
    interview: "인터뷰",
    news: "뉴스",
    other: "기타",
  };

  return labels[value] ?? value;
}

function getCompanyLogo(item: SearchResultItem): CompanyLogo {
  const normalizedCompany = item.company.trim().toLowerCase();
  const normalizedSlug = item.sourceSlug.trim().toLowerCase();

  return (
    companyLogos[normalizedCompany] ??
    (normalizedSlug.startsWith("aws-") ? companyLogos.aws : undefined) ?? {
      label: item.company.slice(0, 2).toUpperCase(),
      background: "#eef2ef",
      foreground: "#2c5f4f",
      border: "#d8e1dc",
    }
  );
}

function uniqueKeywords(keywords: string[]): string[] {
  const seen = new Set<string>();

  return keywords.filter((keyword) => {
    const normalized = keyword.trim().toLowerCase();

    if (!normalized || seen.has(normalized)) {
      return false;
    }

    seen.add(normalized);
    return true;
  });
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
  const [suggestions, setSuggestions] = useState<SuggestionItem[]>([]);
  const [isSuggestOpen, setIsSuggestOpen] = useState(false);
  const [activeSuggestionIndex, setActiveSuggestionIndex] = useState(-1);
  const suggestAbortRef = useRef<AbortController | null>(null);
  const committedQueryRef = useRef<string | null>(null);

  useEffect(() => {
    const trimmedQuery = query.trim();

    suggestAbortRef.current?.abort();
    setActiveSuggestionIndex(-1);

    if (trimmedQuery.length < 2) {
      setSuggestions([]);
      setIsSuggestOpen(false);
      return;
    }

    if (committedQueryRef.current === trimmedQuery) {
      setSuggestions([]);
      setIsSuggestOpen(false);
      return;
    }

    const abortController = new AbortController();
    suggestAbortRef.current = abortController;

    const timer = window.setTimeout(async () => {
      try {
        const response = await fetch(
          `${apiBaseUrl}/api/suggest?q=${encodeURIComponent(trimmedQuery)}`,
          { signal: abortController.signal },
        );

        if (!response.ok) {
          throw new Error(`자동완성 요청 실패: ${response.status}`);
        }

        const data = (await response.json()) as SuggestResponse;
        setSuggestions(data.items);
        setIsSuggestOpen(data.items.length > 0);
      } catch (error) {
        if (error instanceof DOMException && error.name === "AbortError") {
          return;
        }

        setSuggestions([]);
        setIsSuggestOpen(false);
      }
    }, 180);

    return () => {
      window.clearTimeout(timer);
      abortController.abort();
    };
  }, [query]);

  async function runSearch(nextQuery: string) {
    const trimmedQuery = nextQuery.trim();
    committedQueryRef.current = trimmedQuery;
    setQuery(nextQuery);
    setIsSuggestOpen(false);
    setActiveSuggestionIndex(-1);
    setSuggestions([]);

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
    const activeSuggestion = suggestions[activeSuggestionIndex];
    void runSearch(activeSuggestion?.label ?? query);
  }

  function handleInputKeyDown(event: KeyboardEvent<HTMLInputElement>) {
    if (!isSuggestOpen || suggestions.length === 0) {
      return;
    }

    if (event.key === "ArrowDown") {
      event.preventDefault();
      setActiveSuggestionIndex((current) => (current + 1) % suggestions.length);
      return;
    }

    if (event.key === "ArrowUp") {
      event.preventDefault();
      setActiveSuggestionIndex((current) =>
        current <= 0 ? suggestions.length - 1 : current - 1,
      );
      return;
    }

    if (event.key === "Escape") {
      setIsSuggestOpen(false);
      setActiveSuggestionIndex(-1);
    }
  }

  return (
    <section className="search-panel" aria-label="기술 사례 검색">
      <form className="search-row" onSubmit={handleSubmit}>
        <div className="search-input-wrap">
          <input
            className="search-input"
            name="q"
            placeholder="Lambda, EventBridge, migration, event-driven..."
            aria-label="검색어"
            value={query}
            autoComplete="off"
            aria-autocomplete="list"
            aria-expanded={isSuggestOpen}
            aria-controls="search-suggestions"
            onChange={(event) => {
              committedQueryRef.current = null;
              setQuery(event.target.value);
            }}
            onFocus={() => setIsSuggestOpen(suggestions.length > 0)}
            onKeyDown={handleInputKeyDown}
          />
          {isSuggestOpen ? (
            <SuggestionList
              suggestions={suggestions}
              activeIndex={activeSuggestionIndex}
              onSelect={(suggestion) => void runSearch(suggestion.label)}
              onHover={setActiveSuggestionIndex}
            />
          ) : null}
        </div>
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

function SuggestionList({
  suggestions,
  activeIndex,
  onSelect,
  onHover,
}: {
  suggestions: SuggestionItem[];
  activeIndex: number;
  onSelect: (suggestion: SuggestionItem) => void;
  onHover: (index: number) => void;
}) {
  return (
    <div className="suggestions" id="search-suggestions" role="listbox">
      {suggestions.map((suggestion, index) => (
        <button
          className={`suggestion-item${index === activeIndex ? " is-active" : ""}`}
          type="button"
          key={suggestion.id}
          role="option"
          aria-selected={index === activeIndex}
          onMouseEnter={() => onHover(index)}
          onMouseDown={(event) => event.preventDefault()}
          onClick={() => onSelect(suggestion)}
        >
          <span className="suggestion-main">
            <span>{suggestion.label}</span>
            <span>{suggestion.description}</span>
          </span>
          {suggestion.articleCount > 0 ? (
            <span className="suggestion-count">{suggestion.articleCount}개 글</span>
          ) : null}
        </button>
      ))}
    </div>
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
            <div className="result-card-header">
              <div className="source-heading">
                <CompanyLogo item={item} />
                <div>
                  <div className="source-company">{item.company}</div>
                  <div className="result-meta">
                    <span>{item.source}</span>
                    <span>{formatDate(item.publishedAt)}</span>
                  </div>
                </div>
              </div>
              {formatContentType(item.contentType) ? (
                <span className="result-type">{formatContentType(item.contentType)}</span>
              ) : null}
            </div>
            <h2>
              <a href={item.url} target="_blank" rel="noreferrer">
                <HighlightedText value={highlightOrText(item, "title", item.title)} />
              </a>
            </h2>
            <section className="case-summary" aria-label="사례 요약">
              <span>사례 요약</span>
              <p>
                <HighlightedText
                  value={highlightOrText(item, "caseSummary", bestSnippet(item))}
                />
              </p>
            </section>
            <CaseDetails item={item} />
            <MatchReasons item={item} />
            <KeywordList item={item} />
            <a className="source-link" href={item.url} target="_blank" rel="noreferrer">
              원문 보기
            </a>
          </article>
        ))}
      </div>
    </div>
  );
}

function HighlightedText({ value }: { value: string }) {
  return splitHighlight(value).map((part, index) =>
    part.isHighlighted ? (
      <mark className="search-highlight" key={`${part.text}-${index}`}>
        {part.text}
      </mark>
    ) : (
      <span key={`${part.text}-${index}`}>{part.text}</span>
    ),
  );
}

function CompanyLogo({ item }: { item: SearchResultItem }) {
  const logo = getCompanyLogo(item);

  return (
    <span
      className="company-logo"
      style={
        {
          "--logo-background": logo.background,
          "--logo-foreground": logo.foreground,
          "--logo-border": logo.border ?? logo.background,
        } as CSSProperties
      }
      aria-label={`${item.company} 로고`}
      title={item.company}
    >
      {logo.imageSrc ? <img src={logo.imageSrc} alt="" /> : logo.label}
    </span>
  );
}

function CaseDetails({ item }: { item: SearchResultItem }) {
  if (!item.caseProblem && !item.caseSolution) {
    return null;
  }

  return (
    <dl className="case-details">
      {item.caseProblem ? (
        <div>
          <dt>문제</dt>
          <dd>
            <HighlightedText value={highlightOrText(item, "caseProblem", item.caseProblem)} />
          </dd>
        </div>
      ) : null}
      {item.caseSolution ? (
        <div>
          <dt>해결</dt>
          <dd>
            <HighlightedText value={highlightOrText(item, "caseSolution", item.caseSolution)} />
          </dd>
        </div>
      ) : null}
    </dl>
  );
}

function MatchReasons({ item }: { item: SearchResultItem }) {
  const reasons = matchReasons(item);

  if (reasons.length === 0) {
    return null;
  }

  return (
    <section className="match-reasons" aria-label="검색 매칭 근거">
      <span>매칭 근거</span>
      <div className="match-reason-list">
        {reasons.map((reason) => (
          <div className="match-reason" key={reason.field}>
            <span>{reason.label}</span>
            <div>
              {reason.snippets.map((snippet, index) => (
                <p key={`${reason.field}-${index}`}>
                  <HighlightedText value={snippet} />
                </p>
              ))}
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}

function KeywordList({ item }: { item: SearchResultItem }) {
  const technologyKeywords = uniqueKeywords(item.technologies).slice(0, 5);
  const problemKeywords = uniqueKeywords(item.problemKeywords).slice(0, 4);
  const architectureKeywords = uniqueKeywords(item.architectureKeywords).slice(0, 4);

  if (
    technologyKeywords.length === 0 &&
    problemKeywords.length === 0 &&
    architectureKeywords.length === 0
  ) {
    return null;
  }

  return (
    <div className="keyword-groups">
      <KeywordGroup label="기술" keywords={technologyKeywords} />
      <KeywordGroup label="문제 상황" keywords={problemKeywords} />
      <KeywordGroup label="아키텍처" keywords={architectureKeywords} />
    </div>
  );
}

function KeywordGroup({ label, keywords }: { label: string; keywords: string[] }) {
  if (keywords.length === 0) {
    return null;
  }

  return (
    <div className="keyword-group">
      <span className="keyword-group-label">{label}</span>
      <div className="result-keywords">
        {keywords.map((keyword) => (
          <span key={`${label}-${keyword}`}>{keyword}</span>
        ))}
      </div>
    </div>
  );
}
