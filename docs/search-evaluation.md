# 검색 평가 데이터셋

이 문서는 TechCase 검색 품질을 개선할 때, 이전 검색 결과보다 실제로 좋아졌는지 판단하기 위한 기준을 정리합니다.

평가 데이터셋 원본은 다음 파일에 둡니다.

```text
apps/backend/app/search/evaluation/queries.json
```

## 목적

검색 품질 개선은 단순히 결과가 더 많이 나오는지보다, 사용자가 원하는 사례가 상위 결과에 잘 노출되는지가 중요합니다.

TechCase의 검색 평가는 다음 질문에 답하는 것을 목표로 합니다.

- 기술명으로 검색했을 때 관련 기업 사례가 상위에 나오는가?
- 문제 상황으로 검색했을 때 적절한 해결 사례가 나오는가?
- 아키텍처 키워드로 검색했을 때 연결된 기술 사례가 나오는가?
- 검색 개선 전후를 수치로 비교할 수 있는가?

## 평가 쿼리 구성

초기 평가셋은 AWS 기술 블로그 RSS에서 실제로 수집된 글을 기준으로 만들었습니다.

이후 Toss Tech, NAVER D2, Kakao Tech, Woowa Tech Blog를 추가하면서 한글 검색 평가 쿼리도 포함했습니다.
한국어 우선순위 기술 블로그 10곳을 추가한 뒤에는 신규 기업 사례를 반영한 한글 평가 쿼리를 보강했습니다.

쿼리 유형은 다음과 같이 나눴습니다.

```text
technology: Lambda, DynamoDB, EKS, OpenSearch, Apache Flink
problem: cost optimization, observability, incident response
architecture: streaming data pipeline, Change Data Capture, cross-Region resilience
migration: Kafka MSK migration
ko query: 비용 최적화, 장애 대응, 카프카 마이그레이션, 서버리스
new ko source query: EKS 오토스케일링, 옵저버빌리티, 카나리 배포, 검색 개선, 로그 플랫폼, JVM 응답 지연, 게임 서버, 이벤트 기반 상품 조회
```

각 쿼리는 다음 정보를 가집니다.

```text
id: 평가 쿼리 식별자
query: 실제 검색어
category: 검색 의도 유형
intent: 사용자가 이 검색어로 찾으려는 내용
expectedResults: 검색 결과에 포함되면 좋은 정답 문서 목록
```

`expectedResults`의 `relevance`는 다음 기준을 사용합니다.

```text
3: 검색 의도와 매우 직접적으로 관련 있음
2: 검색 의도와 관련 있지만 핵심 사례는 아님
1: 약하게 관련 있음
```

현재 데이터셋에서는 명확한 비교를 위해 `relevance` 2 이상만 포함했습니다.

## 평가 지표

MVP 단계에서는 다음 지표를 우선 사용합니다.

### Precision@5

상위 5개 검색 결과 중 관련 있는 글의 비율입니다.

사용자는 보통 검색 결과의 상단만 보기 때문에 체감 품질과 가장 가깝습니다.

```text
Precision@5 = top 5 안의 정답 결과 수 / 5
```

### Recall@10

기대 결과 중 상위 10개 안에 포함된 비율입니다.

검색 개선 후 관련 사례를 더 잘 찾아내는지 확인할 수 있습니다.

```text
Recall@10 = top 10 안에 포함된 정답 결과 수 / 기대 결과 수
```

### MRR

첫 번째 정답 결과가 몇 번째에 나오는지 보는 지표입니다.

```text
MRR = 1 / 첫 번째 정답 결과의 순위
```

예를 들어 첫 번째 정답이 1위면 `1.0`, 3위면 `0.333`입니다.

### NDCG@10

관련도가 높은 결과가 상위에 잘 배치되는지 보는 지표입니다.

단순히 정답이 포함됐는지뿐 아니라, `relevance: 3`인 결과가 `relevance: 2`보다 위에 있는지도 평가할 수 있습니다.

## 개선 전후 비교 방법

검색 품질 개선 작업을 하기 전후로 같은 평가셋을 사용해 결과를 비교합니다.

```text
1. 현재 검색 API로 queries.json의 query를 실행한다.
2. top 10 결과 URL을 저장한다.
3. Precision@5, Recall@10, MRR, NDCG@10을 계산한다.
4. 키워드 추출, 동의어 처리, 검색 가중치 조정 등을 적용한다.
5. 같은 쿼리로 다시 평가한다.
6. 개선 전후 점수를 비교한다.
```

예시:

```text
Lambda

Before:
Precision@5 = 0.60
Recall@10 = 0.67
MRR = 1.00

After:
Precision@5 = 0.80
Recall@10 = 1.00
MRR = 1.00
```

이렇게 기록하면 검색 품질 개선을 구현 내용이 아니라 수치 기반으로 설명할 수 있습니다.

## 현재 한계

현재 평가셋은 AWS RSS에서 수집된 글만 기준으로 만들어졌습니다.

따라서 다음 한계가 있습니다.

- AWS 외 기업 사례는 아직 포함하지 않았습니다.
- Kafka, Kubernetes, Terraform 같은 범용 기술은 AWS RSS 안의 일부 사례만 평가합니다.
- 본문 추출이 아직 없기 때문에 제목과 요약에 표현되지 않은 관련성은 평가하기 어렵습니다.
- 사람이 직접 고른 expected result이므로, 데이터가 늘어나면 주기적으로 보정해야 합니다.

## 자동 평가 명령

이 데이터셋을 사용하는 자동 평가 명령을 추가했습니다.

```bash
npm run search:evaluate
```

이 명령은 다음 흐름으로 동작합니다.

```text
queries.json 로드
각 query를 search service로 실행
검색 결과 URL과 expectedResults URL 비교
Precision@5, Recall@10, MRR, NDCG@10 계산
전체 평균 점수 출력
JSON 평가 결과 저장
낮은 점수 쿼리 리포트 저장
```

실행 전에는 Elasticsearch에 `articles` index가 생성되어 있고 문서가 색인되어 있어야 합니다.

```bash
npm run search:reindex
npm run search:evaluate
```

기본 산출물은 다음 위치에 생성됩니다.

```text
docs/search-evaluation-results.json
docs/search-evaluation-low-score.md
```

`search-evaluation-results.json`은 검색 튜닝 전후 비교에 사용할 수 있는 구조화된 결과입니다.

`search-evaluation-low-score.md`는 다음 기본 기준을 만족하지 못한 쿼리를 우선 검토 대상으로 분리합니다.

```text
Precision@5 >= 0.4
Recall@10 >= 0.8
MRR >= 0.5
NDCG@10 >= 0.7
```

기준값은 직접 실행 시 옵션으로 조정할 수 있습니다.

```bash
cd apps/backend
uv run python -m app.search.evaluation.evaluator \
  --min-precision-at-5 0.5 \
  --min-recall-at-10 0.8 \
  --min-mrr 0.7 \
  --min-ndcg-at-10 0.75
```

파일을 쓰지 않고 콘솔 표만 보고 싶을 때는 다음 옵션을 사용합니다.

```bash
cd apps/backend
uv run python -m app.search.evaluation.evaluator --no-write
```

낮은 점수 쿼리를 검토한 뒤에는 다음 문서에서 원인을 분류합니다.

```text
docs/search-evaluation-triage.md
```

이 문서는 낮은 점수 원인을 `evaluation_dataset`, `ranking`, `query_scope`로 분리해 다음 작업 순서를 정하는 데 사용합니다.

## 현재 기준 점수

2026-05-16 기준, AWS RSS 100개 글을 색인한 상태에서의 초기 검색 점수는 다음과 같습니다.

키워드 추출 전:

```text
average precision@5 = 0.383
average recall@10 = 0.708
average mrr = 0.875
average ndcg@10 = 0.752
```

쿼리별 결과:

```text
query_id                               category     total    p@5   r@10    mrr  ndcg@10
------------------------------------------------------------------------------------------
tech-lambda                            technology       9  0.200  1.000  0.500    0.612
tech-dynamodb                          technology       3  0.600  1.000  1.000    1.000
tech-eks                               technology       4  0.600  1.000  1.000    0.959
tech-opensearch                        technology       4  0.600  1.000  1.000    1.000
tech-apache-flink                      technology       3  0.600  1.000  1.000    0.845
problem-cost-optimization              problem          0  0.000  0.000  0.000    0.000
problem-observability                  problem          7  0.400  0.667  1.000    0.884
problem-incident-response              problem          4  0.600  1.000  1.000    0.906
architecture-streaming-pipeline        architecture     3  0.400  0.667  1.000    0.813
architecture-cdc                       architecture     1  0.200  0.500  1.000    0.787
architecture-cross-region-resilience   architecture     1  0.200  0.333  1.000    0.674
migration-kafka-msk                    migration        1  0.200  0.333  1.000    0.542
```

현재 검색은 아직 제목과 RSS 요약 중심입니다. 따라서 `cost optimization`, `streaming data pipeline`, `cross-Region resilience`, `Kafka MSK migration`처럼 여러 단어의 문제/아키텍처 검색에서 한계가 드러납니다.

`dictionary_v1` 키워드 추출 적용 후:

```text
average precision@5 = 0.467
average recall@10 = 0.944
average mrr = 0.917
average ndcg@10 = 0.860
```

쿼리별 결과:

```text
query_id                               category     total    p@5   r@10    mrr  ndcg@10
------------------------------------------------------------------------------------------
tech-lambda                            technology       9  0.200  1.000  0.500    0.612
tech-dynamodb                          technology       3  0.600  1.000  1.000    1.000
tech-eks                               technology       4  0.600  1.000  1.000    0.959
tech-opensearch                        technology       4  0.600  1.000  1.000    1.000
tech-apache-flink                      technology       3  0.600  1.000  1.000    0.845
problem-cost-optimization              problem         10  0.200  1.000  0.500    0.590
problem-observability                  problem         16  0.400  1.000  1.000    0.957
problem-incident-response              problem          8  0.600  1.000  1.000    0.906
architecture-streaming-pipeline        architecture     6  0.600  1.000  1.000    0.913
architecture-cdc                       architecture     2  0.400  1.000  1.000    1.000
architecture-cross-region-resilience   architecture     3  0.600  1.000  1.000    1.000
migration-kafka-msk                    migration        1  0.200  0.333  1.000    0.542
```

개선 폭:

```text
average precision@5: 0.383 -> 0.467
average recall@10: 0.708 -> 0.944
average mrr: 0.875 -> 0.917
average ndcg@10: 0.752 -> 0.860
```

다음 검색 품질 개선 작업에서는 이 baseline보다 다음 지표가 올라가는지 확인합니다.

```text
average precision@5
average recall@10
problem/architecture category의 recall@10
```

한국 기술 블로그 source와 한글 query expansion을 추가한 뒤, AWS 100개 글과 한국 기술 블로그 60개 글을 합쳐 총 160개 글을 색인한 기준 점수는 다음과 같습니다.

```text
evaluation queries = 16
indexed articles = 160

average precision@5 = 0.475
average recall@10 = 0.958
average mrr = 0.896
average ndcg@10 = 0.847
```

한글 평가 쿼리:

```text
ko-problem-cost-optimization
ko-problem-incident-response
ko-migration-kafka
ko-architecture-serverless
```

우아한형제들 기술블로그 RSS pagination을 적용한 뒤에는 색인 글 수가 662개로 증가했습니다.

```text
AWS blogs = 100
Toss Tech = 20
NAVER D2 = 20
Kakao Tech = 10
Woowa Tech Blog = 512
indexed articles = 662
```

662개 글 기준 평가 점수:

```text
average precision@5 = 0.438
average recall@10 = 0.927
average mrr = 0.729
average ndcg@10 = 0.738
```

글 수가 늘면서 recall은 여전히 높은 편이지만, 일부 query의 상위 순위가 흔들렸습니다. 특히 `ko-migration-kafka`, `ko-problem-cost-optimization`처럼 한글 query expansion을 거친 검색에서 관련도 낮은 글이 상위에 섞일 수 있습니다.

다음 ranking 개선에서는 다음을 우선 검토합니다.

```text
정확히 매칭된 기술 키워드 우선 정렬
technology + problem 조합이 함께 매칭된 글 가중치 강화
source 확장 후 평가셋 expected result 보정
한글 query expansion의 boost 조정
```

한국어 우선순위 기술 블로그 10곳을 추가한 뒤, 신규 source 기반 평가 쿼리 8개를 추가했습니다.

추가 쿼리:

```text
ko-tech-eks-autoscaling
ko-problem-observability
ko-deployment-canary
ko-tech-search
ko-data-log-platform
ko-problem-jvm-latency
ko-game-server
ko-event-driven-commerce
```

1116개 글 기준 평가 점수:

```text
evaluation queries = 24
indexed articles = 1116

average precision@5 = 0.367
average recall@10 = 0.749
average mrr = 0.701
average ndcg@10 = 0.632
```

신규 쿼리는 실제 수집된 한국어 기업 블로그 글을 기준으로 만들었습니다.

좋게 나온 쿼리:

```text
ko-tech-eks-autoscaling
ko-game-server
ko-event-driven-commerce
ko-deployment-canary
```

개선이 필요한 쿼리:

```text
ko-problem-cost-optimization
ko-data-log-platform
ko-tech-search
ko-problem-jvm-latency
```

특히 `로그 플랫폼`, `검색 개선`처럼 일반 명사 조합으로 이루어진 쿼리는 관련 없는 글도 함께 많이 검색됩니다. 다음 검색 품질 개선에서는 한글 복합어/문제상황 키워드에 대한 boost와 LLM 요약 필드 반영을 우선 검토합니다.

한글 복합 쿼리 개선 후:

```text
evaluation queries = 24
indexed articles = 1116

average precision@5 = 0.375
average recall@10 = 0.832
average mrr = 0.778
average ndcg@10 = 0.714
```

개선 폭:

```text
average precision@5: 0.367 -> 0.375
average recall@10:   0.749 -> 0.832
average mrr:         0.701 -> 0.778
average ndcg@10:     0.632 -> 0.714
```

적용한 변경:

```text
한글 복합어 사전 확장
title/case/summary/content phrase match boost 추가
사전 매칭 keyword field boost 추가
너무 넓게 매칭되던 cost/costs alias 제거
신규 source에 맞춰 비용 최적화 expected result 보정
```

개선된 대표 쿼리:

```text
ko-problem-cost-optimization
ko-data-log-platform
ko-problem-jvm-latency
ko-deployment-canary
ko-event-driven-commerce
```

신규 한국어 source 19개 글에 LLM 요약을 생성하고 재색인한 뒤의 점수는 다음과 같습니다.

```text
average precision@5 = 0.375
average recall@10 = 0.825
average mrr = 0.792
average ndcg@10 = 0.716
```

LLM 요약은 평가 지표를 크게 끌어올리기보다는, 검색 결과 카드에서 `caseSummary`, `caseProblem`, `caseSolution`을 보여주어 사용자가 글의 문제/해결 맥락을 더 빨리 판단하게 만드는 효과가 큽니다.

## 기술명 alias와 오탈자 보정

`Elasticsearch`처럼 한글/영문 표기가 섞여 쓰이는 기술명을 더 잘 찾기 위해 alias와 오탈자 보정을 추가했습니다.

적용한 변경:

```text
Elasticsearch 기술 키워드 추가
elasticsearch, elastic search, elastic-search alias 추가
엘라스틱서치, 엘라스틱 서치, 엘라스틱 검색 alias 추가
alias 매칭 시 canonical keyword phrase boost 추가
영문 alias에 대해 작은 편집거리 기반 오탈자 보정 추가
일반 Elasticsearch fuzzy query는 사전으로 보정하지 못한 영문 검색어에만 낮은 boost로 적용
```

샘플 확인:

```text
엘라스틱서치 -> Elasticsearch 관련 글 상위 노출
엘라스틱 서치 -> Elasticsearch 관련 글 상위 노출
elasticsearch -> Elasticsearch 관련 글 상위 노출
elastic search -> Elasticsearch 관련 글 상위 노출
elastcsearch -> Elasticsearch 관련 글 상위 노출
```

1116개 글 기준 평가 점수:

```text
average precision@5 = 0.383
average recall@10 = 0.819
average mrr = 0.814
average ndcg@10 = 0.736
```

## 자동완성 후보 사전 보강 후 평가

`suggest:audit` 상위 후보 중 자동완성 가치가 높은 항목을 `KEYWORD_RULES`에 추가했습니다.

추가 항목:

```text
AWS IAM
Amazon EC2
Amazon VPC
Java
Kotlin
React
Node.js
Spring Boot
JPA
LLM
```

재처리 후:

```text
keywords = 2583
suggestions = 68
```

1116개 글 기준 평가 점수:

```text
average precision@5 = 0.392
average recall@10 = 0.819
average mrr = 0.814
average ndcg@10 = 0.735
```

사전 후보가 늘면서 자동완성 체감 품질이 좋아졌고, 검색 평가도 기존 수준을 유지했습니다.

## 신규 한국어 source 평가셋 보강

한국어 source가 1539개 article까지 늘어나면서 기존 평가셋만으로는 현재 검색 후보 풀을 충분히 대표하기 어려워졌습니다. 특히 새로 수집한 `banksalad-blog`, `inflab-tech-blog`, `gmarket-tech-blog`, `netmarble-tech-blog`, `upstage-blog`의 실제 사례를 평가셋에 반영했습니다.

추가한 평가 쿼리:

```text
ko-problem-data-consistency
ko-architecture-pr-preview
ko-problem-s3-cdn-cost
ko-problem-bottlerocket-gpu
ko-tech-redis-stream
ko-tech-kubernetes-operator
ko-tech-document-parse
ko-architecture-data-pipeline
ko-tech-aws-dms
```

보강한 기존 쿼리:

```text
ko-tech-search
```

신규 평가셋은 다음 source의 실제 글을 expected result로 포함합니다.

```text
뱅크샐러드
인프랩
G마켓
넷마블
Upstage
Wantedlab
여기어때
카카오페이
우아한형제들
```

1539개 글 기준 평가 점수:

```text
evaluation queries = 33

average precision@5 = 0.394
average recall@10 = 0.839
average mrr = 0.854
average ndcg@10 = 0.784
```

이전 24개 평가셋과 비교:

```text
average precision@5: 0.375 -> 0.394
average recall@10:   0.806 -> 0.839
average mrr:         0.799 -> 0.854
average ndcg@10:     0.731 -> 0.784
```

해석:

```text
새 source 추가 후 낮아졌던 precision@5가 일부 회복됨
신규 source 기반 실제 정답 문서가 평가에 반영되면서 recall@10, mrr, ndcg@10이 개선됨
후보 풀이 넓은 ko-tech-search, ko-problem-cost-optimization은 여전히 정밀도 개선 여지가 큼
```

## Redis 키워드와 필터 반영 후 평가

검색 결과 필터 facet에서 Redis 계열 글을 잘 좁힐 수 있도록 `Redis`, `Redis Stream` 기술 키워드를 사전에 추가했습니다.

재처리 후:

```text
keywords = 3290
suggestions = 80
```

1539개 글 기준 평가 점수:

```text
evaluation queries = 33

average precision@5 = 0.400
average recall@10 = 0.839
average mrr = 0.854
average ndcg@10 = 0.782
```

Redis 관련 쿼리는 더 많은 Redis 운영 사례를 정답으로 반영하도록 expected result를 보정했습니다.

## Facet 품질 개선

검색어와 직접 매칭되는 facet을 우선 표시하도록 `isRecommended` 값을 추가했습니다.

샘플 확인:

```text
Redis Stream technologies facet:
Redis, Redis Stream, Apache Kafka, Spring Boot ...

MQTT technologies facet:
MQTT, Redis, Amazon S3, Apache Kafka ...

엘라스틱서치 technologies facet:
Elasticsearch, Apache Kafka, Amazon S3, Kubernetes ...
```

`search`, `Java`, `observability`처럼 여러 글에 넓게 붙는 facet은 검색어와 직접 매칭되지 않으면 뒤로 보냅니다. 이를 통해 사용자는 검색 결과 상단에서 "왜 이 결과가 나왔는지"와 "어떤 기준으로 더 좁힐 수 있는지"를 더 빠르게 판단할 수 있습니다.

검색 평가 지표는 facet 정렬 변경 후에도 유지되었습니다.

```text
evaluation queries = 33

average precision@5 = 0.400
average recall@10 = 0.839
average mrr = 0.854
average ndcg@10 = 0.782
```
