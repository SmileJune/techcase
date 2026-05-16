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

쿼리 유형은 다음과 같이 나눴습니다.

```text
technology: Lambda, DynamoDB, EKS, OpenSearch, Apache Flink
problem: cost optimization, observability, incident response
architecture: streaming data pipeline, Change Data Capture, cross-Region resilience
migration: Kafka MSK migration
ko query: 비용 최적화, 장애 대응, 카프카 마이그레이션, 서버리스
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
```

실행 전에는 Elasticsearch에 `articles` index가 생성되어 있고 문서가 색인되어 있어야 합니다.

```bash
npm run search:reindex
npm run search:evaluate
```

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
