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

빈 query는 기본 페이지 탐색용으로 사용합니다.

```text
GET /api/search?q=&sort=latest
```

이 경우 `match_all` query를 사용하고 최신순으로 글을 반환합니다. 사용자가 검색어를 입력하기 전에도 최신 기업 기술 블로그 글을 둘러볼 수 있게 하기 위한 동작입니다.

페이지네이션은 `page`, `page_size` query parameter로 받습니다.

```text
GET /api/search?q=&sort=latest&page=1&page_size=20
GET /api/search?q=Kafka&sort=relevance&page=2&page_size=20
```

페이지네이션 응답 필드:

```text
page
pageSize
totalPages
total
items
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

## 복합 의도 검색 랭킹 설계

`검색 플랫폼 Kafka`처럼 기술명과 아키텍처/문제 의도가 함께 들어간 query는 단순 키워드 매칭만으로는 품질을 올리기 어렵습니다.

예:

```text
검색 플랫폼 Kafka
```

이 query는 하나의 문자열이지만 실제 의도는 다음처럼 나뉩니다.

```text
technology: Apache Kafka
architecture: search platform, search indexing pipeline
problem/context: 검색 데이터 동기화, 실시간 색인, 이벤트 기반 검색 연동
```

현재 검색은 `Apache Kafka` 또는 `search` 중 하나만 강하게 매칭돼도 높은 점수를 받을 수 있습니다. 이 때문에 다음처럼 한쪽 의도만 맞는 글이 상위에 섞일 수 있습니다.

```text
Kafka는 맞지만 검색 플랫폼 사례는 아닌 글
검색은 맞지만 Kafka 기반 색인/플랫폼 사례는 아닌 글
```

따라서 복합 의도 검색은 "각 키워드가 등장하는가"보다 "서로 다른 의도 축이 같은 사례 안에서 함께 충족되는가"를 ranking feature로 다루어야 합니다.

### Query Intent 분해

검색어를 다음 축으로 분해합니다.

```text
technology: Kafka, Redis, Elasticsearch, OpenSearch, Kubernetes
problem: 비용 최적화, 장애 대응, 성능 개선, 데이터 정합성
architecture: 검색 플랫폼, 로그 플랫폼, 데이터 파이프라인, 실시간 인덱싱
company/source: Woowa Brothers, Kurly, AWS, NAVER
```

초기 구현에서는 완전한 query parser를 만들기보다 기존 `KeywordRule` 기반으로 분해합니다.

예:

```text
검색 플랫폼 Kafka
-> technology: Apache Kafka
-> architecture 후보: search
-> raw phrase 후보: 검색 플랫폼
```

단, `search`처럼 너무 넓은 키워드는 단독 매칭만으로 큰 가산점을 주면 안 됩니다. `Kafka + search`, `Elasticsearch + indexing`, `OpenSearch + analyzer`처럼 조합으로 의미가 생기는 경우에만 별도 가산점을 주는 편이 안전합니다.

### Ranking Feature 후보

복합 의도 query에서는 다음 feature를 추가 후보로 둡니다.

```text
technology_exact_match
architecture_exact_match
problem_exact_match
technology_architecture_co_match
technology_problem_co_match
raw_phrase_in_title_or_case_summary
content_type_case_boost
```

예상 가산점 방향:

```text
기술명과 아키텍처 키워드가 모두 keyword field에 존재하면 가산
기술명이 technologies에 있고 query phrase가 title/caseSummary에 있으면 가산
문제 키워드와 해결 요약이 함께 맞으면 가산
contentType이 technical_case이면 기존 사례성 가산점 유지
```

중요한 점은 co-match feature를 전역으로 크게 적용하지 않는 것입니다. 이전 실험에서 복합 키워드 co-occurrence boost를 넓게 적용했을 때 `검색 플랫폼 Kafka`가 개선되지 않았고, 다른 query의 순위가 흔들렸습니다.

### 구현 원칙

첫 구현은 다음 원칙을 따릅니다.

```text
1. 복합 의도 query에서만 적용한다.
2. 단일 넓은 키워드(search, observability, Java)에는 큰 가산점을 주지 않는다.
3. keyword field와 LLM 요약 field를 함께 본다.
4. 기존 평균 평가 지표가 악화되면 반영하지 않는다.
5. audit 리포트에서 특정 query의 상위 10개 변화를 반드시 확인한다.
```

구현 후보:

```text
matched_rules(query)로 KeywordRule 전체를 반환
keyword_type별로 technology/problem/architecture bucket 구성
technology + architecture가 모두 존재할 때만 function_score 추가
function_score filter는 terms 중심으로 좁게 구성
raw query phrase는 title/caseSummary/caseProblem/caseSolution에 낮은 boost로만 추가
```

예상 pseudo query:

```json
{
  "function_score": {
    "query": "<base bool query>",
    "functions": [
      {
        "filter": {
          "bool": {
            "must": [
              { "terms": { "technologies": ["Apache Kafka", "apache kafka"] } },
              { "terms": { "architectureKeywords": ["search", "검색 플랫폼"] } }
            ]
          }
        },
        "weight": 25
      }
    ],
    "score_mode": "sum",
    "boost_mode": "sum"
  }
}
```

단, 현재 `검색 플랫폼`은 정식 keyword로 안정적으로 추출되지 않습니다. 단순히 사전에 `검색 플랫폼`을 추가하는 실험은 `검색 플랫폼 Kafka`를 개선하지 못했습니다. 따라서 먼저 LLM 요약의 `architectureKeywords` 품질을 확인하고, 필요하면 "검색 플랫폼", "검색 인덱싱", "색인 파이프라인" 같은 아키텍처 키워드를 LLM 추출 단계에서 더 잘 생성하도록 개선해야 합니다.

### 평가 대상

복합 의도 ranking 변경 시 최소한 다음 query를 함께 비교합니다.

```text
ko-search-platform-kafka
ko-search-realtime-indexing
ko-tech-search
ko-event-driven-commerce
migration-kafka-msk
ko-migration-kafka
ko-data-log-platform
```

성공 기준:

```text
ko-search-platform-kafka의 mrr과 ndcg@10 개선
기존 ko-tech-search, migration-kafka-msk 품질 유지
average precision@5, ndcg@10 악화 없음
상위 5개 결과가 사람이 봐도 query intent와 맞음
```

## Query-only alias audit

일부 기술명은 일반 단어와 충돌합니다. 예를 들어 `next`를 기술 사전 alias로 그대로 등록하면 `next step`, `Google Cloud Next` 같은 맥락까지 `Next.js`로 과하게 해석될 수 있습니다. 반대로 `next`를 완전히 무시하면 사용자가 `Next.js`를 기대하고 검색했을 때 원하는 결과가 늦게 나옵니다.

이런 케이스는 일반 `KeywordRule` alias가 아니라 `QUERY_ONLY_KEYWORD_ALIASES`로 관리합니다.

```text
next -> Next.js
```

운영 원칙:

```text
일반 alias에는 명확한 표기만 넣는다. 예: next.js, nextjs
짧거나 일반적인 단어는 query-only alias로만 둔다. 예: next
문장 안 부분 매칭은 하지 않는다. 예: next step은 Next.js로 보지 않음
검색 결과와 자동완성이 모두 기대대로 동작하는지 audit으로 확인한다.
```

점검 명령:

```bash
npm run search:alias-audit
```

현재 이 명령은 다음을 확인합니다.

```text
alias 입력이 기대 keyword로 매칭되는가
query expansion에 반영되는가
상위 검색 결과에 기대 keyword가 포함되는가
자동완성 prefix에서도 기대 keyword가 노출되는가
```

예시 결과:

```text
PASS next -> Next.js
expanded: next next.js
top: 5/5
suggestions(nex): Next.js
```

## Ambiguous query audit

`query-only alias`로 승격하기 전에는 짧고 모호한 검색어의 현재 동작을 먼저 확인합니다. 이를 위해 별도 audit 명령을 둡니다.

```bash
npm run search:ambiguous-audit
```

기본 점검 대상:

```text
next
go
golang
spring
node
ai
r
```

이 명령은 각 query에 대해 다음 정보를 출력합니다.

```text
total result count
query expansion 결과
matched keyword 목록
자동완성 후보
상위 검색 결과 제목, source, score, technologies
```

판단 기준:

```text
검색 상위 결과가 사용자의 일반적인 기술 의도와 맞는가
기술 keyword가 제대로 붙어 facet과 ranking에 활용되는가
자동완성 후보가 사용자를 더 명확한 기술명으로 유도하는가
일반 alias로 추가했을 때 본문 오탐이 커지지 않는가
query-only alias 또는 별도 추출 전략이 필요한가
```

현재 관찰된 주의 케이스:

```text
go:
  Go 언어 글은 검색되지만 기술 keyword가 없음
  일반 alias로 go를 추가하면 영어 동사 go 오탐 가능성이 큼

node:
  node 검색 상위가 EKS Node Group 중심으로 올라옴
  Node.js 의도와 Kubernetes node 의도를 구분해야 함

spring:
  Spring Boot 자동완성은 가능하지만 spring 자체는 keyword 매칭이 아님
  Spring Framework, Spring Batch, Spring Cloud 등 더 넓은 분류가 필요할 수 있음

ai:
  LLM, MLOps, AI 제품 소식, 리터러시 글이 섞임
  기술 alias보다 content type, technology, problem facet로 좁히는 편이 안전함
```

### Go/Golang 처리 방식

`go`는 대표적인 모호 검색어입니다. 기술명으로는 Go 언어를 뜻하지만, 영어 본문에서는 일반 동사로도 매우 자주 등장합니다. 따라서 TechCase는 `go`를 일반 사전 alias로 두지 않습니다.

현재 처리:

```text
Keyword: Go
normal aliases: golang, go language, go programming language
query-only alias: go -> Go
title-only extraction alias: Go 제목 안의 단독 go
```

의도:

```text
golang처럼 명확한 표현은 본문/요약/제목에서 Go keyword로 추출
go 단독 검색은 사용자의 기술 검색 의도로 보고 Go로 query expansion
본문 속 일반 동사 go는 Go keyword로 추출하지 않음
제목의 Go는 기술 글 제목일 가능성이 높으므로 keyword로 추출
```

`query-only alias` 검색에서는 원문 단어를 넓게 본문 검색하지 않고 canonical keyword 중심으로 랭킹합니다. 이를 통해 `next`, `go`처럼 짧은 단어가 본문에서 우연히 등장해 상위로 올라오는 현상을 줄입니다.

검증 기준:

```text
npm run search:alias-audit
npm run search:ambiguous-audit
npm run search:evaluate
```

현재 결과:

```text
go -> Go 자동완성 노출
go 검색 상위 5개 모두 Go keyword 포함
tech-go precision@5 = 0.600
tech-go recall@10 = 1.000
tech-go ndcg@10 = 0.955
```

아직 완벽한 상태는 아닙니다. Go가 글의 주제인지, 본문에서 보조적으로 언급된 기술인지 구분하려면 keyword confidence나 LLM summary의 technologies confidence를 ranking에 반영할 필요가 있습니다.

### Node.js 처리 방식

`node`도 모호한 검색어입니다. JavaScript 런타임인 Node.js를 뜻할 수도 있고, Kubernetes/EKS node를 뜻할 수도 있습니다. TechCase의 일반 검색창에서는 `node` 단독 입력을 Node.js 기술 검색 의도로 우선 해석하되, 인프라 node 검색은 더 구체적인 query로 다루는 방향을 택했습니다.

현재 처리:

```text
Keyword: Node.js
normal aliases: node.js, nodejs, node js
query-only alias: node -> Node.js
```

의도:

```text
node.js/nodejs처럼 명확한 표현은 기존처럼 Node.js keyword로 추출
node 단독 검색은 Node.js로 query expansion
본문 속 일반 node만으로는 Node.js keyword를 추출하지 않음
Kubernetes node 문맥은 Kubernetes, Amazon EKS, node group 관련 query로 별도 관리
```

검증 결과:

```text
node -> Node.js 자동완성 노출
node 검색 상위 5개 모두 Node.js keyword 포함
tech-nodejs precision@5 = 0.800
tech-nodejs recall@10 = 1.000
tech-nodejs ndcg@10 = 0.972
```

남은 설계 과제:

```text
EKS node group
Kubernetes node
GPU node
node autoscaling
```

위와 같은 인프라 node 의도는 Node.js와 다른 평가셋으로 관리해야 합니다. 이를 분리하지 않으면 `node` 한 단어에 서로 다른 사용자 의도가 섞입니다.

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
