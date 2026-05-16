import { SearchExperience } from "./components/SearchExperience";

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

      <SearchExperience />
    </main>
  );
}
