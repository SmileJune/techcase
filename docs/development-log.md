# TechCase 개발 로그

이 문서는 TechCase를 개발하면서 결정한 내용과 구현 진행 상황을 시간순으로 정리합니다.

## 1. 서비스 방향 정리

TechCase는 기업 기술 블로그를 기반으로, 개발자가 기술 스택 도입이나 기술적 이슈 해결을 고민할 때 실제 기업 적용 사례를 빠르게 탐색할 수 있도록 돕는 기술 사례 검색 서비스로 정의했습니다.

초기 아이디어는 새로운 기술을 공부하기 전 실제 사례를 탐색하는 서비스에 가까웠지만, 이후 포지셔닝을 다음처럼 조정했습니다.

```text
기술 학습 전 탐색
→ 기술 스택 도입과 이슈 해결을 위한 사례 탐색
```

이 방향이 더 적합하다고 판단한 이유는 다음과 같습니다.

- 일반 검색에는 광고성 콘텐츠와 신뢰도 낮은 글이 많이 섞입니다.
- 기업 기술 블로그는 실제 문제 상황과 해결 과정을 담고 있어 신뢰도가 높습니다.
- TechCase의 차별점은 단순 검색이 아니라 실제 적용 사례를 찾는 데 있습니다.
- 기술 도입 판단, 이슈 해결, 아키텍처 검토에 더 직접적으로 도움이 됩니다.

서비스명은 `TechSearch`와 비교했지만, 단순 검색보다 사례 중심 서비스라는 의미가 강한 `TechCase`를 유지하기로 했습니다.

## 2. 문서 구조 정리

README는 서비스 설명 중심으로 유지하고, 개발/설계 내용은 별도 문서로 분리했습니다.

현재 문서 구조는 다음과 같습니다.

```text
README.md
docs/development.md
docs/architecture.md
docs/data-model.md
docs/search-design.md
docs/aws-infra.md
docs/development-log.md
```

각 문서의 역할은 다음과 같습니다.

- `README.md`: 서비스 설명, 문제 정의, 핵심 아이디어
- `docs/development.md`: MVP 범위, 기술 스택, 개발/배포 방향
- `docs/architecture.md`: 전체 시스템 구조와 데이터 흐름
- `docs/data-model.md`: PostgreSQL 데이터 모델
- `docs/search-design.md`: Elasticsearch 검색 설계
- `docs/aws-infra.md`: AWS 인프라 구성
- `docs/development-log.md`: 개발 진행 기록

## 3. 기술 스택 결정

초기 기술 스택은 다음과 같이 결정했습니다.

```text
Frontend: Next.js + TypeScript
Backend: FastAPI
Crawler: Python
Database: PostgreSQL
Search Engine: Elasticsearch
Infrastructure: AWS
IaC: Terraform
```

선택 이유는 다음과 같습니다.

- Python과 Java에 익숙한 상황에서 RSS 수집, HTML 파싱, 텍스트 처리, 향후 AI 기능 확장을 고려해 Python 중심 백엔드가 적합했습니다.
- FastAPI는 Python 타입 힌트 기반으로 API를 빠르게 만들 수 있고 OpenAPI 문서화도 쉽습니다.
- Next.js는 공개 웹서비스에서 라우팅, SEO, 정적 배포, 향후 SSR/ISR 전환 가능성이 있어 React 단독보다 적합합니다.
- PostgreSQL은 JSONB, 텍스트 검색, pgvector 확장 가능성 때문에 MySQL보다 TechCase에 잘 맞습니다.
- Elasticsearch는 TechCase의 핵심인 검색 품질 실험을 위해 MVP부터 포함하기로 했습니다.

## 4. AWS 인프라 방향 결정

초기부터 AWS 자원을 사용하되 비용을 최소화하는 방향으로 정리했습니다.

최종 초기 인프라 방향은 다음과 같습니다.

```text
Web: S3 + CloudFront
Load Balancer: public subnet의 ALB
Backend/Search/Crawler: private subnet의 EC2
Database: private subnet의 RDS PostgreSQL
Outbound Internet: public subnet의 NAT Instance
Access: Systems Manager Session Manager
IaC: Terraform
```

주요 결정은 다음과 같습니다.

- Next.js는 초기에는 static export로 S3 + CloudFront에 배포합니다.
- FastAPI, crawler, Elasticsearch는 초기 비용과 복잡도를 줄이기 위해 private EC2 한 대에서 실행합니다.
- EC2에 public IP를 부여하지 않고 ALB를 통해 API만 노출합니다.
- Elasticsearch와 Kibana는 외부에 공개하지 않습니다.
- private EC2가 RSS feed에 접근해야 하므로 NAT Gateway 대신 NAT Instance를 사용합니다.
- AWS 콘솔 수동 작업을 줄이기 위해 Terraform으로 인프라를 관리하기로 했습니다.

## 5. Git 초기화와 문서 커밋

Git 기본 브랜치를 `master`에서 `main`으로 변경했습니다.

GitHub 원격 저장소:

```text
https://github.com/SmileJune/techcase.git
```

초기 문서 작업을 커밋하고 원격 저장소에 push했습니다.

주요 커밋:

```text
ff0f798 docs: define TechCase MVP direction
a2b076d docs: 설계 문서 정리
```

## 6. 모노레포 기본 구조 생성

초기 모노레포 구조를 생성했습니다.

```text
apps/
  web/
  backend/
infra/
  docker-compose.yml
docs/
```

루트 실행 스크립트도 추가했습니다.

```json
{
  "dev:web": "pnpm --dir apps/web dev",
  "build:web": "pnpm --dir apps/web build",
  "dev:backend": "cd apps/backend && uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000",
  "infra:up": "docker compose -f infra/docker-compose.yml up -d",
  "infra:down": "docker compose -f infra/docker-compose.yml down"
}
```

## 7. 로컬 인프라 구성

로컬 개발용 Docker Compose를 추가했습니다.

구성 요소:

```text
PostgreSQL 16
Elasticsearch 8.15.3
Kibana 8.15.3
```

주요 포트:

```text
PostgreSQL: localhost:5432
Elasticsearch: localhost:9200
Kibana: localhost:5601
```

실행 명령:

```bash
npm run infra:up
npm run infra:down
```

## 8. FastAPI 백엔드 골격 생성

FastAPI 기본 앱을 추가했습니다.

구성:

```text
apps/backend/app/main.py
apps/backend/app/config.py
apps/backend/app/routers/health.py
apps/backend/app/routers/search.py
apps/backend/app/db/session.py
apps/backend/app/search/client.py
```

초기 API:

```text
GET /health
GET /api/search?q=...
```

초기 검색 API는 빈 결과를 반환하는 placeholder로 시작했습니다.

## 9. Next.js 웹 골격 생성

Next.js 정적 웹 앱 골격을 추가했습니다.

초기 화면은 다음 요소를 포함했습니다.

- TechCase 브랜드
- 서비스 설명
- 검색 입력창
- 추천 검색어 버튼
- MVP 상태 메시지

초기에는 실제 API와 연결하지 않은 정적 UI였습니다.

Next.js는 AWS S3 + CloudFront 배포를 고려해 `output: "export"`로 설정했습니다.

## 10. pnpm build script 승인 이슈 해결

`npm run dev:web` 실행 중 pnpm 11의 build script 승인 정책에 걸렸습니다.

문제:

```text
ERR_PNPM_IGNORED_BUILDS
Ignored build scripts: sharp, unrs-resolver
```

해결:

`pnpm-workspace.yaml`에 build script 허용 목록을 명시했습니다.

```yaml
allowBuilds:
  sharp: true
  unrs-resolver: true
```

이후 `pnpm install`을 다시 실행해 `sharp`, `unrs-resolver`의 build script가 정상 실행되는 것을 확인했습니다.

## 11. PostgreSQL 모델과 Alembic 설정

SQLAlchemy 모델과 Alembic 마이그레이션을 추가했습니다.

초기 모델:

```text
Source
Article
CrawlRun
ArticleKeyword
```

생성된 테이블:

```text
sources
articles
crawl_runs
article_keywords
```

Alembic 초기 마이그레이션:

```text
202605160001_create_initial_tables.py
```

실행 명령:

```bash
npm run db:migrate
npm run db:history
```

검증:

- `ruff check` 통과
- Python compile 통과
- Alembic head 확인
- Alembic SQL 생성 확인
- 로컬 PostgreSQL에 마이그레이션 적용 확인

## 12. AWS RSS Source Seed 추가

초기 수집 대상 AWS 블로그 source seed를 추가했습니다.

등록한 source:

```text
aws-architecture-blog
aws-database-blog
aws-compute-blog
aws-big-data-blog
aws-devops-blog
```

실행 명령:

```bash
npm run db:seed
```

검증:

```text
1회차: created=5, updated=0
2회차: created=0, updated=5
```

즉, 반복 실행해도 중복 생성되지 않고 upsert됩니다.

## 13. RSS Crawler 1차 구현

enabled source의 RSS feed를 읽고 `articles` 테이블에 저장하는 crawler를 구현했습니다.

실행 명령:

```bash
npm run crawl:rss
```

초기 동작:

```text
sources에서 enabled=true인 feed 조회
RSS feed fetch
RSS entry title/url/published_at/summary/metadata 추출
url 기준 Article upsert
CrawlRun에 실행 결과 저장
```

최초 실행 결과:

```text
5개 source 각각 20개씩 수집
총 100개 article 생성
```

## 14. unchanged_count 개선

처음에는 기존 URL을 다시 만나면 항상 `updated_count`로 집계했습니다.

하지만 동일한 RSS item이면 DB row를 update하지 않는 것이 더 정확하다고 판단했습니다.

개선 후 집계:

```text
created: 새 article
updated: 기존 article인데 값이 변경됨
unchanged: 기존 article이고 값이 동일함
failed: 처리 실패
```

추가 마이그레이션:

```text
202605160002_add_unchanged_count_to_crawl_runs.py
```

검증 결과:

```text
반복 crawl 실행 시
created=0
updated=0
unchanged=100
```

## 15. Elasticsearch 색인 구현

수집된 `articles`를 Elasticsearch `articles` index에 색인하는 기능을 추가했습니다.

추가한 구성:

```text
apps/backend/app/search/indexes.py
apps/backend/app/search/documents.py
apps/backend/app/search/indexer.py
```

실행 명령:

```bash
npm run search:reindex
```

초기 Elasticsearch 문서 필드:

```text
id
title
url
company
source
sourceSlug
publishedAt
summary
content
technologies
architectureKeywords
problemKeywords
```

검증:

```text
Indexed articles: 100
Elasticsearch articles count: 100
```

## 16. Elasticsearch Client 버전 이슈 해결

처음에는 Python Elasticsearch client 9.x가 설치되어 로컬 Elasticsearch 8.15.3과 호환되지 않았습니다.

오류:

```text
Invalid media-type value on headers [Accept, Content-Type]
Accept version must be either version 8 or 7, but found 9
```

해결:

`pyproject.toml`에서 Elasticsearch client를 8.x로 고정했습니다.

```toml
elasticsearch>=8.15.1,<9
```

이후 `uv lock`, `uv sync`로 의존성을 갱신했습니다.

## 17. 검색 API를 Elasticsearch와 연결

기존 placeholder 검색 API를 실제 Elasticsearch 검색으로 교체했습니다.

검색 대상 필드:

```text
technologies^5
title^4
architectureKeywords^3
problemKeywords^3
summary^2
content
```

현재는 아직 `ArticleKeyword` 추출과 본문 추출이 구현되지 않았기 때문에 실질적으로는 `title`, `summary` 중심 검색입니다.

검증:

```text
/api/search?q=Lambda
status: 200
total: 9
```

샘플 결과:

```text
.NET 10 runtime now available in AWS Lambda
Building Memory-Intensive Apps with AWS Lambda Managed Instances
Build high-performance apps with AWS Lambda Managed Instances
```

## 18. 웹 검색 UI 연결

Next.js 검색 화면을 실제 FastAPI 검색 API와 연결했습니다.

추가 파일:

```text
apps/web/app/components/SearchExperience.tsx
```

구현 내용:

- 검색어 입력
- 추천 검색어 버튼
- `/api/search` 호출
- 검색 결과 카드 표시
- 로딩 상태 표시
- 에러 상태 표시
- 빈 결과 상태 표시
- 원문 링크 연결

검증:

```bash
npm run build:web
```

Next.js static export가 정상 완료되었습니다.

## 19. 현재 검색의 한계

현재 검색은 Elasticsearch 기반이지만 아직 다음 기능은 구현되지 않았습니다.

```text
본문 content_text 추출
ArticleKeyword 자동 추출
AWS 서비스명 사전 기반 태깅
아키텍처 키워드 태깅
문제 상황 키워드 태깅
동의어 검색
오타 보정
한글/영문 매핑
기술 조합 검색
```

따라서 현재 검색은 다음에 가깝습니다.

```text
RSS title/summary 기반 Elasticsearch 가중치 검색
```

## 20. 다음 작업 후보

다음 작업으로 가장 적합한 것은 검색 품질 개선입니다.

추천 순서:

```text
1. 사전 기반 키워드 추출기 구현
2. AWS 서비스명/기술명/아키텍처/문제 키워드 사전 작성
3. ArticleKeyword 저장
4. Elasticsearch 재색인
5. 검색 결과 품질 비교
6. 원문 HTML 본문 추출
7. content_text 기반 검색 강화
```

현재 가장 자연스러운 다음 구현 단위는 다음입니다.

```text
keywords:extract
```

이 명령은 `articles`의 title/summary를 읽고 사전 기반으로 키워드를 추출한 뒤 `article_keywords`에 저장하게 됩니다.

## 21. 검색 평가 데이터셋과 자동 평가 명령 추가

검색 품질 개선을 수치로 판단하기 위해 평가 데이터셋을 추가했습니다.

추가 파일:

```text
apps/backend/app/search/evaluation/queries.json
apps/backend/app/search/evaluation/evaluator.py
docs/search-evaluation.md
```

평가 쿼리는 AWS RSS에서 실제로 수집된 글을 기준으로 구성했습니다.

평가 범주:

```text
technology
problem
architecture
migration
```

평가 지표:

```text
Precision@5
Recall@10
MRR
NDCG@10
```

실행 명령:

```bash
npm run search:evaluate
```

키워드 추출 전 baseline:

```text
average precision@5 = 0.383
average recall@10 = 0.708
average mrr = 0.875
average ndcg@10 = 0.752
```

이 baseline을 통해 이후 검색 개선 작업이 실제로 좋아졌는지 비교할 수 있게 되었습니다.

## 22. 사전 기반 키워드 추출기 구현

검색 품질을 개선하기 위해 `dictionary_v1` 기반 키워드 추출기를 구현했습니다.

추가 파일:

```text
apps/backend/app/keywords/dictionaries.py
apps/backend/app/keywords/extractor.py
```

추출 대상:

```text
aws_service
technology
architecture
problem
```

실행 명령:

```bash
npm run keywords:extract
```

실행 결과:

```text
Extracted keywords: articles=100, keywords=181
```

추출된 키워드는 `article_keywords`에 저장되고, 이후 재색인을 통해 Elasticsearch 문서의 다음 필드에 반영됩니다.

```text
technologies
architectureKeywords
problemKeywords
```

재색인:

```bash
npm run search:reindex
```

키워드 추출 후 평가 결과:

```text
average precision@5 = 0.467
average recall@10 = 0.944
average mrr = 0.917
average ndcg@10 = 0.860
```

개선 폭:

```text
average precision@5: 0.383 -> 0.467
average recall@10: 0.708 -> 0.944
average mrr: 0.875 -> 0.917
average ndcg@10: 0.752 -> 0.860
```

특히 `cost optimization`, `streaming data pipeline`, `Change Data Capture`, `cross-Region resilience`처럼 제목/요약 검색만으로는 약했던 문제 상황 및 아키텍처 검색의 recall이 개선되었습니다.

## 23. 한국 기술 블로그 source 추가와 한글 검색 대응

AWS 영어 블로그만으로는 한글/영문 검색 대응을 검증하기 어렵기 때문에 한국 기술 블로그 source를 추가했습니다.

추가 source:

```text
Toss Tech
NAVER D2
Kakao Tech
Woowa Tech Blog
```

RSS feed:

```text
https://toss.tech/rss.xml
https://d2.naver.com/d2.atom
https://tech.kakao.com/feed/
https://techblog.woowahan.com/feed/
```

우아한형제들 기술블로그는 기본 HTTP 요청에서 차단 페이지가 내려올 수 있어 crawler에 User-Agent를 추가했습니다.

수집 결과:

```text
kakao-tech: created=10
naver-d2: created=20
toss-tech: created=20
woowa-tech-blog: created=10
```

전체 article 수:

```text
100 -> 160
```

한글/영문 검색 대응을 위해 keyword dictionary에 한글 alias를 추가했습니다.

예:

```text
비용 최적화 -> cost optimization
장애 대응 -> incident response
관측성 -> observability
카프카 -> kafka
서버리스 -> serverless
쿠버네티스 -> kubernetes
```

검색어에 한글 alias가 포함된 경우에만 영어 alias를 붙이는 query expansion을 추가했습니다.

이렇게 처리한 이유는 영어 검색어까지 과도하게 확장하면 `Lambda` 같은 검색에서 결과 수가 불필요하게 늘어 precision이 떨어질 수 있기 때문입니다.

재실행:

```bash
npm run db:seed
npm run crawl:rss
npm run keywords:extract
npm run search:reindex
npm run search:evaluate
```

최종 평가:

```text
evaluation queries = 16
indexed articles = 160

average precision@5 = 0.475
average recall@10 = 0.958
average mrr = 0.896
average ndcg@10 = 0.847
```

## 24. 우아한형제들 기술블로그 전체 RSS pagination 수집

우아한형제들 기술블로그는 RSS 첫 페이지에서는 10개 글만 내려주지만, `?paged=N` 방식으로 오래된 글을 더 가져올 수 있음을 확인했습니다.

확인 결과:

```text
page 1~51: 페이지당 10개
page 52: 2개
page 53: 404
unique_urls = 512
```

이를 crawler에 반영했습니다.

구현 방식:

```text
woowa-tech-blog source는 paginated source로 취급
feed_url?page=N 대신 feed_url?paged=N 사용
404 또는 새 URL이 없는 페이지를 만나면 종료
중복 URL은 수집 대상에서 제거
```

수집 결과:

```text
Crawled woowa-tech-blog: status=succeeded, fetched=512, created=502, updated=0, unchanged=10, failed=0
```

전체 article 수:

```text
160 -> 662
```

키워드 재추출:

```text
Extracted keywords: articles=662, keywords=275
```

재색인:

```text
Indexed articles: 662
```

662개 글 기준 평가:

```text
average precision@5 = 0.438
average recall@10 = 0.927
average mrr = 0.729
average ndcg@10 = 0.738
```

글 수가 크게 늘면서 검색 결과 후보는 풍부해졌지만, 일부 query에서는 기존 정답 문서의 순위가 밀리는 현상이 생겼습니다. 다음 작업에서는 기술 키워드와 문제 키워드가 함께 매칭되는 글에 더 높은 가중치를 주는 ranking 개선이 필요합니다.
