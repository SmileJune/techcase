# TechCase AWS 인프라

이 문서는 TechCase MVP의 AWS 인프라 구성을 정리합니다.

초기 인프라는 AWS 자원을 사용하되, 비용과 운영 복잡도를 최소화하는 방향으로 설계합니다. Elasticsearch는 관리형 OpenSearch Service를 사용하지 않고 private EC2에 직접 설치합니다.

## 목표

- EC2를 public internet에 직접 노출하지 않습니다.
- FastAPI는 public ALB를 통해서만 접근합니다.
- Elasticsearch와 Kibana는 외부에 공개하지 않습니다.
- RDS PostgreSQL은 private subnet에 둡니다.
- private EC2의 outbound internet 접근은 NAT Gateway 대신 NAT Instance로 처리합니다.
- 인프라는 Terraform으로 관리합니다.

## 초기 구성

```text
Web: S3 + CloudFront
Load Balancer: public subnet의 Application Load Balancer
Backend API: private subnet의 EC2에서 FastAPI 실행
Crawler: private EC2 내부 cron 또는 systemd timer
Search: private EC2 내부 Elasticsearch 단일 노드
Database: private subnet의 Amazon RDS for PostgreSQL
Outbound internet: public subnet의 NAT Instance
Access: AWS Systems Manager Session Manager
IaC: Terraform
```

## 네트워크 구조

```text
VPC
  Public Subnets
    - ALB
    - NAT Instance
    - Internet Gateway route

  Private Subnets
    - EC2 backend/search/crawler
    - RDS PostgreSQL
    - default route to NAT Instance
```

요청 흐름:

```text
User
  |
  v
CloudFront
  |
  v
S3 - Next.js static web
  |
  v
Public ALB
  |
  v
Private EC2 - FastAPI
```

crawler outbound 흐름:

```text
Private EC2 - crawler
  |
  v
NAT Instance
  |
  v
AWS RSS feeds / article pages
```

데이터 접근 흐름:

```text
Private EC2
  +--> RDS PostgreSQL
  +--> Local Elasticsearch
```

## 리소스별 역할

### S3

Next.js static export 결과물을 저장합니다.

역할:

- 정적 HTML, JS, CSS, image 파일 저장
- CloudFront origin

보안:

- public bucket으로 열지 않습니다.
- CloudFront Origin Access Control 또는 유사한 접근 제한을 사용합니다.

### CloudFront

정적 웹 애플리케이션을 사용자에게 제공합니다.

역할:

- S3 정적 파일 캐싱
- HTTPS 제공
- 전 세계 edge cache

초기에는 검색 결과 자체를 서버 렌더링하지 않고, 브라우저에서 ALB API를 호출합니다.

### Application Load Balancer

FastAPI API 서버로 들어오는 public HTTP/HTTPS 트래픽을 private EC2로 전달합니다.

역할:

- public endpoint
- HTTPS termination
- health check
- private EC2 target forwarding

보안:

- ALB security group은 80/443만 허용합니다.
- EC2 security group은 ALB security group에서 오는 API 포트만 허용합니다.

### EC2 Backend

private subnet에 배치되는 핵심 서버입니다.

실행 프로세스:

- FastAPI server
- Elasticsearch
- crawler cron 또는 systemd timer
- Kibana, 필요할 때만 실행
- CloudWatch Agent, 선택

보안:

- public IP를 부여하지 않습니다.
- SSH inbound를 열지 않습니다.
- Systems Manager Session Manager로 접속합니다.
- Elasticsearch `9200`은 외부에 공개하지 않습니다.
- Kibana `5601`은 외부에 공개하지 않습니다.

### NAT Instance

private EC2의 outbound internet 접근을 제공합니다.

사용 이유:

- crawler가 AWS RSS feed와 원문 HTML에 접근해야 합니다.
- NAT Gateway보다 비용을 낮출 수 있습니다.

필수 설정:

- public subnet에 배치
- Elastic IP 연결
- source/destination check 비활성화
- private route table의 `0.0.0.0/0` target으로 지정
- private EC2의 outbound 트래픽 허용

주의:

- NAT Instance는 직접 운영해야 합니다.
- OS 패치, 장애 복구, 재부팅 후 동작 확인이 필요합니다.
- 운영 부담이 커지면 NAT Gateway로 전환합니다.

### RDS PostgreSQL

원본 article 데이터의 기준 저장소입니다.

역할:

- Source 저장
- Article 저장
- CrawlRun 저장
- ArticleKeyword 저장
- Elasticsearch 재색인의 기준 데이터 제공

초기 설정:

- PostgreSQL
- Single-AZ
- 작은 인스턴스 클래스
- 최소 gp3 스토리지
- 짧은 백업 보존 기간
- public access 비활성화

보안:

- private subnet에 배치합니다.
- RDS security group은 EC2 security group에서 오는 5432만 허용합니다.

### Elasticsearch on EC2

검색 전용 엔진입니다.

역할:

- articles index 저장
- query DSL 기반 검색
- field boosting
- highlighting
- analyzer/synonym 실험

보안:

- 외부 공개 금지
- FastAPI와 crawler만 접근
- Kibana는 Session Manager port forwarding으로 접근

운영:

- heap size 설정
- disk watermark 확인
- 로그 로테이션
- snapshot 전략은 추후 S3 연동으로 확장

### Systems Manager Session Manager

private EC2 접속 수단입니다.

사용 이유:

- SSH 포트를 열지 않아도 됩니다.
- EC2 public IP가 필요 없습니다.
- 접근 이력을 남기기 쉽습니다.
- Kibana port forwarding에 사용할 수 있습니다.

필요 조건:

- EC2 IAM instance profile
- SSM Agent
- private EC2에서 SSM endpoint 접근 가능

주의:

- private subnet에서 SSM을 사용하려면 NAT Instance를 통한 outbound 또는 VPC endpoint 구성이 필요합니다.
- 초기에는 NAT Instance outbound를 사용하고, 나중에 비용/보안 최적화를 위해 SSM VPC endpoint를 검토합니다.

## Security Group 초안

```text
alb_sg
- inbound 80/443 from 0.0.0.0/0
- outbound api port to backend_sg

backend_sg
- inbound api port from alb_sg
- inbound optional internal ports from self
- outbound 5432 to rds_sg
- outbound 443 to nat path
- outbound 9200 to self/local only

rds_sg
- inbound 5432 from backend_sg

nat_sg
- inbound from private subnet or backend_sg
- outbound 80/443 to 0.0.0.0/0
```

Elasticsearch와 Kibana 포트는 security group inbound로 열지 않습니다.

## Terraform 관리 대상

초기 Terraform 관리 대상:

```text
VPC
public subnets
private subnets
route tables
internet gateway
NAT Instance
ALB
target group
listener
security groups
EC2 instance
IAM role/profile for EC2 and SSM
RDS PostgreSQL
S3 bucket
CloudFront distribution
```

초기 Terraform 디렉터리 구조:

```text
infra/
  terraform/
    main.tf
    variables.tf
    outputs.tf
    versions.tf
    terraform.tfvars.example
```

리소스가 늘어나면 다음처럼 모듈화합니다.

```text
infra/
  terraform/
    envs/
      dev/
    modules/
      network/
      web/
      compute/
      database/
      security/
```

## Terraform 실행 원칙

- `terraform.tfvars`와 secret 값은 커밋하지 않습니다.
- 변경 후 `terraform fmt`를 실행합니다.
- `terraform validate`로 문법과 provider 설정을 확인합니다.
- `terraform plan`으로 변경 사항을 검토합니다.
- `terraform apply`는 명시적으로 요청했을 때만 실행합니다.
- 삭제가 포함된 plan은 반드시 별도로 확인합니다.

## 비용 관리 포인트

초기 비용에서 주의할 리소스:

- EC2 backend instance
- NAT Instance
- ALB
- RDS PostgreSQL
- CloudFront data transfer
- EBS volume

비용을 줄이기 위한 선택:

- NAT Gateway 대신 NAT Instance 사용
- OpenSearch Service 대신 Elasticsearch on EC2 사용
- Next.js는 S3 + CloudFront 정적 배포
- RDS는 Single-AZ, 작은 인스턴스, 최소 스토리지로 시작
- Kibana는 필요할 때만 실행

## 관련 문서

- [아키텍처](./architecture.md)
- [데이터 모델](./data-model.md)
- [검색 설계](./search-design.md)
- [개발 계획](./development.md)
