# TechCase 개발 계획

이 문서는 TechCase의 MVP 개발을 위한 기술 스택, 레포지토리 구조, 아키텍처, 로컬 개발 계획, AWS 인프라 구성을 정리합니다.

README는 서비스 설명에 집중하고, 구현과 운영에 가까운 내용은 이 문서에서 관리합니다.

## MVP 범위

첫 번째 MVP는 AWS 기술 블로그를 대상으로 검색 경험을 검증하는 데 집중합니다.

MVP 목표는 다음과 같습니다.

1. AWS 기술 블로그 RSS 피드에서 글을 수집합니다.
2. 수집한 글의 출처, 제목, URL, 발행일, 요약, 본문 텍스트를 PostgreSQL에 저장합니다.
3. 검색에 필요한 문서를 Elasticsearch에 색인합니다.
4. 기술명, AWS 서비스명, 문제 상황, 아키텍처 키워드로 검색할 수 있는 API를 제공합니다.
5. 검색 결과를 확인할 수 있는 간단한 웹 UI를 만듭니다.
6. 검색 결과에서 제목, 출처, 발행일, 요약, 관련 키워드를 보여줍니다.

MVP의 핵심 검증 질문은 다음과 같습니다.

- AWS 기술 블로그만으로도 의미 있는 기술 사례 검색 경험이 만들어지는가?
- `Lambda`, `EKS`, `DynamoDB`, `Kinesis`, `EventBridge` 같은 서비스명 검색이 잘 동작하는가?
- `event-driven`, `cost optimization`, `high availability`, `migration` 같은 문제/아키텍처 키워드 검색이 유효한가?
- 제목만 검색하는 것보다 본문, 요약, 태그까지 함께 검색했을 때 결과 품질이 좋아지는가?
- 검색 결과 카드만 보고도 글을 읽을 가치가 있는지 판단할 수 있는가?

## 초기 데이터 소스

초기 데이터 소스는 AWS 기술 블로그를 사용합니다. AWS 블로그는 신뢰도가 높고, 기술 사례가 많으며, RSS 기반 수집이 가능하다는 장점이 있습니다.

초기 후보는 다음과 같습니다.

- AWS Architecture Blog
- AWS Database Blog
- AWS Compute Blog
- AWS Big Data Blog
- AWS DevOps Blog
- AWS Machine Learning Blog
- AWS Security Blog
- AWS News Blog

다만 AWS News Blog는 제품 출시나 업데이트 성격의 글이 많을 수 있으므로, 검색 품질 검증 초기에는 Architecture, Database, Compute, Big Data, DevOps 블로그를 우선적으로 보는 것이 좋습니다.

## 기술 스택과 선택 이유

이 프로젝트는 Python에 익숙한 개발자가 빠르게 구현하고, 이후 텍스트 처리와 AI 기반 기능까지 확장하기 좋은 스택을 선택합니다.

### 프론트엔드

- Next.js
- TypeScript
- Tailwind CSS

Next.js는 React 기반 웹 프레임워크입니다. TechCase는 공개 검색 서비스이므로 기술별 페이지, 회사별 페이지, 글 상세 페이지가 검색엔진에 노출될 가능성이 있습니다. 따라서 단순 React SPA보다 라우팅, 서버 렌더링, 메타데이터 관리, SEO 측면에서 유리한 Next.js를 사용합니다.

초기에는 AWS 비용을 줄이기 위해 Next.js를 정적 자원 중심으로 배포합니다. 홈, 서비스 소개, 주요 기술 페이지처럼 변경 빈도가 낮고 SEO가 필요한 화면은 정적으로 생성하고, 검색 결과처럼 사용자 입력에 따라 바뀌는 화면은 브라우저에서 FastAPI 검색 API를 호출하는 방식으로 처리합니다.

이 선택의 장점은 다음과 같습니다.

- S3와 CloudFront만으로 웹을 배포할 수 있어 서버 운영 비용이 낮습니다.
- Next.js를 사용하므로 이후 SSR이나 ISR이 필요해졌을 때 전환 여지가 있습니다.
- 검색 UI는 정적 배포로 충분히 제공할 수 있습니다.
- 기술별/회사별 페이지를 나중에 정적 생성하면 SEO도 점진적으로 강화할 수 있습니다.

### 백엔드 API

- FastAPI
- Pydantic
- SQLAlchemy 또는 SQLModel
- Alembic

FastAPI는 Python 타입 힌트를 기반으로 빠르게 API를 만들 수 있고, OpenAPI 문서도 자동으로 생성됩니다. TechCase는 RSS 수집, HTML 파싱, 텍스트 처리, 검색 색인, 이후 AI 요약/키워드 추출 가능성이 있으므로 Python 생태계와 잘 맞습니다.

초기에는 FastAPI 서버를 private subnet의 EC2 한 대에서 실행합니다. API 서버를 Lambda, App Runner, ECS로 분리할 수도 있지만, Elasticsearch를 같은 EC2에서 직접 운영하기로 했기 때문에 초기에는 백엔드 실행 환경을 한곳에 모으는 편이 단순합니다. 외부 사용자는 public ALB를 통해 FastAPI에 접근하고, EC2 자체는 public IP를 가지지 않습니다.

이 선택의 장점은 다음과 같습니다.

- FastAPI와 crawler가 같은 Python 코드베이스와 의존성을 공유할 수 있습니다.
- Elasticsearch가 같은 EC2 내부에 있으면 네트워크 구성이 단순합니다.
- Lambda의 VPC, NAT Gateway, cold start, ASGI adapter 같은 초기 복잡도를 피할 수 있습니다.
- App Runner나 ECS처럼 상시 컨테이너 인프라를 추가로 관리하지 않아도 됩니다.
- 비용을 예측하기 쉽습니다. EC2, ALB, NAT Instance, RDS 비용을 중심으로 관리하면 됩니다.

### 크롤러

- Python
- feedparser
- BeautifulSoup
- readability-lxml
- httpx

크롤러는 RSS 피드를 읽고, 글 메타데이터를 정규화하고, 원문 본문을 추출한 뒤 PostgreSQL에 저장하고 Elasticsearch에 색인하는 역할을 합니다.

초기에는 크롤러를 별도 서버로 분리하지 않고, private EC2 내부에서 cron 또는 systemd timer로 실행합니다. EventBridge, Lambda, ECS Scheduled Task를 사용할 수도 있지만, crawler가 외부 RSS 피드에 접근하고 RDS와 Elasticsearch에 동시에 접근해야 하므로 초기에는 EC2 내부 작업으로 두는 것이 네트워크와 비용 면에서 단순합니다. private EC2의 outbound 인터넷 접근은 NAT Gateway 대신 NAT Instance를 통해 처리합니다.

이 선택의 장점은 다음과 같습니다.

- NAT Gateway 없이 NAT Instance를 통해 외부 RSS 피드에 접근할 수 있습니다.
- Elasticsearch가 같은 서버에 있어 색인 작업이 단순합니다.
- crawler와 API가 같은 backend 패키지 안에서 데이터 모델과 유틸리티를 공유할 수 있습니다.
- 작업 실패 로그를 EC2와 CloudWatch Agent 중심으로 단순하게 확인할 수 있습니다.
- 나중에 수집량이 늘어나면 `apps/crawler`와 ECS Scheduled Task로 분리하기 쉽습니다.

### 데이터베이스

- PostgreSQL

PostgreSQL은 수집된 원본 데이터의 기준 저장소 역할을 합니다. 글, 출처, 수집 이력, 추출된 메타데이터, 키워드 관계 등을 저장합니다.

MySQL 대신 PostgreSQL을 선택한 이유는 다음과 같습니다.

- 텍스트 검색 기능이 강합니다.
- JSONB 지원이 좋아 RSS 원본 메타데이터나 추출 결과 같은 반정형 데이터를 다루기 좋습니다.
- 복잡한 인덱싱과 쿼리 확장성이 좋습니다.
- 나중에 pgvector를 사용해 임베딩 기반 검색을 실험하기 쉽습니다.
- AWS에서 RDS로 운영하기 좋습니다.

초기 인프라에서는 PostgreSQL을 EC2에 직접 설치하지 않고 Amazon RDS for PostgreSQL을 사용합니다.

이 선택의 장점은 다음과 같습니다.

- 검색 엔진과 API는 실험적으로 EC2에 올리더라도, 원본 데이터 저장소는 안정적으로 분리할 수 있습니다.
- 자동 백업, 스냅샷, 모니터링 같은 기본 운영 기능을 활용할 수 있습니다.
- EC2 장애나 Elasticsearch 재설치가 발생해도 원본 article 데이터는 보존됩니다.
- 나중에 API 서버나 crawler를 분리해도 동일한 RDS를 기준 저장소로 사용할 수 있습니다.

초기 설정은 비용을 줄이기 위해 Single-AZ, 작은 인스턴스, 최소 스토리지로 시작합니다. Multi-AZ, read replica, 고성능 인스턴스는 검색 트래픽과 수집량이 늘어난 뒤 검토합니다.

### 검색 엔진

- Elasticsearch

Elasticsearch는 TechCase의 핵심 검색 경험을 담당합니다. analyzer, mapping, field boosting, highlighting, synonym 등을 실험할 수 있어 기술명, 문제 상황, 아키텍처 키워드 기반 검색 품질을 개선하기 좋습니다.

초기에는 Amazon OpenSearch Service 같은 관리형 검색 서비스를 사용하지 않고, EC2에 Elasticsearch 단일 노드를 직접 설치합니다.

이 선택의 장점은 다음과 같습니다.

- 현재 Elasticsearch를 직접 공부하는 목적과 서비스 구현 목적이 잘 맞습니다.
- 관리형 OpenSearch보다 초기 비용을 낮출 수 있습니다.
- index mapping, analyzer, heap, disk, snapshot 같은 검색 엔진 운영 요소를 직접 경험할 수 있습니다.
- TechCase의 차별점인 검색 품질 실험을 MVP부터 수행할 수 있습니다.
- PostgreSQL만으로 시작했을 때 생기는 검색 랭킹, 하이라이팅, 동의어, analyzer 실험 한계를 줄일 수 있습니다.

다만 Elasticsearch는 메모리와 디스크 사용량이 크기 때문에 `t3.micro` 같은 매우 작은 인스턴스에는 적합하지 않을 수 있습니다. 초기에는 `t3.small` 또는 `t3.medium` 수준을 검토하고, Kibana는 비용과 메모리 사용량을 고려해 필요할 때만 실행하는 방향을 우선합니다.

## 모노레포 구조

초기에는 하나의 public repository에서 전체 코드를 관리하는 모노레포로 시작합니다.

예상 구조는 다음과 같습니다.

```text
techcase/
  apps/
    web/              # Next.js 프론트엔드
    backend/          # FastAPI API와 초기 크롤러 코드
  packages/
    shared/           # 공통 키워드 사전, AWS 서비스 사전, 프로젝트 상수
  infra/
    docker-compose.yml
    terraform/
    elasticsearch/
    postgres/
  docs/
    development.md
```

레포는 하나로 관리하지만 배포 단위는 분리합니다.

- `apps/web`: 사용자에게 노출되는 웹 애플리케이션
- `apps/backend`: 검색 API 서버
- crawler job: backend 코드 안의 별도 명령 또는 스케줄 작업
- PostgreSQL: 로컬 Docker 또는 관리형 DB
- Elasticsearch: 로컬 Docker 또는 관리형 Elasticsearch
- Terraform: AWS 인프라 관리

크롤러가 커지면 이후 `apps/crawler`로 분리할 수 있습니다.

## 초기 AWS 인프라 구성

초기 구성은 AWS 자원을 사용하되 비용과 운영 복잡도를 최소화하는 것을 목표로 합니다.

결정된 초기 구성은 다음과 같습니다.

- Web: S3 + CloudFront
- Load Balancer: public subnet의 Application Load Balancer
- Backend API: private subnet의 EC2에서 FastAPI 실행
- Crawler: private EC2 내부 cron 또는 systemd timer
- Search: private EC2 내부 Elasticsearch 단일 노드
- Database: Amazon RDS for PostgreSQL
- Outbound internet: public subnet의 NAT Instance
- Access: AWS Systems Manager Session Manager
- Reverse proxy: Nginx, 선택 사항
- Logs/Monitoring: CloudWatch Agent, 선택
- IaC: Terraform

전체 구조는 다음과 같습니다.

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

## 인프라 선택 이유

### S3 + CloudFront

Next.js 웹 애플리케이션은 초기에는 정적 사이트로 배포합니다. 검색 결과는 API를 통해 동적으로 가져오고, 정적 배포가 가능한 화면은 S3에 업로드한 뒤 CloudFront로 제공합니다.

이 방식을 선택한 이유는 다음과 같습니다.

- 상시 웹 서버가 필요 없어 비용이 낮습니다.
- CloudFront를 통해 전 세계 캐싱과 HTTPS 구성이 가능합니다.
- AWS 기반 배포 경험을 가져가면서도 Amplify나 SSR 서버 비용을 피할 수 있습니다.
- 나중에 SSR/ISR이 꼭 필요해질 때 Amplify, ECS, Lambda 기반 Next.js 배포로 확장할 수 있습니다.

초기 한계도 있습니다.

- 검색 결과 페이지 자체를 서버에서 렌더링하지 않기 때문에 검색 결과 조합 페이지의 SEO는 약합니다.
- 정적 생성된 페이지는 데이터 변경 시 다시 빌드해야 합니다.
- ISR은 단순 S3 정적 배포만으로는 사용하기 어렵습니다.

초기에는 검색 품질 검증이 우선이므로 이 한계를 수용합니다. SEO는 홈, 서비스 소개, 기술별 대표 페이지처럼 정적으로 만들 수 있는 페이지부터 강화합니다.

### Application Load Balancer

ALB는 public subnet에 배치하고, 사용자 요청을 private EC2의 FastAPI 서버로 전달합니다.

이 방식을 선택한 이유는 다음과 같습니다.

- EC2를 public internet에 직접 노출하지 않을 수 있습니다.
- HTTPS 인증서 연결과 HTTP to HTTPS 리다이렉션을 ALB에서 처리할 수 있습니다.
- 이후 EC2를 여러 대로 늘리거나 API 서버를 분리할 때 확장 경로가 자연스럽습니다.
- FastAPI만 외부에 노출하고 Elasticsearch와 Kibana는 외부 접근을 차단할 수 있습니다.

ALB는 비용이 발생합니다. MVP에서는 트래픽이 작더라도 실행 시간 기준 비용과 LCU 비용이 발생하므로, 보안 이점을 위해 감수하는 고정 비용으로 봅니다.

### EC2

EC2는 private subnet에 두고 FastAPI, crawler, Elasticsearch를 함께 실행하는 초기 백엔드 서버로 사용합니다.

이 방식을 선택한 이유는 다음과 같습니다.

- Elasticsearch를 직접 설치하고 운영하며 학습할 수 있습니다.
- API, crawler, Elasticsearch 사이의 네트워크 구성이 단순합니다.
- EC2에 public IP를 부여하지 않아 Elasticsearch와 Kibana 노출 위험을 줄일 수 있습니다.
- Lambda를 VPC에 넣고 NAT Gateway를 붙이는 구성을 피할 수 있습니다.
- App Runner, ECS, OpenSearch Service를 동시에 도입하는 것보다 초기 인프라가 단순합니다.
- 서버 한 대에 백엔드 역할을 모아 비용과 운영 대상을 줄일 수 있습니다.

초기 EC2에서 실행할 프로세스는 다음과 같습니다.

- FastAPI server
- Elasticsearch
- crawler cron job
- Nginx, 선택
- Kibana, 필요할 때만 실행

단점도 있습니다.

- 서버 한 대에 역할이 몰립니다.
- EC2 패치, 디스크 관리, Elasticsearch 보안 설정을 직접 챙겨야 합니다.
- Elasticsearch 장애가 API 서버 리소스에 영향을 줄 수 있습니다.
- private subnet에 있으므로 outbound 인터넷 접근에는 NAT Instance가 필요합니다.
- 트래픽이나 데이터가 늘어나면 역할 분리가 필요합니다.

초기에는 학습과 비용 절감을 위해 이 단순한 구성을 선택하고, 운영 부담이 커지면 crawler, API, Elasticsearch를 순서대로 분리합니다.

### NAT Instance

NAT Instance는 private subnet의 EC2가 외부 인터넷에 접근하기 위한 통로로 사용합니다. TechCase crawler는 AWS RSS 피드와 원문 HTML을 가져와야 하므로 outbound 인터넷 접근이 필요합니다.

NAT Gateway 대신 NAT Instance를 선택한 이유는 다음과 같습니다.

- NAT Gateway보다 비용을 낮출 수 있습니다.
- 초기 crawler 트래픽은 크지 않을 것으로 예상됩니다.
- AWS 네트워크 라우팅, 보안 그룹, source/destination check 같은 개념을 직접 학습할 수 있습니다.
- private EC2 구조를 유지하면서도 crawler의 인터넷 접근을 제공할 수 있습니다.

NAT Instance 사용 시 챙겨야 할 항목은 다음과 같습니다.

- public subnet에 배치합니다.
- Elastic IP를 연결합니다.
- source/destination check를 비활성화합니다.
- private subnet route table의 `0.0.0.0/0`을 NAT Instance로 라우팅합니다.
- NAT Instance 보안 그룹은 private EC2의 outbound 트래픽을 허용합니다.
- OS 패치와 장애 대응은 직접 관리합니다.

NAT Instance는 비용을 줄이는 대신 운영 책임이 생깁니다. 서비스가 안정적으로 운영될 가치가 커지거나 NAT 장애가 부담스러워지면 NAT Gateway로 전환합니다.

### RDS PostgreSQL

PostgreSQL은 EC2에 직접 설치하지 않고 private subnet의 RDS를 사용합니다.

이 방식을 선택한 이유는 다음과 같습니다.

- 원본 article 데이터는 검색 엔진보다 더 안정적으로 보존되어야 합니다.
- EC2에 문제가 생겨도 RDS에 저장된 원본 데이터는 유지됩니다.
- 자동 백업과 스냅샷을 사용할 수 있습니다.
- 나중에 백엔드 서버를 여러 개로 분리해도 동일한 데이터베이스를 기준으로 사용할 수 있습니다.

초기 비용을 줄이기 위해 다음 기준으로 시작합니다.

- Single-AZ
- 작은 인스턴스 클래스
- 최소 gp3 스토리지
- 자동 백업은 짧은 보존 기간으로 활성화
- Multi-AZ와 read replica는 사용하지 않음

### Elasticsearch on EC2

Elasticsearch는 관리형 OpenSearch Service 대신 private EC2에 직접 설치합니다.

이 방식을 선택한 이유는 다음과 같습니다.

- TechCase의 핵심 경쟁력이 검색 품질이므로 MVP부터 검색 엔진을 직접 다룹니다.
- 현재 Elasticsearch를 공부하고 있기 때문에 프로젝트 학습 목표와 잘 맞습니다.
- OpenSearch가 아니라 Elasticsearch 자체의 mapping, analyzer, query DSL, scoring, highlighting을 경험할 수 있습니다.
- 관리형 OpenSearch Service보다 비용을 낮출 수 있습니다.

초기에는 단일 노드로 시작합니다.

- index: `articles`
- shard/replica는 소규모 데이터 기준으로 단순하게 설정
- snapshot은 추후 S3 저장소로 확장
- Kibana는 항상 켜두지 않고 필요할 때만 실행하는 방향을 우선 검토

주의할 점은 다음과 같습니다.

- Elasticsearch는 외부에 공개하지 않습니다.
- FastAPI와 crawler만 localhost 또는 private network로 접근하도록 제한합니다.
- Kibana는 public으로 열지 않고 Session Manager port forwarding으로 접근합니다.
- heap size, disk watermark, 로그 로테이션을 초기에 설정해야 합니다.
- EC2 디스크 사용량이 늘어날 수 있으므로 article 원문, 색인 크기, 로그 크기를 주기적으로 확인해야 합니다.

### Crawler on EC2

크롤러는 EventBridge + Lambda 또는 ECS Scheduled Task 대신 private EC2 내부 스케줄 작업으로 시작합니다.

이 방식을 선택한 이유는 다음과 같습니다.

- crawler는 외부 AWS RSS 피드에 접근해야 하므로 NAT Instance를 통해 outbound 인터넷 접근을 제공합니다.
- RDS와 Elasticsearch 접근 구성이 단순합니다.
- 수집, 본문 추출, DB 저장, 색인을 하나의 작업 흐름으로 빠르게 실험할 수 있습니다.
- 실패 시 EC2 로그를 바로 확인하며 디버깅하기 쉽습니다.

초기에는 하루 1회 또는 몇 시간 간격으로 실행합니다. 수집 대상이 늘어나고 작업 시간이 길어지면 crawler를 별도 private EC2, ECS Scheduled Task, EventBridge 기반 작업으로 분리합니다.

### Systems Manager Session Manager

private EC2에는 SSH 포트를 직접 열지 않고 AWS Systems Manager Session Manager로 접근합니다.

이 방식을 선택한 이유는 다음과 같습니다.

- EC2에 public IP가 없어도 접속할 수 있습니다.
- SSH 22번 포트를 internet에 열 필요가 없습니다.
- 접근 기록을 남기기 쉽습니다.
- Kibana 접근도 Session Manager port forwarding으로 처리할 수 있습니다.

예를 들어 Kibana는 EC2 내부에서 `localhost:5601`로 실행하고, 필요한 경우 로컬 개발 환경에서 Session Manager port forwarding으로 접속합니다.

### Terraform

AWS 인프라는 Terraform으로 관리합니다.

이 방식을 선택한 이유는 다음과 같습니다.

- AWS 콘솔 수동 작업을 줄이고 인프라 변경 이력을 코드로 남길 수 있습니다.
- public repository에서 인프라 설계를 투명하게 확인할 수 있습니다.
- Codex가 Terraform 파일 작성, 수정, `terraform fmt`, `terraform validate`, `terraform plan`을 빠르게 도와줄 수 있습니다.
- 비용이 큰 리소스 생성 전에 plan으로 변경 사항을 검토할 수 있습니다.
- 같은 환경을 다시 만들거나 수정하기 쉽습니다.

초기 Terraform 관리 대상은 다음과 같습니다.

- VPC
- public subnet
- private subnet
- route table
- internet gateway
- NAT Instance
- ALB
- security group
- EC2 instance
- IAM role/profile for EC2 and SSM
- RDS PostgreSQL
- S3 bucket
- CloudFront distribution

Terraform 실행 원칙은 다음과 같습니다.

- `terraform.tfvars`와 secret 값은 커밋하지 않습니다.
- 변경 후 `terraform fmt`와 `terraform validate`를 실행합니다.
- `terraform plan`으로 변경 사항을 확인합니다.
- `terraform apply`는 명시적으로 요청했을 때만 실행합니다.
- 리소스 삭제가 포함된 plan은 반드시 별도로 확인합니다.

## 로컬 개발 계획

초기 로컬 개발 환경은 Docker Compose를 사용합니다.

로컬에서 실행할 주요 구성 요소는 다음과 같습니다.

- PostgreSQL
- Elasticsearch
- Kibana, 선택 사항
- FastAPI backend
- Next.js frontend

첫 번째 구현 마일스톤은 다음 흐름을 증명하는 것입니다.

1. 로컬에서 PostgreSQL과 Elasticsearch를 실행합니다.
2. AWS RSS 피드 소스를 등록합니다.
3. 크롤러를 수동으로 실행합니다.
4. 수집한 글을 PostgreSQL에 저장합니다.
5. 검색 문서를 Elasticsearch에 색인합니다.
6. FastAPI 검색 엔드포인트에서 검색 결과를 확인합니다.
7. Next.js UI에서 검색 결과를 표시합니다.

## 배포 방향

초기 배포는 AWS 자원을 사용하되, 관리형 검색 서비스와 상시 컨테이너 서비스를 피하는 방향으로 시작합니다.

초기 배포 단위는 다음과 같습니다.

- `apps/web`: Next.js static export 후 S3 업로드, CloudFront로 제공
- `apps/backend`: private EC2에서 FastAPI 실행, public ALB를 통해 접근
- crawler: private EC2 내부 cron 또는 systemd timer로 실행
- PostgreSQL: Amazon RDS for PostgreSQL
- Elasticsearch: private EC2 내부 단일 노드
- Kibana: private EC2 내부 실행, Session Manager port forwarding으로 접근
- NAT Instance: private EC2의 outbound internet 접근 제공
- Terraform: AWS 인프라 생성과 변경 관리

나중에 트래픽과 데이터가 늘어나면 다음 순서로 분리합니다.

1. Elasticsearch를 별도 private EC2로 분리합니다.
2. crawler를 별도 private EC2 또는 ECS Scheduled Task로 분리합니다.
3. FastAPI를 App Runner, ECS, 또는 Lambda 기반 API로 분리합니다.
4. NAT Instance 운영 부담이 커지면 NAT Gateway로 전환합니다.
5. 검색 엔진 운영 부담이 커지면 Amazon OpenSearch Service 또는 Elastic Cloud를 검토합니다.

## Elasticsearch 문서 초안

검색 색인에 저장할 문서의 예시는 다음과 같습니다.

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

초기 검색 가중치 아이디어는 다음과 같습니다.

- `technologies`: 5
- `title`: 4
- `architectureKeywords`: 3
- `problemKeywords`: 3
- `summary`: 2
- `content`: 1
