# TechCase 아키텍처

이 문서는 TechCase MVP의 전체 시스템 구조와 주요 데이터 흐름을 정리합니다.

TechCase는 기업 기술 블로그를 수집하고, 원본 데이터를 PostgreSQL에 저장한 뒤, 검색에 최적화된 문서를 Elasticsearch에 색인하여 사용자가 기술명, 문제 상황, 아키텍처 키워드로 사례를 탐색할 수 있게 합니다.

## 목표

MVP 아키텍처의 목표는 다음과 같습니다.

- AWS 기술 블로그 RSS 기반 수집 흐름을 만든다.
- 원본 데이터와 검색 색인을 분리한다.
- 검색 품질을 Elasticsearch에서 직접 실험할 수 있게 한다.
- 초기 비용을 줄이되 AWS 인프라 운영 경험을 가져간다.
- 이후 crawler, API, Elasticsearch를 독립 서비스로 분리할 수 있는 구조를 만든다.

## 주요 컴포넌트

```text
apps/web
- Next.js 정적 웹 애플리케이션
- 검색 UI
- 결과 카드
- 기술/출처/문제 상황 탐색 화면

apps/backend
- FastAPI API 서버
- 검색 API
- article/source API
- crawler command
- indexing command

PostgreSQL
- 수집 원본 데이터의 기준 저장소
- source, article, crawl run, keyword 저장

Elasticsearch
- 검색 전용 색인
- field boosting, highlighting, analyzer, synonym 실험

AWS Infrastructure
- S3 + CloudFront
- ALB
- private EC2
- RDS PostgreSQL
- NAT Instance
- Systems Manager Session Manager
```

## 런타임 구조

초기 배포 구조는 다음과 같습니다.

```text
User Browser
    |
    v
CloudFront
    |
    v
S3 - Next.js Static Web
    |
    v
Public ALB
    |
    v
Private EC2 - FastAPI API
    |
    +--> Private RDS PostgreSQL
    |
    +--> Local Elasticsearch

Private EC2 - Crawler Cron
    |
    +--> NAT Instance --> AWS RSS Feeds
    +--> Private RDS PostgreSQL
    +--> Local Elasticsearch
```

## 스케줄러 흐름

새 글 수집과 후처리는 `ingest:scheduled` 명령으로 실행합니다.

```text
1. 스케줄러 실행 시작 시각을 기록한다.
2. enabled RSS source를 수집한다.
3. 새 article이 없으면 후처리를 건너뛴다.
4. 새 article 또는 업데이트 article이 있으면 키워드를 재추출한다.
5. 이번 실행 중 새로 생성된 article만 LLM 요약 대상으로 선택한다.
6. 요약 생성 후 Elasticsearch를 재색인한다.
```

핵심 기준:

```text
Article.created_at >= scheduler started_at
```

이 기준을 사용해 기존 미요약 글이 아니라, 새로 올라온 글만 자동 요약합니다.

## 요청 흐름

사용자가 검색할 때의 흐름은 다음과 같습니다.

```text
1. 사용자가 CloudFront를 통해 Next.js 정적 웹에 접근한다.
2. 브라우저에서 검색어를 입력한다.
3. 웹 앱이 ALB를 통해 FastAPI 검색 API를 호출한다.
4. FastAPI가 Elasticsearch에 검색 쿼리를 보낸다.
5. Elasticsearch가 score, highlight, matched fields를 포함한 결과를 반환한다.
6. FastAPI가 검색 결과 카드에 필요한 형태로 응답을 정리한다.
7. Next.js UI가 결과를 표시한다.
```

## 수집 흐름

AWS 기술 블로그 수집 흐름은 다음과 같습니다.

```text
1. EC2 내부 scheduler가 crawler command를 실행한다.
2. crawler가 NAT Instance를 통해 AWS RSS feed에 접근한다.
3. RSS item에서 title, url, published_at, summary, raw metadata를 추출한다.
4. article url 기준으로 PostgreSQL에 upsert한다.
5. 필요한 경우 원문 HTML을 가져와 본문 텍스트를 추출한다.
6. 추출한 content_text와 metadata를 PostgreSQL에 저장한다.
7. article을 Elasticsearch 문서 형태로 변환한다.
8. Elasticsearch articles index에 bulk indexing한다.
9. crawl run 결과와 에러를 PostgreSQL 또는 로그에 기록한다.
```

## 기업별 수집 전략

기업 기술 블로그는 제공 방식이 모두 다르기 때문에 source마다 수집 전략을 분리합니다.

```text
Source
  collection_strategy
  pagination_strategy
  content_strategy
```

초기 전략은 다음과 같이 나눕니다.

```text
rss
- RSS/Atom feed만으로 목록과 기본 요약을 수집할 수 있는 블로그
- AWS, Toss, NAVER D2, Kakao Tech 등

rss + wordpress_paged
- WordPress RSS 페이지네이션을 통해 과거 글까지 확장 수집할 수 있는 블로그
- Woowa Tech Blog

rss_with_article_fetch
- RSS에는 목록과 짧은 요약만 있고, 상세 본문은 글 URL에서 별도로 가져와야 하는 블로그
- MVP 이후 본문 품질 개선 단계에서 연결

sitemap / html_list
- RSS가 없거나 RSS 품질이 낮아 sitemap 또는 HTML 목록 페이지를 탐색해야 하는 블로그
- 수집 가능성 점검 후 별도 crawler로 연결

deferred
- 공식 블로그이지만 RSS/HTML 구조, 접근 정책, 수집 안정성을 아직 확인하지 않은 후보
```

이렇게 분리하는 이유는 다음과 같습니다.

- 기업 블로그를 추가할 때 crawler 코드에 회사명을 하드코딩하지 않아도 됩니다.
- RSS만으로 충분한 블로그와 상세 본문 fetch가 필요한 블로그를 구분할 수 있습니다.
- 수집 가능성은 낮지만 가치 있는 공식 블로그를 `deferred` 상태로 관리할 수 있습니다.
- 이후 source probe, sitemap crawler, article fetcher를 독립적으로 추가하기 쉽습니다.

## 저장소 분리

TechCase는 PostgreSQL과 Elasticsearch의 역할을 분리합니다.

PostgreSQL은 기준 저장소입니다.

- 수집 원본 보존
- URL 중복 방지
- 수집 이력 관리
- 재색인 시 기준 데이터 제공
- article, source, keyword 관계 관리

Elasticsearch는 검색 전용 저장소입니다.

- 검색 랭킹
- field boosting
- highlighting
- analyzer/synonym 실험
- 복합 키워드 검색

이 구조를 선택한 이유는 검색 색인은 언제든 재생성할 수 있어야 하고, 원본 article 데이터는 안정적으로 보존되어야 하기 때문입니다.

## 초기 모듈 경계

초기에는 `apps/backend` 안에 API, crawler, indexing 코드를 함께 둡니다.

```text
apps/backend/
  app/
    main.py
    config.py
    db/
    sources/
    articles/
    crawler/
    search/
```

이렇게 시작하는 이유는 다음과 같습니다.

- crawler와 API가 같은 데이터 모델을 공유한다.
- 검색 색인 문서 변환 로직을 API와 crawler가 함께 사용할 수 있다.
- 초기 배포 단위를 줄일 수 있다.
- 기능이 커졌을 때 `apps/crawler`로 분리하기 쉽다.

## 확장 방향

초기에는 EC2 한 대에 backend, crawler, Elasticsearch를 같이 둡니다. 이후 다음 순서로 분리합니다.

1. Elasticsearch를 별도 private EC2로 분리한다.
2. crawler를 별도 private EC2 또는 ECS Scheduled Task로 분리한다.
3. FastAPI를 App Runner, ECS, 또는 Lambda 기반 API로 분리한다.
4. NAT Instance 운영 부담이 커지면 NAT Gateway로 전환한다.
5. 검색 엔진 운영 부담이 커지면 Amazon OpenSearch Service 또는 Elastic Cloud를 검토한다.

## 관련 문서

- [데이터 모델](./data-model.md)
- [검색 설계](./search-design.md)
- [AWS 인프라](./aws-infra.md)
- [개발 계획](./development.md)
- [기술 블로그 수집 전략](./source-collection-strategy.md)
- [스케줄러 운영 설계](./scheduler.md)
