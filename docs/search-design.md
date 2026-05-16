# TechCase 검색 설계

이 문서는 TechCase MVP의 Elasticsearch 기반 검색 설계를 정리합니다.

TechCase 검색의 목표는 단순히 키워드가 포함된 글을 찾는 것이 아니라, 기술 스택 도입이나 기술적 이슈 해결을 고민할 때 참고할 만한 실제 기업 사례를 빠르게 찾게 하는 것입니다.

## 검색 목표

MVP 검색은 다음 질문에 답할 수 있어야 합니다.

- 특정 기술은 어떤 문제를 해결하는 데 사용되었는가?
- 특정 AWS 서비스는 어떤 아키텍처 맥락에서 사용되었는가?
- 비용 최적화, 마이그레이션, 고가용성 같은 문제를 다룬 사례는 무엇인가?
- 기술명과 문제 상황을 함께 검색했을 때 관련 사례가 잘 나오는가?
- 검색 결과만 보고 글을 읽을 가치가 있는지 판단할 수 있는가?

## 검색 축

초기 검색 축은 다음과 같습니다.

```text
technology
aws_service
architecture
problem
source/company
```

예:

```text
technology: Kafka, Redis, Kubernetes, Terraform
aws_service: Lambda, EKS, DynamoDB, Kinesis, EventBridge
architecture: event-driven, serverless, microservices, CDC, GitOps
problem: cost optimization, high availability, migration, large-scale traffic
source/company: AWS Architecture Blog, AWS Database Blog
```

## Elasticsearch index

초기 index 이름은 `articles`로 둡니다.

문서 초안:

```json
{
  "id": "article-id",
  "title": "Building event-driven architectures with Amazon EventBridge",
  "url": "https://aws.amazon.com/blogs/...",
  "company": "AWS",
  "source": "AWS Architecture Blog",
  "publishedAt": "2025-01-01",
  "summary": "기술 사례에 대한 짧은 요약",
  "content": "추출된 본문 텍스트",
  "technologies": ["EventBridge", "Lambda", "SQS"],
  "architectureKeywords": ["event-driven architecture", "serverless"],
  "problemKeywords": ["service decoupling", "real-time processing"]
}
```

## Field 설계

검색 필드는 다음처럼 구분합니다.

```text
title
summary
content
company
source
technologies
architectureKeywords
problemKeywords
publishedAt
```

초기 가중치:

```text
technologies: 5
title: 4
architectureKeywords: 3
problemKeywords: 3
summary: 2
content: 1
```

이렇게 두는 이유는 본문에 우연히 포함된 단어보다, 제목이나 추출된 기술 키워드에 등장한 단어가 더 강한 관련성을 가진다고 보기 때문입니다.

## Query 설계

초기 검색 API는 단순하게 시작합니다.

```text
GET /api/search?q=lambda
```

내부 Elasticsearch query는 `multi_match` 중심으로 시작합니다.

개념:

```text
q를 title, summary, content, technologies, architectureKeywords, problemKeywords에 대해 검색한다.
field별 boost를 적용한다.
highlight를 반환한다.
publishedAt 최신순 보조 정렬은 추후 검토한다.
```

초기 검색 필터:

```text
source
company
published_year
keyword_type
```

## Highlighting

검색 결과 카드에는 사용자가 왜 해당 글이 검색되었는지 이해할 수 있는 단서가 필요합니다.

초기 highlighting 대상:

```text
title
summary
content
```

검색 결과 응답 예:

```json
{
  "id": "article-id",
  "title": "Building event-driven architectures with Amazon EventBridge",
  "url": "https://aws.amazon.com/blogs/...",
  "source": "AWS Architecture Blog",
  "publishedAt": "2025-01-01",
  "summary": "...",
  "score": 12.4,
  "matchedKeywords": ["EventBridge", "event-driven"],
  "highlights": [
    "...event-driven architecture..."
  ]
}
```

## Keyword extraction

초기에는 복잡한 NLP보다 사전 기반 추출을 우선합니다.

사전 예:

```text
AWS services
- Lambda
- EKS
- ECS
- S3
- DynamoDB
- Kinesis
- EventBridge
- SQS
- SNS

Architecture keywords
- event-driven
- serverless
- microservices
- CDC
- GitOps
- data pipeline

Problem keywords
- cost optimization
- high availability
- migration
- observability
- scalability
- disaster recovery
```

추출 순서:

```text
1. title, summary, content_text를 합친다.
2. 정규화한다.
3. 사전 기반 키워드 매칭을 수행한다.
4. ArticleKeyword로 저장한다.
5. Elasticsearch document의 keyword fields에 반영한다.
```

초기 구현은 `dictionary_v1` 기반으로 동작합니다.

실행 명령:

```bash
npm run keywords:extract
npm run search:reindex
```

현재 추출 대상:

```text
aws_service: AWS Lambda, Amazon DynamoDB, Amazon EKS, Amazon OpenSearch Service, Amazon MSK 등
technology: Apache Kafka, Apache Flink, OpenTelemetry, Kubernetes 등
architecture: serverless, streaming data pipeline, Change Data Capture, cross-Region resilience 등
problem: cost optimization, observability, migration, incident response 등
```

추출된 키워드는 `article_keywords`에 저장되고, 재색인 시 Elasticsearch 문서의 다음 필드로 반영됩니다.

```text
technologies
architectureKeywords
problemKeywords
```

## Synonym과 alias

MVP 이후에는 synonym을 추가합니다.

예:

```text
k8s, Kubernetes, 쿠버네티스
serverless, 서버리스
event driven, event-driven, event-driven architecture
EventBridge, Amazon EventBridge
DynamoDB, Amazon DynamoDB
```

초기에는 애플리케이션 레벨에서 query expansion을 적용하고, 이후 Elasticsearch synonym filter를 검토합니다.

## 한글/영문 검색 대응

TechCase는 영어 기술 블로그와 한글 기술 블로그를 함께 다룹니다.

따라서 검색어와 문서 언어가 달라도 같은 기술/문제 맥락으로 연결될 수 있어야 합니다.

초기 대응 방식:

```text
1. 사전 alias에 한글/영문 표현을 함께 등록한다.
2. article title/summary/content에서 한글 alias도 추출한다.
3. 검색어에 한글 alias가 포함되면 영어 검색 alias를 함께 붙여 query expansion을 수행한다.
4. 영어 검색어는 불필요하게 확장하지 않아 기존 검색 precision 하락을 줄인다.
```

예:

```text
비용 최적화 -> cost optimization
장애 대응 -> incident response
관측성 -> observability
카프카 -> kafka
서버리스 -> serverless
쿠버네티스 -> kubernetes
```

이 방식은 Elasticsearch synonym filter를 쓰기 전 단계의 애플리케이션 레벨 확장입니다. MVP에서는 구현과 조정이 빠르다는 장점이 있고, 이후 데이터가 늘어나면 Elasticsearch analyzer/synonym 설정으로 일부를 이전할 수 있습니다.

## Source 확장

초기 source는 AWS 기술 블로그 5개로 시작했습니다.

이후 한글/영문 검색 품질을 함께 확인하기 위해 다음 한국 기술 블로그를 추가했습니다.

```text
Toss Tech: https://toss.tech/rss.xml
NAVER D2: https://d2.naver.com/d2.atom
Kakao Tech: https://tech.kakao.com/feed/
Woowa Tech Blog: https://techblog.woowahan.com/feed/
```

우아한형제들 기술블로그는 기본 HTTP client 요청에서 차단 페이지가 내려올 수 있어 crawler에 명시적인 User-Agent를 추가했습니다.

## Ranking 개선 방향

초기 ranking은 field boosting 중심입니다.

이후 개선 아이디어:

- title에 검색어가 있으면 가중치 증가
- technology keyword와 query가 정확히 일치하면 가중치 증가
- problem keyword와 architecture keyword가 함께 매칭되면 가중치 증가
- 너무 오래된 글은 약하게 감점하거나 최신순 보조 정렬
- source 신뢰도 또는 글 유형에 따른 가중치
- 클릭 로그 기반 ranking 개선

## 검색 품질 검증 쿼리

MVP 검색 품질은 다음 쿼리로 반복 검증합니다.

```text
Lambda
EventBridge
DynamoDB
EKS
event-driven
serverless
cost optimization
migration
high availability
data pipeline
```

검증 기준:

- 상위 결과가 실제 사례 중심인가?
- 단순 릴리스 글이 과도하게 상위에 오지 않는가?
- 검색 결과 카드만 보고 글의 맥락을 이해할 수 있는가?
- 같은 기술이라도 문제 상황별로 구분되는가?
- field boosting을 조정했을 때 결과 품질이 개선되는가?

## 운영 고려사항

Elasticsearch는 private EC2 내부에서 실행합니다.

초기 운영 기준:

- 외부에 `9200` 포트를 공개하지 않습니다.
- FastAPI와 crawler만 Elasticsearch에 접근합니다.
- Kibana는 public으로 열지 않고 Session Manager port forwarding으로 접근합니다.
- index mapping은 코드 또는 infra 설정으로 재현 가능하게 관리합니다.
- 전체 재색인 명령을 제공합니다.
- 원본 데이터는 PostgreSQL에 있으므로 Elasticsearch index는 재생성 가능해야 합니다.

## 관련 문서

- [아키텍처](./architecture.md)
- [데이터 모델](./data-model.md)
- [AWS 인프라](./aws-infra.md)
- [개발 계획](./development.md)
