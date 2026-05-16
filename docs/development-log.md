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

## 25. LLM 기반 사례 요약 파이프라인 골격 추가

RSS 요약과 rule-based 발췌만으로는 TechCase가 원하는 사례 중심 정보를 충분히 제공하기 어렵다고 판단했습니다.

따라서 `display_summary` 방식은 중단하고, 별도 `article_summaries` 테이블에 LLM이 생성한 사례 요약을 저장하는 방향으로 전환했습니다.

추가한 구조:

```text
article_summaries
- article_id
- summary_type
- language
- model
- prompt_version
- case_summary
- problem
- solution
- technologies
- architecture_keywords
- problem_keywords
- confidence
- raw_response
```

추가 명령:

```bash
npm run llm:summarize -- --limit 3 --dry-run
npm run llm:summarize -- --source woowa-tech-blog --limit 10
```

요약 생성은 검색 요청 시점에 LLM을 호출하는 RAG 방식이 아니라, 미리 article을 enrich하는 offline batch 방식입니다.

이렇게 처리한 이유:

```text
검색 응답 속도 유지
LLM 비용 제어
요약 품질 검수 가능
프롬프트/모델 버전 관리 가능
장애 시에도 기존 검색 기능 유지
```

검색 문서에는 최신 `case_summary`를 `caseSummary`로 투영하고, 검색 결과 카드에서는 `caseSummary`를 RSS summary보다 우선 표시합니다.

## 26. LLM 요약 content_type 분류와 batch 안정성 개선

모든 기술 블로그 글을 요약 대상으로 유지하되, 글의 성격은 `content_type`으로 분류하기로 했습니다.

추가한 content_type 후보:

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

이렇게 하면 글을 제외하지 않고도, 이후 검색 ranking이나 필터에서 기술 사례성 글을 더 우선할 수 있습니다.

batch 생성도 article 단위로 안정화했습니다.

변경 전:

```text
한 article에서 LLM 호출 또는 JSON 파싱 실패 시 전체 명령 중단 가능
```

변경 후:

```text
article별 try/catch
성공 article은 즉시 commit
실패 article은 rollback 후 다음 article 계속 처리
selected/generated/failed 카운트 출력
```

Source별 본문 확보율도 확인했습니다.

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

검증:

```text
npm run llm:summarize -- --source woowa-tech-blog --limit 1
Generated summary: 별점 뒤에 숨겨진 리뷰의 온도, LLM으로 한 끗 차이가 다른 추천 만들기
LLM summaries: selected=1, generated=1, failed=0
```

저장된 content_type:

```text
technical_case
```

## 27. 기업별 수집 전략 분리

기업 기술 블로그를 더 많이 추가하기 전에, source마다 수집 방식을 데이터로 관리할 수 있게 변경했습니다.

추가한 `sources` 필드:

```text
collection_strategy
pagination_strategy
content_strategy
language
country
trust_level
```

전략 의미:

```text
collection_strategy
- rss
- rss_with_article_fetch
- sitemap
- html_list
- manual
- deferred

pagination_strategy
- none
- wordpress_paged
- sitemap
- cursor
- page_number

content_strategy
- feed_only
- article_fetch
- deferred
```

현재 적용:

```text
AWS, Toss, NAVER D2, Kakao Tech: rss + none + feed_only
Woowa Tech Blog: rss + wordpress_paged + feed_only
```

변경 이유:

- 기업 블로그마다 RSS 품질, 페이지네이션, 본문 제공 방식이 다릅니다.
- crawler 코드에 특정 회사명을 하드코딩하면 source가 늘어날수록 유지보수가 어려워집니다.
- RSS가 없는 공식 기술 블로그도 `feed_url = null`, `collection_strategy = deferred`로 후보 관리할 수 있어야 합니다.
- 이후 source probe, article fetcher, sitemap crawler를 각각 독립적으로 추가할 수 있습니다.

구현 변경:

- `Source` 모델과 Alembic migration에 수집 전략 필드를 추가했습니다.
- seed 데이터에 언어, 국가, 신뢰도, 페이지네이션 전략을 채웠습니다.
- 기존 우아한형제들 전용 페이지네이션 하드코딩을 제거하고, `pagination_strategy = wordpress_paged`를 기준으로 동작하게 변경했습니다.

## 28. 추가 기술 블로그 후보 분류

기업 기술 블로그 후보를 실제 feed 요청 기준으로 분류했습니다.

문서:

```text
docs/source-collection-strategy.md
```

RSS로 바로 수집 가능한 한국어 후보:

```text
당근
LY Corporation
카카오페이
쏘카
컬리
여기어때
요기요
무신사
29CM
데브시스터즈
```

RSS로 바로 수집 가능한 영어 후보:

```text
Netflix
Airbnb
Cloudflare
GitHub
Stripe
Slack
Datadog
Pinterest
Dropbox
Lyft
```

별도 수집기 검토 대상:

```text
쿠팡
넥슨
Shopify
LinkedIn
Uber
```

## 29. 우선순위 한국어 기술 블로그 수집 시작

RSS가 바로 확인된 한국어 기업 기술 블로그 10곳을 source seed에 추가하고, source별로 하나씩 수집했습니다.

추가 source:

```text
daangn-tech-blog
ly-corporation-tech-blog
kakaopay-tech-blog
socar-tech-blog
kurly-tech-blog
gc-company-tech-blog
yogiyo-tech-blog
musinsa-tech-blog
29cm-team
devsisters-tech-blog
```

crawler는 특정 source만 수집할 수 있도록 `--source` 옵션을 추가했습니다.

예:

```bash
npm run crawl:rss -- --source daangn-tech-blog
```

수집 결과:

```text
29cm-team                  10
daangn-tech-blog           10
devsisters-tech-blog       66
gc-company-tech-blog       10
kakaopay-tech-blog        159
kurly-tech-blog           119
ly-corporation-tech-blog   50
musinsa-tech-blog          10
socar-tech-blog            10
yogiyo-tech-blog           10
```

신규 source에서 총 454개 article을 수집했습니다.

후속 처리:

```text
keywords:extract  articles=1116, keywords=1482
search:reindex    Indexed articles=1116
```

검색 평가:

```text
average precision@5 0.425
average recall@10   0.865
average mrr         0.615
average ndcg@10     0.654
```

새로운 article이 많이 추가되면서 기존 평가 데이터셋의 정답 기준과 실제 검색 후보 풀이 달라졌습니다. 다음 단계에서는 신규 기업 블로그 글을 반영해 한글 검색 평가 데이터셋을 보강해야 합니다.

## 30. 신규 한국어 source 기반 검색 평가 데이터셋 보강

새로 수집한 한국어 기업 기술 블로그 글을 기준으로 검색 평가 쿼리 8개를 추가했습니다.

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

평가셋 설명도 AWS 중심에서 AWS + 한국 기업 기술 블로그 기준으로 수정했습니다.

평가 결과:

```text
evaluation queries = 24
indexed articles = 1116

average precision@5 0.367
average recall@10   0.749
average mrr         0.701
average ndcg@10     0.632
```

관찰:

- `EKS 오토스케일링`, `게임 서버`, `이벤트 기반 상품 조회`는 기대 결과가 상위에 잘 노출됐습니다.
- `검색 개선`, `로그 플랫폼`은 관련 결과가 일부 잡히지만 일반 명사 조합이라 ranking이 흔들립니다.
- `비용 최적화`는 여전히 한글 검색 품질 개선이 필요한 대표 쿼리입니다.

다음 개선 후보:

```text
한글 복합어/문제상황 키워드 boost
LLM 요약 필드 검색 가중치 강화
신규 source 글에 대한 LLM 요약 확대
검색 평가 쿼리별 top 10 결과 스냅샷 저장
```

## 31. 한글 복합 쿼리 검색 품질 개선

신규 한국어 source 평가에서 약점으로 드러난 `검색 개선`, `로그 플랫폼`, `비용 최적화`, `JVM 응답 지연`, `카나리 배포` 같은 한글 복합 쿼리를 개선했습니다.

적용한 변경:

```text
검색 쿼리에 phrase match boost 추가
사전 매칭 keyword field boost 추가
한글 복합어 사전 확장
cost/costs처럼 너무 넓게 매칭되던 alias 제거
비용 최적화 평가셋 expected result 보정
```

추가한 주요 키워드:

```text
옵저버빌리티
로그 플랫폼
로그 파이프라인
검색 개선
검색 성능
JVM
카나리 배포
이벤트 기반
ClickStack
Vertex AI Search
Argo Rollouts
Spinnaker
Istio
```

키워드 재추출 결과:

```text
before keywords = 1482
after keywords = 1743
articles = 1116
```

검색 평가 개선 전:

```text
average precision@5 0.367
average recall@10   0.749
average mrr         0.701
average ndcg@10     0.632
```

검색 평가 개선 후:

```text
average precision@5 0.375
average recall@10   0.832
average mrr         0.778
average ndcg@10     0.714
```

이번 개선으로 모든 평균 지표가 상승했습니다. 다만 `검색 개선`, `로그 플랫폼`처럼 일반 명사 조합이 포함된 쿼리는 검색 후보가 여전히 넓으므로, 다음 단계에서는 LLM 요약 필드와 문제상황 키워드의 품질을 더 높이는 작업이 필요합니다.

## 32. 신규 한국어 source LLM 요약 샘플 생성

신규 한국어 기술 블로그 source에 대해 LLM 기반 사례 요약을 샘플 생성했습니다.

대상 source:

```text
kakaopay-tech-blog       3
kurly-tech-blog          3
devsisters-tech-blog     3
ly-corporation-tech-blog 3
daangn-tech-blog         3
gc-company-tech-blog     2
socar-tech-blog          2
```

총 19개 article 요약을 생성했습니다.

content_type 분포:

```text
technical_case 18
other           1
```

좋았던 샘플:

```text
당근 PyPI 공급망 공격 대응
여기어때 옵저버빌리티 Right-Sizing
여기어때 Argo Rollouts 카나리 배포
쏘카 로그 파이프라인 개선
쏘카 Node.js 컨테이너 graceful shutdown
데브시스터즈 게임 서버 돌아보기
```

요약 품질 관찰:

- `case_summary`, `problem`, `solution`이 실제 사례 탐색에 사용할 만큼 구체적으로 생성됐습니다.
- RSS summary보다 검색 결과 카드에서 보여주기 적합합니다.
- 최신순으로 생성하면 이벤트성 글도 포함되므로, 대량 생성 전에는 기술 사례 우선순위 선정 기준이 필요합니다.

후속 처리:

```text
search:reindex
search:evaluate
```

평가 결과:

```text
average precision@5 0.375
average recall@10   0.825
average mrr         0.792
average ndcg@10     0.716
```

LLM 요약 반영 전과 비교하면 MRR/NDCG가 소폭 상승했습니다. 수치 개선보다 더 중요한 변화는 검색 결과 카드에서 문제/해결 맥락을 바로 보여줄 수 있게 됐다는 점입니다.

## 33. 신규 글 자동 후처리 스케줄러 명령 추가

새 글이 올라왔을 때 신규 article만 LLM 요약하고 검색 색인에 반영하는 스케줄러용 명령을 추가했습니다.

명령:

```bash
npm run ingest:scheduled
```

트리거 구조:

```text
systemd timer
-> systemd service
-> npm run ingest:scheduled
```

초기 AWS 구성에서는 private EC2 안의 systemd timer가 주기적으로 service를 실행합니다. service는 backend 코드베이스에서 `npm run ingest:scheduled`를 실행하고, 이 명령이 수집/키워드/요약/색인 파이프라인을 담당합니다.

이 방식을 선택한 이유:

```text
추가 AWS 비용이 거의 없음
FastAPI, crawler, Elasticsearch가 같은 private EC2 안에 있어 네트워크 구성이 단순함
초기 수집량이 크지 않아 ECS Scheduled Task나 EventBridge까지 분리할 필요가 낮음
나중에 crawler가 커지면 ECS Scheduled Task 또는 EventBridge Scheduler로 전환 가능
```

처리 흐름:

```text
crawl RSS
-> 새 article이 없으면 종료
-> keyword extraction
-> 이번 실행에서 새로 생성된 article만 LLM 요약
-> Elasticsearch reindex
```

신규 글 판단 기준:

```text
scheduler started_at 기록
Article.created_at >= started_at 인 article만 요약
```

기존 `llm:summarize`는 요약이 없는 과거 글도 대상으로 삼을 수 있지만, `ingest:scheduled`는 새 글만 요약하도록 분리했습니다.

검증:

```bash
npm run ingest:scheduled -- --source daangn-tech-blog --summary-limit 2
```

기존에 모두 수집된 source라 새 글이 없었고, 후처리가 건너뛰어졌습니다.

```text
Crawled daangn-tech-blog: status=succeeded, fetched=10, created=0, updated=0, unchanged=10, failed=0
Post process: keyword_articles=0, keywords=0, summary_selected=0, summary_generated=0, summary_failed=0, indexed=0
```

운영 문서:

```text
docs/scheduler.md
```

## 34. 검색 결과 카드 맥락 강화

상세 페이지를 만들기보다는 검색 결과 카드에서 바로 판단할 수 있는 정보를 보강했습니다. TechCase의 역할은 원문을 대체하는 것이 아니라, 사용자가 읽을 가치가 있는 기업 기술 블로그 글을 빠르게 고르게 하는 것이기 때문입니다.

추가한 카드 정보:

```text
회사 로고/회사명/source/발행일
사례 유형
LLM 사례 요약
문제/해결
기술/문제 상황/아키텍처 키워드 그룹
원문 보기 링크
검색 매칭 근거
```

공식 출처 기반 로고:

```text
NAVER  docs/logo-assets.md 기준 공식 브랜드 리소스
Toss   Toss 브랜드 리소스 센터
Kakao  Kakao 공식 CI 페이지
```

공식 로고 파일이 있는 회사는 이미지 로고를 사용하고, 없는 회사는 기존 텍스트 기반 로고 배지를 fallback으로 사용합니다. 로고는 출처 식별 목적으로만 사용하며, 각 회사와 TechCase의 제휴를 의미하지 않는다는 상표 안내 문구를 README에 추가했습니다.

검색 하이라이트:

```text
Elasticsearch highlight의 <em>...</em> 조각을 React에서 안전하게 분해
제목/사례 요약/문제/해결에 검색어 highlight 표시
매칭 근거 섹션에서 어떤 필드가 검색어와 매칭됐는지 표시
```

이 변경으로 사용자는 “왜 이 글이 검색 결과에 나왔는지”를 카드 안에서 바로 확인할 수 있습니다.

검증:

```bash
npm run build:web
git diff --check
```

## 35. 기술명 alias와 오탈자 검색 보정

`엘라스틱서치`, `엘라스틱 서치`, `elasticsearch`, `elastic search`, 오탈자까지 같은 기술 사례로 연결되도록 검색 보정을 추가했습니다.

추가한 Elasticsearch alias:

```text
elasticsearch
elastic search
elastic-search
엘라스틱서치
엘라스틱 서치
엘라스틱 검색
```

추가한 MQTT alias:

```text
mqtt
mq telemetry transport
엠큐티티
```

검색 보정 방식:

```text
KEYWORD_RULES alias 매칭 시 canonical keyword phrase boost 적용
영문 기술명 오탈자는 alias와 편집거리 기반으로 보정
일반 fuzzy query는 사전으로 보정하지 못한 영문 검색어에만 낮은 boost로 적용
```

샘플 확인:

```text
엘라스틱서치  -> Elasticsearch 관련 글 상위 노출
엘라스틱 서치 -> Elasticsearch 관련 글 상위 노출
elastic search -> Elasticsearch 관련 글 상위 노출
elastcsearch -> Elasticsearch 관련 글 상위 노출
mq/mqt/mqtt/엠큐 -> MQTT 자동완성 후보 노출
```

MQTT 보강 후 재처리:

```bash
npm run keywords:extract
npm run search:reindex
npm run suggest:reindex
```

MQTT 검색 결과는 5개 사례가 잡히며, 관련 article의 `technologies`에도 `MQTT`가 반영됐습니다.

## 36. Elasticsearch completion suggester 기반 자동완성

검색창에 입력 중인 기술명/회사명/문제 상황을 제안하기 위해 Elasticsearch `completion suggester` 기반 자동완성을 추가했습니다.

인덱스 구조:

```text
articles      실제 검색 결과용 인덱스
suggestions   자동완성 후보 전용 인덱스
```

후보 생성 소스:

```text
KEYWORD_RULES      기술명, AWS 서비스, 문제 상황, 아키텍처 키워드
sources            회사명
article_keywords   후보별 articleCount와 weight 보정
```

추가 API:

```text
GET /api/suggest?q=ka
```

추가 명령:

```bash
npm run suggest:reindex
```

weight 정책:

```text
AWS 서비스와 기술 후보를 회사 후보보다 우선
articleCount는 최대 50까지만 반영해 대형 source가 자동완성을 과도하게 지배하지 않도록 제한
completion fuzzy는 min_length와 prefix_length로 과도한 후보 확장을 제한
```

프론트 UI:

```text
검색어 2글자 이상부터 debounce 180ms로 suggest API 호출
방향키로 후보 이동
Enter로 후보 선택 검색
Escape로 후보 닫기
후보 클릭 시 즉시 검색
```

샘플 확인:

```text
ka    -> Apache Kafka, Kakao Pay, Kakao
kaf   -> Apache Kafka
elas  -> Elasticsearch, Amazon ElastiCache
elastc -> Elasticsearch
엘라   -> Elasticsearch
쿠버   -> Kubernetes
```

검증:

```bash
npm run suggest:reindex
uv run python -m compileall app
uv run python -c 'from fastapi.testclient import TestClient; from app.main import app; ...'
npm run build:web
git diff --check
```

## 37. 자동완성 누락 후보 점검 스크립트 추가

MQTT처럼 검색 결과에는 존재하지만 자동완성 후보에는 빠지는 기술을 찾기 위해 `suggest:audit` 명령을 추가했습니다.

명령:

```bash
npm run suggest:audit
```

목표:

```text
article 제목/RSS 요약/본문/LLM 요약 technologies에서 반복 등장하는 기술 후보 수집
이미 KEYWORD_RULES 또는 source/company 후보에 등록된 항목 제외
후보별 article 수와 예시 글 제목 출력
```

기본 실행 기준:

```text
min_articles = 3
limit = 30
```

샘플 실행:

```bash
npm run suggest:audit -- --min-articles 3 --limit 20
```

주요 후보 예:

```text
IAM
EC2
Java
React
LLM
Spring Boot
JPA
VPC
Node.js
Kotlin
```

이 결과는 자동으로 사전에 반영하지 않습니다. `IAM`, `EC2`, `Java`, `React`처럼 실제로 자동완성 후보로 넣을 가치가 있는 항목과, 너무 일반적이거나 맥락 의존적인 항목을 사람이 한 번 검토한 뒤 `KEYWORD_RULES`에 추가합니다.

스케줄러 후처리도 보강했습니다.

```text
crawl
keyword extraction
LLM summary
articles reindex
suggestions reindex
```

이제 신규 글이 수집되면 검색 인덱스뿐 아니라 자동완성 인덱스도 함께 갱신됩니다.
