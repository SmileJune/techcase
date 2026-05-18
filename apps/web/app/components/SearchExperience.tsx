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

const pageSize = 20;

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
  sort: SearchSort;
  filters: SearchFilters;
  facets: SearchFacets;
  total: number;
  page: number;
  pageSize: number;
  totalPages: number;
  items: SearchResultItem[];
};

type SearchSort = "relevance" | "latest";

type SearchFilters = {
  sources: string[];
  technologies: string[];
  problemKeywords: string[];
  contentTypes: string[];
};

type FacetItem = {
  value: string;
  label: string;
  count: number;
  isRecommended?: boolean;
};

type SearchFacets = {
  sources: FacetItem[];
  technologies: FacetItem[];
  problemKeywords: FacetItem[];
  contentTypes: FacetItem[];
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

type FavoriteItem = SearchResultItem & {
  favoritedAt: string;
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

const sortOptions: { value: SearchSort; label: string }[] = [
  { value: "relevance", label: "관련도순" },
  { value: "latest", label: "최신순" },
];

const emptyFilters: SearchFilters = {
  sources: [],
  technologies: [],
  problemKeywords: [],
  contentTypes: [],
};

const apiBaseUrl = process.env.NEXT_PUBLIC_API_BASE_URL ?? "http://localhost:8000";
const favoritesStorageKey = "techcase.favorites.v1";

const companyLogos: Record<string, CompanyLogo> = {
  "29cm": { label: "29", background: "#111111", foreground: "#ffffff" },
  aws: { label: "AWS", background: "#232f3e", foreground: "#ff9900" },
  banksalad: {
    label: "BS",
    background: "#ffffff",
    foreground: "#00c27a",
    border: "#d8e1dc",
    imageSrc: "/logos/banksalad.png",
  },
  daangn: { label: "당근", background: "#ff6f0f", foreground: "#ffffff" },
  devsisters: { label: "DS", background: "#e72d2c", foreground: "#ffffff" },
  "gc company": { label: "GC", background: "#00a676", foreground: "#ffffff" },
  gmarket: {
    label: "G",
    background: "#ffffff",
    foreground: "#00a676",
    border: "#d8e1dc",
    imageSrc: "/logos/gmarket.svg",
  },
  kakao: {
    label: "K",
    background: "#fee500",
    foreground: "#191919",
    border: "#dfc900",
    imageSrc: "/logos/kakao.png",
  },
  "kakao pay": {
    label: "PAY",
    background: "#ffffff",
    foreground: "#111111",
    border: "#d8e1dc",
    imageSrc: "/logos/kakaopay.svg",
  },
  kurly: {
    label: "K",
    background: "#ffffff",
    foreground: "#5f0080",
    border: "#d8e1dc",
    imageSrc: "/logos/kurly.png",
  },
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
  upstage: {
    label: "UP",
    background: "#ffffff",
    foreground: "#111111",
    border: "#d8e1dc",
    imageSrc: "/logos/upstage.svg",
  },
  "woowa brothers": {
    label: "배민",
    background: "#ffffff",
    foreground: "#2ac1bc",
    border: "#d8e1dc",
    imageSrc: "/logos/woowa.svg",
  },
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
  return getCompanyLogoByName(item.company, item.sourceSlug);
}

function getCompanyLogoByName(company: string, sourceSlug = ""): CompanyLogo {
  const normalizedCompany = company.trim().toLowerCase();
  const normalizedSlug = sourceSlug.trim().toLowerCase();

  return (
    companyLogos[normalizedCompany] ??
    (normalizedSlug.startsWith("aws-") ? companyLogos.aws : undefined) ?? {
      label: company.slice(0, 2).toUpperCase(),
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

function loadFavoriteItems(): FavoriteItem[] {
  try {
    const rawValue = window.localStorage.getItem(favoritesStorageKey);

    if (!rawValue) {
      return [];
    }

    const parsedValue = JSON.parse(rawValue);

    if (!Array.isArray(parsedValue)) {
      return [];
    }

    return parsedValue.filter(isFavoriteItem);
  } catch {
    return [];
  }
}

function saveFavoriteItems(items: FavoriteItem[]) {
  window.localStorage.setItem(favoritesStorageKey, JSON.stringify(items));
}

function isFavoriteItem(value: unknown): value is FavoriteItem {
  if (!value || typeof value !== "object") {
    return false;
  }

  const item = value as Partial<FavoriteItem>;

  return (
    typeof item.id === "string" &&
    typeof item.title === "string" &&
    typeof item.url === "string" &&
    typeof item.company === "string" &&
    typeof item.source === "string" &&
    typeof item.sourceSlug === "string" &&
    typeof item.favoritedAt === "string"
  );
}

export function SearchExperience() {
  const [query, setQuery] = useState("");
  const [sortOrder, setSortOrder] = useState<SearchSort>("latest");
  const [filters, setFilters] = useState<SearchFilters>(emptyFilters);
  const [currentPage, setCurrentPage] = useState(1);
  const [result, setResult] = useState<SearchResponse | null>(null);
  const [companyFacets, setCompanyFacets] = useState<FacetItem[]>([]);
  const [favoriteItems, setFavoriteItems] = useState<FavoriteItem[]>([]);
  const [showFavoritesOnly, setShowFavoritesOnly] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [errorMessage, setErrorMessage] = useState<string | null>(null);
  const [suggestions, setSuggestions] = useState<SuggestionItem[]>([]);
  const [isSuggestOpen, setIsSuggestOpen] = useState(false);
  const [activeSuggestionIndex, setActiveSuggestionIndex] = useState(-1);
  const suggestAbortRef = useRef<AbortController | null>(null);
  const committedQueryRef = useRef<string | null>(null);

  useEffect(() => {
    void runSearch("", "latest", emptyFilters, 1);
    setFavoriteItems(loadFavoriteItems());
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

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

  async function runSearch(
    nextQuery: string,
    nextSort: SearchSort = sortOrder,
    nextFilters: SearchFilters = filters,
    nextPage = 1,
  ) {
    const trimmedQuery = nextQuery.trim();
    const effectiveSort = trimmedQuery ? nextSort : "latest";
    committedQueryRef.current = trimmedQuery;
    setQuery(nextQuery);
    setSortOrder(effectiveSort);
    setCurrentPage(nextPage);
    setIsSuggestOpen(false);
    setActiveSuggestionIndex(-1);
    setSuggestions([]);

    setIsLoading(true);
    setErrorMessage(null);

    try {
      const params = new URLSearchParams({
        q: trimmedQuery,
        sort: effectiveSort,
        page: String(nextPage),
        page_size: String(pageSize),
      });
      appendFilterParams(params, nextFilters);
      const response = await fetch(
        `${apiBaseUrl}/api/search?${params.toString()}`,
      );

      if (!response.ok) {
        throw new Error(`검색 요청 실패: ${response.status}`);
      }

      const data = (await response.json()) as SearchResponse;
      setResult(data);
      if (nextFilters.sources.length === 0) {
        setCompanyFacets(data.facets.sources);
      }
    } catch (error) {
      setResult(null);
      setErrorMessage(error instanceof Error ? error.message : "검색 중 오류가 발생했습니다.");
    } finally {
      setIsLoading(false);
    }
  }

  function handleSortChange(nextSort: SearchSort) {
    const effectiveSort = query.trim() ? nextSort : "latest";
    setSortOrder(effectiveSort);

    if (result) {
      void runSearch(query, effectiveSort, filters, 1);
    }
  }

  function handleFilterToggle(key: keyof SearchFilters, value: string) {
    const nextFilters = toggleFilter(filters, key, value);
    setFilters(nextFilters);

    void runSearch(query, sortOrder, nextFilters, 1);
  }

  function handleCompanyToggle(value: string) {
    const nextFilters = {
      ...emptyFilters,
      sources: toggleValue(filters.sources, value),
    };
    setFilters(nextFilters);

    void runSearch("", "latest", nextFilters, 1);
  }

  function handleClearFilters() {
    setFilters(emptyFilters);
    void runSearch(query, sortOrder, emptyFilters, 1);
  }

  function handlePageChange(nextPage: number) {
    void runSearch(query, sortOrder, filters, nextPage);
  }

  function handleFavoriteToggle(item: SearchResultItem) {
    setFavoriteItems((currentItems) => {
      const isAlreadyFavorite = currentItems.some((favorite) => favorite.id === item.id);
      const nextItems = isAlreadyFavorite
        ? currentItems.filter((favorite) => favorite.id !== item.id)
        : [{ ...item, favoritedAt: new Date().toISOString() }, ...currentItems];

      saveFavoriteItems(nextItems);

      if (showFavoritesOnly && nextItems.length === 0) {
        setShowFavoritesOnly(false);
      }

      return nextItems;
    });
  }

  function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    const activeSuggestion = suggestions[activeSuggestionIndex];
    void runSearch(activeSuggestion?.label ?? query, sortOrder, filters, 1);
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
              onSelect={(suggestion) => void runSearch(suggestion.label, sortOrder, filters, 1)}
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
          <button
            className="tag"
            type="button"
            key={keyword}
            onClick={() => void runSearch(keyword, sortOrder, filters, 1)}
          >
            {keyword}
          </button>
        ))}
      </div>

      {companyFacets.length > 0 ? (
        <CompanyExplorer
          facets={companyFacets}
          selectedValues={filters.sources}
          onToggle={handleCompanyToggle}
        />
      ) : null}

      <div className="search-toolbar" aria-label="검색 정렬">
        <button
          className={`favorite-filter-button${showFavoritesOnly ? " is-active" : ""}`}
          type="button"
          aria-pressed={showFavoritesOnly}
          onClick={() => setShowFavoritesOnly((current) => !current)}
        >
          즐겨찾기 {favoriteItems.length}
        </button>
        <span>정렬</span>
        <div className="sort-control" role="radiogroup" aria-label="검색 결과 정렬">
          {sortOptions.map((option) => (
            <button
              className={`sort-option${sortOrder === option.value ? " is-active" : ""}`}
              type="button"
              key={option.value}
              role="radio"
              aria-checked={sortOrder === option.value}
              onClick={() => handleSortChange(option.value)}
            >
              {option.label}
            </button>
          ))}
        </div>
      </div>

      {result ? (
        <FilterPanel
          facets={result.facets}
          filters={filters}
          onToggle={handleFilterToggle}
          onClear={handleClearFilters}
        />
      ) : null}
      <SearchState
        result={result}
        isLoading={isLoading}
        errorMessage={errorMessage}
        currentPage={currentPage}
        favoriteItems={favoriteItems}
        showFavoritesOnly={showFavoritesOnly}
        favoriteIds={new Set(favoriteItems.map((item) => item.id))}
        onFavoriteToggle={handleFavoriteToggle}
        onPageChange={handlePageChange}
      />
    </section>
  );
}

function appendFilterParams(params: URLSearchParams, filters: SearchFilters) {
  filters.sources.forEach((value) => params.append("source", value));
  filters.technologies.forEach((value) => params.append("technology", value));
  filters.problemKeywords.forEach((value) => params.append("problem", value));
  filters.contentTypes.forEach((value) => params.append("content_type", value));
}

function toggleFilter(
  filters: SearchFilters,
  key: keyof SearchFilters,
  value: string,
): SearchFilters {
  return {
    ...filters,
    [key]: toggleValue(filters[key], value),
  };
}

function toggleValue(values: string[], value: string): string[] {
  return values.includes(value)
    ? values.filter((currentValue) => currentValue !== value)
    : [...values, value];
}

function selectedFilterCount(filters: SearchFilters): number {
  return Object.values(filters).reduce((total, values) => total + values.length, 0);
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

function CompanyExplorer({
  facets,
  selectedValues,
  onToggle,
}: {
  facets: FacetItem[];
  selectedValues: string[];
  onToggle: (value: string) => void;
}) {
  const visibleCompanies = mergeSelectedFacets(facets, selectedValues).slice(0, 16);

  if (visibleCompanies.length === 0) {
    return null;
  }

  return (
    <section className="company-explorer" aria-label="기업별 최신 글 탐색">
      <div className="company-explorer-header">
        <span>기업별 최신 글</span>
      </div>
      <div className="company-chip-list">
        {visibleCompanies.map((facet) => {
          const isSelected = selectedValues.includes(facet.value);
          const logo = getCompanyLogoByName(facet.label, facet.value);

          return (
            <button
              className={`company-chip${isSelected ? " is-active" : ""}`}
              type="button"
              key={`company-${facet.value}`}
              aria-pressed={isSelected}
              aria-label={`${facet.label} 최신 글 보기`}
              title={facet.label}
              onClick={() => onToggle(facet.value)}
            >
              <CompanyLogoMark logo={logo} label={facet.label} />
              <span>{facet.count}</span>
            </button>
          );
        })}
      </div>
    </section>
  );
}

function SearchState({
  result,
  isLoading,
  errorMessage,
  currentPage,
  favoriteItems,
  showFavoritesOnly,
  favoriteIds,
  onFavoriteToggle,
  onPageChange,
}: {
  result: SearchResponse | null;
  isLoading: boolean;
  errorMessage: string | null;
  currentPage: number;
  favoriteItems: FavoriteItem[];
  showFavoritesOnly: boolean;
  favoriteIds: Set<string>;
  onFavoriteToggle: (item: SearchResultItem) => void;
  onPageChange: (page: number) => void;
}) {
  if (showFavoritesOnly) {
    if (favoriteItems.length === 0) {
      return <p className="result-empty">아직 즐겨찾기한 사례가 없습니다.</p>;
    }

    return (
      <div className="results">
        <div className="result-summary">
          즐겨찾기한 사례 <strong>{favoriteItems.length}</strong>개를 보고 있습니다.
        </div>
        <ResultList
          items={favoriteItems}
          favoriteIds={favoriteIds}
          onFavoriteToggle={onFavoriteToggle}
        />
      </div>
    );
  }

  if (isLoading) {
    return <p className="result-empty">검색 결과를 불러오는 중입니다.</p>;
  }

  if (errorMessage) {
    return <p className="result-error">{errorMessage}</p>;
  }

  if (!result) {
    return (
      <p className="result-empty">
        최신 기업 기술 블로그 사례를 불러오는 중입니다.
      </p>
    );
  }

  if (result.items.length === 0) {
    return <p className="result-empty">`{result.query}`에 대한 검색 결과가 없습니다.</p>;
  }

  return (
    <div className="results">
      <div className="result-summary">
        {result.query ? (
          <>
            <strong>{result.total}</strong>개 사례 중 {formatResultRange(result)}를{" "}
            {formatSortLabel(result.sort)}으로 보고 있습니다.
          </>
        ) : (
          <>
            {result.filters.sources.length > 0 ? "선택한 기업의 최신 글" : "최신 기업 기술 블로그"}{" "}
            <strong>{result.total}</strong>개 중 {formatResultRange(result)}를 보고 있습니다.
          </>
        )}
      </div>
      <ResultOverview result={result} />
      <ResultList
        items={result.items}
        favoriteIds={favoriteIds}
        onFavoriteToggle={onFavoriteToggle}
      />
      <PaginationControls
        page={currentPage}
        totalPages={result.totalPages}
        onPageChange={onPageChange}
      />
    </div>
  );
}

function ResultList({
  items,
  favoriteIds,
  onFavoriteToggle,
}: {
  items: SearchResultItem[];
  favoriteIds: Set<string>;
  onFavoriteToggle: (item: SearchResultItem) => void;
}) {
  return (
    <div className="result-list">
      {items.map((item) => (
        <ResultCard
          item={item}
          isFavorite={favoriteIds.has(item.id)}
          key={item.id}
          onFavoriteToggle={onFavoriteToggle}
        />
      ))}
    </div>
  );
}

function ResultCard({
  item,
  isFavorite,
  onFavoriteToggle,
}: {
  item: SearchResultItem;
  isFavorite: boolean;
  onFavoriteToggle: (item: SearchResultItem) => void;
}) {
  const contentType = formatContentType(item.contentType);

  return (
    <article className="result-card">
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
        <div className="result-card-actions">
          {contentType ? <span className="result-type">{contentType}</span> : null}
          <button
            className={`favorite-button${isFavorite ? " is-active" : ""}`}
            type="button"
            aria-pressed={isFavorite}
            aria-label={isFavorite ? "즐겨찾기 해제" : "즐겨찾기 추가"}
            title={isFavorite ? "즐겨찾기 해제" : "즐겨찾기 추가"}
            onClick={() => onFavoriteToggle(item)}
          >
            ★
          </button>
        </div>
      </div>
      <h2>
        <a href={item.url} target="_blank" rel="noreferrer">
          <HighlightedText value={highlightOrText(item, "title", item.title)} />
        </a>
      </h2>
      <section className="case-summary" aria-label="사례 요약">
        <p>{bestSnippet(item)}</p>
      </section>
      <CaseDetails item={item} />
      <KeywordList item={item} />
      <div className="result-card-footer">
        <MatchEvidenceDetails item={item} />
        <a className="source-link" href={item.url} target="_blank" rel="noreferrer">
          원문 보기
        </a>
      </div>
    </article>
  );
}

function PaginationControls({
  page,
  totalPages,
  onPageChange,
}: {
  page: number;
  totalPages: number;
  onPageChange: (page: number) => void;
}) {
  if (totalPages <= 1) {
    return null;
  }

  const clampedPage = Math.min(Math.max(page, 1), totalPages);

  return (
    <nav className="pagination" aria-label="검색 결과 페이지">
      <button
        type="button"
        onClick={() => onPageChange(clampedPage - 1)}
        disabled={clampedPage <= 1}
      >
        이전
      </button>
      <span>
        {clampedPage} / {totalPages}
      </span>
      <button
        type="button"
        onClick={() => onPageChange(clampedPage + 1)}
        disabled={clampedPage >= totalPages}
      >
        다음
      </button>
    </nav>
  );
}

function ResultOverview({ result }: { result: SearchResponse }) {
  const technologyFacets = topFacets(result.facets.technologies, 3);
  const problemFacets = topFacets(result.facets.problemKeywords, 3);
  const sourceFacets = topFacets(result.facets.sources, 3);
  const activeFilterCount = selectedFilterCount(result.filters);

  if (
    technologyFacets.length === 0 &&
    problemFacets.length === 0 &&
    sourceFacets.length === 0 &&
    activeFilterCount === 0
  ) {
    return null;
  }

  return (
    <section className="result-overview" aria-label="검색 결과 요약">
      <OverviewGroup label="주요 기술" facets={technologyFacets} />
      <OverviewGroup label="문제 맥락" facets={problemFacets} />
      <OverviewGroup label="주요 출처" facets={sourceFacets} />
      {activeFilterCount > 0 ? (
        <div className="overview-group">
          <span>적용 필터</span>
          <div className="overview-chips">
            <span>{activeFilterCount}개 적용 중</span>
          </div>
        </div>
      ) : null}
    </section>
  );
}

function OverviewGroup({ label, facets }: { label: string; facets: FacetItem[] }) {
  if (facets.length === 0) {
    return null;
  }

  return (
    <div className="overview-group">
      <span>{label}</span>
      <div className="overview-chips">
        {facets.map((facet) => (
          <span className={facet.isRecommended ? "is-recommended" : ""} key={facet.value}>
            {facet.label}
          </span>
        ))}
      </div>
    </div>
  );
}

function topFacets(facets: FacetItem[], limit: number): FacetItem[] {
  return facets.slice(0, limit);
}

function FilterPanel({
  facets,
  filters,
  onToggle,
  onClear,
}: {
  facets: SearchFacets;
  filters: SearchFilters;
  onToggle: (key: keyof SearchFilters, value: string) => void;
  onClear: () => void;
}) {
  const activeCount = selectedFilterCount(filters);
  const summaryText = activeCount > 0 ? `${activeCount}개 적용 중` : "필터 열기";

  return (
    <details className="filter-panel" open={activeCount > 0 ? true : undefined}>
      <summary className="filter-panel-summary">
        <span>결과 좁히기</span>
        <span>{summaryText}</span>
      </summary>
      <div className="filter-panel-body">
        <div className="filter-panel-header">
          <span>필터</span>
          {activeCount > 0 ? (
            <button type="button" onClick={onClear}>
              필터 초기화
            </button>
          ) : null}
        </div>
        <FacetGroup
          label="회사"
          filterKey="sources"
          facets={facets.sources}
          selectedValues={filters.sources}
          onToggle={onToggle}
        />
        <FacetGroup
          label="기술"
          filterKey="technologies"
          facets={facets.technologies}
          selectedValues={filters.technologies}
          onToggle={onToggle}
        />
        <FacetGroup
          label="문제 상황"
          filterKey="problemKeywords"
          facets={facets.problemKeywords}
          selectedValues={filters.problemKeywords}
          onToggle={onToggle}
        />
        <FacetGroup
          label="유형"
          filterKey="contentTypes"
          facets={facets.contentTypes}
          selectedValues={filters.contentTypes}
          onToggle={onToggle}
        />
      </div>
    </details>
  );
}

function FacetGroup({
  label,
  filterKey,
  facets,
  selectedValues,
  onToggle,
}: {
  label: string;
  filterKey: keyof SearchFilters;
  facets: FacetItem[];
  selectedValues: string[];
  onToggle: (key: keyof SearchFilters, value: string) => void;
}) {
  const visibleFacets = mergeSelectedFacets(facets, selectedValues);

  if (visibleFacets.length === 0) {
    return null;
  }

  return (
    <section className="facet-group" aria-label={`${label} 필터`}>
      <span>{label}</span>
      <div className="facet-list">
        {visibleFacets.map((facet) => {
          const isSelected = selectedValues.includes(facet.value);

          return (
            <button
              className={`facet-chip${isSelected ? " is-active" : ""}${
                facet.isRecommended ? " is-recommended" : ""
              }`}
              type="button"
              key={`${filterKey}-${facet.value}`}
              aria-pressed={isSelected}
              onClick={() => onToggle(filterKey, facet.value)}
            >
              <span>{facet.label}</span>
              <span>{facet.count}</span>
            </button>
          );
        })}
      </div>
    </section>
  );
}

function mergeSelectedFacets(facets: FacetItem[], selectedValues: string[]): FacetItem[] {
  const facetValues = new Set(facets.map((facet) => facet.value));
  const missingSelectedFacets = selectedValues
    .filter((value) => !facetValues.has(value))
    .map((value) => ({ value, label: value, count: 0 }));

  return [...missingSelectedFacets, ...facets].slice(0, 12);
}

function formatSortLabel(sort: SearchSort): string {
  return sortOptions.find((option) => option.value === sort)?.label ?? "관련도순";
}

function formatResultRange(result: SearchResponse): string {
  if (result.total === 0 || result.items.length === 0) {
    return "0개";
  }

  const start = (result.page - 1) * result.pageSize + 1;
  const end = start + result.items.length - 1;

  return `${start}-${end}번째`;
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

  return <CompanyLogoMark logo={logo} label={item.company} />;
}

function CompanyLogoMark({ logo, label }: { logo: CompanyLogo; label: string }) {
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
      aria-label={`${label} 로고`}
      title={label}
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

function MatchEvidenceDetails({ item }: { item: SearchResultItem }) {
  const reasons = matchReasons(item);

  if (reasons.length === 0) {
    return null;
  }

  return (
    <details className="evidence-details">
      <summary>검색 근거 보기</summary>
      <MatchReasons item={item} />
    </details>
  );
}

function KeywordList({ item }: { item: SearchResultItem }) {
  const technologyKeywords = uniqueKeywords(item.technologies);
  const problemKeywords = uniqueKeywords(item.problemKeywords);
  const architectureKeywords = uniqueKeywords(item.architectureKeywords);

  if (
    technologyKeywords.length === 0 &&
    problemKeywords.length === 0 &&
    architectureKeywords.length === 0
  ) {
    return null;
  }

  return (
    <div className="keyword-groups">
      <KeywordGroup label="기술" keywords={technologyKeywords} limit={3} />
      <KeywordGroup label="문제" keywords={problemKeywords} limit={2} />
      <KeywordGroup label="구조" keywords={architectureKeywords} limit={2} />
    </div>
  );
}

function KeywordGroup({
  label,
  keywords,
  limit,
}: {
  label: string;
  keywords: string[];
  limit: number;
}) {
  if (keywords.length === 0) {
    return null;
  }

  const visibleKeywords = keywords.slice(0, limit);
  const hiddenCount = Math.max(keywords.length - visibleKeywords.length, 0);

  return (
    <div className="keyword-group">
      <span className="keyword-group-label">{label}</span>
      <div className="result-keywords">
        {visibleKeywords.map((keyword) => (
          <span key={`${label}-${keyword}`}>{keyword}</span>
        ))}
        {hiddenCount > 0 ? <span className="keyword-more">+{hiddenCount}</span> : null}
      </div>
    </div>
  );
}
