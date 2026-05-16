const quickSearches = [
  "Lambda",
  "EventBridge",
  "DynamoDB",
  "EKS",
  "event-driven",
  "cost optimization",
];

export default function Home() {
  return (
    <main className="page-shell">
      <header className="topbar">
        <div className="brand">TechCase</div>
        <div className="status-pill">AWS 기술 블로그 MVP</div>
      </header>

      <section className="hero">
        <h1>기술 도입과 이슈 해결을 위한 기업 사례 검색</h1>
        <p>
          TechCase는 신뢰도 높은 기업 기술 블로그를 기반으로 기술 스택 도입 배경,
          아키텍처 맥락, 문제 해결 사례를 빠르게 탐색할 수 있도록 돕습니다.
        </p>
      </section>

      <section className="search-panel" aria-label="기술 사례 검색">
        <form className="search-row">
          <input
            className="search-input"
            name="q"
            placeholder="Lambda, EventBridge, migration, event-driven..."
            aria-label="검색어"
          />
          <button className="search-button" type="submit">
            검색
          </button>
        </form>

        <div className="tag-list" aria-label="추천 검색어">
          {quickSearches.map((keyword) => (
            <button className="tag" type="button" key={keyword}>
              {keyword}
            </button>
          ))}
        </div>

        <p className="result-empty">
          아직 검색 UI 골격 단계입니다. 다음 단계에서 FastAPI 검색 API와 연결하고 AWS RSS 수집
          데이터를 표시합니다.
        </p>
      </section>
    </main>
  );
}

