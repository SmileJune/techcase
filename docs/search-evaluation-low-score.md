# Search Evaluation Low Score Report

- generated at: 2026-05-22T14:25:07.197176+00:00
- queries: 42
- low score queries: 11
- thresholds: p@5>=0.4, r@10>=0.8, mrr>=0.5, ndcg@10>=0.7

## Review Targets

| query_id | query | category | total | p@5 | r@10 | mrr | ndcg@10 | reasons |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| architecture-cross-region-resilience | cross-Region resilience | architecture | 278 | 0.200 | 1.000 | 1.000 | 0.861 | low_precision |
| ko-architecture-pr-preview | PR Preview Argo CD Linkerd | architecture | 306 | 0.200 | 1.000 | 1.000 | 0.889 | low_precision |
| ko-problem-s3-cdn-cost | S3 비용 이미지 CDN 최적화 | problem | 139 | 0.200 | 1.000 | 1.000 | 0.900 | low_precision |
| ko-architecture-serverless | 서버리스 | architecture | 57 | 0.400 | 1.000 | 0.500 | 0.611 | low_ndcg |
| architecture-streaming-pipeline | streaming data pipeline | architecture | 107 | 0.400 | 1.000 | 0.500 | 0.686 | low_ndcg |
| ko-data-log-platform | 로그 플랫폼 | architecture | 577 | 0.400 | 0.600 | 1.000 | 0.801 | low_recall |
| ko-search-elasticsearch-index | Elasticsearch 인덱스 구조 | technology | 48 | 0.400 | 0.750 | 1.000 | 0.801 | low_recall |
| ko-search-quality-improvement | 검색 품질 개선 | technology | 709 | 0.600 | 0.500 | 1.000 | 0.641 | low_recall, low_ndcg |
| ko-problem-cost-optimization | 비용 최적화 | problem | 483 | 0.800 | 0.545 | 0.500 | 0.545 | low_recall, low_ndcg |
| ko-tech-search | 검색 개선 | technology | 640 | 0.800 | 0.364 | 1.000 | 0.609 | low_recall, low_ndcg |
| tech-lambda | Lambda | technology | 102 | 0.800 | 0.800 | 0.500 | 0.699 | low_ndcg |

## Details

### architecture-cross-region-resilience

- query: cross-Region resilience
- category: architecture
- reasons: low_precision
- scores: p@5=0.200, r@10=1.000, mrr=1.000, ndcg@10=0.861

| rank | expected | title | company/source |
| ---: | --- | --- | --- |
| 1 | yes:3 | [How to build a cross-Region resilience for Amazon OpenSearch Service with Amazon MSK](https://aws.amazon.com/blogs/big-data/how-to-build-a-cross-region-resilience-for-amazon-opensearch-service-with-amazon-msk/) | AWS / AWS Big Data Blog |
| 2 | - | [Enabling high availability of Amazon EC2 instances on AWS Outposts servers (Part 3)](https://aws.amazon.com/blogs/compute/enabling-high-availability-of-amazon-ec2-instances-on-aws-outposts-servers-part-3/) | AWS / AWS Compute Blog |
| 3 | - | [How we rebuilt the search architecture for high availability in GitHub Enterprise Server](https://github.blog/engineering/architecture-optimization/how-we-rebuilt-the-search-architecture-for-high-availability-in-github-enterprise-server/) | GitHub / GitHub Engineering |
| 4 | - | [개발자를 위한 레디스 튜토리얼 03 : NHN Cloud Meetup](https://meetup.nhncloud.com/posts/226) | NHN Cloud / NHN Cloud Meetup |
| 5 | - | [Streamlining access to powerful disaster recovery capabilities of AWS](https://aws.amazon.com/blogs/architecture/streamlining-access-to-powerful-disaster-recovery-capabilities-of-aws/) | AWS / AWS Architecture Blog |
| 6 | - | [Amazon Aurora DSQL for global-scale financial transactions](https://aws.amazon.com/blogs/database/amazon-aurora-dsql-for-global-scale-financial-transactions/) | AWS / AWS Database Blog |
| 7 | yes:2 | [How to consolidate cross-Region S3 data into OpenSearch](https://aws.amazon.com/blogs/big-data/how-to-consolidate-cross-region-s3-data-into-opensearch/) | AWS / AWS Big Data Blog |
| 8 | yes:2 | [Simplify cross-account and cross-Region stack output references with AWS CloudFormation and CDK’s new Fn::GetStackOutput](https://aws.amazon.com/blogs/devops/simplify-cross-account-and-cross-region-stack-output-references-with-aws-cloudformation-and-cdks-new-fngetstackoutput/) | AWS / AWS DevOps Blog |
| 9 | - | [Amazon Aurora DSQL connections: Drivers, strings, and best practices](https://aws.amazon.com/blogs/database/amazon-aurora-dsql-connections-drivers-strings-and-best-practices/) | AWS / AWS Database Blog |
| 10 | - | [Migrate third-party and self-managed Apache Kafka clusters to Amazon MSK Express brokers with Amazon MSK Replicator](https://aws.amazon.com/blogs/big-data/migrate-third-party-and-self-managed-apache-kafka-clusters-to-amazon-msk-express-brokers-with-amazon-msk-replicator/) | AWS / AWS Big Data Blog |

### ko-architecture-pr-preview

- query: PR Preview Argo CD Linkerd
- category: architecture
- reasons: low_precision
- scores: p@5=0.200, r@10=1.000, mrr=1.000, ndcg@10=0.889

| rank | expected | title | company/source |
| ---: | --- | --- | --- |
| 1 | yes:3 | [Argo CD, Linkerd 기반 QA 병목 제거: PR Preview 환경 구축](https://tech.inflab.com/20251121-pr-preview/) | Inflab / Inflab Tech Blog |
| 2 | - | [Github PR을 올리면 자동으로 테스트가? 심지어 멀티 프로젝트에도 가능하다! : NHN Cloud Meetup](https://meetup.nhncloud.com/posts/212) | NHN Cloud / NHN Cloud Meetup |
| 3 | - | [CI 소요시간을 최대 4.6배 개선하는 방법](https://tech.inflab.com/20231101-optimizing-ci-pipeline/) | Inflab / Inflab Tech Blog |
| 4 | - | [누구나 찾아볼 수 있는 중고거래 서버 LLM 릴리즈 노트 도입기](https://medium.com/daangn/%EB%88%84%EA%B5%AC%EB%82%98-%EC%B0%BE%EC%95%84%EB%B3%BC-%EC%88%98-%EC%9E%88%EB%8A%94-%EC%A4%91%EA%B3%A0%EA%B1%B0%EB%9E%98-%EC%84%9C%EB%B2%84-llm-%EB%A6%B4%EB%A6%AC%EC%A6%88-%EB%85%B8%ED%8A%B8-%EB%8F%84%EC%9E%85%EA%B8%B0-93afe203d766?source=rss----4505f82a2dbd---4) | Daangn / Daangn Tech Blog |
| 5 | - | [ODW #1: AI로 리뷰 정체를 해소하다 - PR 리뷰 지원과 사내 워크숍으로 리뷰 문화 바꾸기](https://techblog.lycorp.co.jp/ko/resolving-pr-review-bottlenecks-with-ai-and-transforming-review-culture) | LY Corporation / LY Corporation Tech Blog |
| 6 | - | [AWX를 이용한 CI/CD Pipeline: Pylon](https://tech.kakaopay.com/post/sre-re-pylon/) | Kakao Pay / Kakao Pay Tech Blog |
| 7 | - | [라이더스 개발팀 모바일에서 CI/CD 도입](https://techblog.woowahan.com/2579/) | Woowa Brothers / Woowa Tech Blog |
| 8 | - | [Linger 로 오버헤드 줄이기](https://dev.gmarket.com/26) | Gmarket / Gmarket Tech Blog |
| 9 | yes:2 | [EKS + ALB 환경에서 Argo Rollouts 503 에러 없는 카나리 배포 적용기](https://techblog.gccompany.co.kr/eks-alb-%ED%99%98%EA%B2%BD%EC%97%90%EC%84%9C-argo-rollouts-503-%EC%97%90%EB%9F%AC-%EC%97%86%EB%8A%94-%EC%B9%B4%EB%82%98%EB%A6%AC-%EB%B0%B0%ED%8F%AC-%EC%A0%81%EC%9A%A9%EA%B8%B0-689eedaf8d1a?source=rss----18356045d353---4) | GC Company / GC Company Tech Blog |
| 10 | - | [Yarn Classic에서 Pnpm으로 전환하기 with TurboRepo](https://medium.com/wantedjobs/yarn-classic%EC%97%90%EC%84%9C-pnpm%EC%9C%BC%EB%A1%9C-%EC%A0%84%ED%99%98%ED%95%98%EA%B8%B0-with-turborepo-7c0c37cb3f9e?source=rss----fb47eceee74c---4) | Wantedlab / Wantedlab Tech Blog |

### ko-problem-s3-cdn-cost

- query: S3 비용 이미지 CDN 최적화
- category: problem
- reasons: low_precision
- scores: p@5=0.200, r@10=1.000, mrr=1.000, ndcg@10=0.900

| rank | expected | title | company/source |
| ---: | --- | --- | --- |
| 1 | yes:3 | [Amazon S3 보관 비용과 이미지 CDN 트래픽 최적화](https://tech.inflab.com/20251029-optimize-s3/) | Inflab / Inflab Tech Blog |
| 2 | - | [Optimize Amazon S3 Tables queries with Amazon Redshift](https://aws.amazon.com/blogs/big-data/optimize-amazon-s3-tables-queries-with-amazon-redshift/) | AWS / AWS Big Data Blog |
| 3 | - | [Enable real-time mainframe analytics with Precisely Connect and Amazon S3](https://aws.amazon.com/blogs/big-data/enable-real-time-mainframe-analytics-with-precisely-connect-and-amazon-s3/) | AWS / AWS Big Data Blog |
| 4 | - | [AWS re:Invent 2024 Recap: Database, Storage](https://tech.kakaopay.com/post/aws-reinvent-2024-database-and-storage/) | Kakao Pay / Kakao Pay Tech Blog |
| 5 | - | [How to use streamlined permissions for Amazon S3 Tables and Iceberg materialized views](https://aws.amazon.com/blogs/big-data/how-to-use-streamlined-permissions-for-amazon-s3-tables-and-iceberg-materialized-views/) | AWS / AWS Big Data Blog |
| 6 | - | [Query billion-scale vectors with SQL: Integrating Amazon S3 Vectors and Aurora PostgreSQL](https://aws.amazon.com/blogs/database/query-billion-scale-vectors-with-sql-integrating-amazon-s3-vectors-and-aurora-postgresql/) | AWS / AWS Database Blog |
| 7 | yes:2 | [CloudFront의 숨은 힘: 캐싱 없이도 극대화 되는 성능과 비용 효율성](https://medium.com/wantedjobs/cloudfront%EC%9D%98-%EC%88%A8%EC%9D%80-%ED%9E%98-%EC%BA%90%EC%8B%B1-%EC%97%86%EC%9D%B4%EB%8F%84-%EA%B7%B9%EB%8C%80%ED%99%94-%EB%90%98%EB%8A%94-%EC%84%B1%EB%8A%A5%EA%B3%BC-%EB%B9%84%EC%9A%A9-%ED%9A%A8%EC%9C%A8%EC%84%B1-44f66701d1eb?source=rss----fb47eceee74c---4) | Wantedlab / Wantedlab Tech Blog |
| 8 | - | [데이터 분석 라이브러리 개발기 (2) - 통합 테스팅과 문서화를 동시에 잡는 방법](https://tech.devsisters.com/posts/testing-devplay-analytics-library) | Devsisters / Devsisters Tech Blog |
| 9 | - | [스타트업 엔지니어의 AWS 비용 최적화 경험기](https://tech.inflab.com/20240227-finops-for-startup/) | Inflab / Inflab Tech Blog |
| 10 | - | [Streamlined monitoring and debugging for Amazon EMR on EC2](https://aws.amazon.com/blogs/big-data/streamlined-monitoring-and-debugging-for-amazon-emr-on-ec2/) | AWS / AWS Big Data Blog |

### ko-architecture-serverless

- query: 서버리스
- category: architecture
- reasons: low_ndcg
- scores: p@5=0.400, r@10=1.000, mrr=0.500, ndcg@10=0.611

| rank | expected | title | company/source |
| ---: | --- | --- | --- |
| 1 | - | [Serverless ICYMI Q4 2025](https://aws.amazon.com/blogs/compute/serverless-icymi-q4-2025/) | AWS / AWS Compute Blog |
| 2 | yes:2 | [Serverless ICYMI Q1 2026](https://aws.amazon.com/blogs/compute/serverless-icymi-q1-2026/) | AWS / AWS Compute Blog |
| 3 | yes:3 | [Optimizing Compute-Intensive Serverless Workloads with Multi-threaded Rust on AWS Lambda](https://aws.amazon.com/blogs/compute/optimizing-compute-intensive-serverless-workloads-with-multi-threaded-rust-on-aws-lambda/) | AWS / AWS Compute Blog |
| 4 | - | [.NET 10 runtime now available in AWS Lambda](https://aws.amazon.com/blogs/compute/net-10-runtime-now-available-in-aws-lambda/) | AWS / AWS Compute Blog |
| 5 | - | [More room to build: serverless services now support payloads up to 1 MB](https://aws.amazon.com/blogs/compute/more-room-to-build-serverless-services-now-support-payloads-up-to-1-mb/) | AWS / AWS Compute Blog |
| 6 | yes:3 | [Modernizing KYC with AWS serverless solutions and agentic AI for financial services](https://aws.amazon.com/blogs/architecture/modernizing-kyc-with-aws-serverless-solutions-and-agentic-ai-for-financial-services/) | AWS / AWS Architecture Blog |
| 7 | - | [Google Cloud Next 2024 참관 후기 2편 - Google Cloud Serverless for Java developer](https://tech.kakaopay.com/post/2024-google-cloud-next-2/) | Kakao Pay / Kakao Pay Tech Blog |
| 8 | - | [서버리스에서 쿠버네티스로 - Airflow 운영 경험기](https://helloworld.kurly.com/blog/airflow-1/) | Kurly / Kurly Tech Blog |
| 9 | - | [Building an end-to-end agentic SRE using AWS DevOps Agent](https://aws.amazon.com/blogs/devops/building-an-end-to-end-agentic-sre-using-aws-devops-agent/) | AWS / AWS DevOps Blog |
| 10 | - | [6,000 AWS accounts, three people, one platform: Lessons learned](https://aws.amazon.com/blogs/architecture/6000-aws-accounts-three-people-one-platform-lessons-learned/) | AWS / AWS Architecture Blog |

### architecture-streaming-pipeline

- query: streaming data pipeline
- category: architecture
- reasons: low_ndcg
- scores: p@5=0.400, r@10=1.000, mrr=0.500, ndcg@10=0.686

| rank | expected | title | company/source |
| ---: | --- | --- | --- |
| 1 | - | [Getting started with Change Data Capture in Amazon Aurora DSQL](https://aws.amazon.com/blogs/database/getting-started-with-change-data-capture-in-amazon-aurora-dsql/) | AWS / AWS Database Blog |
| 2 | yes:3 | [Building unified data pipelines with Apache Iceberg and Apache Flink](https://aws.amazon.com/blogs/big-data/building-unified-data-pipelines-with-apache-iceberg-and-apache-flink/) | AWS / AWS Big Data Blog |
| 3 | yes:3 | [Build streaming applications on Amazon Managed Service for Apache Flink with AI-assisted guidance](https://aws.amazon.com/blogs/big-data/build-streaming-applications-on-amazon-managed-service-for-apache-flink-with-ai-assisted-guidance/) | AWS / AWS Big Data Blog |
| 4 | - | [How to consolidate cross-Region S3 data into OpenSearch](https://aws.amazon.com/blogs/big-data/how-to-consolidate-cross-region-s3-data-into-opensearch/) | AWS / AWS Big Data Blog |
| 5 | - | [How to build a cross-Region resilience for Amazon OpenSearch Service with Amazon MSK](https://aws.amazon.com/blogs/big-data/how-to-build-a-cross-region-resilience-for-amazon-opensearch-service-with-amazon-msk/) | AWS / AWS Big Data Blog |
| 6 | - | [Meet Coupang’s Machine Learning Platform](https://medium.com/coupang-engineering/meet-coupangs-machine-learning-platform-cd00e9ccc172?source=rss----fb028911af07---4) | Coupang / Coupang Engineering Blog |
| 7 | yes:3 | [Building Jetflow: a framework for flexible, performant data pipelines at Cloudflare](https://blog.cloudflare.com/building-jetflow-a-framework-for-flexible-performant-data-pipelines-at-cloudflare/) | Cloudflare / Cloudflare Engineering |
| 8 | - | [Announcing aggregations on Amazon ElastiCache](https://aws.amazon.com/blogs/database/announcing-aggregations-on-amazon-elasticache/) | AWS / AWS Database Blog |
| 9 | - | [Inside the feature store powering real-time AI in Dropbox Dash](https://dropbox.tech/machine-learning/feature-store-powering-realtime-ai-in-dropbox-dash) | Dropbox / Dropbox Tech Blog |
| 10 | yes:2 | [Streaming CloudWatch metrics to VPC-based OpenTelemetry collectors using Lambda](https://aws.amazon.com/blogs/architecture/streaming-cloudwatch-metrics-to-vpc-based-opentelemetry-collectors-using-lambda/) | AWS / AWS Architecture Blog |

### ko-data-log-platform

- query: 로그 플랫폼
- category: architecture
- reasons: low_recall
- scores: p@5=0.400, r@10=0.600, mrr=1.000, ndcg@10=0.801

| rank | expected | title | company/source |
| ---: | --- | --- | --- |
| 1 | yes:3 | [비용, 성능, 안정성을 목표로 한 지능형 로그 파이프라인 도입](https://d2.naver.com/helloworld/0004394) | NAVER / NAVER D2 |
| 2 | yes:3 | [로그 파이프라인 개선기 - 기존 파이프라인 문제 정의 및 해결 방안 적용](https://tech.socarcorp.kr/data/2025/02/25/log-pipeline-revamp.html) | SOCAR / SOCAR Tech Blog |
| 3 | - | [Data-Driven 문화를 만드는 사람들 - 데이터플랫폼셀](https://tech.devsisters.com/posts/data-driven-story-1-data-platform-cell) | Devsisters / Devsisters Tech Blog |
| 4 | - | [MySQL 3분 vs ClickHouse 0.3초 — 같은 쿼리입니다 : NHN Cloud Meetup](https://meetup.nhncloud.com/posts/414) | NHN Cloud / NHN Cloud Meetup |
| 5 | - | [데브시스터즈 엔지니어링 데이 - Data 돌아보기](https://tech.devsisters.com/posts/2025-engineering-day-data) | Devsisters / Devsisters Tech Blog |
| 6 | yes:3 | [일 41TB, 200억 건의 로그를 ClickStack으로 실시간 처리하기 - 호그와트 도서관 프로젝트](https://tech.kakaopay.com/post/pallas-v2-log-platform/) | Kakao Pay / Kakao Pay Tech Blog |
| 7 | - | [따끈따끈한 전사 로그 시스템 전환기: ELK Stack에서 Loki로 전환한 이유](https://techblog.woowahan.com/14505/) | Woowa Brothers / Woowa Tech Blog |
| 8 | - | [AI 데이터 분석가 ‘물어보새’ 등장 – 2부. Data Discovery](https://techblog.woowahan.com/18362/) | Woowa Brothers / Woowa Tech Blog |
| 9 | - | [입사 후, 벌써 1년](https://techblog.woowahan.com/2632/) | Woowa Brothers / Woowa Tech Blog |
| 10 | - | [TOAST Log&Crash Search의 데이터 무결성 검증 기능 사용하기 : NHN Cloud Meetup](https://meetup.nhncloud.com/posts/254) | NHN Cloud / NHN Cloud Meetup |

### ko-search-elasticsearch-index

- query: Elasticsearch 인덱스 구조
- category: technology
- reasons: low_recall
- scores: p@5=0.400, r@10=0.750, mrr=1.000, ndcg@10=0.801

| rank | expected | title | company/source |
| ---: | --- | --- | --- |
| 1 | yes:3 | [실시간 인덱싱을 위한 Elasticsearch 구조를 찾아서](https://techblog.woowahan.com/7425/) | Woowa Brothers / Woowa Tech Blog |
| 2 | yes:2 | [배민상회와 검색플랫폼 연동기](https://techblog.woowahan.com/11732/) | Woowa Brothers / Woowa Tech Blog |
| 3 | - | [CDC & CDC Sink Platform 개발 2편 - CDC Sink Platform 개발 및 CQRS 패턴의 적용](https://hyperconnect.github.io/2021/03/22/cdc-sink-platform.html) | Hyperconnect / Hyperconnect Tech Blog |
| 4 | - | [Elasticsearch 병렬 테스트를 향한 여정](https://techblog.woowahan.com/18486/) | Woowa Brothers / Woowa Tech Blog |
| 5 | - | [Trino로 타임아웃 개선하기 : NHN Cloud Meetup](https://meetup.nhncloud.com/posts/391) | NHN Cloud / NHN Cloud Meetup |
| 6 | yes:3 | [검색 성능 개선을 위한 Elasticsearch 인덱스 구조와 쿼리 최적화](https://techblog.woowahan.com/20161/) | Woowa Brothers / Woowa Tech Blog |
| 7 | - | [How we rebuilt the search architecture for high availability in GitHub Enterprise Server](https://github.blog/engineering/architecture-optimization/how-we-rebuilt-the-search-architecture-for-high-availability-in-github-enterprise-server/) | GitHub / GitHub Engineering |
| 8 | - | [우리 서비스와 연결된 MCP Server 빠르게 구현해보기: MCP 해커톤 후기](https://techblog.woowahan.com/22342/) | Woowa Brothers / Woowa Tech Blog |
| 9 | - | [실시간 마케팅을 위한 PoC 개발기](https://techblog.woowahan.com/22043/) | Woowa Brothers / Woowa Tech Blog |
| 10 | - | [쿠폰, 어디에 쓸 수 있어요? — 이벤트 기반 적용 상품 조회 시스템 구축](https://medium.com/29cm/%EC%BF%A0%ED%8F%B0-%EC%96%B4%EB%94%94%EC%97%90-%EC%93%B8-%EC%88%98-%EC%9E%88%EC%96%B4%EC%9A%94-%EC%9D%B4%EB%B2%A4%ED%8A%B8-%EA%B8%B0%EB%B0%98-%EC%A0%81%EC%9A%A9-%EC%83%81%ED%92%88-%EC%A1%B0%ED%9A%8C-%EC%8B%9C%EC%8A%A4%ED%85%9C-%EA%B5%AC%EC%B6%95-4dc35eb97c1f?source=rss----fbd022693005---4) | 29CM / 29CM TEAM |

### ko-search-quality-improvement

- query: 검색 품질 개선
- category: technology
- reasons: low_recall, low_ndcg
- scores: p@5=0.600, r@10=0.500, mrr=1.000, ndcg@10=0.641

| rank | expected | title | company/source |
| ---: | --- | --- | --- |
| 1 | yes:3 | [Using LLMs to amplify human labeling and improve Dash search relevance](https://dropbox.tech/machine-learning/llm-human-labeling-improving-search-relevance-dropbox-dash) | Dropbox / Dropbox Tech Blog |
| 2 | yes:3 | [MongoDB Atlas Search 정렬이슈 해결기](https://tech.inflab.com/202211-mongodb-atlas-search/) | Inflab / Inflab Tech Blog |
| 3 | yes:2 | [How we rebuilt the search architecture for high availability in GitHub Enterprise Server](https://github.blog/engineering/architecture-optimization/how-we-rebuilt-the-search-architecture-for-high-availability-in-github-enterprise-server/) | GitHub / GitHub Engineering |
| 4 | - | [배민상회와 검색플랫폼 연동기](https://techblog.woowahan.com/11732/) | Woowa Brothers / Woowa Tech Blog |
| 5 | - | [Log&Crash Search의 Network Insight 기능 소개 : NHN Cloud Meetup](https://meetup.nhncloud.com/posts/156) | NHN Cloud / NHN Cloud Meetup |
| 6 | - | [TOAST Log&Crash Search의 데이터 무결성 검증 기능 사용하기 : NHN Cloud Meetup](https://meetup.nhncloud.com/posts/254) | NHN Cloud / NHN Cloud Meetup |
| 7 | - | [Full-text, exact-match, range, and hybrid search on Amazon ElastiCache](https://aws.amazon.com/blogs/database/enhanced-search-for-amazon-elasticache/) | AWS / AWS Database Blog |
| 8 | - | [SEO 주도 개발 실천기: 구글이 인정한 ‘좋은 URL’ 99% 달성 여정](https://medium.com/wantedjobs/seo-%EC%A3%BC%EB%8F%84-%EA%B0%9C%EB%B0%9C-%EC%8B%A4%EC%B2%9C%EA%B8%B0-%EA%B5%AC%EA%B8%80%EC%9D%B4-%EC%9D%B8%EC%A0%95%ED%95%9C-%EC%A2%8B%EC%9D%80-url-99-%EB%8B%AC%EC%84%B1-%EC%97%AC%EC%A0%95-7e494b56d39b?source=rss----fb47eceee74c---4) | Wantedlab / Wantedlab Tech Blog |
| 9 | - | [CDC & CDC Sink Platform 개발 2편 - CDC Sink Platform 개발 및 CQRS 패턴의 적용](https://hyperconnect.github.io/2021/03/22/cdc-sink-platform.html) | Hyperconnect / Hyperconnect Tech Blog |
| 10 | - | [[AI 트렌드] 매출 성장의 비결로 떠오른 검색· 추천 기술, Seargest](https://www.upstage.ai/blog/ko/2023-ai-tech-trend-seargest) | Upstage / Upstage Blog |

### ko-problem-cost-optimization

- query: 비용 최적화
- category: problem
- reasons: low_recall, low_ndcg
- scores: p@5=0.800, r@10=0.545, mrr=0.500, ndcg@10=0.545

| rank | expected | title | company/source |
| ---: | --- | --- | --- |
| 1 | - | [AWS re:Invent 2023, 관심 세션을 중심으로 (2편): Cost Optimization, Observability](https://tech.kakaopay.com/post/2023-aws-reinvent-2/) | Kakao Pay / Kakao Pay Tech Blog |
| 2 | yes:3 | [스타트업 엔지니어의 AWS 비용 최적화 경험기](https://tech.inflab.com/20240227-finops-for-startup/) | Inflab / Inflab Tech Blog |
| 3 | yes:3 | [클라우드 서비스 사용량 관리를 통한 운영 비용 최적화](https://medium.com/coupang-engineering/%ED%81%B4%EB%9D%BC%EC%9A%B0%EB%93%9C-%EC%84%9C%EB%B9%84%EC%8A%A4-%EC%82%AC%EC%9A%A9%EB%9F%89-%EA%B4%80%EB%A6%AC%EB%A5%BC-%ED%86%B5%ED%95%9C-%EC%9A%B4%EC%98%81-%EB%B9%84%EC%9A%A9-%EC%B5%9C%EC%A0%81%ED%99%94-1521565c64ec?source=rss----fb028911af07---4) | Coupang / Coupang Engineering Blog |
| 4 | yes:3 | [데이터는 지웠는데 비용은 그대로? Aurora 스토리지 비용 최적화 하기](https://medium.com/wantedjobs/%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%8A%94-%EC%A7%80%EC%9B%A0%EB%8A%94%EB%8D%B0-%EB%B9%84%EC%9A%A9%EC%9D%80-%EA%B7%B8%EB%8C%80%EB%A1%9C-aurora-%EC%8A%A4%ED%86%A0%EB%A6%AC%EC%A7%80-%EB%B9%84%EC%9A%A9-%EC%B5%9C%EC%A0%81%ED%99%94-%ED%95%98%EA%B8%B0-43d208f6564d?source=rss----fb47eceee74c---4) | Wantedlab / Wantedlab Tech Blog |
| 5 | yes:2 | [Cloud expenditure optimization for cost efficiency](https://medium.com/coupang-engineering/cloud-expenditure-optimization-for-cost-efficiency-44e9bea3d91b?source=rss----fb028911af07---4) | Coupang / Coupang Engineering Blog |
| 6 | yes:2 | [The Hidden Price Tag: Uncovering Hidden Costs in Cloud Architectures with the AWS Well-Architected Framework](https://aws.amazon.com/blogs/architecture/the-hidden-price-tag-uncovering-hidden-costs-in-cloud-architectures-with-the-aws-well-architected-framework/) | AWS / AWS Architecture Blog |
| 7 | - | [이달의 Nclouder 10월 주인공을 소개합니다!](https://medium.com/naver-cloud-platform/%EC%9D%B4%EB%8B%AC%EC%9D%98-nclouder-10%EC%9B%94-%EC%A3%BC%EC%9D%B8%EA%B3%B5%EC%9D%84-%EC%86%8C%EA%B0%9C%ED%95%A9%EB%8B%88%EB%8B%A4-9d7e18801b7c?source=rss----c7f2bfeb6b98---4) | NAVER Cloud / NAVER Cloud Platform Tech Blog |
| 8 | yes:3 | [우아한 Cloud FinOps 여정](https://techblog.woowahan.com/22855/) | Woowa Brothers / Woowa Tech Blog |
| 9 | - | [데이터분석가로서 업무 과정과 경험, 배움을 공유합니다](https://techblog.woowahan.com/2686/) | Woowa Brothers / Woowa Tech Blog |
| 10 | - | [Data Product (3) 데이터로 실제 운영 효율화가 가능할까?](https://tech.socarcorp.kr/data/2025/02/11/weather-wash.html) | SOCAR / SOCAR Tech Blog |

### ko-tech-search

- query: 검색 개선
- category: technology
- reasons: low_recall, low_ndcg
- scores: p@5=0.800, r@10=0.364, mrr=1.000, ndcg@10=0.609

| rank | expected | title | company/source |
| ---: | --- | --- | --- |
| 1 | yes:3 | [Using LLMs to amplify human labeling and improve Dash search relevance](https://dropbox.tech/machine-learning/llm-human-labeling-improving-search-relevance-dropbox-dash) | Dropbox / Dropbox Tech Blog |
| 2 | yes:3 | [MongoDB Atlas Search 정렬이슈 해결기](https://tech.inflab.com/202211-mongodb-atlas-search/) | Inflab / Inflab Tech Blog |
| 3 | yes:3 | [How we rebuilt the search architecture for high availability in GitHub Enterprise Server](https://github.blog/engineering/architecture-optimization/how-we-rebuilt-the-search-architecture-for-high-availability-in-github-enterprise-server/) | GitHub / GitHub Engineering |
| 4 | yes:3 | [배민상회와 검색플랫폼 연동기](https://techblog.woowahan.com/11732/) | Woowa Brothers / Woowa Tech Blog |
| 5 | - | [Log&Crash Search의 Network Insight 기능 소개 : NHN Cloud Meetup](https://meetup.nhncloud.com/posts/156) | NHN Cloud / NHN Cloud Meetup |
| 6 | - | [TOAST Log&Crash Search의 데이터 무결성 검증 기능 사용하기 : NHN Cloud Meetup](https://meetup.nhncloud.com/posts/254) | NHN Cloud / NHN Cloud Meetup |
| 7 | - | [Full-text, exact-match, range, and hybrid search on Amazon ElastiCache](https://aws.amazon.com/blogs/database/enhanced-search-for-amazon-elasticache/) | AWS / AWS Database Blog |
| 8 | - | [Real-time Service Configuration으로 Consul을 신주소 서비스에 적용한 사례](https://techblog.woowahan.com/2586/) | Woowa Brothers / Woowa Tech Blog |
| 9 | - | [CDC & CDC Sink Platform 개발 2편 - CDC Sink Platform 개발 및 CQRS 패턴의 적용](https://hyperconnect.github.io/2021/03/22/cdc-sink-platform.html) | Hyperconnect / Hyperconnect Tech Blog |
| 10 | - | [Building the future: highlights from Dropbox’s 2025 summer intern class](https://dropbox.tech/culture/highlights-from-dropbox-2025-summer-intern-class) | Dropbox / Dropbox Tech Blog |

### tech-lambda

- query: Lambda
- category: technology
- reasons: low_ndcg
- scores: p@5=0.800, r@10=0.800, mrr=0.500, ndcg@10=0.699

| rank | expected | title | company/source |
| ---: | --- | --- | --- |
| 1 | - | [.NET 10 runtime now available in AWS Lambda](https://aws.amazon.com/blogs/compute/net-10-runtime-now-available-in-aws-lambda/) | AWS / AWS Compute Blog |
| 2 | yes:3 | [lambda@edge를 활용한 이미지 워터마킹](https://medium.com/zigbang/lambda-edge%EB%A5%BC-%ED%99%9C%EC%9A%A9%ED%95%9C-%EC%9D%B4%EB%AF%B8%EC%A7%80-%EC%9B%8C%ED%84%B0%EB%A7%88%ED%82%B9-41f1cb282682?source=rss----2f055286701b---4) | Zigbang / Zigbang Tech Blog |
| 3 | yes:3 | [Building fault-tolerant applications with AWS Lambda durable functions](https://aws.amazon.com/blogs/compute/building-fault-tolerant-long-running-application-with-aws-lambda-durable-functions/) | AWS / AWS Compute Blog |
| 4 | yes:3 | [Squeezing every millisecond: How we rebuilt the Datadog Lambda Extension in Rust](https://www.datadoghq.com/blog/engineering/datadog-lambda-extension-rust/) | Datadog / Datadog Engineering Blog |
| 5 | yes:3 | [Building Memory-Intensive Apps with AWS Lambda Managed Instances](https://aws.amazon.com/blogs/compute/building-memory-intensive-apps-with-aws-lambda-managed-instances/) | AWS / AWS Compute Blog |
| 6 | yes:2 | [Build high-performance apps with AWS Lambda Managed Instances](https://aws.amazon.com/blogs/compute/build-high-performance-apps-with-aws-lambda-managed-instances/) | AWS / AWS Compute Blog |
| 7 | yes:2 | [Automate AWS Lambda Runtime Upgrades with AWS Transform custom](https://aws.amazon.com/blogs/devops/automate-aws-lambda-runtime-upgrades-with-aws-transform-custom/) | AWS / AWS DevOps Blog |
| 8 | yes:2 | [잘못 작성된 람다 코드를 삭제하기까지의 여정](https://helloworld.kurly.com/blog/study-in-lambda/) | Kurly / Kurly Tech Blog |
| 9 | yes:3 | [Optimizing Compute-Intensive Serverless Workloads with Multi-threaded Rust on AWS Lambda](https://aws.amazon.com/blogs/compute/optimizing-compute-intensive-serverless-workloads-with-multi-threaded-rust-on-aws-lambda/) | AWS / AWS Compute Blog |
| 10 | - | [Lambda Calculus에 대해 알아보자](https://helloworld.kurly.com/blog/lambda-calculus-1/) | Kurly / Kurly Tech Blog |

