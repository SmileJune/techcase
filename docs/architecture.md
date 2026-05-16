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
