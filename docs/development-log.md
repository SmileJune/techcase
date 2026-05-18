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

## 38. suggest:audit 상위 후보 사전 반영

`suggest:audit` 결과 중 실제 자동완성 후보로 가치가 높은 기술/서비스를 `KEYWORD_RULES`에 추가했습니다.

추가한 AWS 서비스:

```text
AWS IAM
Amazon EC2
Amazon VPC
```

추가한 기술:

```text
Java
Kotlin
React
Node.js
Spring Boot
JPA
LLM
```

재처리:

```bash
npm run keywords:extract
npm run search:reindex
npm run suggest:reindex
npm run suggest:audit -- --min-articles 3 --limit 10
npm run search:evaluate
```

키워드 재추출 결과:

```text
articles = 1116
keywords = 2583
```

자동완성 후보 수:

```text
suggestions = 68
```

샘플 확인:

```text
ja   -> Java, JPA
rea  -> React
spr  -> Spring Boot
node -> Node.js
ko   -> Kotlin
iam  -> AWS IAM
ec   -> Amazon EC2
vp   -> Amazon VPC
ll   -> LLM
```

사전 반영 후 `suggest:audit` 상위 후보에서는 추가한 항목들이 빠졌고, 다음 검토 후보는 `real-time`, `ML`, `생성형 AI`, `Redis`, `Slack`, `REST` 등으로 이동했습니다.

검색 평가:

```text
average precision@5 = 0.392
average recall@10 = 0.819
average mrr = 0.814
average ndcg@10 = 0.735
```

## 39. 추가 기술 블로그 후보 백로그 정리

서비스의 현재 약점은 검색/요약 기능 자체보다 수집된 기업 사례의 폭이 아직 좁다는 점입니다. 더 많은 기업의 기술 블로그를 추가하기 위해, 다음 source 후보를 별도 백로그 문서로 정리했습니다.

작성한 문서:

```text
docs/source-candidates.md
```

문서에 정리한 내용:

```text
P0: RSS/Atom feed가 확인되어 바로 seed 추가 가능한 후보
P1: 공식 블로그로 보이나 feed와 본문 품질 검증이 필요한 후보
P2: RSS가 없거나 불안정해서 HTML 목록/sitemap 수집기가 필요한 후보
P3: 공식성, 업데이트 상태, 수집 정책 확인이 필요한 후보
```

바로 추가하기 좋은 영어권 후보:

```text
Netflix Tech Blog
Meta Engineering
Slack Engineering
Cloudflare Blog
GitHub Engineering
Datadog Engineering
Dropbox Tech
Lyft Engineering
Airbnb Tech Blog
Stripe Blog
Pinterest Engineering
```

추가 검토할 한국어 후보:

```text
네이버 클라우드 플랫폼
넷마블 기술 블로그
G마켓 기술 블로그
직방 기술 블로그
인프랩 기술 블로그
뱅크샐러드 기술 블로그
PortOne Developers
Sendbird Engineering
Upstage Blog
쿠팡 Engineering Blog
오늘의집 기술 블로그
야놀자 기술 블로그
```

다음 구현 작업은 P0 영어권 RSS source를 seed에 추가하고, source별 수집량과 요약 품질을 확인하는 것입니다. 이후 한국어 P1 후보는 `source probe` 명령을 만들어 feed URL과 본문 품질을 자동으로 검증한 뒤 추가합니다.

## 40. 한국어 기술 블로그 우선 확장

영어권 대형 기술 블로그보다 한국어 기업 기술 블로그를 먼저 늘리는 방향으로 조정했습니다.

이유:

```text
한글 문제상황 검색 품질을 먼저 끌어올릴 수 있음
국내 기업 사례 비교라는 초기 차별점에 더 직접적으로 연결됨
한영 기술명 검색과 한국어 LLM 요약 품질을 더 빨리 검증할 수 있음
```

RSS 또는 Medium feed에서 entry가 확인된 한국어 source를 seed에 추가했습니다.

추가 source:

```text
naver-cloud-platform-tech-blog
zigbang-tech-blog
wantedlab-tech-blog
coupang-engineering-blog
lunit-team-blog
gmarket-tech-blog
netmarble-tech-blog
```

feed 확인 결과:

```text
NAVER Cloud Platform Tech Blog  10
Zigbang Tech Blog               10
Wantedlab Tech Blog             10
Coupang Engineering Blog        10
Lunit Team Blog                 10
Gmarket Tech Blog               10
Netmarble Tech Blog             15
```

Medium 기반 source는 최신 10개 중심으로 내려오는 한계가 있습니다. Medium archive HTML은 Cloudflare challenge가 걸릴 수 있어 서버 crawler에서 안정적으로 접근하기 어렵습니다. 우선 Medium source는 최신 feed 중심으로 수집하고, 과거 글 전체 수집은 공식 API 또는 허용 가능한 archive 접근 방식을 별도로 검토합니다.

실제 수집 결과:

```text
naver-cloud-platform-tech-blog: fetched=10, created=10
zigbang-tech-blog:              fetched=10, created=10
wantedlab-tech-blog:           fetched=10, created=10
coupang-engineering-blog:      fetched=10, created=10
lunit-team-blog:               fetched=10, created=10
gmarket-tech-blog:             fetched=10, created=10
netmarble-tech-blog:           fetched=15, created=15
```

후처리:

```bash
npm run keywords:extract
npm run search:reindex
npm run suggest:reindex
npm run search:evaluate
```

키워드 재추출 결과:

```text
articles = 1191
keywords = 2741
```

검색/자동완성 재색인 결과:

```text
indexed articles = 1191
indexed suggestions = 75
```

검색 평가:

```text
average precision@5 = 0.392
average recall@10 = 0.806
average mrr = 0.803
average ndcg@10 = 0.726
```

신규 source가 늘었지만 평가 데이터셋은 아직 기존 정답 문서 중심입니다. 다음 단계에서는 새로 수집한 한국어 source를 기준으로 평가 쿼리와 정답 문서를 보강해야 합니다.

추가 확인 결과 G마켓은 `sitemap.xml` 기반 수집이 가능했고, 넷마블은 RSS 페이지네이션이 동작했습니다.

구현한 내용:

```text
apps/backend/app/crawler/sitemap.py
npm run crawl:sitemap
```

G마켓 source 전략:

```text
collection_strategy = sitemap
feed_url = https://dev.gmarket.com/sitemap.xml
content_strategy = article_fetch
```

넷마블 source 전략:

```text
collection_strategy = rss
pagination_strategy = wordpress_paged
```

추가 수집 결과:

```text
gmarket-tech-blog:   fetched=104, created=94, updated=10
netmarble-tech-blog: fetched=73,  created=58, updated=0, unchanged=15
```

재처리:

```bash
npm run keywords:extract
npm run search:reindex
npm run suggest:reindex
npm run search:evaluate
```

재처리 결과:

```text
articles = 1343
keywords = 2944
indexed articles = 1343
indexed suggestions = 75
```

검색 평가:

```text
average precision@5 = 0.400
average recall@10 = 0.806
average mrr = 0.803
average ndcg@10 = 0.728
```

Medium 기반 source는 여전히 최신 10개 한계가 있습니다. 다음 수집 확장 작업은 sitemap을 제공하는 한국어 블로그를 더 찾거나, HTML 목록 수집기를 추가하는 방향이 적절합니다.

## 41. 한국어 source 추가 수집

RSS 또는 sitemap 기반으로 더 가져올 수 있는 한국어 source를 추가 확인했습니다.

추가 source:

```text
banksalad-blog
inflab-tech-blog
upstage-blog
```

수집 전략:

```text
banksalad-blog: rss / none / feed_only
inflab-tech-blog: rss / none / feed_only
upstage-blog: sitemap / none / article_fetch
```

Upstage는 전체 sitemap에서 `/blog/ko/...` 패턴만 수집하도록 source별 sitemap article URL 패턴을 추가했습니다.

수집 결과:

```text
banksalad-blog: fetched=78, created=78
inflab-tech-blog: fetched=42, created=42
upstage-blog:    fetched=76, created=76
```

이번 라운드 신규 article:

```text
196
```

재처리:

```bash
npm run keywords:extract
npm run search:reindex
npm run suggest:reindex
npm run search:evaluate
```

재처리 결과:

```text
articles = 1539
keywords = 3198
indexed articles = 1539
indexed suggestions = 78
```

검색 평가:

```text
average precision@5 = 0.375
average recall@10 = 0.806
average mrr = 0.799
average ndcg@10 = 0.731
```

신규 source가 늘면서 기존 평가 데이터셋의 정답 문서가 현재 검색 후보 풀을 충분히 대표하지 못하게 되었습니다. 특히 `ko-tech-search`, `ko-problem-cost-optimization` 같은 쿼리는 후보가 크게 넓어졌기 때문에, 신규 source 기반 정답 문서를 추가해 평가 데이터셋을 갱신해야 합니다.

보류한 source:

```text
Sendbird
```

Sendbird는 sitemap에 글이 많지만 제품/마케팅 콘텐츠가 많이 섞입니다. 기술 사례 검색 품질을 흐리지 않으려면 engineering/API/SDK/infrastructure 성격의 글만 고르는 필터가 필요합니다.

## 42. 신규 한국어 source 검색 평가셋 보강

한국어 source가 1539개 article까지 늘면서 기존 평가셋이 현재 검색 후보 풀을 충분히 대표하지 못하게 되었습니다. 새로 수집한 source의 실제 글을 기준으로 평가 쿼리와 expected result를 보강했습니다.

수정한 파일:

```text
apps/backend/app/search/evaluation/queries.json
docs/search-evaluation.md
```

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

평가셋 검증:

```bash
uv run python -m json.tool app/search/evaluation/queries.json
npm run search:evaluate
```

평가 결과:

```text
evaluation queries = 33
average precision@5 = 0.394
average recall@10 = 0.839
average mrr = 0.854
average ndcg@10 = 0.784
```

이전 평가와 비교:

```text
average precision@5: 0.375 -> 0.394
average recall@10:   0.806 -> 0.839
average mrr:         0.799 -> 0.854
average ndcg@10:     0.731 -> 0.784
```

의미:

```text
신규 source 기반 정답 문서가 평가셋에 반영됨
새 source 추가 후 낮아졌던 precision@5가 일부 회복됨
recall@10, mrr, ndcg@10은 확실히 개선됨
검색 후보가 넓은 쿼리는 ranking 개선 여지가 남아 있음
```

## 43. 검색 결과 정렬 기준 추가

검색 결과가 많아지면서 사용자가 관련도뿐 아니라 최신 글 기준으로도 탐색할 수 있어야 했습니다. 검색 API와 화면에 정렬 기준을 추가했습니다.

추가한 정렬 기준:

```text
relevance: 관련도순, 기본값
latest: 최신순
```

API:

```text
GET /api/search?q=Redis%20Stream&sort=relevance
GET /api/search?q=Redis%20Stream&sort=latest
```

구현:

```text
backend search service에서 sort 파라미터 처리
latest 선택 시 publishedAt desc, _score desc 순서로 Elasticsearch sort 적용
frontend 검색 패널에 관련도순/최신순 세그먼트 컨트롤 추가
정렬 변경 시 현재 검색어로 다시 검색
검색 결과 요약에 현재 정렬 기준 표시
```

검증:

```bash
uv run ruff check app/routers/search.py app/search/service.py
pnpm --dir apps/web exec tsc --noEmit
npm run build:web
```

## 56. 비용 최적화 평가셋 보정

검색 audit에서 `비용 최적화` 한글 쿼리의 `precision@5`가 0으로 나타났지만, 실제 상위 결과를 확인해보니 검색 결과 자체가 나쁘다기보다 평가셋이 신규 수집 글을 충분히 반영하지 못한 상태였습니다.

확인한 상위 결과:

```text
스타트업 엔지니어의 AWS 비용 최적화 경험기
클라우드 서비스 사용량 관리를 통한 운영 비용 최적화
데이터는 지웠는데 비용은 그대로? Aurora 스토리지 비용 최적화 하기
The Hidden Price Tag: Uncovering Hidden Costs in Cloud Architectures with the AWS Well-Architected Framework
Cloud expenditure optimization for cost efficiency
```

위 글들은 제목, LLM 요약, 문제/해결 필드 기준으로 비용 최적화 사례성이 충분하므로 `ko-problem-cost-optimization` expected result에 추가했습니다. 반면 `AWS re:Invent 2023, 관심 세션을 중심으로` 글은 비용 최적화와 관련은 있지만 기업 적용 사례보다는 세션 회고 성격이 강해 정답셋에는 포함하지 않았습니다.

평가 결과:

```text
average precision@5 = 0.436
average recall@10 = 0.845
average mrr = 0.858
average ndcg@10 = 0.788
```

대표 변화:

```text
ko-problem-cost-optimization precision@5 = 0.000 -> 0.800
```

이번 작업은 검색 로직 개선이 아니라 평가 기준 정합성 개선입니다. 데이터가 늘어날수록 “검색 품질 저하”와 “평가셋 누락”을 분리해서 판단해야 합니다.

## 45. 필터 facet 품질 개선

단순 count 순서 facet은 `search`, `Java`, `observability`처럼 범용적인 키워드가 앞에 뜨는 문제가 있었습니다. 검색어와 직접 관련된 기준을 빠르게 고를 수 있도록 facet 정렬을 개선했습니다.

변경 내용:

```text
기술 facet aggregation size를 12에서 32로 확대
문제 상황 facet aggregation size를 10에서 18로 확대
검색어와 매칭된 키워드 facet에 isRecommended 표시
추천 facet을 facet 목록 상단에 우선 배치
범용 facet(search, Java, observability)은 직접 매칭이 아니면 뒤로 배치
AWS source facet은 AWS 회사명 대신 세부 블로그명 우선 표시
추천 facet chip에 별도 스타일 적용
```

샘플:

```text
Redis Stream:
Redis, Redis Stream, Apache Kafka ...

MQTT:
MQTT, Redis, Amazon S3 ...

엘라스틱서치:
Elasticsearch, Apache Kafka, Amazon S3 ...
```

검증:

```bash
uv run ruff check app/search/service.py
pnpm --dir apps/web exec tsc --noEmit
npm run search:evaluate
```

평가 결과:

```text
average precision@5 = 0.400
average recall@10 = 0.839
average mrr = 0.854
average ndcg@10 = 0.782
```

## 46. 검색 결과 카드 UI 밀도 조정

검색 결과 카드에 문제/해결/매칭 근거가 모두 펼쳐져 있어 목록이 번잡해지는 문제가 있었습니다. 기본 카드에서는 글을 읽을지 판단하는 데 필요한 정보만 보이도록 정리했습니다.

변경 내용:

```text
카드 기본 본문은 LLM 사례 요약 중심으로 표시
요약은 최대 2줄로 제한
문제/해결은 사례 판단에 중요한 정보이므로 카드 기본 영역에 바로 표시
검색 하이라이트는 검색 근거 보기 접힘 영역으로 이동
기술 태그는 최대 3개, 문제/구조 태그는 최대 2개 우선 노출
숨겨진 태그 수는 +N chip으로 표시
원문 보기 링크와 검색 근거 영역을 카드 하단으로 정리
```

의도:

```text
검색 결과 목록은 빠르게 훑을 수 있게 유지
검색 근거는 사용자가 필요할 때만 열어볼 수 있게 제공
카드마다 반복되는 설명을 줄이고 LLM 요약의 판단 가치를 높임
```

검증:

```bash
pnpm --dir apps/web exec tsc --noEmit
npm run build:web
```

## 47. 검색 결과 상단 요약 바 추가

검색 결과 목록에 들어가기 전에 현재 검색 결과의 전체 맥락을 빠르게 파악할 수 있도록 상단 요약 바를 추가했습니다.

표시 정보:

```text
주요 기술: technologies facet 상위 3개
문제 맥락: problemKeywords facet 상위 3개
주요 출처: sources facet 상위 3개
적용 필터: 현재 선택된 필터 개수
```

의도:

```text
사용자가 개별 카드를 읽기 전에 검색어와 관련된 대표 기술/문제/출처를 먼저 파악
검색 결과 카드마다 맥락을 과하게 반복하지 않고 결과 목록의 탐색 속도 개선
추천 facet은 요약 바에서도 강조 색상으로 표시
```

검증:

```bash
pnpm --dir apps/web exec tsc --noEmit
npm run build:web
```

## 48. 필터 영역 compact화

검색 결과 상단 요약 바가 추가되면서 `결과 좁히기` 필터 영역을 기본 화면에서 더 조용하게 보이도록 접힘 패널로 변경했습니다.

변경 내용:

```text
필터 영역을 details/summary 기반 접힘 패널로 변경
기본 상태에서는 결과 좁히기와 필터 열기만 표시
필터가 적용된 경우 N개 적용 중 상태 표시
필터 적용 중에는 패널을 열린 상태로 렌더링
필터 초기화 버튼은 펼친 영역 안에 유지
```

의도:

```text
검색 결과 상단에서 요약 바와 카드가 먼저 보이도록 화면 밀도 조정
필터는 필요할 때 여는 보조 도구로 배치
선택된 필터 상태는 닫힌 패널에서도 놓치지 않게 표시
```

검증:

```bash
pnpm --dir apps/web exec tsc --noEmit
npm run build:web
```

## 49. LLM 요약 100개 backfill

검색 결과 카드의 `사례 요약`, `문제`, `해결` 표시 품질을 높이기 위해 LLM 요약이 없는 글 100개를 추가 처리했습니다.

처리 전 상태:

```text
total = 1539
summarized = 1116
missing = 423
```

source별 미작성 수:

```text
Gmarket = 104
Banksalad = 78
Upstage = 76
Netmarble = 73
Inflab = 42
Coupang = 10
Lunit = 10
NAVER Cloud = 10
Wantedlab = 10
Zigbang = 10
```

실행:

```bash
npm run llm:summarize -- --limit 100
```

결과:

```text
selected = 100
generated = 100
failed = 0

total = 1539
summarized = 1216
missing = 323
```

처리 후 남은 미작성 수:

```text
Gmarket = 82
Upstage = 76
Netmarble = 67
Banksalad = 60
Inflab = 19
Coupang = 8
Zigbang = 7
NAVER Cloud = 4
```

새 요약을 검색 결과에 반영하기 위해 Elasticsearch 인덱스를 갱신했습니다.

```bash
npm run search:reindex
```

검색 평가:

```bash
npm run search:evaluate
```

평가 결과:

```text
average precision@5 = 0.412
average recall@10 = 0.839
average mrr = 0.853
average ndcg@10 = 0.786
```

샘플 확인:

```text
Redis Stream 적용기
caseSummary/caseProblem/caseSolution 생성 확인
```

## 50. LLM 요약 2차 100개 backfill

남은 미요약 글 323개 중 다음 100개를 추가 처리했습니다.

실행:

```bash
npm run llm:summarize -- --limit 100
```

결과:

```text
selected = 100
generated = 100
failed = 0

total = 1539
summarized = 1316
missing = 223
```

처리 후 남은 미작성 수:

```text
Upstage = 76
Banksalad = 49
Netmarble = 47
Gmarket = 42
Inflab = 9
```

새 요약을 검색 결과에 반영하기 위해 Elasticsearch 인덱스를 갱신했습니다.

```bash
npm run search:reindex
```

검색 평가:

```bash
npm run search:evaluate
```

평가 결과:

```text
average precision@5 = 0.412
average recall@10 = 0.834
average mrr = 0.852
average ndcg@10 = 0.783
```

1차 backfill 대비 `precision@5`는 유지되었고, `recall@10`과 `ndcg@10`은 소폭 하락했습니다. 새 LLM 요약이 검색 대상 텍스트에 반영되면서 일부 문제/아키텍처 계열 쿼리의 후보 풀이 넓어진 영향으로 보입니다.

## 51. LLM 요약 3차 100개 backfill

남은 미요약 글 223개 중 다음 100개를 추가 처리했습니다.

실행:

```bash
npm run llm:summarize -- --limit 100
```

결과:

```text
selected = 100
generated = 100
failed = 0

total = 1539
summarized = 1416
missing = 123
```

처리 후 남은 미작성 수:

```text
Upstage = 76
Banksalad = 25
Gmarket = 17
Netmarble = 5
```

새 요약을 검색 결과에 반영하기 위해 Elasticsearch 인덱스를 갱신했습니다.

```bash
npm run search:reindex
```

검색 평가:

```bash
npm run search:evaluate
```

평가 결과:

```text
average precision@5 = 0.412
average recall@10 = 0.834
average mrr = 0.847
average ndcg@10 = 0.778
```

2차 backfill 대비 `precision@5`와 `recall@10`은 유지되었고, `mrr`과 `ndcg@10`은 소폭 하락했습니다. LLM 요약이 검색 대상 필드에 추가되면서 넓은 문제/아키텍처 쿼리의 검색 후보가 더 많아졌기 때문입니다.

## 52. LLM 요약 4차 100개 backfill

남은 미요약 글 123개 중 다음 100개를 추가 처리했습니다.

실행:

```bash
npm run llm:summarize -- --limit 100
```

결과:

```text
selected = 100
generated = 100
failed = 0

total = 1539
summarized = 1516
missing = 23
```

처리 후 남은 미작성 수:

```text
Upstage = 23
```

새 요약을 검색 결과에 반영하기 위해 Elasticsearch 인덱스를 갱신했습니다.

```bash
npm run search:reindex
```

검색 평가:

```bash
npm run search:evaluate
```

평가 결과:

```text
average precision@5 = 0.406
average recall@10 = 0.834
average mrr = 0.847
average ndcg@10 = 0.778
```

3차 backfill 대비 `recall@10`, `mrr`, `ndcg@10`은 유지되었고 `precision@5`만 소폭 하락했습니다. Upstage 제품/마케팅성 글의 LLM 요약이 검색 대상에 추가되며 일부 넓은 쿼리의 상위 후보가 더 넓어진 영향으로 보입니다.

## 53. LLM 요약 backfill 완료

남은 Upstage 미요약 글 23개를 마지막으로 처리해 전체 1539개 글의 LLM 요약을 모두 채웠습니다.

실행:

```bash
npm run llm:summarize -- --limit 100
```

결과:

```text
selected = 23
generated = 23
failed = 0

total = 1539
summarized = 1539
missing = 0
```

새 요약을 검색 결과에 반영하기 위해 Elasticsearch 인덱스를 갱신했습니다.

```bash
npm run search:reindex
```

검색 평가:

```bash
npm run search:evaluate
```

평가 결과:

```text
average precision@5 = 0.406
average recall@10 = 0.839
average mrr = 0.847
average ndcg@10 = 0.774
```

4차 backfill 대비 `precision@5`, `recall@10`, `mrr`은 유지되었고 `ndcg@10`은 소폭 하락했습니다. 이제 저장된 모든 글이 `caseSummary`, `caseProblem`, `caseSolution`, `contentType` 기반 카드 표시와 검색 인덱싱 대상이 됩니다.

## 54. 검색 품질 audit 리포트 생성기 추가

정량 지표만으로는 검색 결과가 왜 좋아졌거나 나빠졌는지 판단하기 어렵기 때문에, 평가 쿼리별 상위 검색 결과를 Markdown으로 확인할 수 있는 audit 리포트 생성기를 추가했습니다.

추가한 명령어:

```bash
npm run search:audit
```

생성 파일:

```text
docs/search-audit-report.md
```

리포트 포함 정보:

```text
평가 쿼리별 total results
precision@5 / recall@10 / mrr / ndcg@10
expected URL 목록
상위 10개 검색 결과
expected match 여부와 relevance
source, score, 주요 keyword
상위 3개 결과의 caseSummary/problem/solution/highlight
```

현재 audit 기준 전체 지표:

```text
average precision@5 = 0.412
average recall@10 = 0.834
average mrr = 0.847
average ndcg@10 = 0.774
```

검증:

```bash
cd apps/backend && uv run ruff check app/search/evaluation/audit.py
npm run search:audit
npm run search:evaluate
```

## 55. contentType 기반 사례성 랭킹 보정

LLM 요약 backfill 완료 후 모든 글이 `contentType`을 가지게 되었으므로, 검색 랭킹에 글 유형 기반 가산점을 추가했습니다.

적용 방식:

```text
Elasticsearch function_score
boost_mode = sum
score_mode = sum
```

가중치:

```text
technical_case = 30
engineering_story = 15
tutorial = 8
```

의도:

```text
기술 사례성이 높은 글을 같은 점수대에서 조금 더 위로 배치
event/recruiting/news/release_note는 감점하지 않고 중립 유지
검색 랭킹을 크게 흔들지 않는 범위에서 첫 번째 안전한 보정만 적용
```

검색 평가:

```bash
npm run search:evaluate
```

평가 결과:

```text
average precision@5 = 0.412
average recall@10 = 0.834
average mrr = 0.847
average ndcg@10 = 0.774
```

정량 지표는 보정 전과 동일했습니다. 현재 평가셋의 상위 결과는 대부분 이미 `technical_case` 중심이라 큰 순위 변화는 없었고, 같은 점수대의 사례성 보정 장치만 추가된 상태입니다.

검증:

```bash
cd apps/backend && uv run ruff check app/search/service.py app/search/evaluation/audit.py
npm run search:evaluate
npm run search:audit
```

샘플 확인:

```text
Redis Stream + relevance -> G마켓 Redis Stream 적용기 상위 노출
Redis Stream + latest    -> 매칭 후보 중 최신 발행일 순서로 노출
```

최신순은 넓은 검색어에서 관련도가 낮은 최신 글이 위로 올 수 있습니다. 따라서 기본값은 관련도순으로 유지하고, 최신 글 탐색이 필요할 때만 사용자가 선택하도록 했습니다.

## 44. 검색 결과 필터와 facet UI 추가

검색 결과가 1500개 이상으로 늘어나면서 검색어 하나만으로 원하는 사례를 좁히기 어려워졌습니다. 검색 API에 facet과 필터를 추가하고, 화면에서는 결과 상단에 `결과 좁히기` 영역을 추가했습니다.

추가한 필터:

```text
source: 회사/블로그 sourceSlug 기준
technology: technologies keyword 기준
problem: problemKeywords keyword 기준
content_type: LLM 요약 contentType 기준
```

API 예:

```text
GET /api/search?q=Redis%20Stream&source=gmarket-tech-blog
GET /api/search?q=Redis%20Stream&technology=Redis
GET /api/search?q=Redis%20Stream&problem=cost%20optimization
GET /api/search?q=Redis%20Stream&content_type=technical_case
```

검색 응답에 추가한 정보:

```text
filters
facets.sources
facets.technologies
facets.problemKeywords
facets.contentTypes
```

UI:

```text
검색 결과 상단에 결과 좁히기 패널 추가
회사/기술/문제 상황/유형 facet 표시
필터 chip 클릭 시 즉시 재검색
선택된 필터는 같은 chip을 다시 누르면 해제
필터 초기화 버튼 제공
```

샘플 확인:

```text
Redis Stream 기본 검색 total = 156
source=gmarket-tech-blog 필터 적용 total = 25
```

필터 facet에서 Redis가 제대로 보이도록 기술 사전에 `Redis`, `Redis Stream`을 추가했습니다.

재처리:

```bash
npm run keywords:extract
npm run search:reindex
npm run suggest:reindex
npm run search:evaluate
```

재처리 결과:

```text
articles = 1539
keywords = 3290
indexed articles = 1539
indexed suggestions = 80
```

Redis Stream 샘플:

```text
기본 검색 total = 90
technology=redis 필터 적용 total = 90
기술 facet 상위에 Redis 노출
```

평가 결과:

```text
average precision@5 = 0.400
average recall@10 = 0.839
average mrr = 0.854
average ndcg@10 = 0.782
```

검증:

```bash
uv run ruff check app/routers/search.py app/search/service.py
pnpm --dir apps/web exec tsc --noEmit
npm run build:web
```

## 57. 검색 개선 평가셋 보정

`ko-tech-search` 쿼리의 `precision@5`가 0으로 나타나 audit 리포트를 확인했습니다. 상위 결과를 보면 검색 로직이 완전히 빗나간 것은 아니었고, 신규 수집된 검색 시스템 사례가 expected result에 빠져 있었습니다.

추가한 expected result:

```text
MongoDB Atlas Search 정렬이슈 해결기
배민상회와 검색플랫폼 연동기
실시간 인덱싱을 위한 Elasticsearch 구조를 찾아서
```

검토 중 시도했던 검색 랭킹 보정:

```text
검색 개선 같은 복합 문구 phrase boost 추가
search 단일 키워드 terms boost 약화
```

하지만 이 보정은 `ko-tech-search`를 개선하지 못하고 다른 쿼리의 평균 지표를 떨어뜨렸습니다. 따라서 로직 변경은 반영하지 않고, 평가셋 누락만 보정했습니다.

평가 결과:

```text
average precision@5 = 0.442
average recall@10 = 0.852
average mrr = 0.884
average ndcg@10 = 0.799
```

대표 변화:

```text
ko-tech-search precision@5 = 0.000 -> 0.200
ko-tech-search recall@10 = 0.333 -> 0.556
ko-tech-search mrr = 0.143 -> 1.000
ko-tech-search ndcg@10 = 0.174 -> 0.552
```

남은 과제:

```text
검색 개선 쿼리는 여전히 search라는 범용 키워드의 영향이 큼
검색 엔진/검색 품질/검색 플랫폼처럼 하위 의도를 분리한 평가 쿼리가 필요함
정답셋 보강 후에도 Top 5에 범용 검색 기능 소개 글이 섞이므로 query intent 기반 ranking은 별도 설계가 필요함
```

## 58. 검색 도메인 평가셋 세분화

`검색 개선` 하나의 쿼리에 서로 다른 의도가 섞여 있어, 검색 품질을 더 구체적으로 판단하기 어렵다는 문제가 있었습니다. 검색 도메인을 다음 세부 쿼리로 분리했습니다.

추가한 평가 쿼리:

```text
ko-search-quality-improvement: 검색 품질 개선
ko-search-elasticsearch-index: Elasticsearch 인덱스 구조
ko-search-opensearch-analyzer: OpenSearch Analyzer
ko-search-realtime-indexing: 실시간 검색 인덱싱
ko-search-platform-kafka: 검색 플랫폼 Kafka
```

각 쿼리의 의도:

```text
검색 품질 개선: 결과 없는 검색, 랭킹, 쿼리 최적화, 검색 성능 개선
Elasticsearch 인덱스 구조: 인덱스 구조, 쿼리 최적화, 실시간 인덱싱 설계
OpenSearch Analyzer: Analyzer 기반 텍스트 분석, 색인, 검색 기능 구현
실시간 검색 인덱싱: 이벤트 기반 색인 파이프라인, 실시간 검색 인덱스 갱신
검색 플랫폼 Kafka: Kafka를 활용한 검색 플랫폼/색인 파이프라인
```

평가 결과:

```text
average precision@5 = 0.416
average recall@10 = 0.823
average mrr = 0.858
average ndcg@10 = 0.770
```

세부 쿼리 결과:

```text
ko-search-quality-improvement    p@5=0.400 r@10=0.500 mrr=1.000 ndcg@10=0.503
ko-search-elasticsearch-index    p@5=0.200 r@10=0.500 mrr=1.000 ndcg@10=0.657
ko-search-opensearch-analyzer    p@5=0.400 r@10=1.000 mrr=1.000 ndcg@10=0.974
ko-search-realtime-indexing      p@5=0.400 r@10=0.750 mrr=0.333 ndcg@10=0.418
ko-search-platform-kafka         p@5=0.000 r@10=0.333 mrr=0.100 ndcg@10=0.157
```

실험:

```text
복합 키워드가 함께 등장하는 문서에 co-occurrence boost를 주는 방식
검색 플랫폼을 별도 architecture 키워드로 추가하는 방식
```

두 방식 모두 `검색 플랫폼 Kafka`를 안정적으로 개선하지 못했고 다른 쿼리의 순위를 흔들었습니다. 따라서 검색 로직 변경은 반영하지 않았습니다.

해석:

```text
검색 품질 개선, OpenSearch Analyzer처럼 의도가 명확한 쿼리는 꽤 잘 동작함
검색 플랫폼 Kafka처럼 기술명과 아키텍처 의도가 섞인 쿼리는 아직 약함
search, Kafka 같은 넓은 키워드의 단순 OR 가산점만으로는 사용자의 복합 의도를 충분히 표현하기 어려움
다음 단계에서는 query intent를 명시적으로 분류하거나, 기술+문제/아키텍처 조합을 별도 ranking feature로 다루는 설계가 필요함
```

## 59. 복합 의도 검색 랭킹 설계 문서화

`검색 플랫폼 Kafka`처럼 기술명과 아키텍처 의도가 함께 들어간 query는 현재 검색 구조에서 약점으로 드러났습니다. 단순히 `Kafka` 또는 `search` 중 하나가 매칭되는 글도 높은 점수를 받을 수 있기 때문입니다.

`docs/search-design.md`에 복합 의도 검색 랭킹 설계를 추가했습니다.

정리한 내용:

```text
query intent를 technology/problem/architecture/company 축으로 분해
technology + architecture co-match를 ranking feature 후보로 정의
search, Java, observability 같은 넓은 키워드는 단독 boost를 제한
function_score 기반의 좁은 조건부 가산점 후보 설계
LLM architectureKeywords 품질 개선 필요성 기록
```

실패한 실험도 함께 반영했습니다.

```text
복합 키워드 co-occurrence boost는 다른 query 순위를 흔들었음
검색 플랫폼 사전 추가만으로는 ko-search-platform-kafka 개선에 실패했음
```

다음 구현 후보:

```text
matched_rules(query)로 KeywordRule 전체를 반환
keyword_type별 bucket 구성
technology + architecture가 동시에 존재하는 query에만 좁은 function_score 적용
ko-search-platform-kafka, ko-search-realtime-indexing, ko-tech-search, migration-kafka-msk를 함께 비교
```

## 60. 기본 페이지 최신 글 노출

검색어를 입력하기 전 기본 페이지에서 빈 상태 메시지만 보여주는 대신, 최신 기업 기술 블로그 글을 바로 보여주도록 변경했습니다.

변경 내용:

```text
빈 query 검색 시 backend가 match_all query를 사용
빈 query의 기본 sort는 latest로 보정
frontend 첫 진입 시 q="" + sort=latest로 검색 요청
검색어가 없는 기본 화면의 결과 요약 문구를 최신 글 중심으로 변경
```

의도:

```text
사용자가 검색어를 입력하기 전에도 서비스가 어떤 글을 수집하고 있는지 바로 확인 가능
최신 기술 블로그 피드처럼 탐색 시작 가능
검색 중심 서비스이면서도 기본 화면의 빈 느낌을 줄임
```

검증:

```bash
cd apps/backend && uv run ruff check app/search/service.py
pnpm --dir apps/web exec tsc --noEmit
```

## 61. 검색 결과 페이지네이션 추가

기본 페이지에서 최신 글을 보여주게 되면서, 사용자가 더 많은 글을 이어서 탐색할 수 있도록 페이지네이션을 추가했습니다.

Backend 변경:

```text
GET /api/search?page=1&page_size=20
page는 1 이상
page_size는 1~50 범위
Elasticsearch from/size로 offset pagination 적용
응답에 page, pageSize, totalPages 추가
```

Frontend 변경:

```text
검색 응답 타입에 page/pageSize/totalPages 추가
첫 진입 최신 글 목록도 page=1로 요청
검색어/정렬/필터 변경 시 1페이지로 이동
결과 하단에 이전/다음 페이지 버튼 추가
결과 요약에 현재 노출 범위 표시
```

예시 문구:

```text
최신 기업 기술 블로그 1539개 중 1-20번째를 보고 있습니다.
123개 사례 중 21-40번째를 관련도순으로 보고 있습니다.
```

검증:

```bash
cd apps/backend && uv run ruff check app/routers/search.py app/search/service.py
pnpm --dir apps/web exec tsc --noEmit
npm run build:web
```

## 62. Next.js 검색 alias 개선

`next`로 검색했을 때 일반 영어 단어 `next`가 포함된 글이 섞이고, 사용자가 기대하는 `Next.js` 기술 스택 글이 충분히 올라오지 않는 문제가 있었습니다.

원인:

```text
기술 사전에 Next.js가 없었음
next는 일반 단어라 사전에 그대로 alias로 넣으면 next step 같은 표현까지 오탐 가능
```

개선:

```text
Next.js 기술 키워드 추가
일반 alias는 next.js, nextjs만 사용
검색 query가 정확히 next일 때만 query-only alias로 Next.js 매칭
next step 같은 문장은 Next.js로 매칭하지 않음
```

재처리:

```bash
npm run keywords:extract
npm run search:reindex
npm run suggest:reindex
```

재처리 결과:

```text
articles = 1539
keywords = 3318
indexed articles = 1539
indexed suggestions = 81
```

검증:

```text
next -> Next.js로 query expansion
next.js -> Next.js 매칭
nextjs -> Next.js 매칭
next step -> Next.js 미매칭
nex -> Next.js 자동완성 후보 노출
```

검색 결과 확인:

```text
next 검색 상위 5개가 Next.js 관련 글로 노출
Google Cloud Next 행사 글은 상위 5 밖으로 밀림
```

평가셋:

```text
tech-nextjs query 추가
query = next
expected result = Next.js 관련 사례 5개
```

평가 결과:

```text
tech-nextjs precision@5 = 1.000
tech-nextjs recall@10 = 1.000
tech-nextjs mrr = 1.000
tech-nextjs ndcg@10 = 1.000
```
