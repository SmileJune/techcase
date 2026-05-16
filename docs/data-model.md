# TechCase 데이터 모델

이 문서는 TechCase MVP에서 사용할 PostgreSQL 중심 데이터 모델을 정리합니다.

MVP 데이터 모델의 핵심은 기업 기술 블로그 글을 안정적으로 수집하고, 중복 없이 저장하고, Elasticsearch 색인을 언제든 재생성할 수 있게 만드는 것입니다.

## 설계 원칙

- PostgreSQL을 원본 데이터의 기준 저장소로 사용합니다.
- URL 기준으로 article 중복 저장을 방지합니다.
- RSS 원본 메타데이터와 추출 결과는 보존합니다.
- 검색 색인에 필요한 키워드는 article과 분리해 관리할 수 있게 합니다.
- 초기에는 단순하게 시작하되, 이후 기술/문제/아키텍처 분류를 확장할 수 있게 합니다.

## MVP 엔티티

초기 MVP의 최소 엔티티는 다음과 같습니다.

```text
Source
Article
CrawlRun
ArticleKeyword
ArticleSummary
```

## Source

수집 대상 블로그 또는 RSS feed를 나타냅니다.

예:

- AWS Architecture Blog
- AWS Database Blog
- AWS Compute Blog
- AWS Big Data Blog
- AWS DevOps Blog

필드 초안:

```text
id
name
slug
company_name
feed_url
site_url
description
enabled
created_at
updated_at
```

제약:

- `slug`는 unique입니다.
- `feed_url`은 unique입니다.

## Article

수집된 기술 블로그 글을 나타냅니다.

필드 초안:

```text
id
source_id
title
url
canonical_url
author
published_at
summary
content_text
content_html
language
raw_metadata
created_at
updated_at
collected_at
indexed_at
```

주요 제약:

- `url` 또는 `canonical_url` 기준 unique 제약을 둡니다.
- `source_id`는 `Source.id`를 참조합니다.

필드 설명:

- `summary`: RSS summary 또는 추출 요약입니다.
- `content_text`: 검색 색인에 사용할 정제된 본문 텍스트입니다.
- `content_html`: 필요 시 원문 HTML 일부 또는 정제 HTML을 저장합니다.
- `raw_metadata`: RSS item 원본과 파싱 결과를 JSONB로 보존합니다.
- `indexed_at`: Elasticsearch 색인 완료 시각입니다.

## CrawlRun

수집 작업의 실행 이력을 나타냅니다.

필드 초안:

```text
id
source_id
status
started_at
finished_at
fetched_count
created_count
updated_count
failed_count
error_message
metadata
```

status 후보:

```text
running
succeeded
failed
partial_failed
```

이 엔티티가 필요한 이유는 다음과 같습니다.

- 어떤 source를 언제 수집했는지 추적할 수 있습니다.
- 수집 실패를 확인할 수 있습니다.
- crawler 변경 후 결과 차이를 비교할 수 있습니다.
- 나중에 관리자 화면에서 수집 상태를 보여줄 수 있습니다.

## ArticleKeyword

article에서 추출하거나 수동으로 부여한 검색 키워드를 나타냅니다.

필드 초안:

```text
id
article_id
keyword
keyword_type
confidence
matched_by
created_at
```

keyword_type 후보:

```text
technology
aws_service
architecture
problem
company
```

matched_by 후보:

```text
manual
dictionary
rss_category
rule
llm
```

예:

```text
keyword: EventBridge
keyword_type: aws_service
confidence: 0.95
matched_by: dictionary
```

초기에는 사전 기반 추출을 우선하고, 이후 LLM 또는 embedding 기반 추출을 추가합니다.

## ArticleSummary

LLM이 생성한 TechCase용 사례 요약을 나타냅니다.

RSS summary나 본문 발췌는 `Article`에 보존하고, LLM 요약은 별도 테이블에서 버전 관리합니다.

필드 초안:

```text
id
article_id
summary_type
language
model
prompt_version
content_type
case_summary
problem
solution
technologies
architecture_keywords
problem_keywords
confidence
raw_response
created_at
updated_at
```

summary_type 후보:

```text
case_summary
detail_summary
comparison_summary
```

content_type 후보:

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

이 엔티티가 필요한 이유는 다음과 같습니다.

- 프롬프트 버전을 바꿔 요약을 재생성할 수 있습니다.
- 모델별 결과를 비교할 수 있습니다.
- 원본 LLM 응답을 보존해 디버깅할 수 있습니다.
- 검색 카드용 짧은 요약과 상세 페이지용 긴 요약을 분리할 수 있습니다.
- 검색 시점에 LLM을 호출하지 않고 미리 생성된 요약을 사용할 수 있습니다.

## 이후 확장 엔티티

MVP 이후에는 다음 엔티티를 분리할 수 있습니다.

```text
Company
Technology
ArticleTechnology
ProblemCategory
ArchitectureKeyword
SearchQueryLog
```

## Company

초기에는 `Source.company_name`으로 충분하지만, 여러 회사 블로그를 다루게 되면 별도 엔티티로 분리합니다.

```text
id
name
slug
website_url
logo_url
created_at
updated_at
```

## Technology

기술명과 alias를 체계적으로 관리하기 위한 엔티티입니다.

```text
id
name
slug
aliases
category
created_at
updated_at
```

예:

```json
{
  "name": "Kubernetes",
  "aliases": ["k8s", "쿠버네티스"]
}
```

## ArticleTechnology

article과 technology의 관계를 나타냅니다.

```text
article_id
technology_id
confidence
matched_by
created_at
```

초기 `ArticleKeyword`에서 충분한 데이터가 쌓이면 이 관계로 정규화합니다.

## SearchQueryLog

검색 품질 개선을 위해 사용자 검색어를 기록하는 엔티티입니다.

```text
id
query
filters
result_count
clicked_article_id
created_at
```

초기에는 개인정보를 저장하지 않고, 검색어와 결과 수 중심으로만 기록합니다.

## ERD 초안

```text
Source 1 --- N Article
Article 1 --- N ArticleKeyword
Source 1 --- N CrawlRun

Future:
Company 1 --- N Source
Article N --- N Technology
Article N --- N ProblemCategory
```

## 인덱스 초안

PostgreSQL 인덱스:

```text
sources.slug unique
sources.feed_url unique
articles.url unique
articles.canonical_url unique, nullable
articles.source_id
articles.published_at
article_keywords.article_id
article_keywords.keyword
article_keywords.keyword_type
crawl_runs.source_id
crawl_runs.started_at
```

검색 자체는 Elasticsearch가 담당하지만, 관리자 검색이나 재색인 대상 조회를 위해 PostgreSQL에도 기본 인덱스를 둡니다.

## 관련 문서

- [아키텍처](./architecture.md)
- [검색 설계](./search-design.md)
- [개발 계획](./development.md)
