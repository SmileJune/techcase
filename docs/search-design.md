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

정렬 기준은 query parameter로 받습니다.

```text
GET /api/search?q=lambda&sort=relevance
GET /api/search?q=lambda&sort=latest
```

정렬 기준:

```text
relevance: Elasticsearch score 기반 관련도순. 기본값.
latest: 검색 후보 중 publishedAt 최신순. 같은 날짜 또는 날짜 없음 처리 후 _score로 보조 정렬.
```

검색 결과를 좁히는 필터도 query parameter로 받습니다.

```text
GET /api/search?q=Redis&source=gmarket-tech-blog
GET /api/search?q=Redis&technology=Redis&problem=cost%20optimization
GET /api/search?q=Redis&content_type=technical_case
```

필터 기준:

```text
source: sourceSlug 기준 회사/블로그 필터
technology: technologies keyword field 기준 필터
problem: problemKeywords keyword field 기준 필터
content_type: LLM 요약에서 분류한 contentType 필터
```

검색 응답에는 현재 검색 결과에 대한 facet도 함께 반환합니다.

```text
facets.sources
facets.technologies
facets.problemKeywords
facets.contentTypes
```

프론트엔드는 facet을 결과 상단의 `결과 좁히기` 영역에 표시하고, 사용자가 버튼형 필터를 선택하면 같은 검색어로 다시 검색합니다.

facet은 단순 count 순서만 사용하지 않습니다. 검색어와 직접 매칭되는 기술 키워드는 `isRecommended`로 표시해 상단에 배치하고, `search`, `Java`, `observability`처럼 지나치게 넓게 잡히기 쉬운 facet은 직접 매칭된 경우가 아니라면 뒤로 보냅니다. 예를 들어 `Redis Stream` 검색에서는 `Redis`, `Redis Stream`이 먼저 보이고, `Elasticsearch` 검색에서는 `Elasticsearch`가 먼저 보이도록 합니다.

AWS 블로그는 여러 세부 블로그가 같은 회사명으로 묶이면 필터가 헷갈릴 수 있어, source facet에서는 `AWS Database Blog`, `AWS Architecture Blog`처럼 세부 블로그명을 우선 표시합니다.

내부 Elasticsearch query는 `multi_match` 중심으로 시작합니다.

개념:

```text
q를 title, summary, content, technologies, architectureKeywords, problemKeywords에 대해 검색한다.
field별 boost를 적용한다.
contentType 기반 사례성 가산점을 function_score로 적용한다.
highlight를 반환한다.
기본은 관련도순으로 두고, 사용자가 선택하면 최신순 정렬을 적용한다.
source/technology/problem/content_type 필터를 bool filter로 적용한다.
source, technology, problem, contentType facet을 반환한다.
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
Elasticsearch, elastic search, elastic-search, 엘라스틱서치, 엘라스틱 서치
```

초기에는 애플리케이션 레벨에서 query expansion을 적용하고, 이후 Elasticsearch synonym filter를 검토합니다.

사전에 등록된 alias가 검색어와 매칭되면 canonical keyword를 추가로 강하게 반영합니다. 예를 들어 `엘라스틱서치`, `엘라스틱 서치`, `elastic search`는 모두 `Elasticsearch` 기술 키워드로 확장됩니다.

영문 기술명은 작은 오탈자도 보정합니다. `elastcsearch`, `elasticseach`처럼 한두 글자 정도의 편집거리 안에 있는 검색어는 사전 alias와 비교해 canonical keyword로 승격합니다. 단, fuzzy 검색은 결과가 지나치게 넓어질 수 있으므로 사전 alias로 보정하지 못한 영문 검색어에만 낮은 boost로 적용합니다.

## 한글/영문 검색 대응

TechCase는 영어 기술 블로그와 한글 기술 블로그를 함께 다룹니다.

따라서 검색어와 문서 언어가 달라도 같은 기술/문제 맥락으로 연결될 수 있어야 합니다.

초기 대응 방식:

```text
1. 사전 alias에 한글/영문 표현을 함께 등록한다.
2. article title/summary/content에서 한글 alias도 추출한다.
3. 검색어가 alias와 매칭되면 canonical keyword를 검색 쿼리에 함께 반영한다.
4. 영어 기술명 오탈자는 사전 alias와 편집거리 기반으로 보정한다.
5. 사전으로 보정하지 못한 영문 검색어에만 Elasticsearch fuzzy query를 낮은 boost로 추가한다.
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

## 자동완성

TechCase는 검색어 입력 중 기술명, 회사명, 문제 상황, 아키텍처 키워드를 제안하기 위해 Elasticsearch `completion suggester`를 사용합니다.

자동완성은 글 검색 인덱스와 분리합니다.

```text
articles      실제 검색 결과용 인덱스
suggestions   자동완성 후보 전용 인덱스
```

분리하는 이유:

```text
글 검색은 title, summary, content, caseSummary 같은 긴 문서 필드 중심이다.
자동완성은 label, aliases, type, weight 같은 짧고 정제된 후보 중심이다.
두 목적을 같은 mapping에 섞으면 후보 품질과 색인 구조가 복잡해진다.
```

후보 생성 소스:

```text
KEYWORD_RULES      기술명, AWS 서비스, 문제 상황, 아키텍처 키워드
sources            회사명
article_keywords   후보별 articleCount와 weight 보정
```

후보 문서 예:

```json
{
  "id": "technology:elasticsearch",
  "label": "Elasticsearch",
  "type": "technology",
  "description": "기술",
  "aliases": ["Elasticsearch", "elastic search", "엘라스틱서치", "엘라스틱 서치"],
  "articleCount": 26,
  "suggest": {
    "input": ["Elasticsearch", "elastic search", "엘라스틱서치", "엘라스틱 서치"],
    "weight": 151
  }
}
```

자동완성 검색 API:

```text
GET /api/suggest?q=ka
```

운영 명령:

```bash
npm run suggest:reindex
```

사전 누락 후보 점검:

```bash
npm run suggest:audit
```

`suggest:audit`은 article 제목, RSS 요약, 본문, LLM 요약의 `technologies`에서 반복적으로 등장하지만 아직 `KEYWORD_RULES`에 등록되지 않은 기술 후보를 찾습니다. MQTT처럼 검색 결과에는 존재하지만 자동완성 후보에는 빠져 있는 항목을 운영 중에 발견하기 위한 도구입니다.

초기 weight 정책:

```text
AWS 서비스와 기술 후보를 회사 후보보다 우선한다.
articleCount는 후보 품질을 보정하되 과도하게 지배하지 않도록 최대 50까지만 반영한다.
fuzzy는 completion suggester의 fuzzy 옵션을 사용하되, prefix_length와 min_length로 과도한 후보 확장을 제한한다.
```

## LLM 사례 요약

검색 결과 카드에서 RSS 요약만 보여주면 글의 실제 문제 상황과 적용 기술을 파악하기 어렵습니다.

따라서 TechCase는 LLM을 검색 요청 시점에 호출하지 않고, 수집된 article을 대상으로 offline enrichment를 수행합니다.

흐름:

```text
RSS 수집
본문 정제
키워드 추출
LLM 사례 요약 생성
article_summaries 저장
Elasticsearch 재색인
검색 결과에서 caseSummary 우선 표시
```

요약은 `articles` 테이블에 직접 저장하지 않고 `article_summaries` 테이블에 저장합니다.

이유:

```text
모델 변경 추적
프롬프트 버전 관리
재생성 가능성 확보
짧은 카드 요약과 긴 상세 요약 분리 가능
raw LLM response 보존
```

LLM 요약은 모든 기술 블로그 글에 대해 생성하되, 글을 제외하지 않고 `content_type`으로 성격을 분류합니다.

분류 후보:

```text
technical_case
engineering_story
tutorial
release_note
event
recruiting
interview
news
other
```

이렇게 하면 채용/세미나/인터뷰성 글도 TechCase 데이터 자산으로 보존하면서, 이후 검색 ranking이나 필터에서 글 성격을 활용할 수 있습니다.

초기 명령:

```bash
npm run llm:summarize -- --limit 3 --dry-run
npm run llm:summarize -- --source woowa-tech-blog --limit 10
npm run search:reindex
```

batch 생성은 article 단위로 commit합니다. 한 글에서 LLM 호출, JSON 파싱, 저장 중 오류가 나더라도 전체 batch가 중단되지 않고 실패 건수만 기록합니다.

필요 환경 변수:

```text
OPENAI_API_KEY
OPENAI_MODEL
```

Source별 RSS 본문 확보율:

```text
aws-architecture-blog  total=20   content_text=20   content_1000_plus=20
aws-big-data-blog      total=20   content_text=20   content_1000_plus=20
aws-compute-blog       total=20   content_text=20   content_1000_plus=20
aws-database-blog      total=20   content_text=20   content_1000_plus=20
aws-devops-blog        total=20   content_text=20   content_1000_plus=20
kakao-tech             total=10   content_text=0    content_1000_plus=0
naver-d2               total=20   content_text=20   content_1000_plus=16
toss-tech              total=20   content_text=20   content_1000_plus=20
woowa-tech-blog        total=512  content_text=512  content_1000_plus=492
```

Kakao Tech는 현재 RSS description 중심이므로, 더 좋은 LLM 요약을 위해서는 이후 원문 HTML 수집 전략이 필요합니다.

초기 프롬프트 버전:

```text
case-summary-v1
```

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

또한 우아한형제들 기술블로그는 RSS pagination을 지원합니다.

확인된 수집 범위:

```text
page 1~51: 페이지당 10개
page 52: 2개
page 53: 404
unique article URL: 512
```

따라서 crawler는 `woowa-tech-blog` source에 대해 `?paged=2`, `?paged=3`처럼 페이지를 순회하고, 404 또는 새 URL이 없는 페이지를 만나면 종료합니다.

## Ranking 개선 방향

초기 ranking은 field boosting 중심입니다.

현재는 LLM 요약에서 분류한 `contentType`을 활용해 사례성이 높은 글에 가산점을 줍니다.

```text
technical_case     +30
engineering_story  +15
tutorial           +8
```

이 보정은 `function_score`의 `boost_mode=sum` 방식으로 적용합니다. 감점은 아직 적용하지 않습니다. 제품 소개, 이벤트, 채용, 뉴스성 글도 데이터 자산으로 유지하되, 같은 점수대에서는 기술 사례와 엔지니어링 경험 글이 더 위로 오도록 하는 것이 목적입니다.

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
