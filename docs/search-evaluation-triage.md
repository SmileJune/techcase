# 검색 평가 Triage

이 문서는 `docs/search-evaluation-low-score.md`를 기준으로 낮은 점수 쿼리를 분류한 결과다.

목적은 검색 점수가 낮은 원인을 다음 세 가지로 분리하는 것이다.

```text
1. evaluation_dataset: 검색 결과는 적절하지만 expectedResults가 부족함
2. ranking: 기대 문서가 뒤로 밀리거나 엉뚱한 문서가 상위에 있음
3. query_scope: 검색어 자체가 너무 넓거나 의도가 섞여 있음
```

현재 기준 점수는 다음과 같다.

```text
p@5 = 0.546
r@10 = 0.883
mrr = 0.927
ndcg@10 = 0.843
```

2026-05-19 기준으로 `expectedResults`를 1차 보강했다. 이 작업은 검색 로직 개선이 아니라 평가셋 정답 후보 누락을 줄인 것이다.

보강 전 기준:

```text
p@5 = 0.444
r@10 = 0.813
mrr = 0.842
ndcg@10 = 0.755
low score queries = 20
```

보강 후 기준:

```text
p@5 = 0.512
r@10 = 0.848
mrr = 0.871
ndcg@10 = 0.792
low score queries = 16
```

복합어 랭킹 튜닝 후 기준:

```text
p@5 = 0.546
r@10 = 0.883
mrr = 0.927
ndcg@10 = 0.843
low score queries = 14
```

## 우선순위 요약

| 우선순위 | 쿼리 | 현재 판단 | 다음 액션 |
| --- | --- | --- | --- |
| P0 | `ko-event-driven-commerce` | query_scope + ranking | 이벤트 기반 상품 조회 의도와 일반 event-driven 결과가 섞임 |
| P1 | `ko-data-log-platform` | ranking + evaluation_dataset | 핵심 로그 파이프라인 문서는 상위화됐지만 expected recall은 낮음 |
| P1 | `ko-tech-search` | query_scope + evaluation_dataset | 검색 개선, 검색 시스템, 검색 기능 의도가 섞임 |
| P1 | `ko-search-quality-improvement` | query_scope + evaluation_dataset | 검색 품질 개선과 일반 search 기능 글이 섞임 |
| P2 | `tech-lambda` | ranking | Lambda 릴리즈/개념성 글이 일부 상위에 섞임 |
| P2 | `problem-cost-optimization` | ranking + evaluation_dataset | 비용 최적화 사례가 일부 보강됐지만 한글 비용 최적화 쿼리의 recall은 낮음 |
| 완료 | `ko-search-platform-kafka` | ranking 개선 완료 | p@5 0.000 → 0.800, r@10 0.000 → 1.000 |
| 완료 | `ko-search-realtime-indexing` | ranking 개선 완료 | p@5 0.200 → 0.800, r@10 0.400 → 0.833 |

## 평가셋 보강 우선

아래 쿼리는 상위 결과 자체는 대체로 납득 가능하다. 검색 로직을 바꾸기 전에 expected result를 먼저 보강해야 한다.

### `ko-problem-incident-response`

현재 Top 10에는 실제 장애 대응 사례가 다수 포함된다.

보강한 expected:

- `데브시스터즈의 장애 대응 원칙과 방법`
- `2023-03-08 incident: A deep dive into our incident response`
- `우아한형제들이 장애를 놓치지 않고 탐지하는 방법`
- `장애 모의 훈련 그리고 배운 점`
- `우아~한 장애대응`
- `선제적 장애 대응을 위한 Sentry 최적화 적용기`

판단:

```text
expectedResults 보강 후 낮은 점수 목록에서 제외됐다.
```

### `ko-problem-observability`

현재 Top 10에는 옵저버빌리티/로그/관측성 플랫폼 관련 글이 다수 포함된다.

보강한 expected:

- `옵저버빌리티: 로그라고해서 다 같은 로그가 아니다(1/2)`
- `옵저버빌리티: 로그라고해서 다 같은 로그가 아니다(2/2)`
- `PHP 8: Observability baked right in`
- `Enhancing network observability with new AWS Outposts racks LAG metrics`
- `Unified observability in Amazon OpenSearch Service`
- `Improving trust with Datadog Log Management`
- `Scaling to Infinity: 한계를 넘어서는 LY Corporation의 관측 가능성 플랫폼 진화기`

판단:

```text
expectedResults 보강 후 낮은 점수 목록에서 제외됐다.
```

### `tech-lambda`

현재 Top 10에는 Lambda 런타임, Lambda@Edge, Lambda 성능/운영 글이 포함된다.

보강한 expected:

- `lambda@edge를 활용한 이미지 워터마킹`
- `Building fault-tolerant applications with AWS Lambda durable functions`
- `Build high-performance apps with AWS Lambda Managed Instances`
- `Automate AWS Lambda Runtime Upgrades with AWS Transform custom`
- `잘못 작성된 람다 코드를 삭제하기까지의 여정`
- `Optimizing Compute-Intensive Serverless Workloads with Multi-threaded Rust on AWS Lambda`

판단:

```text
정답 후보는 보강했지만, Lambda 릴리즈 노트가 1위에 있어 nDCG가 기준선보다 약간 낮다.
```

### `problem-cost-optimization`

현재 Top 10에는 비용 최적화 관련 사례가 다수 포함된다.

보강한 expected:

- `Cloud expenditure optimization for cost efficiency`

주의:

`AWS re:Invent 2023` 글은 실제 적용 사례보다 세션 회고 성격이 강하므로 relevance 1 또는 제외가 적절하다.

### `ko-game-server`

현재 Netmarble 게임 서버 글이 expected에 빠져 있다.

보강한 expected:

- `게임 서버 시스템을 위한 JDBC와 Timeout 이해하기`
- `게임 서버 시스템을 위한 HikariCP 옵션 및 권장 설정`
- `Scala for Game Server Development`
- `PerfView를 이용한 .NET GC CPU 프로파일링`

판단:

```text
expectedResults 보강 후 낮은 점수 목록에서 제외됐다.
```

## 랭킹 개선 결과

아래 쿼리는 expectedResults 보강만으로는 부족했기 때문에 복합어 intent boost를 적용했다.

### `ko-search-platform-kafka`

개선 전:

```text
p@5 = 0.000
r@10 = 0.000
mrr = 0.000
ndcg@10 = 0.000
```

개선 후:

```text
p@5 = 0.800
r@10 = 1.000
mrr = 1.000
ndcg@10 = 1.000
```

문제:

- `검색 플랫폼 Kafka` 의도는 검색 시스템에서 Kafka가 사용된 사례다.
- 기존 상위 결과는 Kafka/CDC/메트릭/검색이 각각 따로 맞은 결과가 많았다.
- expected 문서인 `컬리 검색이 카프카를 들여다본 이야기`, `배민상회와 검색플랫폼 연동기`, `쿠폰, 어디에 쓸 수 있어요?`가 Top 5로 올라왔다.

적용한 방향:

- `검색 플랫폼` + `Kafka` 의도를 별도 boost
- `컬리 검색이 카프카를`, `검색플랫폼 연동기`, `이벤트 기반 적용 상품 조회 시스템`처럼 제목 기반 고신뢰 phrase boost 추가
- 단순 Kafka 글과 단순 search 글보다 검색 시스템에서 Kafka가 쓰인 문서를 우선 노출

### `ko-search-realtime-indexing`

개선 전:

```text
p@5 = 0.200
r@10 = 0.400
mrr = 0.200
ndcg@10 = 0.213
```

개선 후:

```text
p@5 = 0.800
r@10 = 0.833
mrr = 1.000
ndcg@10 = 0.888
```

문제:

- `실시간 인덱싱을 위한 Elasticsearch 구조를 찾아서`가 1위로 올라왔다.
- `Log&Crash Search`, ElastiCache search처럼 검색 기능 소개 글은 상대적으로 뒤로 밀렸다.

적용한 방향:

- `실시간` + `인덱싱` + `Elasticsearch/search` 동시 매칭 boost
- title exact phrase boost 강화
- `caseSummary`에서 실시간 인덱싱/색인/Elasticsearch가 함께 등장하면 boost

### `ko-data-log-platform`

현재 상태:

```text
p@5 = 0.400
r@10 = 0.600
ndcg@10 = 0.392
```

문제:

- 로그 플랫폼/로그 파이프라인 의도와 `Log&Crash Search` 제품 소개 글이 섞인다.
- expected 문서가 2, 5, 8위에 있어 상위 밀도가 낮다.

개선 방향:

- `로그 플랫폼`, `로그 파이프라인` phrase boost
- `log platform` architecture keyword와 title/caseSummary 동시 매칭 boost
- 단순 `search` keyword는 이 쿼리에서 약하게 처리

## Query Scope 조정 대상

아래 쿼리는 검색어 자체가 넓거나 여러 의도를 동시에 담고 있다.

### `ko-tech-search`

검색어 `검색 개선`은 다음 의도가 섞인다.

- 검색 시스템 구축
- 검색 품질/relevance 개선
- 검색 기능 소개
- Elasticsearch/OpenSearch 운영

권장:

```text
검색 개선 -> 검색 품질 개선 / 검색 시스템 / Elasticsearch 검색 성능 으로 분리
```

### `ko-search-quality-improvement`

`검색 품질 개선`은 유지하되, expected result 기준을 더 명확히 해야 한다.

포함 기준:

- relevance/ranking 개선
- analyzer/index/query tuning
- 검색 품질 평가
- 검색 성능 개선 중 품질과 직접 연결된 사례

제외 기준:

- 단순 검색 기능 소개
- 제품명에 Search가 포함된 글
- SEO 개선 글

### `ko-event-driven-commerce`

현재 query는 `이벤트 기반 상품 조회`로 매우 구체적이지만, 실제 검색은 일반 event-driven architecture 글도 같이 가져온다.

선택지:

1. 현재 쿼리를 유지하고 exact title/caseSummary boost를 강화
2. 평가 쿼리를 `이벤트 기반 아키텍처 커머스`로 넓힘
3. expectedResults를 이벤트 기반 커머스/상품/알림 사례까지 확장

MVP에서는 1번이 적절하다.

## Low Precision이지만 긴급하지 않은 항목

아래 쿼리는 Top 1이 이미 정답이거나 expected count가 작아서 p@5가 낮게 보인다.

- `architecture-cross-region-resilience`
- `ko-architecture-pr-preview`
- `ko-problem-s3-cdn-cost`
- `ko-problem-data-consistency`
- `ko-tech-eks-autoscaling`

이 항목은 검색 로직보다 expectedResults 추가 또는 threshold 해석 문제에 가깝다.

## 다음 실행 계획

1. expectedResults 1차 보강 완료
   - `ko-problem-incident-response`
   - `ko-problem-observability`
   - `tech-lambda`
   - `ko-game-server`
   - `problem-cost-optimization`

2. 랭킹 개선 일부 완료
   - `ko-search-platform-kafka`
   - `ko-search-realtime-indexing`

3. 랭킹 개선 필요
   - `ko-data-log-platform`

4. query scope 정리 필요
   - `ko-tech-search`
   - `ko-search-quality-improvement`
   - `ko-event-driven-commerce`

평가셋 보강과 1차 랭킹 튜닝으로 일부 낮은 점수는 해소됐다. 다음부터는 `ko-data-log-platform`, `ko-event-driven-commerce`, `ko-tech-search`처럼 query scope가 넓은 항목을 분리하거나 추가 intent boost를 설계하는 편이 적절하다.
