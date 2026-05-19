# 검색 키워드 Probe 운영 방식

TechCase 검색 품질은 두 가지 평가 루프로 관리한다.

1. `search:evaluate`: 사람이 정답 URL을 지정한 소수 핵심 쿼리의 정량 평가
2. `search:keyword-probe`: 많은 키워드의 Top N 결과를 자동 수집하고 이상 후보를 찾는 탐색 평가

`search:keyword-probe`는 검색 품질을 확정적으로 채점하지 않는다. 대신 공개 전 점검해야 할 키워드를 빠르게 찾기 위한 triage 도구다.

## 실행 명령

```bash
npm run search:keyword-probe
```

기본 입력 파일:

```text
apps/backend/app/search/evaluation/keyword_pool.json
```

기본 출력 파일:

```text
docs/search-keyword-probe-report.md
docs/search-keyword-probe-results.json
```

일부만 빠르게 확인하고 싶으면 backend 경로에서 직접 실행한다.

```bash
cd apps/backend
uv run python -m app.search.evaluation.keyword_probe --limit 20
```

## 키워드 풀 구조

각 검색어는 다음 정보를 가진다.

```json
{
  "query": "Kafka",
  "category": "technology",
  "priority": "high",
  "aliases": ["카프카", "Apache Kafka", "MSK"],
  "intent": "Kafka가 메시징, 이벤트 처리, CDC, 로그 파이프라인, 스트리밍 맥락에서 사용된 사례가 상위에 나와야 한다.",
  "intendedTerms": ["kafka", "카프카", "msk", "event", "cdc", "stream", "log"]
}
```

- `query`: 실제 검색어
- `category`: technology, problem, architecture, domain, company 등
- `priority`: high, medium, low
- `aliases`: 같은 의도의 다른 표현
- `intent`: 사람이 결과를 판단할 때 기준이 되는 기대 의도
- `intendedTerms`: 자동 진단에서 상위 결과가 의도와 맞는지 대략 확인할 단어

## 자동 진단 항목

- `no_results`: 검색 결과가 0개
- `url_title`: 상위 결과 제목이 URL 형태
- `broad_results`: 결과가 지나치게 많아 검색어가 넓게 매칭됨
- `other_dominant`: 상위 5개 중 `other` 타입이 3개 이상
- `weak_intent_match`: 상위 결과 텍스트에서 query, alias, intendedTerms가 거의 확인되지 않음
- `missing_case_summary`: 상위 결과에 LLM 사례 요약이 없음
- `no_highlights`: 검색어가 있는데 하이라이트가 없음
- `single_source_dominance`: 상위 5개 중 4개 이상이 같은 source

이 진단은 오탐이 있을 수 있다. 목적은 “문제일 가능성이 높은 검색어를 먼저 보게 하는 것”이다.

## 개선 루프

1. `npm run search:keyword-probe` 실행
2. `docs/search-keyword-probe-report.md`의 `Review Priority` 확인
3. 문제 유형 분류
4. alias, keyword dictionary, 검색 boost, LLM 요약, source 수집 상태 중 원인 선택
5. 수정 후 `search:reindex`, `suggest:reindex`, `search:keyword-probe` 재실행
6. 개선된 검색어는 필요하면 `queries.json`의 정답셋 평가로 승격

## 해석 기준

`search:keyword-probe`에서 진단이 잡혔다고 모두 버그는 아니다.

예를 들어 회사명 검색은 특정 source가 상위에 몰리는 것이 정상일 수 있다. 반대로 `Kafka`, `Redis`, `장애 대응`, `검색 품질 개선` 같은 핵심 검색어에서 `weak_intent_match`, `other_dominant`, `no_results`가 나오면 우선적으로 개선해야 한다.
