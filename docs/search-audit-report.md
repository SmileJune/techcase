# Search Audit Report

Generated at: 2026-05-17T07:17:48.036001+00:00

## Summary

- queries: 33
- average precision@5: 0.412
- average recall@10: 0.834
- average mrr: 0.847
- average ndcg@10: 0.774

## Query Audits

### tech-lambda - `Lambda`

- category: technology
- intent: AWS Lambda가 실제로 어떤 서버리스/관측성/고성능 워크로드 사례에 사용되는지 찾는다.
- total results: 87
- precision@5: 0.200
- recall@10: 0.667
- mrr: 0.333
- ndcg@10: 0.338

#### Expected URLs

- relevance 3: [Streaming CloudWatch metrics to VPC-based OpenTelemetry collectors using Lambda](https://aws.amazon.com/blogs/architecture/streaming-cloudwatch-metrics-to-vpc-based-opentelemetry-collectors-using-lambda/)
- relevance 3: [Building Memory-Intensive Apps with AWS Lambda Managed Instances](https://aws.amazon.com/blogs/compute/building-memory-intensive-apps-with-aws-lambda-managed-instances/)
- relevance 2: [Best practices for Lambda durable functions using a fraud detection example](https://aws.amazon.com/blogs/compute/best-practices-for-lambda-durable-functions-using-a-fraud-detection-example/)

#### Top Results

| Rank | Match | Title | Source | Score | Keywords |
|---:|---|---|---|---:|---|
| 1 | - | [.NET 10 runtime now available in AWS Lambda](https://aws.amazon.com/blogs/compute/net-10-runtime-now-available-in-aws-lambda/) | AWS / AWS Compute Blog | 436.65 | AWS CDK, AWS CloudFormation, AWS Lambda, Amazon EC2, migration, observability |
| 2 | - | [lambda@edge를 활용한 이미지 워터마킹](https://medium.com/zigbang/lambda-edge%EB%A5%BC-%ED%99%9C%EC%9A%A9%ED%95%9C-%EC%9D%B4%EB%AF%B8%EC%A7%80-%EC%9B%8C%ED%84%B0%EB%A7%88%ED%82%B9-41f1cb282682?source=rss----2f055286701b---4) | Zigbang / Zigbang Tech Blog | 435.34 | AWS IAM, AWS Lambda, Amazon CloudWatch, Amazon S3, Node.js |
| 3 | expected:3 | [Building Memory-Intensive Apps with AWS Lambda Managed Instances](https://aws.amazon.com/blogs/compute/building-memory-intensive-apps-with-aws-lambda-managed-instances/) | AWS / AWS Compute Blog | 424.86 | AWS CloudFormation, AWS IAM, AWS Lambda, Amazon CloudWatch, Amazon EC2, Amazon S3 |
| 4 | - | [Building fault-tolerant applications with AWS Lambda durable functions](https://aws.amazon.com/blogs/compute/building-fault-tolerant-long-running-application-with-aws-lambda-durable-functions/) | AWS / AWS Compute Blog | 421.36 | AWS CDK, AWS CloudFormation, AWS IAM, AWS Lambda, Amazon DynamoDB, Amazon S3 |
| 5 | - | [Build high-performance apps with AWS Lambda Managed Instances](https://aws.amazon.com/blogs/compute/build-high-performance-apps-with-aws-lambda-managed-instances/) | AWS / AWS Compute Blog | 416.25 | AWS IAM, AWS Lambda, Amazon CloudWatch, Amazon DynamoDB, Amazon EC2, Amazon EventBridge |
| 6 | - | [Automate AWS Lambda Runtime Upgrades with AWS Transform custom](https://aws.amazon.com/blogs/devops/automate-aws-lambda-runtime-upgrades-with-aws-transform-custom/) | AWS / AWS DevOps Blog | 416.25 | AWS CDK, AWS IAM, AWS Lambda, Amazon CloudWatch, Amazon DynamoDB, Amazon EC2 |
| 7 | - | [잘못 작성된 람다 코드를 삭제하기까지의 여정](https://helloworld.kurly.com/blog/study-in-lambda/) | Kurly / Kurly Tech Blog | 412.68 | AWS Lambda |
| 8 | - | [Optimizing Compute-Intensive Serverless Workloads with Multi-threaded Rust on AWS Lambda](https://aws.amazon.com/blogs/compute/optimizing-compute-intensive-serverless-workloads-with-multi-threaded-rust-on-aws-lambda/) | AWS / AWS Compute Blog | 395.82 | AWS CloudFormation, AWS IAM, AWS Lambda, Amazon CloudWatch, Node.js, observability |
| 9 | - | [Lambda Calculus에 대해 알아보자](https://helloworld.kurly.com/blog/lambda-calculus-1/) | Kurly / Kurly Tech Blog | 367.39 | AWS Lambda |
| 10 | expected:2 | [Best practices for Lambda durable functions using a fraud detection example](https://aws.amazon.com/blogs/compute/best-practices-for-lambda-durable-functions-using-a-fraud-detection-example/) | AWS / AWS Compute Blog | 361.04 | AWS Lambda, Amazon DynamoDB, Amazon S3, high availability, event-driven architecture, serverless |

#### Top Result Details

##### 1. .NET 10 runtime now available in AWS Lambda

- match: not expected
- source: AWS / AWS Compute Blog
- url: https://aws.amazon.com/blogs/compute/net-10-runtime-now-available-in-aws-lambda/
- technologies: AWS CDK, AWS CloudFormation, AWS Lambda, Amazon EC2
- problem keywords: migration, observability, performance optimization
- case summary: .NET 10 런타임이 AWS Lambda에서 관리형 런타임과 베이스 컨테이너 이미지로 지원되면서, 서버리스 애플리케이션 개발 시 파일 기반 앱과 Native AOT 최적화를 활용할 수 있게 되었다.
- problem: 서버리스 환경에서 .NET 애플리케이션의 실행 성능과 배포 복잡성을 개선하고, 최신 .NET 10 기능을 Lambda에서 효율적으로 활용하는 방법이 필요했다.
- solution: .NET 10 런타임과 파일 기반 C# 앱 지원, Native AOT 컴파일, Lambda Managed Instances를 도입해 실행 속도와 배포 간소화를 달성하고, AWS 도구와 통합해 개발 및 디버깅 환경을 최적화했다.

Highlights:

- title: .NET 10 runtime now available in **AWS Lambda**
- caseSolution: .NET 10 런타임과 파일 기반 C# 앱 지원, Native AOT 컴파일, **Lambda** Managed Instances를 도입해 실행 속도와 배포 간소화를 달성하고, AWS 도구와
- summary: Amazon Web Services (**AWS) Lambda** now supports .NET 10 as both a managed runtime and base container image
- summary: Developers can now use the new features and enhancements in .NET when creating serverless applications on **Lambda**
- content: If using **aws-lambda**-tools-defaults.json , then set function-runtime to dotnet10 . 5. Run dotnet **lambda** deploy-function to deploy.
- content: Right-click the project in Solution Explorer and choose Publish to **AWS Lambda** .

##### 2. lambda@edge를 활용한 이미지 워터마킹

- match: not expected
- source: Zigbang / Zigbang Tech Blog
- url: https://medium.com/zigbang/lambda-edge%EB%A5%BC-%ED%99%9C%EC%9A%A9%ED%95%9C-%EC%9D%B4%EB%AF%B8%EC%A7%80-%EC%9B%8C%ED%84%B0%EB%A7%88%ED%82%B9-41f1cb282682?source=rss----2f055286701b---4
- technologies: AWS IAM, AWS Lambda, Amazon CloudWatch, Amazon S3, Node.js
- problem keywords: -
- case summary: AWS Lambda@Edge를 활용해 CloudFront를 통해 전달되는 S3 이미지에 실시간 워터마킹을 적용한 사례입니다.
- problem: S3에 저장된 이미지를 사용자에게 전달할 때 별도의 서버 부하 없이 이미지에 워터마크를 동적으로 삽입하는 방법이 필요했습니다.
- solution: CloudFront의 요청/응답 흐름에 Lambda@Edge 함수를 배포하여 이미지 요청 시점에 워터마크를 삽입하는 방식을 사용했습니다. Node.js 기반의 Lambda 함수에서 Sharp 라이브러리를 활용해 워터마크 이미지를 원본 크기에 맞게 조절하고 합성하여 처리했습니다.

Highlights:

- title: **lambda**@edge를 활용한 이미지 워터마킹
- caseSummary: **AWS Lambda**@Edge를 활용해 CloudFront를 통해 전달되는 S3 이미지에 실시간 워터마킹을 적용한 사례입니다.
- caseSolution: CloudFront의 요청/응답 흐름에 **Lambda**@Edge 함수를 배포하여 이미지 요청 시점에 워터마크를 삽입하는 방식을 사용했습니다.
- caseSolution: Node.js 기반의 **Lambda** 함수에서 Sharp 라이브러리를 활용해 워터마크 이미지를 원본 크기에 맞게 조절하고 합성하여 처리했습니다.
- summary: 이번 포스팅에서는 **AWS lambda**@edge를 활용하여 이미지에 워터마킹 하는방법에 대해서 이야기 해보겠습니다.
- summary: 다음은 **lambda**@edge 에 대한 AWS 에 설명입니다.

##### 3. Building Memory-Intensive Apps with AWS Lambda Managed Instances

- match: expected relevance 3
- source: AWS / AWS Compute Blog
- url: https://aws.amazon.com/blogs/compute/building-memory-intensive-apps-with-aws-lambda-managed-instances/
- technologies: AWS CloudFormation, AWS IAM, AWS Lambda, Amazon CloudWatch, Amazon EC2, Amazon S3, Amazon VPC, search
- problem keywords: observability, performance optimization
- case summary: AWS Lambda Managed Instances를 활용해 최대 32GB 메모리로 메모리 집약적 서버리스 애플리케이션을 구축하고, AI 기반 고객 분석을 통해 실시간 대규모 데이터 처리와 ML 추론을 구현한 사례이다.
- problem: 기존 AWS Lambda의 10GB 메모리 제한으로 인해 대규모 데이터셋 처리, 복잡한 ML 모델 추론, 실시간 의미 기반 검색 등 메모리 집약적 워크로드를 서버리스 환경에서 실행하기 어려웠다.
- solution: AWS Lambda Managed Instances를 사용해 메모리 최적화 EC2 인스턴스에서 Lambda 함수를 실행함으로써 최대 32GB 메모리를 활용하고, 서버리스의 운영 편의성을 유지하며 대규모 데이터셋과 ML 모델을 메모리에 적재해 실시간 분석 및 검색을 구현했다.

Highlights:

- title: Building Memory-Intensive Apps with **AWS Lambda** Managed Instances
- caseSummary: **AWS Lambda** Managed Instances를 활용해 최대 32GB 메모리로 메모리 집약적 서버리스 애플리케이션을 구축하고, AI 기반 고객 분석을 통해 실시간 대규모 데이터
- caseSolution: **AWS Lambda** Managed Instances를 사용해 메모리 최적화 EC2 인스턴스에서 **Lambda** 함수를 실행함으로써 최대 32GB 메모리를 활용하고, 서버리스의 운영 편의성을
- summary: Building memory-intensive applications with **AWS Lambda** just got easier.
- summary: **AWS Lambda** Managed Instances gives you up to 32 GB of memory—3x more than standard **AWS Lambda**—while maintaining
- content: **AWS Lambda** Managed Instances gives you up to 32 GB of memory—3x more than standard **AWS Lambda**—while maintaining the serverless experience you know.


### tech-dynamodb - `DynamoDB`

- category: technology
- intent: DynamoDB 마이그레이션, 데이터 export, 분석 연동 사례를 찾는다.
- total results: 38
- precision@5: 0.600
- recall@10: 1.000
- mrr: 1.000
- ndcg@10: 0.974

#### Expected URLs

- relevance 3: [Zero-downtime DynamoDB construct migration: from Table to TableV2 with cdk orphan](https://aws.amazon.com/blogs/database/zero-downtime-dynamodb-construct-migration-from-table-to-tablev2-with-cdk-orphan/)
- relevance 3: [Filter, transform, and load your DynamoDB table exports using AWS Glue](https://aws.amazon.com/blogs/database/filter-transform-and-load-your-dynamodb-table-exports-using-aws-glue/)
- relevance 2: [Improve DynamoDB analytics with AWS Glue zero-ETL schema and partition controls](https://aws.amazon.com/blogs/big-data/improve-dynamodb-analytics-with-aws-glue-zero-etl-schema-and-partition-controls/)

#### Top Results

| Rank | Match | Title | Source | Score | Keywords |
|---:|---|---|---|---:|---|
| 1 | expected:3 | [Filter, transform, and load your DynamoDB table exports using AWS Glue](https://aws.amazon.com/blogs/database/filter-transform-and-load-your-dynamodb-table-exports-using-aws-glue/) | AWS / AWS Database Blog | 446.78 | AWS Glue, Amazon DynamoDB, Amazon S3, Java, migration, observability |
| 2 | expected:3 | [Zero-downtime DynamoDB construct migration: from Table to TableV2 with cdk orphan](https://aws.amazon.com/blogs/database/zero-downtime-dynamodb-construct-migration-from-table-to-tablev2-with-cdk-orphan/) | AWS / AWS Database Blog | 403.71 | AWS CDK, AWS CloudFormation, AWS IAM, AWS Lambda, Amazon DynamoDB, Node.js |
| 3 | - | [Spring Boot에서 Repository로 DynamoDB 조작하기 (1) – 설정부터 실행까지](https://techblog.woowahan.com/2633/) | Woowa Brothers / Woowa Tech Blog | 398.25 | Amazon DynamoDB, JPA, Java, React, Spring Boot, performance optimization |
| 4 | - | [Spring Boot에서 Repository로 DynamoDB 조작하기 (2) – Gradle을 활용해 실행 & 테스팅 환경 구축](https://techblog.woowahan.com/2634/) | Woowa Brothers / Woowa Tech Blog | 355.23 | Amazon DynamoDB, Java, Spring Boot |
| 5 | expected:2 | [Improve DynamoDB analytics with AWS Glue zero-ETL schema and partition controls](https://aws.amazon.com/blogs/big-data/improve-dynamodb-analytics-with-aws-glue-zero-etl-schema-and-partition-controls/) | AWS / AWS Big Data Blog | 355.17 | AWS Glue, AWS IAM, Amazon CloudWatch, Amazon DynamoDB, Amazon S3, Apache Iceberg |
| 6 | - | [Serverless ICYMI Q1 2026](https://aws.amazon.com/blogs/compute/serverless-icymi-q1-2026/) | AWS / AWS Compute Blog | 331.17 | AWS CDK, AWS Lambda, Amazon DynamoDB, Amazon EC2, Amazon EventBridge, Java |
| 7 | - | [LocalStack을 활용한 Integration Test 환경 만들기](https://techblog.woowahan.com/2638/) | Woowa Brothers / Woowa Tech Blog | 331.14 | AWS Lambda, Amazon DynamoDB, Amazon S3, Java, Spring Boot |
| 8 | - | [Build a multi-tenant configuration system with tagged storage patterns](https://aws.amazon.com/blogs/architecture/build-a-multi-tenant-configuration-system-with-tagged-storage-patterns/) | AWS / AWS Architecture Blog | 252.04 | AWS CloudFormation, AWS IAM, AWS Lambda, Amazon CloudWatch, Amazon DynamoDB, Amazon ElastiCache |
| 9 | - | [Building zero trust generative AI applications in healthcare with AWS Nitro Enclaves](https://aws.amazon.com/blogs/compute/building-zero-trust-generative-ai-applications-in-healthcare-with-aws-nitro-enclaves/) | AWS / AWS Compute Blog | 250.98 | AWS IAM, AWS Lambda, Amazon DynamoDB, Amazon EC2, Amazon S3, LLM |
| 10 | - | [배달의민족 최전방 시스템! ‘가게노출 시스템’을 소개합니다.](https://techblog.woowahan.com/2667/) | Woowa Brothers / Woowa Tech Blog | 250.55 | Amazon CloudWatch, Amazon DynamoDB, Amazon ElastiCache, JVM, Java, Kotlin |

#### Top Result Details

##### 1. Filter, transform, and load your DynamoDB table exports using AWS Glue

- match: expected relevance 3
- source: AWS / AWS Database Blog
- url: https://aws.amazon.com/blogs/database/filter-transform-and-load-your-dynamodb-table-exports-using-aws-glue/
- technologies: AWS Glue, Amazon DynamoDB, Amazon S3, Java
- problem keywords: migration, observability, performance optimization
- case summary: AWS Glue와 Bulk Executor를 활용해 DynamoDB 전체 및 증분 테이블 내보내기 데이터를 필터링, 변환, 제어된 속도로 다른 DynamoDB 테이블에 로드하는 방법을 다룬다.
- problem: DynamoDB 테이블 내보내기 데이터를 기존 테이블에 원하는 조건으로 필터링, 변환하며 대규모로 안정적이고 제어된 속도로 로드하는 기능이 부족했다.
- solution: AWS Glue 기반 Bulk Executor의 load-export 명령어를 사용해 S3에 저장된 전체 및 증분 내보내기 데이터를 병렬 처리, 변환 함수 적용, 쓰기 속도 제한과 진행 상황 관찰 기능을 통해 기존 DynamoDB 테이블에 유연하게 로드한다.

Highlights:

- title: Filter, transform, and load your **DynamoDB** table exports using AWS Glue
- caseSummary: AWS Glue와 Bulk Executor를 활용해 **DynamoDB** 전체 및 증분 테이블 내보내기 데이터를 필터링, 변환, 제어된 속도로 다른 **DynamoDB** 테이블에 로드하는 방법을
- caseProblem: **DynamoDB** 테이블 내보내기 데이터를 기존 테이블에 원하는 조건으로 필터링, 변환하며 대규모로 안정적이고 제어된 속도로 로드하는 기능이 부족했다.
- caseSolution: Executor의 load-export 명령어를 사용해 S3에 저장된 전체 및 증분 내보내기 데이터를 병렬 처리, 변환 함수 적용, 쓰기 속도 제한과 진행 상황 관찰 기능을 통해 기존 **DynamoDB**
- summary: In this post, we show how you can load (import) an **Amazon DynamoDB** full or incremental table export into
- summary: a second **DynamoDB** table with precise control over what gets loaded, at what write rate, and with the

##### 2. Zero-downtime DynamoDB construct migration: from Table to TableV2 with cdk orphan

- match: expected relevance 3
- source: AWS / AWS Database Blog
- url: https://aws.amazon.com/blogs/database/zero-downtime-dynamodb-construct-migration-from-table-to-tablev2-with-cdk-orphan/
- technologies: AWS CDK, AWS CloudFormation, AWS IAM, AWS Lambda, Amazon DynamoDB, Node.js
- problem keywords: migration, performance optimization
- case summary: AWS CDK의 DynamoDB Table에서 TableV2로 무중단 마이그레이션을 cdk orphan 명령어를 활용해 수행하는 방법을 다룹니다.
- problem: 기존 CDK의 Table construct를 TableV2로 교체 시 CloudFormation이 리소스를 교체하며 데이터 손실과 서비스 중단이 발생하는 문제.
- solution: cdk orphan 명령어로 기존 테이블을 CloudFormation 스택에서 분리한 후, TableV2 construct로 동일 테이블을 재임포트하여 무중단 마이그레이션을 수행.

Highlights:

- title: Zero-downtime **DynamoDB** construct migration: from Table to TableV2 with cdk orphan
- caseSummary: AWS CDK의 **DynamoDB** Table에서 TableV2로 무중단 마이그레이션을 cdk orphan 명령어를 활용해 수행하는 방법을 다룹니다.
- summary: In this post, we show you how to use the new cdk orphan command to safely migrate a **DynamoDB** table from
- content: When you define an **Amazon DynamoDB** table using the AWS Cloud Development Kit (AWS CDK), you have two construct options: Table and TableV2 .
- content: **Amazon DynamoDB** Database Engineer based in Donegal, Ireland.

##### 3. Spring Boot에서 Repository로 DynamoDB 조작하기 (1) – 설정부터 실행까지

- match: not expected
- source: Woowa Brothers / Woowa Tech Blog
- url: https://techblog.woowahan.com/2633/
- technologies: Amazon DynamoDB, JPA, Java, React, Spring Boot
- problem keywords: performance optimization
- case summary: 우아한형제들에서 MongoDB를 DynamoDB로 교체하며 Spring Boot 환경에서 DynamoDB를 다양한 방법으로 조작하는 과정을 단계별로 실습하고, 특히 spring-data-dynamodb를 활용한 객체 매핑과 쿼리 메서드 사용법을 소개한다.
- problem: 기존 MongoDB 기반 NoSQL 시스템을 AWS DynamoDB로 전환하면서 DynamoDB 조작 방법과 Spring Boot 연동 방식을 익히고, 로컬 개발 환경에서 효율적으로 DynamoDB를 다루는 방법이 필요했다.
- solution: aws cli, curl, AWS Java SDK, DynamoDBMapper, spring-data-dynamodb 순으로 DynamoDB 조작법을 실습하며, 로컬 DynamoDB 도커 이미지 활용, Java 테스트 코드 작성, 그리고 spring-data-dynamodb를 통한 객체 매핑 및 쿼리 메서드 구현까지 단계별 접근을 통해 DynamoDB를 효과적으로 다루는 방법을 제시했다.

Highlights:

- title: Spring Boot에서 Repository로 **DynamoDB** 조작하기 (1) – 설정부터 실행까지
- caseProblem: 기존 MongoDB 기반 NoSQL 시스템을 AWS DynamoDB로 전환하면서 **DynamoDB** 조작 방법과 Spring Boot 연동 방식을 익히고, 로컬 개발 환경에서 효율적으로
- caseSolution: aws cli, curl, AWS Java SDK, DynamoDBMapper, spring-data-**dynamodb** 순으로 **DynamoDB** 조작법을 실습하며, 로컬 **DynamoDB**
- summary: 다양한 방법들을 예제를 통해 소개합니다. aws cli -> curl -> AmazonDynamoDB 클래스 -> DynamoDBMapper 클래스 -> spring-data-**dynamodb**
- content: DynamoDB를 써보자 aws cli로 **DynamoDB** 조작하기 테이블 생성 항목 추가 항목 조회 항목 수정 항목 삭제 테이블 삭제 curl로 **DynamoDB** 조작하기 테이블 생성 항목 추가 항목 조회 항목 수정 항목 삭제 테이블 삭제 Java **DynamoDB** SDK로 **DynamoDB**
- content: /usr/bin/env bash docker pull **amazon/dynamodb**-local docker run -p 8000:8000 **amazon/dynamodb**-local -jar DynamoDBLocal.jar -inMemory -sharedDb 포트 8000번에 로컬 DynamoDB를


### tech-eks - `EKS`

- category: technology
- intent: Amazon EKS 운영, 환경 프로비저닝, 이벤트 대응 사례를 찾는다.
- total results: 29
- precision@5: 0.600
- recall@10: 1.000
- mrr: 1.000
- ndcg@10: 0.784

#### Expected URLs

- relevance 3: [Deloitte optimizes EKS environment provisioning and achieves 89% faster testing environments using Amazon EKS and vCluster](https://aws.amazon.com/blogs/architecture/deloitte-optimizes-eks-environment-provisioning-and-achieves-89-faster-testing-environments-using-amazon-eks-and-vcluster/)
- relevance 3: [How Generali Malaysia optimizes operations with Amazon EKS](https://aws.amazon.com/blogs/architecture/how-generali-malaysia-optimizes-operations-with-amazon-eks/)
- relevance 2: [AI-powered event response for Amazon EKS](https://aws.amazon.com/blogs/architecture/ai-powered-event-response-for-amazon-eks/)

#### Top Results

| Rank | Match | Title | Source | Score | Keywords |
|---:|---|---|---|---:|---|
| 1 | expected:2 | [AI-powered event response for Amazon EKS](https://aws.amazon.com/blogs/architecture/ai-powered-event-response-for-amazon-eks/) | AWS / AWS Architecture Blog | 467.46 | AWS CDK, AWS CloudFormation, AWS IAM, Amazon CloudWatch, Amazon EKS, Java |
| 2 | expected:3 | [How Generali Malaysia optimizes operations with Amazon EKS](https://aws.amazon.com/blogs/architecture/how-generali-malaysia-optimizes-operations-with-amazon-eks/) | AWS / AWS Architecture Blog | 447.67 | AWS IAM, Amazon CloudWatch, Amazon EC2, Amazon EKS, Kubernetes, cost optimization |
| 3 | - | [EKS Anywhere 구축기](https://techblog.woowahan.com/10221/) | Woowa Brothers / Woowa Tech Blog | 441.34 | AWS CloudFormation, AWS IAM, Amazon CloudWatch, Amazon EC2, Amazon EKS, Amazon S3 |
| 4 | - | [Optimizing storage performance for Amazon EKS on AWS Outposts](https://aws.amazon.com/blogs/compute/optimizing-storage-performance-for-amazon-eks-on-aws-outposts/) | AWS / AWS Compute Blog | 423.49 | AWS IAM, Amazon CloudWatch, Amazon EKS, Amazon S3, Kubernetes, cost optimization |
| 5 | expected:3 | [Deloitte optimizes EKS environment provisioning and achieves 89% faster testing environments using Amazon EKS and vCluster](https://aws.amazon.com/blogs/architecture/deloitte-optimizes-eks-environment-provisioning-and-achieves-89-faster-testing-environments-using-amazon-eks-and-vcluster/) | AWS / AWS Architecture Blog | 404.73 | AWS IAM, Amazon EC2, Amazon EKS, Amazon VPC, Kubernetes, cost optimization |
| 6 | - | [EKS Bottlerocket에서 이미지 캐싱으로 Pull 시간 줄이기](https://tech.inflab.com/20250421-bottlerocket-volume-image-cache/) | Inflab / Inflab Tech Blog | 390.39 | AWS CloudFormation, Amazon EC2, Amazon EKS, Amazon S3, Kubernetes, cost optimization |
| 7 | - | [Job 워크로드를 위한 EKS Node Group 오토스케일링 도입기](https://medium.com/daangn/job-%EC%9B%8C%ED%81%AC%EB%A1%9C%EB%93%9C%EB%A5%BC-%EC%9C%84%ED%95%9C-eks-node-group-%EC%98%A4%ED%86%A0%EC%8A%A4%EC%BC%80%EC%9D%BC%EB%A7%81-%EB%8F%84%EC%9E%85%EA%B8%B0-a6a28376d153?source=rss----4505f82a2dbd---4) | Daangn / Daangn Tech Blog | 381.08 | Amazon EC2, Amazon EKS, Amazon VPC, Istio, Kubernetes, cost optimization |
| 8 | - | [EKS Bottlerocket AMI에서 DCGM 오류로 GPU 노드 반복 교체 문제 해결기](https://tech.inflab.com/20250827-bottlerocket-ami-gpu-issue/) | Inflab / Inflab Tech Blog | 380.85 | Amazon EC2, Amazon EKS, Kubernetes, observability |
| 9 | - | [EKS에서 쿠버네티스 포드의 IAM 권한 제어하기: Pod Identity Webhook](https://tech.devsisters.com/posts/pod-iam-role) | Devsisters / Devsisters Tech Blog | 378.36 | AWS IAM, Amazon EC2, Amazon EKS, Kubernetes |
| 10 | - | [Our Journey to Autoscaling EKS Node Groups for Job Workloads](https://medium.com/daangn/our-journey-to-autoscaling-eks-node-groups-for-job-workloads-e8a6a7ed845e?source=rss----4505f82a2dbd---4) | Daangn / Daangn Tech Blog | 365.20 | Amazon EC2, Amazon EKS, Amazon VPC, Istio, Kubernetes, cost optimization |

#### Top Result Details

##### 1. AI-powered event response for Amazon EKS

- match: expected relevance 2
- source: AWS / AWS Architecture Blog
- url: https://aws.amazon.com/blogs/architecture/ai-powered-event-response-for-amazon-eks/
- technologies: AWS CDK, AWS CloudFormation, AWS IAM, Amazon CloudWatch, Amazon EKS, Java, Kubernetes, OpenTelemetry
- problem keywords: incident response, migration, observability, performance optimization
- case summary: AWS DevOps Agent를 활용해 Amazon EKS 클러스터 내 마이크로서비스의 이벤트를 AI 기반으로 자동 탐지 및 대응하는 사례로, 복잡한 Kubernetes 리소스 간 관계를 이해하고 신속한 근본 원인 분석을 지원한다.
- problem: 대규모 마이크로서비스 환경에서 수천 건의 이벤트 신호를 효과적으로 모니터링하고, 신속하고 정확한 근본 원인 분석 및 자동화된 사건 대응이 어려운 상황.
- solution: Amazon EKS와 통합된 AWS DevOps Agent를 배포하여 OpenTelemetry, CloudWatch, X-Ray 등 다양한 관찰 가능성 데이터를 AI와 머신러닝으로 분석하고, Kubernetes 리소스 간 의존성을 파악해 자동으로 이상 징후를 탐지하고 대응하는 시스템 구축.

Highlights:

- title: AI-powered event response for **Amazon EKS**
- caseSummary: AWS DevOps Agent를 활용해 **Amazon EKS** 클러스터 내 마이크로서비스의 이벤트를 AI 기반으로 자동 탐지 및 대응하는 사례로, 복잡한 Kubernetes 리소스 간
- content: Figure 1: This is an example of target architecture of how **Amazon EKS** workloads are deployed and how AWS DevOps agent can interact with the different managed services
- content: Amazon Elastic Kubernetes Service (**Amazon EKS**) cluster version 1.27 or later OpenTelemetry Operator installed for telemetry collection Amazon Managed Service for

##### 2. How Generali Malaysia optimizes operations with Amazon EKS

- match: expected relevance 3
- source: AWS / AWS Architecture Blog
- url: https://aws.amazon.com/blogs/architecture/how-generali-malaysia-optimizes-operations-with-amazon-eks/
- technologies: AWS IAM, Amazon CloudWatch, Amazon EC2, Amazon EKS, Kubernetes
- problem keywords: cost optimization, high availability, migration, observability, performance optimization
- case summary: Generali Malaysia는 Amazon EKS Auto Mode와 AWS 서비스 통합을 활용해 보험업계의 클라우드 전환과 디지털 서비스 수요 증가에 대응하며 운영 효율성, 보안, 비용 최적화를 달성했다.
- problem: 레거시 애플리케이션의 클라우드 마이그레이션과 다수 컨테이너화된 마이크로서비스의 확장에 따른 운영 복잡성, 비용 과다 지출, 보안 및 컴플라이언스 관리 어려움이 있었다.
- solution: Amazon EKS Auto Mode를 도입해 클러스터 인프라 자동 관리 및 확장, AWS IAM과 네트워크 정책을 통한 보안 강화, Amazon GuardDuty, Inspector, Network Firewall, Secrets Manager 등 AWS 보안 서비스와 통합하여 위협 탐지 및 비밀 관리 자동화, 비용 최적화를 위한 태그 기반 비용 할당과 Savings Plans 활용, Amazon Managed Grafana를 통한 세분화된 모니터링 대시보드 구축으로 운영 효율성과 신뢰성을 확보했다.

Highlights:

- title: How Generali Malaysia optimizes operations with **Amazon EKS**
- caseSummary: Generali Malaysia는 **Amazon EKS** Auto Mode와 AWS 서비스 통합을 활용해 보험업계의 클라우드 전환과 디지털 서비스 수요 증가에 대응하며 운영 효율성, 보안
- caseSolution: **Amazon EKS** Auto Mode를 도입해 클러스터 인프라 자동 관리 및 확장, AWS IAM과 네트워크 정책을 통한 보안 강화, Amazon GuardDuty, Inspector
- summary: In this post, we look at how Generali is using **Amazon EKS** Auto Mode and its integration with other AWS
- content: Previous experience of the Generali DevOps and Cloud team was also a strong factor in selecting **Amazon EKS**.
- content: If you’re interested in learning more about **Amazon EKS**, refer to **Amazon EKS** Best Practices Guide .

##### 3. EKS Anywhere 구축기

- match: not expected
- source: Woowa Brothers / Woowa Tech Blog
- url: https://techblog.woowahan.com/10221/
- technologies: AWS CloudFormation, AWS IAM, Amazon CloudWatch, Amazon EC2, Amazon EKS, Amazon S3, Amazon VPC, Kubernetes, search
- problem keywords: migration, observability
- case summary: 우아한형제들 데이터플랫폼팀은 온프레미스 Hadoop 클러스터를 재활용해 MLOps 플랫폼용 Kubernetes 클러스터를 구축하며, AWS EKS Anywhere를 활용해 베어메탈 환경에서 Kubernetes 클러스터를 설치하고 운영하는 과정에서 발생한 문제와 해결책을 공유한다.
- problem: AWS 이관으로 온프레미스 Hadoop 인프라 사용성이 감소하고, GPU 인프라 부족 문제를 해결하기 위해 온프레미스 환경에 Kubernetes 클러스터를 구축해야 했으며, 베어메탈 환경에서 EKS Anywhere 설치 및 운영 시 기능 제한과 인증 문제 등 다양한 기술적 어려움에 직면했다.
- solution: AWS EKS Anywhere를 선택해 베어메탈 환경에 Kubernetes 클러스터를 구축하고, Tinkerbell 오픈소스를 이용한 자동화 프로비저닝을 적용했으며, 수동 설정과 삽질을 통해 AWS IAM Authenticator 문제 등 인증 및 관리 기능 미지원 문제를 극복했다.

Highlights:

- title: **EKS** Anywhere 구축기
- caseSummary: 우아한형제들 데이터플랫폼팀은 온프레미스 Hadoop 클러스터를 재활용해 MLOps 플랫폼용 Kubernetes 클러스터를 구축하며, AWS **EKS** Anywhere를 활용해 베어메탈
- caseProblem: 이관으로 온프레미스 Hadoop 인프라 사용성이 감소하고, GPU 인프라 부족 문제를 해결하기 위해 온프레미스 환경에 Kubernetes 클러스터를 구축해야 했으며, 베어메탈 환경에서 **EKS**
- caseSolution: AWS **EKS** Anywhere를 선택해 베어메탈 환경에 Kubernetes 클러스터를 구축하고, Tinkerbell 오픈소스를 이용한 자동화 프로비저닝을 적용했으며, 수동 설정과 삽질을
- summary: MLOps 플랫폼 내 컨테이너를 관리하기 위한 도구로 **EKS** Anywhere를 채택하였습니다.
- summary: 이 글에서는 **EKS** Anywhere의 소개와 함께 구축하면서 마주했던 문제들과 이를 해결한 과정에 대해 공유드리고자 합니다. 천상계로의 배달 그 이후… […]


### tech-opensearch - `OpenSearch`

- category: technology
- intent: OpenSearch가 검색, 관측성, 데이터 통합, 복원력 구성에 쓰인 사례를 찾는다.
- total results: 19
- precision@5: 0.600
- recall@10: 1.000
- mrr: 1.000
- ndcg@10: 0.898

#### Expected URLs

- relevance 3: [How to build a cross-Region resilience for Amazon OpenSearch Service with Amazon MSK](https://aws.amazon.com/blogs/big-data/how-to-build-a-cross-region-resilience-for-amazon-opensearch-service-with-amazon-msk/)
- relevance 3: [How to consolidate cross-Region S3 data into OpenSearch](https://aws.amazon.com/blogs/big-data/how-to-consolidate-cross-region-s3-data-into-opensearch/)
- relevance 2: [Unified observability in Amazon OpenSearch Service: metrics, traces, and AI agent debugging in a single interface](https://aws.amazon.com/blogs/big-data/unified-observability-in-amazon-opensearch-service-metrics-traces-and-ai-agent-debugging-in-a-single-interface/)

#### Top Results

| Rank | Match | Title | Source | Score | Keywords |
|---:|---|---|---|---:|---|
| 1 | expected:3 | [How to build a cross-Region resilience for Amazon OpenSearch Service with Amazon MSK](https://aws.amazon.com/blogs/big-data/how-to-build-a-cross-region-resilience-for-amazon-opensearch-service-with-amazon-msk/) | AWS / AWS Big Data Blog | 523.22 | AWS CloudFormation, AWS IAM, AWS Lambda, Amazon CloudWatch, Amazon MSK, Amazon OpenSearch Service |
| 2 | expected:2 | [Unified observability in Amazon OpenSearch Service: metrics, traces, and AI agent debugging in a single interface](https://aws.amazon.com/blogs/big-data/unified-observability-in-amazon-opensearch-service-metrics-traces-and-ai-agent-debugging-in-a-single-interface/) | AWS / AWS Big Data Blog | 475.60 | AWS IAM, Amazon OpenSearch Service, LLM, OpenTelemetry, search, observability |
| 3 | - | [OpenSearch Analyzer를 활용한 검색기능 알아보기](https://tech.kakaopay.com/post/kakaopayins-opensearch-analyzer/) | Kakao Pay / Kakao Pay Tech Blog | 460.12 | Amazon OpenSearch Service, search |
| 4 | - | [후기 서비스 AWS Opensearch 도입기](https://helloworld.kurly.com/blog/2023-review-opensearch/) | Kurly / Kurly Tech Blog | 460.12 | Amazon OpenSearch Service |
| 5 | expected:3 | [How to consolidate cross-Region S3 data into OpenSearch](https://aws.amazon.com/blogs/big-data/how-to-consolidate-cross-region-s3-data-into-opensearch/) | AWS / AWS Big Data Blog | 448.61 | AWS IAM, Amazon OpenSearch Service, Amazon S3, Amazon VPC, search, observability |
| 6 | - | [배달의민족 광고데이터 이관기](https://techblog.woowahan.com/14041/) | Woowa Brothers / Woowa Tech Blog | 416.17 | Amazon OpenSearch Service, Elasticsearch, JVM, search, cost optimization, migration |
| 7 | - | [Detect and resolve HBase inconsistencies faster with AI on Amazon EMR](https://aws.amazon.com/blogs/big-data/detect-and-resolve-hbase-inconsistencies-faster-with-ai-on-amazon-emr/) | AWS / AWS Big Data Blog | 397.65 | AWS CloudFormation, AWS IAM, AWS Lambda, Amazon CloudWatch, Amazon EC2, Amazon OpenSearch Service |
| 8 | - | [데이터카탈로그에서 DataHub를 이용하는 방법](https://techblog.woowahan.com/21434/) | Woowa Brothers / Woowa Tech Blog | 371.30 | Amazon EKS, Amazon OpenSearch Service, Amazon S3, Apache Kafka, Elasticsearch, Java |
| 9 | - | [Orchestrating large-scale document processing with AWS Step Functions and Amazon Bedrock batch inference](https://aws.amazon.com/blogs/compute/orchestrating-large-scale-document-processing-with-aws-step-functions-and-amazon-bedrock-batch-inference/) | AWS / AWS Compute Blog | 334.13 | AWS CDK, AWS CloudFormation, AWS IAM, AWS Lambda, Amazon DynamoDB, Amazon EventBridge |
| 10 | - | [실시간 반응형 추천 개발 일지 2부: 벡터 검색, 그리고 숨겨진 요구사항과 기술 도입 의사 결정을 다루는 방법](https://techblog.woowahan.com/21027/) | Woowa Brothers / Woowa Tech Blog | 324.75 | AWS Lambda, Amazon OpenSearch Service, Amazon RDS, Kubernetes, LLM, Redis |

#### Top Result Details

##### 1. How to build a cross-Region resilience for Amazon OpenSearch Service with Amazon MSK

- match: expected relevance 3
- source: AWS / AWS Big Data Blog
- url: https://aws.amazon.com/blogs/big-data/how-to-build-a-cross-region-resilience-for-amazon-opensearch-service-with-amazon-msk/
- technologies: AWS CloudFormation, AWS IAM, AWS Lambda, Amazon CloudWatch, Amazon MSK, Amazon OpenSearch Service, Amazon S3, Amazon VPC, Apache Kafka, search
- problem keywords: high availability, observability, performance optimization
- case summary: Amazon OpenSearch Service와 Amazon MSK를 활용해 AWS 리전 간 실시간 데이터 동기화 및 액티브-액티브 복제를 구현하여 고가용성과 장애 복구를 자동화한 사례입니다.
- problem: 기존 Amazon OpenSearch Service의 리전 간 복제는 S3 스냅샷이나 크로스 클러스터 복제에 의존해 수동 장애 조치가 필요하고, 이로 인해 다운타임과 데이터 불일치, 지연이 발생하는 문제가 있었습니다.
- solution: Amazon MSK Replicator를 이용한 양방향 리전 간 데이터 복제와 Amazon OpenSearch Ingestion(OSI) 파이프라인을 결합해 액티브-액티브 모델을 구축, 각 리전에서 동일한 데이터셋을 유지하며 자동 장애 조치와 데이터 동기화를 실현했습니다.

Highlights:

- title: How to build a cross-Region resilience for **Amazon OpenSearch Service** with Amazon MSK
- caseSummary: Amazon **OpenSearch** Service와 Amazon MSK를 활용해 AWS 리전 간 실시간 데이터 동기화 및 액티브-액티브 복제를 구현하여 고가용성과 장애 복구를 자동화한
- caseProblem: 기존 Amazon **OpenSearch** Service의 리전 간 복제는 S3 스냅샷이나 크로스 클러스터 복제에 의존해 수동 장애 조치가 필요하고, 이로 인해 다운타임과 데이터 불일치,
- caseSolution: Amazon MSK Replicator를 이용한 양방향 리전 간 데이터 복제와 Amazon **OpenSearch** Ingestion(OSI) 파이프라인을 결합해 액티브-액티브 모델을 구축
- summary: reestablish relationships during a fail-back, using an active-active replication model with Amazon **OpenSearch**
- summary: This solution applies to both **OpenSearch** Service managed clusters and Amazon **OpenSearch** Serverless collections

##### 2. Unified observability in Amazon OpenSearch Service: metrics, traces, and AI agent debugging in a single interface

- match: expected relevance 2
- source: AWS / AWS Big Data Blog
- url: https://aws.amazon.com/blogs/big-data/unified-observability-in-amazon-opensearch-service-metrics-traces-and-ai-agent-debugging-in-a-single-interface/
- technologies: AWS IAM, Amazon OpenSearch Service, LLM, OpenTelemetry, search
- problem keywords: observability, performance optimization
- case summary: Amazon OpenSearch Service는 OpenTelemetry 기반 AI 에이전트 추적과 Amazon Managed Service for Prometheus 통합을 통해 단일 인터페이스에서 메트릭, 트레이스, 로그를 통합 관찰하며, AI 에이전트 및 마이크로서비스 문제를 신속하게 진단할 수 있는 사례를 소개한다.
- problem: 멀티 에이전트 여행 플래너의 지연 문제와 전자상거래 체크아웃 마이크로서비스의 조용한 실패 현상 등 복잡한 분산 시스템에서 발생하는 성능 저하 및 오류 원인 파악이 어려웠다.
- solution: OpenTelemetry의 AI 에이전트용 시맨틱 트레이싱과 Prometheus 메트릭 통합을 활용해 OpenSearch UI 내에서 AI 에이전트의 추론 체인과 마이크로서비스의 RED 지표, PromQL 쿼리를 단일 관찰 공간에서 분석하여 근본 원인을 신속히 진단했다.

Highlights:

- title: Unified observability in **Amazon OpenSearch Service**: metrics, traces, and AI agent debugging in a single
- caseSummary: Amazon **OpenSearch** Service는 OpenTelemetry 기반 AI 에이전트 추적과 Amazon Managed Service for Prometheus 통합을 통해
- caseSolution: OpenTelemetry의 AI 에이전트용 시맨틱 트레이싱과 Prometheus 메트릭 통합을 활용해 **OpenSearch** UI 내에서 AI 에이전트의 추론 체인과 마이크로서비스의 RED
- summary: **Amazon OpenSearch Service** now brings application monitoring, native Amazon Managed Service for Prometheus
- summary: integration, and AI agent tracing together in **OpenSearch** UI's observability workspace.
- content: **Amazon OpenSearch Service** now brings application monitoring, native Amazon Managed Service for Prometheus integration, and AI agent tracing together in **OpenSearch**

##### 3. OpenSearch Analyzer를 활용한 검색기능 알아보기

- match: not expected
- source: Kakao Pay / Kakao Pay Tech Blog
- url: https://tech.kakaopay.com/post/kakaopayins-opensearch-analyzer/
- technologies: Amazon OpenSearch Service, search
- problem keywords: -
- case summary: 카카오페이는 OpenSearch Analyzer를 활용해 검색 기능을 구현하며, 이를 통해 효율적인 텍스트 분석과 검색 정확도 향상을 달성했다.
- problem: 검색 서비스에서 텍스트 분석과 색인 과정의 효율성 및 정확도를 높이는 것이 필요했다.
- solution: Amazon OpenSearch Service의 Analyzer 기능을 활용하여 텍스트를 효과적으로 분해하고 색인해 검색 성능을 개선했다.

Highlights:

- title: **OpenSearch** Analyzer를 활용한 검색기능 알아보기
- caseSummary: 카카오페이는 **OpenSearch** Analyzer를 활용해 검색 기능을 구현하며, 이를 통해 효율적인 텍스트 분석과 검색 정확도 향상을 달성했다.
- caseSolution: Amazon **OpenSearch** Service의 Analyzer 기능을 활용하여 텍스트를 효과적으로 분해하고 색인해 검색 성능을 개선했다.
- summary: **OpenSearch** Analyzer를 활용한 검색 서비스를 간단한 예제와 함께 알아봅니다.


### tech-apache-flink - `Apache Flink`

- category: technology
- intent: Apache Flink 기반 스트리밍 애플리케이션과 데이터 파이프라인 사례를 찾는다.
- total results: 9
- precision@5: 0.600
- recall@10: 1.000
- mrr: 1.000
- ndcg@10: 0.808

#### Expected URLs

- relevance 3: [Build streaming applications on Amazon Managed Service for Apache Flink with AI-assisted guidance](https://aws.amazon.com/blogs/big-data/build-streaming-applications-on-amazon-managed-service-for-apache-flink-with-ai-assisted-guidance/)
- relevance 2: [Migrate to Apache Flink 2.2 on Amazon Managed Service for Apache Flink](https://aws.amazon.com/blogs/big-data/migrate-to-apache-flink-2-2-on-amazon-managed-service-for-apache-flink/)
- relevance 3: [Building unified data pipelines with Apache Iceberg and Apache Flink](https://aws.amazon.com/blogs/big-data/building-unified-data-pipelines-with-apache-iceberg-and-apache-flink/)

#### Top Results

| Rank | Match | Title | Source | Score | Keywords |
|---:|---|---|---|---:|---|
| 1 | expected:2 | [Migrate to Apache Flink 2.2 on Amazon Managed Service for Apache Flink](https://aws.amazon.com/blogs/big-data/migrate-to-apache-flink-2-2-on-amazon-managed-service-for-apache-flink/) | AWS / AWS Big Data Blog | 851.66 | AWS CloudFormation, AWS IAM, Amazon CloudWatch, Amazon DynamoDB, Amazon OpenSearch Service, Amazon S3 |
| 2 | expected:3 | [Building unified data pipelines with Apache Iceberg and Apache Flink](https://aws.amazon.com/blogs/big-data/building-unified-data-pipelines-with-apache-iceberg-and-apache-flink/) | AWS / AWS Big Data Blog | 675.69 | AWS Glue, AWS IAM, Amazon CloudWatch, Amazon EC2, Amazon S3, Amazon VPC |
| 3 | - | [Apache Flink + RocksDB 튜닝으로 광고 Frequency Capping 실시간 집계를 일주일까지 확장하기](https://toss.tech/article/flink-realtime-frequency-capping) | Toss / Toss Tech | 616.82 | Apache Flink, Apache Kafka, JVM, Java, Kubernetes, Redis |
| 4 | expected:3 | [Build streaming applications on Amazon Managed Service for Apache Flink with AI-assisted guidance](https://aws.amazon.com/blogs/big-data/build-streaming-applications-on-amazon-managed-service-for-apache-flink-with-ai-assisted-guidance/) | AWS / AWS Big Data Blog | 576.17 | AWS CloudFormation, AWS IAM, Amazon CloudWatch, Amazon S3, Apache Flink, Java |
| 5 | - | [실시간 마케팅을 위한 PoC 개발기](https://techblog.woowahan.com/22043/) | Woowa Brothers / Woowa Tech Blog | 402.51 | AWS IAM, AWS Lambda, Amazon CloudWatch, Amazon DynamoDB, Amazon OpenSearch Service, Amazon S3 |
| 6 | - | [로그 파이프라인 개선기 - 기존 파이프라인 문제 정의 및 해결 방안 적용](https://tech.socarcorp.kr/data/2025/02/25/log-pipeline-revamp.html) | SOCAR / SOCAR Tech Blog | 399.50 | AWS Lambda, Amazon MSK, Amazon S3, Apache Flink, Apache Kafka, Java |
| 7 | - | [2조 토큰을 카테고리 분류에 쓰면서 알게된 것들](https://medium.com/daangn/2%EC%A1%B0-%ED%86%A0%ED%81%B0%EC%9D%84-%EC%B9%B4%ED%85%8C%EA%B3%A0%EB%A6%AC-%EB%B6%84%EB%A5%98%EC%97%90-%EC%93%B0%EB%A9%B4%EC%84%9C-%EC%95%8C%EA%B2%8C%EB%90%9C-%EA%B2%83%EB%93%A4-f619f1db6b7b?source=rss----4505f82a2dbd---4) | Daangn / Daangn Tech Blog | 399.50 | Apache Flink, Apache Kafka, LLM, search, observability, performance optimization |
| 8 | - | [실시간 반응형 추천 개발 일지 1부: 프로젝트 소개](https://techblog.woowahan.com/17383/) | Woowa Brothers / Woowa Tech Blog | 399.50 | Amazon RDS, Apache Flink, Apache Kafka, LLM, search, observability |
| 9 | - | [네이버 클라우드 플랫폼의 ETL 서비스 Data Flow 실습](https://medium.com/naver-cloud-platform/a27d4a929cf7?source=rss----c7f2bfeb6b98---4) | NAVER Cloud / NAVER Cloud Platform Tech Blog | 399.50 | Apache Flink, Kubernetes |

#### Top Result Details

##### 1. Migrate to Apache Flink 2.2 on Amazon Managed Service for Apache Flink

- match: expected relevance 2
- source: AWS / AWS Big Data Blog
- url: https://aws.amazon.com/blogs/big-data/migrate-to-apache-flink-2-2-on-amazon-managed-service-for-apache-flink/
- technologies: AWS CloudFormation, AWS IAM, Amazon CloudWatch, Amazon DynamoDB, Amazon OpenSearch Service, Amazon S3, Apache Flink, Apache Kafka, Java, search
- problem keywords: migration, observability, performance optimization
- case summary: Amazon Managed Service for Apache Flink에서 Flink 1.x에서 2.2로 마이그레이션하며 Java 17 런타임, 향상된 RocksDB 상태 백엔드, SQL 기반 AI/ML 추론 기능을 도입하여 성능과 운영 효율성을 개선한 사례이다.
- problem: 기존 Flink 1.x 환경에서 Java 11 지원 종료, 느린 상태 백엔드 성능, 분산된 API 사용으로 인한 유지보수 어려움과 최신 기능 부재 문제가 있었다.
- solution: Flink 2.2로 업그레이드하여 Java 17과 Python 3.12 지원, RocksDB 8.10.0 적용, 새로운 SQL/테이블 API 기능 활용, 자동 롤백과 스냅샷 기능으로 안정적인 무중단 마이그레이션을 수행하였다.

Highlights:

- title: Migrate to **Apache Flink** 2.2 on Amazon Managed Service for **Apache Flink**
- caseSummary: Amazon Managed Service for **Apache Flink에서 Flink** 1.x에서 2.2로 마이그레이션하며 Java 17 런타임, 향상된 RocksDB 상태 백엔드,
- summary: In this post, we explain what's new in Amazon Managed Service for **Apache Flink** 2.2, provide a guided
- content: for **Apache Flink**.
- content: Service for **Apache Flink** getting started guide , and the Amazon Managed Service for **Apache Flink** workshop .

##### 2. Building unified data pipelines with Apache Iceberg and Apache Flink

- match: expected relevance 3
- source: AWS / AWS Big Data Blog
- url: https://aws.amazon.com/blogs/big-data/building-unified-data-pipelines-with-apache-iceberg-and-apache-flink/
- technologies: AWS Glue, AWS IAM, Amazon CloudWatch, Amazon EC2, Amazon S3, Amazon VPC, Apache Flink, Apache Iceberg, Java
- problem keywords: migration, observability, performance optimization
- case summary: AWS에서 Apache Iceberg와 Amazon Managed Service for Apache Flink를 활용해 기존의 이중 데이터 파이프라인 문제를 해결하고, 단일 파이프라인으로 실시간 및 배치 데이터 처리를 통합하는 사례를 다룬다.
- problem: 기존에 실시간 스트리밍과 배치 처리를 위해 별도의 두 파이프라인을 운영하면서 인프라 비용 증가, 데이터 동기화 문제, 운영 복잡성 등의 문제가 발생했다.
- solution: Apache Iceberg의 스냅샷 기반 테이블 포맷과 Amazon Managed Service for Apache Flink를 결합해 단일 파이프라인에서 실시간과 배치 데이터를 모두 처리하도록 구현하여 비용 절감과 데이터 일관성 확보, 운영 효율성을 달성했다.

Highlights:

- title: Building unified data pipelines with **Apache** Iceberg and **Apache Flink**
- summary: In this post, you build a unified pipeline using **Apache** Iceberg and Amazon Managed Service for **Apache**
- summary: **Flink** that replaces the dual-pipeline approach.
- content: Set up your **Apache Flink** environment To prepare your **Apache Flink** environment: Download the required JAR files listed in the prerequisites section.
- content: Stop your Amazon Managed Service for **Apache Flink** application.

##### 3. Apache Flink + RocksDB 튜닝으로 광고 Frequency Capping 실시간 집계를 일주일까지 확장하기

- match: not expected
- source: Toss / Toss Tech
- url: https://toss.tech/article/flink-realtime-frequency-capping
- technologies: Apache Flink, Apache Kafka, JVM, Java, Kubernetes, Redis
- problem keywords: observability, performance optimization
- case summary: 토스는 Apache Flink와 RocksDB 튜닝을 통해 광고 Frequency Capping의 실시간 슬라이딩 윈도우 집계를 1분부터 7일까지 확장하며, 기존 배치 기반 시스템의 한계를 극복하고 운영 신뢰성과 성능을 개선했다.
- problem: 기존 Airflow 배치와 Redis 기반의 3계층 집계 구조는 실시간성과 정밀한 슬라이딩 윈도우 집계 제공에 한계가 있었고, 복잡한 의존성 및 다중 Redis 조회로 운영 부담이 컸다.
- solution: 1분~7일 구간을 각각 분리된 3개의 Flink 앱(minutes/hours/days)으로 처리하며, RocksDB 설정을 각 앱 특성에 맞게 튜닝하고, 초기 데이터 적재를 위한 백필과 캐치업 2단계 파이프라인을 설계해 State를 단일 진실 공급원으로 유지하며 Redis와의 정합성을 확보했다.

Highlights:

- title: **Apache Flink** + RocksDB 튜닝으로 광고 Frequency Capping 실시간 집계를 일주일까지 확장하기
- content: Flink와 RocksDB를 실무로 다루는 엔지니어라면 '아키텍처 결정'부터 '**Flink** Changelog'까지 순서대로 읽으시길 권해요. *본문의 코드와 설정은 **Apache Flink** 1.20.1, **flink**-connector-kafka 3.3.0 기준입니다. 1.
- content: RocksDB 튜닝과 함께 **Flink** TM 메모리 구조도 정밀하게 조정했어요.


### problem-cost-optimization - `cost optimization`

- category: problem
- intent: 비용 최적화나 비용 절감 문제를 해결한 기업/아키텍처 사례를 찾는다.
- total results: 65
- precision@5: 0.400
- recall@10: 1.000
- mrr: 0.333
- ndcg@10: 0.552

#### Expected URLs

- relevance 3: [How HotelTrader cut inter-AZ cost 95% and latency by 49% with Valkey GLIDE on Amazon ElastiCache](https://aws.amazon.com/blogs/database/how-hoteltrader-cut-inter-az-cost-95-and-latency-by-49-with-valkey-glide-on-amazon-elasticache/)
- relevance 3: [The Hidden Price Tag: Uncovering Hidden Costs in Cloud Architectures with the AWS Well-Architected Framework](https://aws.amazon.com/blogs/architecture/the-hidden-price-tag-uncovering-hidden-costs-in-cloud-architectures-with-the-aws-well-architected-framework/)
- relevance 2: [How Generali Malaysia optimizes operations with Amazon EKS](https://aws.amazon.com/blogs/architecture/how-generali-malaysia-optimizes-operations-with-amazon-eks/)

#### Top Results

| Rank | Match | Title | Source | Score | Keywords |
|---:|---|---|---|---:|---|
| 1 | - | [AWS re:Invent 2023, 관심 세션을 중심으로 (2편): Cost Optimization, Observability](https://tech.kakaopay.com/post/2023-aws-reinvent-2/) | Kakao Pay / Kakao Pay Tech Blog | 688.34 | cost optimization, observability |
| 2 | - | [Cloud expenditure optimization for cost efficiency](https://medium.com/coupang-engineering/cloud-expenditure-optimization-for-cost-efficiency-44e9bea3d91b?source=rss----fb028911af07---4) | Coupang / Coupang Engineering Blog | 316.09 | Amazon CloudWatch, Amazon EC2, Amazon S3, cost optimization, migration, observability |
| 3 | expected:3 | [The Hidden Price Tag: Uncovering Hidden Costs in Cloud Architectures with the AWS Well-Architected Framework](https://aws.amazon.com/blogs/architecture/the-hidden-price-tag-uncovering-hidden-costs-in-cloud-architectures-with-the-aws-well-architected-framework/) | AWS / AWS Architecture Blog | 159.97 | AWS CloudFormation, AWS IAM, cost optimization, high availability, incident response, observability |
| 4 | expected:2 | [How Generali Malaysia optimizes operations with Amazon EKS](https://aws.amazon.com/blogs/architecture/how-generali-malaysia-optimizes-operations-with-amazon-eks/) | AWS / AWS Architecture Blog | 159.14 | AWS IAM, Amazon CloudWatch, Amazon EC2, Amazon EKS, Kubernetes, cost optimization |
| 5 | - | [Enhancing auto scaling resilience by tracking worker utilization metrics](https://aws.amazon.com/blogs/compute/enhancing-auto-scaling-resilience-by-tracking-worker-utilization-metrics/) | AWS / AWS Compute Blog | 148.57 | AWS CloudFormation, AWS IAM, Amazon CloudWatch, Amazon DynamoDB, Amazon EC2, Java |
| 6 | - | [Accelerate CPU-based AI inference workloads using Intel AMX on Amazon EC2](https://aws.amazon.com/blogs/compute/accelerate-cpu-based-ai-inference-workloads-using-intel-amx-on-amazon-ec2/) | AWS / AWS Compute Blog | 146.35 | Amazon EC2, cost optimization, migration, observability, performance optimization |
| 7 | expected:3 | [How HotelTrader cut inter-AZ cost 95% and latency by 49% with Valkey GLIDE on Amazon ElastiCache](https://aws.amazon.com/blogs/database/how-hoteltrader-cut-inter-az-cost-95-and-latency-by-49-with-valkey-glide-on-amazon-elasticache/) | AWS / AWS Database Blog | 145.52 | AWS IAM, Amazon EC2, Amazon EKS, Amazon ElastiCache, Amazon VPC, Java |
| 8 | - | [Optimizing storage performance for Amazon EKS on AWS Outposts](https://aws.amazon.com/blogs/compute/optimizing-storage-performance-for-amazon-eks-on-aws-outposts/) | AWS / AWS Compute Blog | 142.66 | AWS IAM, Amazon CloudWatch, Amazon EKS, Amazon S3, Kubernetes, cost optimization |
| 9 | - | [Build high-performance apps with AWS Lambda Managed Instances](https://aws.amazon.com/blogs/compute/build-high-performance-apps-with-aws-lambda-managed-instances/) | AWS / AWS Compute Blog | 141.61 | AWS IAM, AWS Lambda, Amazon CloudWatch, Amazon DynamoDB, Amazon EC2, Amazon EventBridge |
| 10 | - | [More room to build: serverless services now support payloads up to 1 MB](https://aws.amazon.com/blogs/compute/more-room-to-build-serverless-services-now-support-payloads-up-to-1-mb/) | AWS / AWS Compute Blog | 141.48 | AWS Lambda, Amazon CloudWatch, Amazon EventBridge, Amazon S3, Apache Kafka, Java |

#### Top Result Details

##### 1. AWS re:Invent 2023, 관심 세션을 중심으로 (2편): Cost Optimization, Observability

- match: not expected
- source: Kakao Pay / Kakao Pay Tech Blog
- url: https://tech.kakaopay.com/post/2023-aws-reinvent-2/
- technologies: -
- problem keywords: cost optimization, observability
- case summary: AWS re:Invent 2023에서 비용 최적화와 관측성 관련 세션을 중심으로 최신 클라우드 운영 전략과 기술을 소개하고 적용 가능성을 검토한 사례입니다.
- problem: 클라우드 환경에서 비용 효율성을 유지하면서도 시스템의 상태를 효과적으로 모니터링하고 문제를 신속히 파악하는 운영상의 어려움이 있었습니다.
- solution: AWS의 최신 비용 최적화 도구와 관측성 솔루션을 활용해 리소스 사용을 최적화하고, 로그 및 메트릭 기반의 통합 모니터링 체계를 구축하여 운영 효율을 높였습니다.

Highlights:

- title: AWS re:Invent 2023, 관심 세션을 중심으로 (2편): **Cost Optimization**, Observability

##### 2. Cloud expenditure optimization for cost efficiency

- match: not expected
- source: Coupang / Coupang Engineering Blog
- url: https://medium.com/coupang-engineering/cloud-expenditure-optimization-for-cost-efficiency-44e9bea3d91b?source=rss----fb028911af07---4
- technologies: Amazon CloudWatch, Amazon EC2, Amazon S3
- problem keywords: cost optimization, migration, observability, performance optimization
- case summary: 쿠팡은 클라우드 비용 과다 지출 문제를 해결하기 위해 중앙팀을 구성하고 AWS 기반의 분석 도구와 최적화 기법을 도입하여 수백만 달러의 비용 절감을 달성했다.
- problem: 엔지니어링 팀들이 클라우드 사용 효율성에 대한 이해 없이 과도한 비용을 지출하고, 재무팀은 지출 내역 파악과 비용 통제에 어려움을 겪으며, 경영진은 클라우드 비용 분석이 부족한 상황이었다.
- solution: 클라우드 인프라 엔지니어와 프로그램 매니저로 구성된 중앙팀을 만들어 각 도메인 팀과 협력해 비용 분석과 최적화 방안을 제시하고, AWS Spot 인스턴스, ARM 기반 Graviton, 최신 인스턴스 세대 전환, EMR 인스턴스 플릿 기능 활용, EBS GP3 마이그레이션, S3 Intelligent-Tiering 적용 등 다양한 AWS 서비스 최적화를 통해 비용 절감과 성능 향상을 동시에 달성했다.

Highlights:

- title: Cloud expenditure **optimization** for **cost** efficiency
- summary: With usage **optimization** and **cost** savings as our main goals, the following initiatives helped save millions
- summary: Additionally, we will be automating some of the monitoring and analytics processes required for **cost **
- content: With usage **optimization** and **cost** savings as our main goals, the following initiatives helped save millions of dollars (On-Demand **cost**) in 2021 on AWS Cloud.
- content: Additionally, we will be automating some of the monitoring and analytics processes required for **cost optimization** in cloud.

##### 3. The Hidden Price Tag: Uncovering Hidden Costs in Cloud Architectures with the AWS Well-Architected Framework

- match: expected relevance 3
- source: AWS / AWS Architecture Blog
- url: https://aws.amazon.com/blogs/architecture/the-hidden-price-tag-uncovering-hidden-costs-in-cloud-architectures-with-the-aws-well-architected-framework/
- technologies: AWS CloudFormation, AWS IAM
- problem keywords: cost optimization, high availability, incident response, observability, performance optimization
- case summary: AWS Well-Architected Framework를 활용해 클라우드 아키텍처의 보안, 가용성, 비용 최적화 측면에서 숨겨진 비용과 위험을 식별하고 개선하는 사례를 다룬다.
- problem: 클라우드 아키텍처 설계 시 보안 사고, 서비스 중단, 자원 과다 할당 등으로 인한 숨겨진 비용과 비즈니스 리스크가 발생하는 문제.
- solution: AWS Well-Architected Framework와 AWS Cloud Adoption Framework를 적용해 보안 강화, 고가용성 설계, 자원 효율화 등 모범 사례를 준수하며 아키텍처를 지속적으로 평가·개선하여 비용과 위험을 최소화하는 접근법.

Highlights:

- content: It provides guidance based on six pillars: Operational Excellence, Security, Reliability, Performance Efficiency, **Cost Optimization**, and Sustainability.
- content: Understanding these models and their differences is crucial for effective **cost optimization** in the AWS Cloud.


### problem-observability - `observability`

- category: problem
- intent: 관측성, 모니터링, 디버깅 문제를 해결한 사례를 찾는다.
- total results: 287
- precision@5: 0.400
- recall@10: 0.667
- mrr: 1.000
- ndcg@10: 0.813

#### Expected URLs

- relevance 3: [Enhancing network observability with new AWS Outposts racks LAG metrics](https://aws.amazon.com/blogs/compute/enhancing-network-observability-with-new-aws-outposts-racks-lag-metrics/)
- relevance 3: [Unified observability in Amazon OpenSearch Service: metrics, traces, and AI agent debugging in a single interface](https://aws.amazon.com/blogs/big-data/unified-observability-in-amazon-opensearch-service-metrics-traces-and-ai-agent-debugging-in-a-single-interface/)
- relevance 2: [Streaming CloudWatch metrics to VPC-based OpenTelemetry collectors using Lambda](https://aws.amazon.com/blogs/architecture/streaming-cloudwatch-metrics-to-vpc-based-opentelemetry-collectors-using-lambda/)

#### Top Results

| Rank | Match | Title | Source | Score | Keywords |
|---:|---|---|---|---:|---|
| 1 | expected:3 | [Enhancing network observability with new AWS Outposts racks LAG metrics](https://aws.amazon.com/blogs/compute/enhancing-network-observability-with-new-aws-outposts-racks-lag-metrics/) | AWS / AWS Compute Blog | 375.23 | AWS CloudFormation, AWS IAM, Amazon CloudWatch, high availability, observability |
| 2 | - | [AWS re:Invent 2023, 관심 세션을 중심으로 (2편): Cost Optimization, Observability](https://tech.kakaopay.com/post/2023-aws-reinvent-2/) | Kakao Pay / Kakao Pay Tech Blog | 375.23 | cost optimization, observability |
| 3 | expected:3 | [Unified observability in Amazon OpenSearch Service: metrics, traces, and AI agent debugging in a single interface](https://aws.amazon.com/blogs/big-data/unified-observability-in-amazon-opensearch-service-metrics-traces-and-ai-agent-debugging-in-a-single-interface/) | AWS / AWS Big Data Blog | 298.75 | AWS IAM, Amazon OpenSearch Service, LLM, OpenTelemetry, search, observability |
| 4 | - | [Scaling to Infinity: 한계를 넘어서는 LY Corporation의 관측 가능성 플랫폼 진화기](https://techblog.lycorp.co.jp/ko/the-evolution-of-the-ly-observability-platform) | LY Corporation / LY Corporation Tech Blog | 279.24 | observability |
| 5 | - | [LLMOps로 확장하는 AI플랫폼 2.0](https://techblog.woowahan.com/22839/) | Woowa Brothers / Woowa Tech Blog | 272.28 | LLM, Redis, observability, performance optimization, streaming data pipeline |
| 6 | - | [AI-powered event response for Amazon EKS](https://aws.amazon.com/blogs/architecture/ai-powered-event-response-for-amazon-eks/) | AWS / AWS Architecture Blog | 271.22 | AWS CDK, AWS CloudFormation, AWS IAM, Amazon CloudWatch, Amazon EKS, Java |
| 7 | - | [6,000 AWS accounts, three people, one platform: Lessons learned](https://aws.amazon.com/blogs/architecture/6000-aws-accounts-three-people-one-platform-lessons-learned/) | AWS / AWS Architecture Blog | 244.59 | AWS CloudFormation, AWS IAM, AWS Lambda, Amazon CloudWatch, Amazon DynamoDB, Amazon EC2 |
| 8 | - | [Building an end-to-end agentic SRE using AWS DevOps Agent](https://aws.amazon.com/blogs/devops/building-an-end-to-end-agentic-sre-using-aws-devops-agent/) | AWS / AWS DevOps Blog | 243.08 | AWS CDK, AWS Lambda, Amazon CloudWatch, Amazon EC2, Amazon EventBridge, Amazon VPC |
| 9 | - | [Securely connect AWS DevOps Agent to private services in your VPCs](https://aws.amazon.com/blogs/devops/securely-connect-aws-devops-agent-to-private-services-in-your-vpcs/) | AWS / AWS DevOps Blog | 243.08 | AWS IAM, Amazon VPC, high availability, incident response, observability, performance optimization |
| 10 | - | [Build high-performance apps with AWS Lambda Managed Instances](https://aws.amazon.com/blogs/compute/build-high-performance-apps-with-aws-lambda-managed-instances/) | AWS / AWS Compute Blog | 243.08 | AWS IAM, AWS Lambda, Amazon CloudWatch, Amazon DynamoDB, Amazon EC2, Amazon EventBridge |

#### Top Result Details

##### 1. Enhancing network observability with new AWS Outposts racks LAG metrics

- match: expected relevance 3
- source: AWS / AWS Compute Blog
- url: https://aws.amazon.com/blogs/compute/enhancing-network-observability-with-new-aws-outposts-racks-lag-metrics/
- technologies: AWS CloudFormation, AWS IAM, Amazon CloudWatch
- problem keywords: high availability, observability
- case summary: AWS Outposts 랙의 네트워크 연결 상태를 모니터링하기 위해 새로운 CloudWatch LagStatus 메트릭을 도입하여 LAG(Link Aggregation Group) 상태를 실시간으로 관찰하고, 기존 VifConnectionStatus 및 VifBgpSessionState 메트릭과 결합해 네트워크 장애 원인을 신속히 파악할 수 있게 했다.
- problem: AWS Outposts 랙을 온프레미스 환경에 배포할 때, AWS 리전과 온프레미스 네트워크 간의 원활한 연결 유지가 필수적이나, 기존에는 LAG 상태에 대한 가시성이 부족해 네트워크 장애 진단이 어려웠다.
- solution: 새로운 LagStatus CloudWatch 메트릭을 도입하여 LAG 연결 상태를 5분 간격으로 모니터링하고, VifConnectionStatus 및 VifBgpSessionState 메트릭과 함께 사용해 네트워크 연결 문제를 빠르게 식별하며, CloudWatch Composite Alarms를 활용해 운영팀에 자동 알림을 설정했다.

Highlights:

- title: Enhancing network **observability** with new AWS Outposts racks LAG metrics
- summary: Implementing an **observability** strategy that uses available network metrics is key to understanding the
- content: Implementing an **observability** strategy that uses available network metrics is key to understanding the health of this connectivity.
- content: Reach out to your AWS account team, or fill out this form to learn more about **observability** for Outposts.

##### 2. AWS re:Invent 2023, 관심 세션을 중심으로 (2편): Cost Optimization, Observability

- match: not expected
- source: Kakao Pay / Kakao Pay Tech Blog
- url: https://tech.kakaopay.com/post/2023-aws-reinvent-2/
- technologies: -
- problem keywords: cost optimization, observability
- case summary: AWS re:Invent 2023에서 비용 최적화와 관측성 관련 세션을 중심으로 최신 클라우드 운영 전략과 기술을 소개하고 적용 가능성을 검토한 사례입니다.
- problem: 클라우드 환경에서 비용 효율성을 유지하면서도 시스템의 상태를 효과적으로 모니터링하고 문제를 신속히 파악하는 운영상의 어려움이 있었습니다.
- solution: AWS의 최신 비용 최적화 도구와 관측성 솔루션을 활용해 리소스 사용을 최적화하고, 로그 및 메트릭 기반의 통합 모니터링 체계를 구축하여 운영 효율을 높였습니다.

Highlights:

- title: AWS re:Invent 2023, 관심 세션을 중심으로 (2편): Cost Optimization, **Observability**

##### 3. Unified observability in Amazon OpenSearch Service: metrics, traces, and AI agent debugging in a single interface

- match: expected relevance 3
- source: AWS / AWS Big Data Blog
- url: https://aws.amazon.com/blogs/big-data/unified-observability-in-amazon-opensearch-service-metrics-traces-and-ai-agent-debugging-in-a-single-interface/
- technologies: AWS IAM, Amazon OpenSearch Service, LLM, OpenTelemetry, search
- problem keywords: observability, performance optimization
- case summary: Amazon OpenSearch Service는 OpenTelemetry 기반 AI 에이전트 추적과 Amazon Managed Service for Prometheus 통합을 통해 단일 인터페이스에서 메트릭, 트레이스, 로그를 통합 관찰하며, AI 에이전트 및 마이크로서비스 문제를 신속하게 진단할 수 있는 사례를 소개한다.
- problem: 멀티 에이전트 여행 플래너의 지연 문제와 전자상거래 체크아웃 마이크로서비스의 조용한 실패 현상 등 복잡한 분산 시스템에서 발생하는 성능 저하 및 오류 원인 파악이 어려웠다.
- solution: OpenTelemetry의 AI 에이전트용 시맨틱 트레이싱과 Prometheus 메트릭 통합을 활용해 OpenSearch UI 내에서 AI 에이전트의 추론 체인과 마이크로서비스의 RED 지표, PromQL 쿼리를 단일 관찰 공간에서 분석하여 근본 원인을 신속히 진단했다.

Highlights:

- title: Unified **observability** in Amazon OpenSearch Service: metrics, traces, and AI agent debugging in a single
- summary: Amazon Managed Service for Prometheus integration, and AI agent tracing together in OpenSearch UI's **observability**
- content: In any **observability** workspace in OpenSearch UI, navigate to Application Map in the left navigation pane.
- content: Agent Health is an open-source, evaluation-driven **observability** tool designed for local development.


### problem-incident-response - `incident response`

- category: problem
- intent: 장애 대응, 사고 조사, SRE 자동화 관련 사례를 찾는다.
- total results: 279
- precision@5: 0.600
- recall@10: 1.000
- mrr: 1.000
- ndcg@10: 0.885

#### Expected URLs

- relevance 3: [Building an end-to-end agentic SRE using AWS DevOps Agent](https://aws.amazon.com/blogs/devops/building-an-end-to-end-agentic-sre-using-aws-devops-agent/)
- relevance 3: [Automating Incident Investigation with AWS DevOps Agent and Salesforce MCP Server](https://aws.amazon.com/blogs/devops/automating-incident-investigation-with-aws-devops-agent-and-salesforce-mcp-server/)
- relevance 3: [Leverage Agentic AI for Autonomous Incident Response with AWS DevOps Agent](https://aws.amazon.com/blogs/devops/leverage-agentic-ai-for-autonomous-incident-response-with-aws-devops-agent/)

#### Top Results

| Rank | Match | Title | Source | Score | Keywords |
|---:|---|---|---|---:|---|
| 1 | expected:3 | [Leverage Agentic AI for Autonomous Incident Response with AWS DevOps Agent](https://aws.amazon.com/blogs/devops/leverage-agentic-ai-for-autonomous-incident-response-with-aws-devops-agent/) | AWS / AWS DevOps Blog | 919.04 | AWS IAM, AWS Lambda, Amazon CloudWatch, Amazon DynamoDB, Amazon EKS, Amazon S3 |
| 2 | - | [AI-powered event response for Amazon EKS](https://aws.amazon.com/blogs/architecture/ai-powered-event-response-for-amazon-eks/) | AWS / AWS Architecture Blog | 682.43 | AWS CDK, AWS CloudFormation, AWS IAM, Amazon CloudWatch, Amazon EKS, Java |
| 3 | expected:3 | [Building an end-to-end agentic SRE using AWS DevOps Agent](https://aws.amazon.com/blogs/devops/building-an-end-to-end-agentic-sre-using-aws-devops-agent/) | AWS / AWS DevOps Blog | 662.09 | AWS CDK, AWS Lambda, Amazon CloudWatch, Amazon EC2, Amazon EventBridge, Amazon VPC |
| 4 | - | [From AI agent prototype to product: Lessons from building AWS DevOps Agent](https://aws.amazon.com/blogs/devops/from-ai-agent-prototype-to-product-lessons-from-building-aws-devops-agent/) | AWS / AWS DevOps Blog | 643.84 | AWS IAM, AWS Lambda, Amazon S3, Kubernetes, LLM, OpenTelemetry |
| 5 | expected:3 | [Automating Incident Investigation with AWS DevOps Agent and Salesforce MCP Server](https://aws.amazon.com/blogs/devops/automating-incident-investigation-with-aws-devops-agent-and-salesforce-mcp-server/) | AWS / AWS DevOps Blog | 376.14 | AWS IAM, Amazon CloudWatch, Amazon EC2, incident response, observability, event response |
| 6 | - | [The Hidden Price Tag: Uncovering Hidden Costs in Cloud Architectures with the AWS Well-Architected Framework](https://aws.amazon.com/blogs/architecture/the-hidden-price-tag-uncovering-hidden-costs-in-cloud-architectures-with-the-aws-well-architected-framework/) | AWS / AWS Architecture Blog | 238.73 | AWS CloudFormation, AWS IAM, cost optimization, high availability, incident response, observability |
| 7 | - | [Best Practices for Deploying AWS DevOps Agent in Production](https://aws.amazon.com/blogs/devops/best-practices-for-deploying-aws-devops-agent-in-production/) | AWS / AWS DevOps Blog | 237.78 | AWS CDK, AWS IAM, AWS Lambda, Amazon CloudWatch, Amazon DynamoDB, Amazon RDS |
| 8 | - | [Securely connect AWS DevOps Agent to private services in your VPCs](https://aws.amazon.com/blogs/devops/securely-connect-aws-devops-agent-to-private-services-in-your-vpcs/) | AWS / AWS DevOps Blog | 218.73 | AWS IAM, Amazon VPC, high availability, incident response, observability, performance optimization |
| 9 | - | [Building hybrid multi-tenant architecture for stateful services on AWS](https://aws.amazon.com/blogs/architecture/building-hybrid-multi-tenant-architecture-for-stateful-services-on-aws/) | AWS / AWS Architecture Blog | 190.81 | AWS IAM, Amazon CloudWatch, Amazon EC2, Amazon VPC, incident response, migration |
| 10 | - | [데브시스터즈의 장애 대응 원칙과 방법](https://tech.devsisters.com/posts/incident-management-principles) | Devsisters / Devsisters Tech Blog | 138.56 | incident response, observability, performance optimization |

#### Top Result Details

##### 1. Leverage Agentic AI for Autonomous Incident Response with AWS DevOps Agent

- match: expected relevance 3
- source: AWS / AWS DevOps Blog
- url: https://aws.amazon.com/blogs/devops/leverage-agentic-ai-for-autonomous-incident-response-with-aws-devops-agent/
- technologies: AWS IAM, AWS Lambda, Amazon CloudWatch, Amazon DynamoDB, Amazon EKS, Amazon S3, Kubernetes, LLM
- problem keywords: high availability, incident response, observability, performance optimization
- case summary: AWS DevOps Agent를 활용해 분산 서버리스 애플리케이션의 장애를 AI 기반으로 자동 탐지 및 원인 분석하여, 수동 대응 시간을 수 시간에서 수 분으로 단축한 사례이다.
- problem: 분산된 서버리스 아키텍처에서 장애 발생 시 로그, 배포 이력, 모니터링 데이터가 여러 곳에 흩어져 있어 SRE가 수동으로 원인 분석에 많은 시간이 소요되는 문제.
- solution: AWS DevOps Agent를 도입해 애플리케이션 토폴로지 자동 탐지, 크로스 계정 및 멀티 클라우드 관찰, AI 기반 자율 조사 및 원인 분석, 그리고 Slack 등 협업 도구와 연동한 자동 대응 체계를 구축함으로써 MTTR을 크게 단축함.

Highlights:

- title: Leverage Agentic AI for Autonomous **Incident Response** with AWS DevOps Agent
- content: For any team operating distributed and complex architectural applications on AWS — DevOps Agent reduces the operational burden of **incident response** while building
- content: Tipu Qureshi Tipu Qureshi is a Senior Principal Technologist in AWS Agentic AI, focusing on operational excellence and **incident response** automation.

##### 2. AI-powered event response for Amazon EKS

- match: not expected
- source: AWS / AWS Architecture Blog
- url: https://aws.amazon.com/blogs/architecture/ai-powered-event-response-for-amazon-eks/
- technologies: AWS CDK, AWS CloudFormation, AWS IAM, Amazon CloudWatch, Amazon EKS, Java, Kubernetes, OpenTelemetry
- problem keywords: incident response, migration, observability, performance optimization
- case summary: AWS DevOps Agent를 활용해 Amazon EKS 클러스터 내 마이크로서비스의 이벤트를 AI 기반으로 자동 탐지 및 대응하는 사례로, 복잡한 Kubernetes 리소스 간 관계를 이해하고 신속한 근본 원인 분석을 지원한다.
- problem: 대규모 마이크로서비스 환경에서 수천 건의 이벤트 신호를 효과적으로 모니터링하고, 신속하고 정확한 근본 원인 분석 및 자동화된 사건 대응이 어려운 상황.
- solution: Amazon EKS와 통합된 AWS DevOps Agent를 배포하여 OpenTelemetry, CloudWatch, X-Ray 등 다양한 관찰 가능성 데이터를 AI와 머신러닝으로 분석하고, Kubernetes 리소스 간 의존성을 파악해 자동으로 이상 징후를 탐지하고 대응하는 시스템 구축.

Highlights:

- title: AI-powered **event response** for Amazon EKS
- content: It brings Kubernetes-native intelligence to **incident response**.
- content: workflows and tools for seamless **incident response** and improvement.

##### 3. Building an end-to-end agentic SRE using AWS DevOps Agent

- match: expected relevance 3
- source: AWS / AWS DevOps Blog
- url: https://aws.amazon.com/blogs/devops/building-an-end-to-end-agentic-sre-using-aws-devops-agent/
- technologies: AWS CDK, AWS Lambda, Amazon CloudWatch, Amazon EC2, Amazon EventBridge, Amazon VPC, search
- problem keywords: high availability, incident response, observability
- case summary: AWS DevOps Agent를 활용해 서버리스, 마이크로서비스, 이벤트 기반 아키텍처에서 발생하는 인시던트를 자동으로 조사하고 근본 원인을 분석하는 엔드투엔드 에이전틱 SRE 솔루션 구축 사례이다.
- problem: 복잡한 현대 애플리케이션 환경에서 수동으로 여러 관찰 도구 데이터를 연관시키고 문제를 해결하는 데 많은 시간이 소요되어 생산성 저하와 신뢰성 저하, 혁신 지연이 발생하는 문제.
- solution: AWS DevOps Agent를 통해 CloudWatch, Splunk, GitHub, Slack 등 다양한 도구와 연동하여 인시던트 발생 즉시 자동으로 조사하고 근본 원인을 도출하며, 상세한 완화 계획을 생성해 엔지니어가 근본 원인에 집중할 수 있도록 지원하는 자동화된 SRE 에이전트 구축.

Highlights:

- summary: As modern applications evolve into complex ecosystems of serverless functions, microservices, and **event**-driven
- summary: architectures, **incident response** becomes increasingly challenging.
- content: Introduction As modern applications evolve into complex ecosystems of serverless functions, microservices, and **event**-driven architectures, **incident response** becomes
- content: telemetry from CloudWatch, Splunk, and GitHub, generates mitigation plans, and coordinates the **incident response**.


### architecture-streaming-pipeline - `streaming data pipeline`

- category: architecture
- intent: 실시간 스트리밍 데이터 처리나 파이프라인 구성 사례를 찾는다.
- total results: 80
- precision@5: 0.400
- recall@10: 0.667
- mrr: 0.500
- ndcg@10: 0.613

#### Expected URLs

- relevance 3: [Build streaming applications on Amazon Managed Service for Apache Flink with AI-assisted guidance](https://aws.amazon.com/blogs/big-data/build-streaming-applications-on-amazon-managed-service-for-apache-flink-with-ai-assisted-guidance/)
- relevance 3: [Building unified data pipelines with Apache Iceberg and Apache Flink](https://aws.amazon.com/blogs/big-data/building-unified-data-pipelines-with-apache-iceberg-and-apache-flink/)
- relevance 2: [Streaming CloudWatch metrics to VPC-based OpenTelemetry collectors using Lambda](https://aws.amazon.com/blogs/architecture/streaming-cloudwatch-metrics-to-vpc-based-opentelemetry-collectors-using-lambda/)

#### Top Results

| Rank | Match | Title | Source | Score | Keywords |
|---:|---|---|---|---:|---|
| 1 | - | [Getting started with Change Data Capture in Amazon Aurora DSQL](https://aws.amazon.com/blogs/database/getting-started-with-change-data-capture-in-amazon-aurora-dsql/) | AWS / AWS Database Blog | 215.19 | AWS IAM, AWS Lambda, Amazon Aurora, Apache Kafka, React, search |
| 2 | expected:3 | [Building unified data pipelines with Apache Iceberg and Apache Flink](https://aws.amazon.com/blogs/big-data/building-unified-data-pipelines-with-apache-iceberg-and-apache-flink/) | AWS / AWS Big Data Blog | 212.00 | AWS Glue, AWS IAM, Amazon CloudWatch, Amazon EC2, Amazon S3, Amazon VPC |
| 3 | expected:3 | [Build streaming applications on Amazon Managed Service for Apache Flink with AI-assisted guidance](https://aws.amazon.com/blogs/big-data/build-streaming-applications-on-amazon-managed-service-for-apache-flink-with-ai-assisted-guidance/) | AWS / AWS Big Data Blog | 206.02 | AWS CloudFormation, AWS IAM, Amazon CloudWatch, Amazon S3, Apache Flink, Java |
| 4 | - | [Meet Coupang’s Machine Learning Platform](https://medium.com/coupang-engineering/meet-coupangs-machine-learning-platform-cd00e9ccc172?source=rss----fb028911af07---4) | Coupang / Coupang Engineering Blog | 95.19 | Kubernetes, LLM, search, observability, performance optimization, canary deployment |
| 5 | - | [How to consolidate cross-Region S3 data into OpenSearch](https://aws.amazon.com/blogs/big-data/how-to-consolidate-cross-region-s3-data-into-opensearch/) | AWS / AWS Big Data Blog | 89.44 | AWS IAM, Amazon OpenSearch Service, Amazon S3, Amazon VPC, search, observability |
| 6 | - | [How to build a cross-Region resilience for Amazon OpenSearch Service with Amazon MSK](https://aws.amazon.com/blogs/big-data/how-to-build-a-cross-region-resilience-for-amazon-opensearch-service-with-amazon-msk/) | AWS / AWS Big Data Blog | 89.22 | AWS CloudFormation, AWS IAM, AWS Lambda, Amazon CloudWatch, Amazon MSK, Amazon OpenSearch Service |
| 7 | - | [Announcing aggregations on Amazon ElastiCache](https://aws.amazon.com/blogs/database/announcing-aggregations-on-amazon-elasticache/) | AWS / AWS Database Blog | 78.98 | AWS IAM, Amazon EC2, Amazon ElastiCache, Amazon VPC, Redis, Valkey |
| 8 | - | [프로젝트 관리를 위한 JIRA 활용기](https://dev.gmarket.com/43) | Gmarket / Gmarket Tech Blog | 74.64 | Apache Kafka, Elasticsearch, Redis, search |
| 9 | - | [[다시 보기] 8월 우아한테크세미나: 행정동을 법정동으로, 배민 지리 체계 프로젝트 살펴보기](https://techblog.woowahan.com/13547/) | Woowa Brothers / Woowa Tech Blog | 71.70 | migration, streaming data pipeline |
| 10 | - | [[다시 보기] 7월 우아한테크세미나: MLOps를 활용한 AI 서비스 개발 스토리](https://techblog.woowahan.com/12924/) | Woowa Brothers / Woowa Tech Blog | 71.70 | streaming data pipeline |

#### Top Result Details

##### 1. Getting started with Change Data Capture in Amazon Aurora DSQL

- match: not expected
- source: AWS / AWS Database Blog
- url: https://aws.amazon.com/blogs/database/getting-started-with-change-data-capture-in-amazon-aurora-dsql/
- technologies: AWS IAM, AWS Lambda, Amazon Aurora, Apache Kafka, React, search
- problem keywords: observability, performance optimization
- case summary: Amazon Aurora DSQL의 Change Data Capture(CDC) 기능을 활용해 데이터베이스 변경 사항을 실시간으로 Amazon Kinesis Data Streams로 스트리밍하는 파이프라인 구축 사례를 다룬다.
- problem: 전통적인 데이터 동기화 방식은 지연과 운영 부담이 크고 데이터 일관성 유지가 어려워, 실시간 데이터 파이프라인 구축이 필요한 상황에서 효율적인 데이터 변경 추적 및 스트리밍 방법이 요구됨.
- solution: Aurora DSQL의 CDC 기능을 사용해 데이터베이스 변경 이벤트를 캡처하고 이를 Kinesis Data Streams로 스트리밍하여, 다운스트림 애플리케이션이 실시간으로 변경 데이터를 처리할 수 있는 이벤트 기반 아키텍처를 구현함.

Highlights:

- summary: In this post, we demonstrate how to configure Aurora DSQL Change **Data** Capture and stream database changes
- summary: into Kinesis **Data** Streams.
- content: To avoid this, you should consider the size characteristics of your **data** model and configure your **streaming** **pipeline** and consumers to handle the expected payload
- content: Cleanup After confirming that your CDC **pipeline** is working correctly and you have successfully validated the **streaming** of database changes into Amazon Kinesis **Data**

##### 2. Building unified data pipelines with Apache Iceberg and Apache Flink

- match: expected relevance 3
- source: AWS / AWS Big Data Blog
- url: https://aws.amazon.com/blogs/big-data/building-unified-data-pipelines-with-apache-iceberg-and-apache-flink/
- technologies: AWS Glue, AWS IAM, Amazon CloudWatch, Amazon EC2, Amazon S3, Amazon VPC, Apache Flink, Apache Iceberg, Java
- problem keywords: migration, observability, performance optimization
- case summary: AWS에서 Apache Iceberg와 Amazon Managed Service for Apache Flink를 활용해 기존의 이중 데이터 파이프라인 문제를 해결하고, 단일 파이프라인으로 실시간 및 배치 데이터 처리를 통합하는 사례를 다룬다.
- problem: 기존에 실시간 스트리밍과 배치 처리를 위해 별도의 두 파이프라인을 운영하면서 인프라 비용 증가, 데이터 동기화 문제, 운영 복잡성 등의 문제가 발생했다.
- solution: Apache Iceberg의 스냅샷 기반 테이블 포맷과 Amazon Managed Service for Apache Flink를 결합해 단일 파이프라인에서 실시간과 배치 데이터를 모두 처리하도록 구현하여 비용 절감과 데이터 일관성 확보, 운영 효율성을 달성했다.

Highlights:

- summary: In this post, you build a unified **pipeline** using Apache Iceberg and Amazon Managed Service for Apache
- summary: Flink that replaces the dual-**pipeline** approach.
- content: **Data** synchronization issues. Your batch and **streaming** consumers read from different copies of the **data**, processed at different times.
- content: **Data** integrity: Misconfigured checkpoints or schema changes during **streaming** can lead to **data** inconsistency.

##### 3. Build streaming applications on Amazon Managed Service for Apache Flink with AI-assisted guidance

- match: expected relevance 3
- source: AWS / AWS Big Data Blog
- url: https://aws.amazon.com/blogs/big-data/build-streaming-applications-on-amazon-managed-service-for-apache-flink-with-ai-assisted-guidance/
- technologies: AWS CloudFormation, AWS IAM, Amazon CloudWatch, Amazon S3, Apache Flink, Java, search
- problem keywords: migration, observability, performance optimization
- case summary: AWS의 Managed Service for Apache Flink용 AI 지원 도구인 Kiro Power와 Agent Skill을 활용해 스트리밍 애플리케이션 개발, 성능 최적화, 그리고 Flink 1.x에서 2.2로의 마이그레이션을 효율적으로 수행하는 사례를 다룬다.
- problem: Apache Flink 기반 스트리밍 애플리케이션 개발과 운영은 복잡한 생태계와 높은 학습 곡선, 그리고 버전 업그레이드 시 호환성 문제로 인해 어려움이 많다.
- solution: AI 기반 Kiro Power와 Agent Skill을 통해 개발 환경 내에서 아키텍처 설계, 상태 관리, 커넥터 선택, 성능 병목 분석, 마이그레이션 호환성 점검 등 전 생애주기 단계별 맞춤형 가이드를 제공하여 개발 생산성과 안정성을 높였다.

Highlights:

- summary: In this post, we walk through installing the Power and Skill, using Amazon Kinesis **Data** Streams to build
- summary: a Kinesis **Data** Stream-to-Kinesis **Data** Stream **streaming** **pipeline**, and migrating an existing application
- content: In this post, we walk through installing the Power and Skill, using Amazon Kinesis **Data** Streams to build a Kinesis **Data** Stream-to-Kinesis **Data** Stream **streaming** **pipeline**
- content: Example: Building a Kinesis-to-Kinesis **streaming** **pipeline** Rather than listing best practices, the Power/Skill actively guides you through making the right architectural


### architecture-cdc - `Change Data Capture`

- category: architecture
- intent: CDC 기반 데이터 동기화나 변경 데이터 처리 사례를 찾는다.
- total results: 17
- precision@5: 0.400
- recall@10: 1.000
- mrr: 1.000
- ndcg@10: 0.932

#### Expected URLs

- relevance 3: [Getting started with Change Data Capture in Amazon Aurora DSQL](https://aws.amazon.com/blogs/database/getting-started-with-change-data-capture-in-amazon-aurora-dsql/)
- relevance 2: [Migrating Amazon RDS for PostgreSQL to Amazon Aurora using seeded logical replication](https://aws.amazon.com/blogs/database/migrating-amazon-rds-for-postgresql-to-amazon-aurora-using-seeded-logical-replication/)

#### Top Results

| Rank | Match | Title | Source | Score | Keywords |
|---:|---|---|---|---:|---|
| 1 | expected:3 | [Getting started with Change Data Capture in Amazon Aurora DSQL](https://aws.amazon.com/blogs/database/getting-started-with-change-data-capture-in-amazon-aurora-dsql/) | AWS / AWS Database Blog | 1115.43 | AWS IAM, AWS Lambda, Amazon Aurora, Apache Kafka, React, search |
| 2 | - | [Enable real-time mainframe analytics with Precisely Connect and Amazon S3](https://aws.amazon.com/blogs/big-data/enable-real-time-mainframe-analytics-with-precisely-connect-and-amazon-s3/) | AWS / AWS Big Data Blog | 695.69 | AWS Glue, Amazon MSK, Amazon RDS, Amazon S3, Apache Iceberg, migration |
| 3 | - | [엔지니어링 프로젝트 임팩트 산정하기](https://medium.com/wantedjobs/%EC%97%94%EC%A7%80%EB%8B%88%EC%96%B4%EB%A7%81-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EC%9E%84%ED%8C%A9%ED%8A%B8-%EC%82%B0%EC%A0%95%ED%95%98%EA%B8%B0-cfc2bf8574eb?source=rss----fb47eceee74c---4) | Wantedlab / Wantedlab Tech Blog | 170.97 | Apache Kafka, search, Change Data Capture, streaming data pipeline |
| 4 | expected:2 | [Migrating Amazon RDS for PostgreSQL to Amazon Aurora using seeded logical replication](https://aws.amazon.com/blogs/database/migrating-amazon-rds-for-postgresql-to-amazon-aurora-using-seeded-logical-replication/) | AWS / AWS Database Blog | 163.00 | AWS IAM, Amazon Aurora, Amazon CloudWatch, Amazon RDS, Amazon VPC, high availability |
| 5 | - | [Sharded MySQL Cluster 도입 배경과 개발기 (부제: 우당탕탕 좌충우돌 개발기)](https://dev.gmarket.com/61) | Gmarket / Gmarket Tech Blog | 158.65 | Apache Kafka, JPA, JVM, Java, Kubernetes, Spring Boot |
| 6 | - | [Troubleshoot Amazon RDS for Oracle to Amazon Redshift DMS migrations with AWS DevOps Agent](https://aws.amazon.com/blogs/database/troubleshoot-amazon-rds-for-oracle-to-amazon-redshift-dms-migrations-with-aws-devops-agent/) | AWS / AWS Database Blog | 148.64 | AWS IAM, AWS Lambda, Amazon CloudWatch, Amazon EventBridge, Amazon RDS, incident response |
| 7 | - | [우리 팀은 카프카를 어떻게 사용하고 있을까](https://techblog.woowahan.com/17386/) | Woowa Brothers / Woowa Tech Blog | 148.37 | Amazon S3, Apache Kafka, Java, Redis, observability, Change Data Capture |
| 8 | - | [How Our Team Uses Kafka](https://techblog.woowahan.com/20078/) | Woowa Brothers / Woowa Tech Blog | 145.45 | Amazon S3, Apache Kafka, Java, Redis, performance optimization, Change Data Capture |
| 9 | - | [Query billion-scale vectors with SQL: Integrating Amazon S3 Vectors and Aurora PostgreSQL](https://aws.amazon.com/blogs/database/query-billion-scale-vectors-with-sql-integrating-amazon-s3-vectors-and-aurora-postgresql/) | AWS / AWS Database Blog | 143.41 | AWS CloudFormation, AWS IAM, AWS Lambda, Amazon Aurora, Amazon CloudWatch, Amazon RDS |
| 10 | - | [Best practices for upgrading Amazon RDS for MySQL 8.0 to 8.4 with prechecks, Blue/Green, and rollback](https://aws.amazon.com/blogs/database/best-practices-for-upgrading-amazon-rds-for-mysql-8-0-to-8-4-with-prechecks-blue-green-and-rollback/) | AWS / AWS Database Blog | 141.30 | AWS IAM, Amazon Aurora, Amazon EC2, Amazon RDS, Amazon VPC, Java |

#### Top Result Details

##### 1. Getting started with Change Data Capture in Amazon Aurora DSQL

- match: expected relevance 3
- source: AWS / AWS Database Blog
- url: https://aws.amazon.com/blogs/database/getting-started-with-change-data-capture-in-amazon-aurora-dsql/
- technologies: AWS IAM, AWS Lambda, Amazon Aurora, Apache Kafka, React, search
- problem keywords: observability, performance optimization
- case summary: Amazon Aurora DSQL의 Change Data Capture(CDC) 기능을 활용해 데이터베이스 변경 사항을 실시간으로 Amazon Kinesis Data Streams로 스트리밍하는 파이프라인 구축 사례를 다룬다.
- problem: 전통적인 데이터 동기화 방식은 지연과 운영 부담이 크고 데이터 일관성 유지가 어려워, 실시간 데이터 파이프라인 구축이 필요한 상황에서 효율적인 데이터 변경 추적 및 스트리밍 방법이 요구됨.
- solution: Aurora DSQL의 CDC 기능을 사용해 데이터베이스 변경 이벤트를 캡처하고 이를 Kinesis Data Streams로 스트리밍하여, 다운스트림 애플리케이션이 실시간으로 변경 데이터를 처리할 수 있는 이벤트 기반 아키텍처를 구현함.

Highlights:

- title: Getting started with **Change Data Capture** in Amazon Aurora DSQL
- caseSummary: Amazon Aurora DSQL의 **Change Data Capture**(CDC) 기능을 활용해 데이터베이스 변경 사항을 실시간으로 Amazon Kinesis **Data** Streams로
- summary: In this post, we demonstrate how to configure Aurora DSQL **Change Data Capture** and stream database changes
- summary: into Kinesis **Data** Streams.
- content: What is **Change Data Capture**? **Change Data Capture** identifies and records modifications made to a database and makes those changes available to external systems.
- content: Understanding Aurora DSQL **Change Data Capture** With today’s release, Aurora DSQL CDC can stream **change** events into Amazon Kinesis **Data** Streams.

##### 2. Enable real-time mainframe analytics with Precisely Connect and Amazon S3

- match: not expected
- source: AWS / AWS Big Data Blog
- url: https://aws.amazon.com/blogs/big-data/enable-real-time-mainframe-analytics-with-precisely-connect-and-amazon-s3/
- technologies: AWS Glue, Amazon MSK, Amazon RDS, Amazon S3, Apache Iceberg
- problem keywords: migration, performance optimization
- case summary: 메인프레임 데이터를 Precisely Connect를 활용해 실시간으로 Amazon S3에 직접 복제하여 중간 시스템 없이 지연 시간을 줄이고 운영 복잡성을 낮추는 아키텍처를 구현한 사례이다.
- problem: 메인프레임에서 발생하는 대량의 거래 데이터를 실시간으로 클라우드에서 분석하기 위해 기존의 다단계 복제 방식이 가진 지연, 운영 비용 증가, 데이터 무결성 문제를 해결해야 했다.
- solution: Precisely Connect를 이용해 Db2 z/OS, IMS, VSAM 등 메인프레임 데이터를 Change Data Capture 방식으로 실시간 스트리밍하여 중간 시스템 없이 직접 Amazon S3에 복제하고, Amazon S3 Tables와 AWS 분석 서비스를 활용해 즉시 분석 가능한 데이터 플랫폼을 구축했다.

Highlights:

- caseSolution: Precisely Connect를 이용해 Db2 z/OS, IMS, VSAM 등 메인프레임 데이터를 **Change Data Capture** 방식으로 실시간 스트리밍하여 중간 시스템 없이
- content: **Change Data Capture** (CDC) technology addresses these challenges through incremental **data** movement that eliminates disruptive bulk extracts by streaming only changed
- content: He is responsible for research and development in areas such as **Change Data Capture** (CDC), streaming ETL, metadata management, and VectorDBs.

##### 3. 엔지니어링 프로젝트 임팩트 산정하기

- match: not expected
- source: Wantedlab / Wantedlab Tech Blog
- url: https://medium.com/wantedjobs/%EC%97%94%EC%A7%80%EB%8B%88%EC%96%B4%EB%A7%81-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EC%9E%84%ED%8C%A9%ED%8A%B8-%EC%82%B0%EC%A0%95%ED%95%98%EA%B8%B0-cfc2bf8574eb?source=rss----fb47eceee74c---4
- technologies: Apache Kafka, search
- problem keywords: -
- case summary: 원티드랩 데이터팀은 Apache Kafka 기반의 Weaver 프로젝트를 도입해 실시간 이벤트 처리 인프라를 구축하고, 이를 통해 개발 시간 절감, SaaS 내재화 비용 절감, 인프라 비용 최적화 등 다양한 방식으로 프로젝트 임팩트를 원화 단위로 산정하였다.
- problem: 기존 배치 처리 중심의 데이터 파이프라인과 외부 툴 의존으로 인해 실시간 사용자 행동 데이터 처리와 이벤트 관리가 비효율적이며, 개발자 작업 임팩트 산정이 어려운 상황이었다.
- solution: Apache Kafka를 활용한 Weaver 프로젝트로 이벤트를 단일 endpoint로 통합하고 CDC를 실시간 이벤트로 전환하여 개발 시간과 인프라 비용을 절감하며, 임팩트를 개발 시간 절약, 유사 서비스 비용 비교, 인프라 사용량 절약 세 가지 방법으로 원화 가치로 산정하였다.

Highlights:

- summary: 안녕하세요, 원티드랩 데이터팀 **Data** Engineer 박찬민입니다. 어느덧 합류한지도 1년이 넘었습니다.
- summary: CDC를 실시간 이벤트로 전환 CDC(**change data capture**)는 데이터베이스 추가, 삭제, 수정 등의 변경 이력를 감지하는 기술입니다.
- content: 안녕하세요, 원티드랩 데이터팀 **Data** Engineer 박찬민입니다. 어느덧 합류한지도 1년이 넘었습니다. 그 동안 크고 작은 다양한 프로젝트를 진행했고, 성과를 측정하기 위해 각 작업의 임팩트를 계산해봤습니다.
- content: CDC를 실시간 이벤트로 전환 CDC(**change data capture**)는 데이터베이스 추가, 삭제, 수정 등의 변경 이력를 감지하는 기술입니다. 기존에는 이를 배치로 처리해 history 기록 이상으로 사용하기 어려웠습니다.


### architecture-cross-region-resilience - `cross-Region resilience`

- category: architecture
- intent: 리전 간 복원력, DR, cross-Region 데이터 구성 사례를 찾는다.
- total results: 171
- precision@5: 0.400
- recall@10: 1.000
- mrr: 1.000
- ndcg@10: 0.881

#### Expected URLs

- relevance 3: [How to build a cross-Region resilience for Amazon OpenSearch Service with Amazon MSK](https://aws.amazon.com/blogs/big-data/how-to-build-a-cross-region-resilience-for-amazon-opensearch-service-with-amazon-msk/)
- relevance 2: [How to consolidate cross-Region S3 data into OpenSearch](https://aws.amazon.com/blogs/big-data/how-to-consolidate-cross-region-s3-data-into-opensearch/)
- relevance 2: [Simplify cross-account and cross-Region stack output references with AWS CloudFormation and CDK’s new Fn::GetStackOutput](https://aws.amazon.com/blogs/devops/simplify-cross-account-and-cross-region-stack-output-references-with-aws-cloudformation-and-cdks-new-fngetstackoutput/)

#### Top Results

| Rank | Match | Title | Source | Score | Keywords |
|---:|---|---|---|---:|---|
| 1 | expected:3 | [How to build a cross-Region resilience for Amazon OpenSearch Service with Amazon MSK](https://aws.amazon.com/blogs/big-data/how-to-build-a-cross-region-resilience-for-amazon-opensearch-service-with-amazon-msk/) | AWS / AWS Big Data Blog | 1071.63 | AWS CloudFormation, AWS IAM, AWS Lambda, Amazon CloudWatch, Amazon MSK, Amazon OpenSearch Service |
| 2 | - | [Enabling high availability of Amazon EC2 instances on AWS Outposts servers (Part 3)](https://aws.amazon.com/blogs/compute/enabling-high-availability-of-amazon-ec2-instances-on-aws-outposts-servers-part-3/) | AWS / AWS Compute Blog | 421.53 | AWS CloudFormation, AWS IAM, AWS Lambda, Amazon CloudWatch, Amazon EC2, high availability |
| 3 | - | [Streamlining access to powerful disaster recovery capabilities of AWS](https://aws.amazon.com/blogs/architecture/streamlining-access-to-powerful-disaster-recovery-capabilities-of-aws/) | AWS / AWS Architecture Blog | 272.16 | AWS IAM, AWS Lambda, Amazon DynamoDB, Amazon EC2, Amazon EKS, Amazon EventBridge |
| 4 | - | [Amazon Aurora DSQL for global-scale financial transactions](https://aws.amazon.com/blogs/database/amazon-aurora-dsql-for-global-scale-financial-transactions/) | AWS / AWS Database Blog | 261.91 | Amazon Aurora, high availability, migration, performance optimization, cross-Region resilience, serverless |
| 5 | expected:2 | [How to consolidate cross-Region S3 data into OpenSearch](https://aws.amazon.com/blogs/big-data/how-to-consolidate-cross-region-s3-data-into-opensearch/) | AWS / AWS Big Data Blog | 213.18 | AWS IAM, Amazon OpenSearch Service, Amazon S3, Amazon VPC, search, observability |
| 6 | - | [Amazon Aurora DSQL connections: Drivers, strings, and best practices](https://aws.amazon.com/blogs/database/amazon-aurora-dsql-connections-drivers-strings-and-best-practices/) | AWS / AWS Database Blog | 212.19 | AWS IAM, AWS Lambda, Amazon Aurora, Amazon CloudWatch, Amazon EventBridge, Amazon RDS |
| 7 | expected:2 | [Simplify cross-account and cross-Region stack output references with AWS CloudFormation and CDK’s new Fn::GetStackOutput](https://aws.amazon.com/blogs/devops/simplify-cross-account-and-cross-region-stack-output-references-with-aws-cloudformation-and-cdks-new-fngetstackoutput/) | AWS / AWS DevOps Blog | 204.54 | AWS CDK, AWS CloudFormation, AWS IAM, Amazon EC2, Amazon VPC, cross-Region resilience |
| 8 | - | [Migrate third-party and self-managed Apache Kafka clusters to Amazon MSK Express brokers with Amazon MSK Replicator](https://aws.amazon.com/blogs/big-data/migrate-third-party-and-self-managed-apache-kafka-clusters-to-amazon-msk-express-brokers-with-amazon-msk-replicator/) | AWS / AWS Big Data Blog | 201.01 | AWS IAM, Amazon CloudWatch, Amazon MSK, Amazon S3, Amazon VPC, Apache Kafka |
| 9 | - | [Migrating data from an Amazon Aurora snapshot into Amazon Aurora DSQL](https://aws.amazon.com/blogs/database/migrating-data-from-an-amazon-aurora-snapshot-into-amazon-aurora-dsql/) | AWS / AWS Database Blog | 199.92 | AWS CloudFormation, AWS Glue, AWS IAM, Amazon Aurora, Amazon RDS, Amazon S3 |
| 10 | - | [Building unified data pipelines with Apache Iceberg and Apache Flink](https://aws.amazon.com/blogs/big-data/building-unified-data-pipelines-with-apache-iceberg-and-apache-flink/) | AWS / AWS Big Data Blog | 156.47 | AWS Glue, AWS IAM, Amazon CloudWatch, Amazon EC2, Amazon S3, Amazon VPC |

#### Top Result Details

##### 1. How to build a cross-Region resilience for Amazon OpenSearch Service with Amazon MSK

- match: expected relevance 3
- source: AWS / AWS Big Data Blog
- url: https://aws.amazon.com/blogs/big-data/how-to-build-a-cross-region-resilience-for-amazon-opensearch-service-with-amazon-msk/
- technologies: AWS CloudFormation, AWS IAM, AWS Lambda, Amazon CloudWatch, Amazon MSK, Amazon OpenSearch Service, Amazon S3, Amazon VPC, Apache Kafka, search
- problem keywords: high availability, observability, performance optimization
- case summary: Amazon OpenSearch Service와 Amazon MSK를 활용해 AWS 리전 간 실시간 데이터 동기화 및 액티브-액티브 복제를 구현하여 고가용성과 장애 복구를 자동화한 사례입니다.
- problem: 기존 Amazon OpenSearch Service의 리전 간 복제는 S3 스냅샷이나 크로스 클러스터 복제에 의존해 수동 장애 조치가 필요하고, 이로 인해 다운타임과 데이터 불일치, 지연이 발생하는 문제가 있었습니다.
- solution: Amazon MSK Replicator를 이용한 양방향 리전 간 데이터 복제와 Amazon OpenSearch Ingestion(OSI) 파이프라인을 결합해 액티브-액티브 모델을 구축, 각 리전에서 동일한 데이터셋을 유지하며 자동 장애 조치와 데이터 동기화를 실현했습니다.

Highlights:

- title: How to build a **cross-Region resilience** for Amazon OpenSearch Service with Amazon MSK
- summary: In this post, we outline the solution that provides **cross**-**Region** resiliency without needing to reestablish
- content: **Cross-Region resilience** for Amazon OpenSearch Service has historically been a complex challenge, relying on S3-based snapshots or **cross**-cluster replication that
- content: OpenSearch Service provides **high availability** (HA) within an AWS **Region** through its Multi-AZ deployment model and provides Regional resiliency with **cross**-cluster

##### 2. Enabling high availability of Amazon EC2 instances on AWS Outposts servers (Part 3)

- match: not expected
- source: AWS / AWS Compute Blog
- url: https://aws.amazon.com/blogs/compute/enabling-high-availability-of-amazon-ec2-instances-on-aws-outposts-servers-part-3/
- technologies: AWS CloudFormation, AWS IAM, AWS Lambda, Amazon CloudWatch, Amazon EC2
- problem keywords: high availability, observability, performance optimization
- case summary: AWS Outposts 서버에서 타사 스토리지를 활용해 EC2 인스턴스의 부팅 및 데이터 볼륨을 공유하고, CloudWatch와 Lambda를 이용해 장애 시 자동 재시작을 구현하여 고가용성을 확보하는 사례이다.
- problem: AWS Outposts 환경에서 EC2 인스턴스가 장애 발생 시 데이터 손실 없이 빠르게 복구할 수 있는 고가용성 아키텍처를 구현하는 문제.
- solution: 두 대 이상의 Outposts 서버를 N+1 이중화 구성으로 연결하고, iSCSI 프로토콜을 지원하는 타사 스토리지에 부팅 및 데이터 볼륨을 저장하여 공유한다. CloudWatch 알람과 SNS 알림으로 장애를 감지하고, Lambda 함수가 자동으로 장애 인스턴스를 다른 Outposts 서버에 재시작하도록 자동화한다. 이를 위해 CloudFormation 템플릿과 EC2 런치 템플릿을 활용해 복구 프로세스를 구성한다.

Highlights:

- title: Enabling **high availability** of Amazon EC2 instances on AWS Outposts servers (Part 3)
- summary: This post is part 3 of the three-part series ‘Enabling **high availability** of Amazon EC2 instances on AWS
- content: This post is part 3 of the three-part series ‘Enabling **high availability** of Amazon EC2 instances on AWS Outposts servers’.
- content: In this post, you will learn how to implement custom logic to provide **high availability** (HA) for your applications running on Outposts servers using two or more

##### 3. Streamlining access to powerful disaster recovery capabilities of AWS

- match: not expected
- source: AWS / AWS Architecture Blog
- url: https://aws.amazon.com/blogs/architecture/streamlining-access-to-powerful-disaster-recovery-capabilities-of-aws/
- technologies: AWS IAM, AWS Lambda, Amazon DynamoDB, Amazon EC2, Amazon EKS, Amazon EventBridge, Amazon RDS, Amazon S3, Amazon VPC, Kubernetes
- problem keywords: high availability
- case summary: AWS의 다양한 네이티브 서비스와 Arpio 솔루션을 활용해 데이터, 컴퓨팅, 네트워크, 인프라 전반에 걸친 크로스 리전 및 크로스 계정 재해 복구 자동화를 구현한 사례이다.
- problem: 재해 발생 시 AWS 클라우드 워크로드의 데이터와 컴퓨팅 자원뿐 아니라 네트워크, 인프라, 구성 정보까지 포함한 완전한 복구를 신속하고 안전하게 수행하는 어려움.
- solution: AWS Backup과 AWS Elastic Disaster Recovery를 기반으로 데이터와 EC2 인스턴스 복구를 자동화하고, Arpio SaaS를 통해 ECS, EKS, Lambda 등 다양한 컴퓨팅 서비스와 네트워크, IAM 권한, 구성 정보까지 포함한 전체 워크로드를 크로스 리전 및 크로스 계정 환경에서 완전 복구하도록 자동화했다.

Highlights:

- content: Your recovery site For DR, your recovery site is usually going to be a different AWS **Region** (**cross**-**Region**) or a different AWS account (**cross**-account) than where
- content: **Cross**-**Region** backup and recovery are essential for disaster recovery.


### migration-kafka-msk - `Kafka MSK migration`

- category: migration
- intent: Kafka에서 Amazon MSK로 이전하거나 MSK 기반으로 확장한 사례를 찾는다.
- total results: 219
- precision@5: 0.600
- recall@10: 1.000
- mrr: 1.000
- ndcg@10: 0.984

#### Expected URLs

- relevance 3: [Migrating TLS Clients managed by third-party Certificate Authorities from self-managed Apache Kafka to Amazon MSK](https://aws.amazon.com/blogs/big-data/migrating-tls-clients-managed-by-third-party-certificate-authorities-from-self-managed-apache-kafka-to-amazon-msk/)
- relevance 3: [Migrate third-party and self-managed Apache Kafka clusters to Amazon MSK Express brokers with Amazon MSK Replicator](https://aws.amazon.com/blogs/big-data/migrate-third-party-and-self-managed-apache-kafka-clusters-to-amazon-msk-express-brokers-with-amazon-msk-replicator/)
- relevance 2: [How to build a cross-Region resilience for Amazon OpenSearch Service with Amazon MSK](https://aws.amazon.com/blogs/big-data/how-to-build-a-cross-region-resilience-for-amazon-opensearch-service-with-amazon-msk/)

#### Top Results

| Rank | Match | Title | Source | Score | Keywords |
|---:|---|---|---|---:|---|
| 1 | expected:3 | [Migrate third-party and self-managed Apache Kafka clusters to Amazon MSK Express brokers with Amazon MSK Replicator](https://aws.amazon.com/blogs/big-data/migrate-third-party-and-self-managed-apache-kafka-clusters-to-amazon-msk-express-brokers-with-amazon-msk-replicator/) | AWS / AWS Big Data Blog | 840.08 | AWS IAM, Amazon CloudWatch, Amazon MSK, Amazon S3, Amazon VPC, Apache Kafka |
| 2 | expected:3 | [Migrating TLS Clients managed by third-party Certificate Authorities from self-managed Apache Kafka to Amazon MSK](https://aws.amazon.com/blogs/big-data/migrating-tls-clients-managed-by-third-party-certificate-authorities-from-self-managed-apache-kafka-to-amazon-msk/) | AWS / AWS Big Data Blog | 688.41 | AWS IAM, Amazon EC2, Amazon MSK, Apache Kafka, Java, migration |
| 3 | - | [Configure a custom domain name for your Amazon MSK cluster enabled with IAM authentication](https://aws.amazon.com/blogs/big-data/configure-a-custom-domain-name-for-your-amazon-msk-cluster-enabled-with-iam-authentication/) | AWS / AWS Big Data Blog | 533.55 | AWS CloudFormation, AWS IAM, Amazon EC2, Amazon MSK, Amazon VPC, Apache Kafka |
| 4 | expected:2 | [How to build a cross-Region resilience for Amazon OpenSearch Service with Amazon MSK](https://aws.amazon.com/blogs/big-data/how-to-build-a-cross-region-resilience-for-amazon-opensearch-service-with-amazon-msk/) | AWS / AWS Big Data Blog | 460.64 | AWS CloudFormation, AWS IAM, AWS Lambda, Amazon CloudWatch, Amazon MSK, Amazon OpenSearch Service |
| 5 | - | [로그 파이프라인 개선기 - 기존 파이프라인 문제 정의 및 해결 방안 적용](https://tech.socarcorp.kr/data/2025/02/25/log-pipeline-revamp.html) | SOCAR / SOCAR Tech Blog | 424.73 | AWS Lambda, Amazon MSK, Amazon S3, Apache Flink, Apache Kafka, Java |
| 6 | - | [Modernizing KYC with AWS serverless solutions and agentic AI for financial services](https://aws.amazon.com/blogs/architecture/modernizing-kyc-with-aws-serverless-solutions-and-agentic-ai-for-financial-services/) | AWS / AWS Architecture Blog | 424.73 | AWS Lambda, Amazon CloudWatch, Amazon DynamoDB, Amazon MSK, Amazon OpenSearch Service, Amazon S3 |
| 7 | - | [Enable real-time mainframe analytics with Precisely Connect and Amazon S3](https://aws.amazon.com/blogs/big-data/enable-real-time-mainframe-analytics-with-precisely-connect-and-amazon-s3/) | AWS / AWS Big Data Blog | 324.49 | AWS Glue, Amazon MSK, Amazon RDS, Amazon S3, Apache Iceberg, migration |
| 8 | - | [Migrate to Apache Flink 2.2 on Amazon Managed Service for Apache Flink](https://aws.amazon.com/blogs/big-data/migrate-to-apache-flink-2-2-on-amazon-managed-service-for-apache-flink/) | AWS / AWS Big Data Blog | 291.53 | AWS CloudFormation, AWS IAM, Amazon CloudWatch, Amazon DynamoDB, Amazon OpenSearch Service, Amazon S3 |
| 9 | - | [[다시보기] 3월 우아한테크세미나｜실시간 음식배달 플랫폼에서 활용한 분산 이벤트 스트리밍](https://techblog.woowahan.com/7894/) | Woowa Brothers / Woowa Tech Blog | 269.34 | Apache Kafka, event-driven architecture, streaming data pipeline |
| 10 | - | [초보 개발자를 위한 Redis Cluster Migration 가이드라인](https://dev.gmarket.com/71) | Gmarket / Gmarket Tech Blog | 232.93 | Java, Node.js, Redis, Spring Boot, search, migration |

#### Top Result Details

##### 1. Migrate third-party and self-managed Apache Kafka clusters to Amazon MSK Express brokers with Amazon MSK Replicator

- match: expected relevance 3
- source: AWS / AWS Big Data Blog
- url: https://aws.amazon.com/blogs/big-data/migrate-third-party-and-self-managed-apache-kafka-clusters-to-amazon-msk-express-brokers-with-amazon-msk-replicator/
- technologies: AWS IAM, Amazon CloudWatch, Amazon MSK, Amazon S3, Amazon VPC, Apache Kafka
- problem keywords: high availability, migration, observability, performance optimization
- case summary: 외부 Apache Kafka 클러스터에서 Amazon MSK Express 브로커로의 데이터 마이그레이션 시 MSK Replicator를 활용해 양방향 복제와 소비자 그룹 오프셋 동기화를 구현하여 다운타임과 데이터 손실 없이 마이그레이션을 수행한 사례이다.
- problem: 기존 Apache Kafka 클러스터를 Amazon MSK Express로 마이그레이션할 때 MirrorMaker 2와 같은 오픈소스 도구의 복잡한 인프라 관리, 제한적인 양방향 복제 지원, 소비자 오프셋 동기화 부재로 인한 높은 다운타임과 데이터 중복 처리 위험이 존재했다.
- solution: MSK Replicator를 사용해 SASL/SCRAM 인증 기반의 외부 Kafka 클러스터와 Amazon MSK Express 간에 양방향 데이터 및 소비자 그룹 오프셋 복제를 설정하여, 애플리케이션을 순서에 상관없이 점진적으로 이전하고 문제가 발생 시 롤백도 가능하도록 하여 마이그레이션 복잡성과 위험을 크게 줄였다.

Highlights:

- title: Migrate third-party and self-managed **Apache Kafka** clusters to **Amazon MSK** Express brokers with **Amazon **
- caseSummary: 외부 **Apache Kafka** 클러스터에서 **Amazon MSK** Express 브로커로의 데이터 마이그레이션 시 MSK Replicator를 활용해 양방향 복제와 소비자 그룹 오프셋 동기화를
- caseProblem: 기존 **Apache Kafka** 클러스터를 **Amazon MSK** Express로 마이그레이션할 때 MirrorMaker 2와 같은 오픈소스 도구의 복잡한 인프라 관리, 제한적인 양방향 복제
- caseSolution: MSK Replicator를 사용해 SASL/SCRAM 인증 기반의 외부 Kafka 클러스터와 **Amazon MSK** Express 간에 양방향 데이터 및 소비자 그룹 오프셋 복제를 설정하여
- summary: In this post, we walk you through how to replicate **Apache Kafka** data from your external **Apache Kafka**
- summary: deployments to **Amazon MSK** Express brokers using **MSK** Replicator.

##### 2. Migrating TLS Clients managed by third-party Certificate Authorities from self-managed Apache Kafka to Amazon MSK

- match: expected relevance 3
- source: AWS / AWS Big Data Blog
- url: https://aws.amazon.com/blogs/big-data/migrating-tls-clients-managed-by-third-party-certificate-authorities-from-self-managed-apache-kafka-to-amazon-msk/
- technologies: AWS IAM, Amazon EC2, Amazon MSK, Apache Kafka, Java
- problem keywords: migration, performance optimization
- case summary: 기존 제3자 인증기관(CA)에서 발급한 클라이언트 TLS 인증서를 재발급 없이 AWS Amazon MSK로 마이그레이션하는 방법을 다룬 사례입니다.
- problem: 자체 관리하는 Apache Kafka에서 Amazon MSK로 이전 시, 기존 제3자 CA가 발급한 클라이언트 인증서를 AWS Private CA로 재발급하지 않고도 신뢰할 수 있도록 하는 인증서 관리 및 신뢰 체인 문제.
- solution: 기존 제3자 CA에서 중간 인증서(Intermediate CA)를 생성하여 AWS Certificate Manager(ACM) Private CA에 임포트하고, Amazon MSK 클러스터를 이 중간 CA와 연동하여 기존 클라이언트 인증서를 재발급 없이 신뢰하도록 구성하는 방법을 적용함.

Highlights:

- title: Migrating TLS Clients managed by third-party Certificate Authorities from self-managed **Apache Kafka** to
- title: **Amazon MSK**
- caseSolution: 기존 제3자 CA에서 중간 인증서(Intermediate CA)를 생성하여 AWS Certificate Manager(ACM) Private CA에 임포트하고, **Amazon MSK**
- summary: This solution enables an accelerated **migration** path by using your current third-party CA infrastructure
- content: Amazon Managed Streaming for **Apache Kafka** (**Amazon MSK**) is a fully managed streaming data service that handles **Apache Kafka** infrastructure and operations, so developers
- content: Migrating to **Amazon MSK** requires no application code changes because **Amazon MSK** uses fully open source **Apache Kafka**, allowing existing applications and tools to

##### 3. Configure a custom domain name for your Amazon MSK cluster enabled with IAM authentication

- match: not expected
- source: AWS / AWS Big Data Blog
- url: https://aws.amazon.com/blogs/big-data/configure-a-custom-domain-name-for-your-amazon-msk-cluster-enabled-with-iam-authentication/
- technologies: AWS CloudFormation, AWS IAM, Amazon EC2, Amazon MSK, Amazon VPC, Apache Kafka, Java
- problem keywords: migration
- case summary: Amazon MSK 클러스터에 IAM 인증을 사용하는 경우, 커스텀 도메인 이름을 설정하여 TLS 암호화 및 인증서 관리를 개선하는 방법을 다룬 사례입니다.
- problem: Amazon MSK 클러스터에 IAM 인증을 적용할 때, 클라이언트와 브로커 간 TLS 통신을 위해 커스텀 도메인 이름과 일치하는 서버 인증서가 필요하며, 이를 위한 인증서 관리와 DNS 설정이 복잡한 문제입니다.
- solution: Network Load Balancer(NLB)와 AWS Certificate Manager(ACM)를 활용해 커스텀 도메인 이름에 맞는 TLS 인증서를 제공하고, Route 53 프라이빗 호스티드 존을 통해 DNS를 관리하며, CloudFormation 템플릿으로 인프라를 자동 배포하고 EC2 인스턴스에서 브로커의 advertised.listeners 설정을 업데이트하는 방식을 적용했습니다.

Highlights:

- title: Configure a custom domain name for your **Amazon MSK** cluster enabled with IAM authentication
- caseSummary: **Amazon MSK** 클러스터에 IAM 인증을 사용하는 경우, 커스텀 도메인 이름을 설정하여 TLS 암호화 및 인증서 관리를 개선하는 방법을 다룬 사례입니다.
- caseProblem: **Amazon MSK** 클러스터에 IAM 인증을 적용할 때, 클라이언트와 브로커 간 TLS 통신을 위해 커스텀 도메인 이름과 일치하는 서버 인증서가 필요하며, 이를 위한 인증서 관리와
- summary: In the first part of Configure a custom domain name for your **Amazon MSK** cluster, we discussed about why
- summary: custom domain names are important and provided details on how to configure a custom domain name in **Amazon MSK**
- content: Most Amazon Managed Streaming for **Apache Kafka** (**Amazon MSK**) customers are simplifying and standardizing access control to **Kafka** resources using AWS Identity and


### ko-problem-cost-optimization - `비용 최적화`

- category: problem
- intent: 한글 검색어로 비용 최적화, 성능 개선, 비용 절감 사례를 찾는다.
- total results: 352
- precision@5: 0.000
- recall@10: 0.167
- mrr: 0.125
- ndcg@10: 0.110

#### Expected URLs

- relevance 3: [우아한 Cloud FinOps 여정](https://techblog.woowahan.com/22855/)
- relevance 3: [클라우드 비용 가시화 그렇게 어렵지 않아요!](https://tech.kakaopay.com/post/cloud-cost-visualization/)
- relevance 3: [최적화된 인스턴스 추천을 위한 Rightsizing Recommendations 시스템 개발 여정](https://techblog.woowahan.com/19685/)
- relevance 2: [안전은 기본, 비용 절감은 덤: AI 서비스에 별도 가드레일이 필요한 이유](https://techblog.lycorp.co.jp/ko/safety-and-cost-saving-why-separate-guardrails-are-necessary)
- relevance 3: [비용, 성능, 안정성을 목표로 한 지능형 로그 파이프라인 도입](https://d2.naver.com/helloworld/0004394)
- relevance 2: [How HotelTrader cut inter-AZ cost 95% and latency by 49% with Valkey GLIDE on Amazon ElastiCache](https://aws.amazon.com/blogs/database/how-hoteltrader-cut-inter-az-cost-95-and-latency-by-49-with-valkey-glide-on-amazon-elasticache/)

#### Top Results

| Rank | Match | Title | Source | Score | Keywords |
|---:|---|---|---|---:|---|
| 1 | - | [AWS re:Invent 2023, 관심 세션을 중심으로 (2편): Cost Optimization, Observability](https://tech.kakaopay.com/post/2023-aws-reinvent-2/) | Kakao Pay / Kakao Pay Tech Blog | 592.06 | cost optimization, observability |
| 2 | - | [스타트업 엔지니어의 AWS 비용 최적화 경험기](https://tech.inflab.com/20240227-finops-for-startup/) | Inflab / Inflab Tech Blog | 537.38 | AWS CDK, AWS CloudFormation, AWS Lambda, Amazon Aurora, Amazon CloudWatch, Amazon DynamoDB |
| 3 | - | [클라우드 서비스 사용량 관리를 통한 운영 비용 최적화](https://medium.com/coupang-engineering/%ED%81%B4%EB%9D%BC%EC%9A%B0%EB%93%9C-%EC%84%9C%EB%B9%84%EC%8A%A4-%EC%82%AC%EC%9A%A9%EB%9F%89-%EA%B4%80%EB%A6%AC%EB%A5%BC-%ED%86%B5%ED%95%9C-%EC%9A%B4%EC%98%81-%EB%B9%84%EC%9A%A9-%EC%B5%9C%EC%A0%81%ED%99%94-1521565c64ec?source=rss----fb028911af07---4) | Coupang / Coupang Engineering Blog | 489.17 | Amazon CloudWatch, Amazon EC2, Amazon S3, cost optimization, migration, observability |
| 4 | - | [데이터는 지웠는데 비용은 그대로? Aurora 스토리지 비용 최적화 하기](https://medium.com/wantedjobs/%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%8A%94-%EC%A7%80%EC%9B%A0%EB%8A%94%EB%8D%B0-%EB%B9%84%EC%9A%A9%EC%9D%80-%EA%B7%B8%EB%8C%80%EB%A1%9C-aurora-%EC%8A%A4%ED%86%A0%EB%A6%AC%EC%A7%80-%EB%B9%84%EC%9A%A9-%EC%B5%9C%EC%A0%81%ED%99%94-%ED%95%98%EA%B8%B0-43d208f6564d?source=rss----fb47eceee74c---4) | Wantedlab / Wantedlab Tech Blog | 468.77 | Amazon Aurora, Amazon CloudWatch, Amazon RDS, cost optimization, observability |
| 5 | - | [The Hidden Price Tag: Uncovering Hidden Costs in Cloud Architectures with the AWS Well-Architected Framework](https://aws.amazon.com/blogs/architecture/the-hidden-price-tag-uncovering-hidden-costs-in-cloud-architectures-with-the-aws-well-architected-framework/) | AWS / AWS Architecture Blog | 360.73 | AWS CloudFormation, AWS IAM, cost optimization, high availability, incident response, observability |
| 6 | - | [Cloud expenditure optimization for cost efficiency](https://medium.com/coupang-engineering/cloud-expenditure-optimization-for-cost-efficiency-44e9bea3d91b?source=rss----fb028911af07---4) | Coupang / Coupang Engineering Blog | 356.94 | Amazon CloudWatch, Amazon EC2, Amazon S3, cost optimization, migration, observability |
| 7 | - | [이달의 Nclouder 10월 주인공을 소개합니다!](https://medium.com/naver-cloud-platform/%EC%9D%B4%EB%8B%AC%EC%9D%98-nclouder-10%EC%9B%94-%EC%A3%BC%EC%9D%B8%EA%B3%B5%EC%9D%84-%EC%86%8C%EA%B0%9C%ED%95%A9%EB%8B%88%EB%8B%A4-9d7e18801b7c?source=rss----c7f2bfeb6b98---4) | NAVER Cloud / NAVER Cloud Platform Tech Blog | 332.08 | cost optimization, high availability, observability |
| 8 | expected:3 | [우아한 Cloud FinOps 여정](https://techblog.woowahan.com/22855/) | Woowa Brothers / Woowa Tech Blog | 317.90 | Amazon CloudWatch, Amazon EC2, Amazon EKS, Amazon ElastiCache, Amazon OpenSearch Service, Amazon RDS |
| 9 | - | [데이터분석가로서 업무 과정과 경험, 배움을 공유합니다](https://techblog.woowahan.com/2686/) | Woowa Brothers / Woowa Tech Blog | 310.87 | cost optimization, observability |
| 10 | - | [엔지니어링 프로젝트 임팩트 산정하기](https://medium.com/wantedjobs/%EC%97%94%EC%A7%80%EB%8B%88%EC%96%B4%EB%A7%81-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EC%9E%84%ED%8C%A9%ED%8A%B8-%EC%82%B0%EC%A0%95%ED%95%98%EA%B8%B0-cfc2bf8574eb?source=rss----fb47eceee74c---4) | Wantedlab / Wantedlab Tech Blog | 273.81 | Apache Kafka, search, Change Data Capture, streaming data pipeline |

#### Top Result Details

##### 1. AWS re:Invent 2023, 관심 세션을 중심으로 (2편): Cost Optimization, Observability

- match: not expected
- source: Kakao Pay / Kakao Pay Tech Blog
- url: https://tech.kakaopay.com/post/2023-aws-reinvent-2/
- technologies: -
- problem keywords: cost optimization, observability
- case summary: AWS re:Invent 2023에서 비용 최적화와 관측성 관련 세션을 중심으로 최신 클라우드 운영 전략과 기술을 소개하고 적용 가능성을 검토한 사례입니다.
- problem: 클라우드 환경에서 비용 효율성을 유지하면서도 시스템의 상태를 효과적으로 모니터링하고 문제를 신속히 파악하는 운영상의 어려움이 있었습니다.
- solution: AWS의 최신 비용 최적화 도구와 관측성 솔루션을 활용해 리소스 사용을 최적화하고, 로그 및 메트릭 기반의 통합 모니터링 체계를 구축하여 운영 효율을 높였습니다.

Highlights:

- title: AWS re:Invent 2023, 관심 세션을 중심으로 (2편): **Cost Optimization**, Observability
- caseSummary: AWS re:Invent 2023에서 **비용** 최적화와 관측성 관련 세션을 중심으로 최신 클라우드 운영 전략과 기술을 소개하고 적용 가능성을 검토한 사례입니다.
- caseProblem: 클라우드 환경에서 **비용** 효율성을 유지하면서도 시스템의 상태를 효과적으로 모니터링하고 문제를 신속히 파악하는 운영상의 어려움이 있었습니다.
- caseSolution: AWS의 최신 **비용 최적화** 도구와 관측성 솔루션을 활용해 리소스 사용을 최적화하고, 로그 및 메트릭 기반의 통합 모니터링 체계를 구축하여 운영 효율을 높였습니다.

##### 2. 스타트업 엔지니어의 AWS 비용 최적화 경험기

- match: not expected
- source: Inflab / Inflab Tech Blog
- url: https://tech.inflab.com/20240227-finops-for-startup/
- technologies: AWS CDK, AWS CloudFormation, AWS Lambda, Amazon Aurora, Amazon CloudWatch, Amazon DynamoDB, Amazon EC2, Amazon ElastiCache, Amazon RDS, Amazon S3, Amazon VPC, Elasticsearch, Istio, Kubernetes, Redis, search
- problem keywords: cost optimization, observability, performance optimization
- case summary: 스타트업 인프랩은 AWS 기반 서비스 운영 중 고비용 문제를 해결하기 위해 MSP 활용, EC2 스팟 인스턴스 도입, 매니지드 서비스 직접 구축 전환 등 다양한 비용 최적화 전략을 적용해 연간 약 3억 9,900만 원을 절감했다.
- problem: 스타트업 환경에서 AWS 클라우드 비용이 급증하며 비용 효율적인 운영과 지속적인 비용 관리가 필요했으며, 매니지드 서비스 사용 시 비용 부담과 벤더 락인 문제도 발생했다.
- solution: 비용이 큰 상위 10개 서비스부터 우선 분석하고, 리소스 태깅 정책을 수립해 비용 추적을 강화했으며, AWS Batch와 EC2 스팟 인스턴스를 활용해 비디오 트랜스코딩과 CI/CD 파이프라인을 직접 구축해 비용을 대폭 절감했다. MSP 계약을 통해 할인 혜택과 기술 지원을 받고, 서버리스 도입 시 적정 워크로드를 고려하는 등 팀 차원의 지속적 비용 모니터링과 개선 문화를 정착시켰다.

Highlights:

- title: 스타트업 엔지니어의 AWS **비용 최적화** 경험기
- caseSummary: 스타트업 인프랩은 AWS 기반 서비스 운영 중 고비용 문제를 해결하기 위해 MSP 활용, EC2 스팟 인스턴스 도입, 매니지드 서비스 직접 구축 전환 등 다양한 **비용 최적화** 전략을
- caseProblem: 스타트업 환경에서 AWS 클라우드 비용이 급증하며 **비용** 효율적인 운영과 지속적인 **비용** 관리가 필요했으며, 매니지드 서비스 사용 시 **비용** 부담과 벤더 락인 문제도 발생했다.
- caseSolution: 비용이 큰 상위 10개 서비스부터 우선 분석하고, 리소스 태깅 정책을 수립해 **비용** 추적을 강화했으며, AWS Batch와 EC2 스팟 인스턴스를 활용해 비디오 트랜스코딩과 CI/CD
- caseSolution: MSP 계약을 통해 할인 혜택과 기술 지원을 받고, 서버리스 도입 시 적정 워크로드를 고려하는 등 팀 차원의 지속적 **비용** 모니터링과 개선 문화를 정착시켰다.
- content: 이번 글에서는 스타트업을 기준으로 AWS를 저렴하고 효율적으로 이용할 수 있는 여러 **비용 최적화** 노하우를 공유드릴게요. 간단한 **비용** 절약 노하우부터, 이를 팀 내 문화로 만들기 위한 노력을 소개해 드리겠습니다.

##### 3. 클라우드 서비스 사용량 관리를 통한 운영 비용 최적화

- match: not expected
- source: Coupang / Coupang Engineering Blog
- url: https://medium.com/coupang-engineering/%ED%81%B4%EB%9D%BC%EC%9A%B0%EB%93%9C-%EC%84%9C%EB%B9%84%EC%8A%A4-%EC%82%AC%EC%9A%A9%EB%9F%89-%EA%B4%80%EB%A6%AC%EB%A5%BC-%ED%86%B5%ED%95%9C-%EC%9A%B4%EC%98%81-%EB%B9%84%EC%9A%A9-%EC%B5%9C%EC%A0%81%ED%99%94-1521565c64ec?source=rss----fb028911af07---4
- technologies: Amazon CloudWatch, Amazon EC2, Amazon S3
- problem keywords: cost optimization, migration, observability
- case summary: 쿠팡은 클라우드 서비스 사용량과 비용을 체계적으로 관리하고 최적화하기 위해 전담 프로젝트 팀을 구성하여 AWS 인스턴스 세대 조정, EMR 인스턴스 플릿 활용, 스토리지 구조 개선 등 다양한 기술적 접근을 통해 수백만 달러의 온디맨드 비용을 절감했다.
- problem: 클라우드 서비스 사용에 대한 엔지니어링 팀의 이해 부족과 비용 지출에 대한 파이낸스 및 리더십 팀의 분석 미흡으로 인해 불필요한 비용이 발생하고, 비용 관리 및 최적화가 어려운 상황이었다.
- solution: 클라우드 인프라 엔지니어와 TPM 중심의 최적화 프로젝트 팀을 구성해 도메인 팀과 협업하며 AWS Spot Instances, ARM 기반 Graviton, 최신 인스턴스 세대 전환, EMR 인스턴스 플릿 기능 활용, Amazon S3 Intelligent-Tiering 적용 등 다양한 최적화 기법을 도입하고, 맞춤형 대시보드와 분석 도구를 제공해 비용 효율적인 클라우드 사용 문화를 정착시켰다.

Highlights:

- title: 클라우드 서비스 사용량 관리를 통한 운영 **비용 최적화**
- caseProblem: 클라우드 서비스 사용에 대한 엔지니어링 팀의 이해 부족과 **비용** 지출에 대한 파이낸스 및 리더십 팀의 분석 미흡으로 인해 불필요한 비용이 발생하고, **비용** 관리 및 최적화가 어려운 상황이었다
- caseSolution: 클라우드 인프라 엔지니어와 TPM 중심의 **최적화** 프로젝트 팀을 구성해 도메인 팀과 협업하며 AWS Spot Instances, ARM 기반 Graviton, 최신 인스턴스 세대 전환
- caseSolution: , EMR 인스턴스 플릿 기능 활용, Amazon S3 Intelligent-Tiering 적용 등 다양한 **최적화** 기법을 도입하고, 맞춤형 대시보드와 분석 도구를 제공해 **비용** 효율적인
- summary: 하나의 팀으로서 저희는 다음과 같은 세 가지 핵심 원칙 하에 **비용 최적화** 작업을 수행했고, 이 포스트를 통해 어떤 작업이 이루어졌는지 공유드리고자 합니다.
- summary: 프로젝트 팀 구성하기 · 2 단계: 더 적게 쓰고 더 적게 지불하기 ∘ 인스턴스 세대 조정 ∘ EMR ∘ 스토리지 · 결론 배경 및 과제 **비용 최적화** 작업을 시작할 당시 쿠팡은 다음과


### ko-problem-incident-response - `장애 대응`

- category: problem
- intent: 한글 검색어로 장애 대응, 사고 조사, SRE 자동화 사례를 찾는다.
- total results: 360
- precision@5: 0.200
- recall@10: 0.333
- mrr: 0.500
- ndcg@10: 0.182

#### Expected URLs

- relevance 3: [장애 대응의 성패를 가르는 First Action: 우아한형제들의 장애 관리 라이프사이클](https://techblog.woowahan.com/25189/)
- relevance 2: [Leverage Agentic AI for Autonomous Incident Response with AWS DevOps Agent](https://aws.amazon.com/blogs/devops/leverage-agentic-ai-for-autonomous-incident-response-with-aws-devops-agent/)
- relevance 2: [Automating Incident Investigation with AWS DevOps Agent and Salesforce MCP Server](https://aws.amazon.com/blogs/devops/automating-incident-investigation-with-aws-devops-agent-and-salesforce-mcp-server/)

#### Top Results

| Rank | Match | Title | Source | Score | Keywords |
|---:|---|---|---|---:|---|
| 1 | - | [데브시스터즈의 장애 대응 원칙과 방법](https://tech.devsisters.com/posts/incident-management-principles) | Devsisters / Devsisters Tech Blog | 649.94 | incident response, observability, performance optimization |
| 2 | expected:2 | [Leverage Agentic AI for Autonomous Incident Response with AWS DevOps Agent](https://aws.amazon.com/blogs/devops/leverage-agentic-ai-for-autonomous-incident-response-with-aws-devops-agent/) | AWS / AWS DevOps Blog | 441.17 | AWS IAM, AWS Lambda, Amazon CloudWatch, Amazon DynamoDB, Amazon EKS, Amazon S3 |
| 3 | - | [우아한형제들이 장애를 놓치지 않고 탐지하는 방법](https://techblog.woowahan.com/24488/) | Woowa Brothers / Woowa Tech Blog | 431.75 | incident response, observability |
| 4 | - | [우아~한 장애대응](https://techblog.woowahan.com/4886/) | Woowa Brothers / Woowa Tech Blog | 386.40 | incident response, observability, performance optimization |
| 5 | - | [나를 술푸게 하는 고민들](https://techblog.woowahan.com/2583/) | Woowa Brothers / Woowa Tech Blog | 368.89 | Java, MQTT, search, incident response |
| 6 | - | [피처 플래그 개발기: 실시간 데이터 동기화를 향한 여정](https://tech.kakaopay.com/post/feature-flag/) | Kakao Pay / Kakao Pay Tech Blog | 368.89 | incident response |
| 7 | - | [데브시스터즈 엔지니어링 데이 - Infra/SRE 돌아보기](https://tech.devsisters.com/posts/2025-engineering-day-infra-sre) | Devsisters / Devsisters Tech Blog | 358.07 | Kubernetes, incident response |
| 8 | - | [Netflix Hystrix를 이용한 MSA 회복성 패턴 톺아보기](https://dev.gmarket.com/40) | Gmarket / Gmarket Tech Blog | 356.17 | Istio, Spring Boot, incident response, observability, performance optimization |
| 9 | - | [훈련은 실전처럼, 실전은…… 싫어요](https://techblog.woowahan.com/7346/) | Woowa Brothers / Woowa Tech Blog | 355.56 | incident response, observability |
| 10 | - | [선제적 장애 대응을 위한 Sentry 최적화 적용기](https://techblog.woowahan.com/21604/) | Woowa Brothers / Woowa Tech Blog | 355.56 | search, incident response, observability |

#### Top Result Details

##### 1. 데브시스터즈의 장애 대응 원칙과 방법

- match: not expected
- source: Devsisters / Devsisters Tech Blog
- url: https://tech.devsisters.com/posts/incident-management-principles
- technologies: -
- problem keywords: incident response, observability, performance optimization
- case summary: 데브시스터즈는 장애 대응 시 서비스 정상화 우선 원칙과 체계적인 알람 티어링, 역할 분담, 기록 및 커뮤니케이션, 포스트모템을 통한 지속적 개선 방법론을 적용하여 장애 대응 역량을 강화하였다.
- problem: 서비스 장애 발생 시 신속하고 효과적인 대응 체계 부재로 인한 서비스 중단 및 복구 지연 문제.
- solution: 장애 대응 목표를 서비스 정상화에 두고, 알람 티어링(FRT 기준)으로 우선순위를 구분하며, 장애 대응 팀을 구성해 지휘자와 기록가 역할을 명확히 분담하고, 실시간 기록과 커뮤니케이션을 통해 협업하며, 장애 종료 후 포스트모템을 통해 원인 분석과 재발 방지 대책을 수립하는 체계적 장애 대응 프로세스를 구축하였다.

Highlights:

- title: 데브시스터즈의 **장애 대응** 원칙과 방법
- caseSummary: 데브시스터즈는 **장애 대응** 시 서비스 정상화 우선 원칙과 체계적인 알람 티어링, 역할 분담, 기록 및 커뮤니케이션, 포스트모템을 통한 지속적 개선 방법론을 적용하여 **장애 대응** 역량을
- caseProblem: 서비스 **장애** 발생 시 신속하고 효과적인 **대응** 체계 부재로 인한 서비스 중단 및 복구 지연 문제.
- caseSolution: **장애 대응** 목표를 서비스 정상화에 두고, 알람 티어링(FRT 기준)으로 우선순위를 구분하며, **장애 대응** 팀을 구성해 지휘자와 기록가 역할을 명확히 분담하고, 실시간 기록과 커뮤니케이션을
- caseSolution: 통해 협업하며, **장애** 종료 후 포스트모템을 통해 원인 분석과 재발 방지 대책을 수립하는 체계적 **장애 대응** 프로세스를 구축하였다.
- summary: 데브시스터즈에서 적용하고 있는 **장애 대응** 원칙과 방법을 공개합니다.

##### 2. Leverage Agentic AI for Autonomous Incident Response with AWS DevOps Agent

- match: expected relevance 2
- source: AWS / AWS DevOps Blog
- url: https://aws.amazon.com/blogs/devops/leverage-agentic-ai-for-autonomous-incident-response-with-aws-devops-agent/
- technologies: AWS IAM, AWS Lambda, Amazon CloudWatch, Amazon DynamoDB, Amazon EKS, Amazon S3, Kubernetes, LLM
- problem keywords: high availability, incident response, observability, performance optimization
- case summary: AWS DevOps Agent를 활용해 분산 서버리스 애플리케이션의 장애를 AI 기반으로 자동 탐지 및 원인 분석하여, 수동 대응 시간을 수 시간에서 수 분으로 단축한 사례이다.
- problem: 분산된 서버리스 아키텍처에서 장애 발생 시 로그, 배포 이력, 모니터링 데이터가 여러 곳에 흩어져 있어 SRE가 수동으로 원인 분석에 많은 시간이 소요되는 문제.
- solution: AWS DevOps Agent를 도입해 애플리케이션 토폴로지 자동 탐지, 크로스 계정 및 멀티 클라우드 관찰, AI 기반 자율 조사 및 원인 분석, 그리고 Slack 등 협업 도구와 연동한 자동 대응 체계를 구축함으로써 MTTR을 크게 단축함.

Highlights:

- title: Leverage Agentic AI for Autonomous **Incident Response** with AWS DevOps Agent
- caseSummary: AWS DevOps Agent를 활용해 분산 서버리스 애플리케이션의 장애를 AI 기반으로 자동 탐지 및 원인 분석하여, 수동 **대응** 시간을 수 시간에서 수 분으로 단축한 사례이다.
- caseProblem: 분산된 서버리스 아키텍처에서 **장애** 발생 시 로그, 배포 이력, 모니터링 데이터가 여러 곳에 흩어져 있어 SRE가 수동으로 원인 분석에 많은 시간이 소요되는 문제.
- caseSolution: DevOps Agent를 도입해 애플리케이션 토폴로지 자동 탐지, 크로스 계정 및 멀티 클라우드 관찰, AI 기반 자율 조사 및 원인 분석, 그리고 Slack 등 협업 도구와 연동한 자동 **대응**
- content: For any team operating distributed and complex architectural applications on AWS — DevOps Agent reduces the operational burden of **incident response** while building
- content: Tipu Qureshi Tipu Qureshi is a Senior Principal Technologist in AWS Agentic AI, focusing on operational excellence and **incident response** automation.

##### 3. 우아한형제들이 장애를 놓치지 않고 탐지하는 방법

- match: not expected
- source: Woowa Brothers / Woowa Tech Blog
- url: https://techblog.woowahan.com/24488/
- technologies: -
- problem keywords: incident response, observability
- case summary: 우아한형제들은 배달의민족 서비스에서 장애를 빠르고 정확하게 탐지하기 위해 서비스 지표 기반의 이상 탐지 시스템을 도입하고, 실시간 경보와 자동화된 장애 대응 프로세스를 구축하여 장애 대응 효율을 크게 향상시켰다.
- problem: 서비스 변화와 복잡성으로 인해 전통적인 시스템 지표 모니터링만으로는 모든 장애를 놓치지 않고 탐지하기 어려웠으며, 장애 발생 시 신속한 인지와 대응이 필수적이었다.
- solution: 실시간 서비스 지표(로그인 수, 주문 수 등)를 중앙값 기반 이상 탐지 기법으로 모니터링하고, 임계 도달 횟수 조건을 추가해 오탐을 줄였으며, Slack과 Opsgenie 연동을 통한 자동 경보 및 담당자 호출, 장애 대응 프로세스 자동화를 구현했다.

Highlights:

- caseSummary: 우아한형제들은 배달의민족 서비스에서 장애를 빠르고 정확하게 탐지하기 위해 서비스 지표 기반의 이상 탐지 시스템을 도입하고, 실시간 경보와 자동화된 **장애 대응** 프로세스를 구축하여 **장애**
- caseSummary: **대응** 효율을 크게 향상시켰다.
- caseProblem: 서비스 변화와 복잡성으로 인해 전통적인 시스템 지표 모니터링만으로는 모든 장애를 놓치지 않고 탐지하기 어려웠으며, **장애** 발생 시 신속한 인지와 대응이 필수적이었다.
- caseSolution: 주문 수 등)를 중앙값 기반 이상 탐지 기법으로 모니터링하고, 임계 도달 횟수 조건을 추가해 오탐을 줄였으며, Slack과 Opsgenie 연동을 통한 자동 경보 및 담당자 호출, **장애**
- caseSolution: **대응** 프로세스 자동화를 구현했다.
- content: **장애 대응** 프로세스 임계 도달 횟수만큼 임계 값에 도달하게 되면 Slack 채널에 경보가 발송 (좌측 이미지)됩니다. 경보 메시지에는 지표 현황이나 긴급도 등의 정보가 포함되어 있어 현재 상황을 빠르게 파악할 수 있습니다.


### ko-migration-kafka - `카프카 마이그레이션`

- category: migration
- intent: 한글 기술명과 문제 상황을 함께 입력해 Kafka/MSK 이전 사례를 찾는다.
- total results: 220
- precision@5: 0.400
- recall@10: 1.000
- mrr: 1.000
- ndcg@10: 1.000

#### Expected URLs

- relevance 3: [Migrate third-party and self-managed Apache Kafka clusters to Amazon MSK Express brokers with Amazon MSK Replicator](https://aws.amazon.com/blogs/big-data/migrate-third-party-and-self-managed-apache-kafka-clusters-to-amazon-msk-express-brokers-with-amazon-msk-replicator/)
- relevance 3: [Migrating TLS Clients managed by third-party Certificate Authorities from self-managed Apache Kafka to Amazon MSK](https://aws.amazon.com/blogs/big-data/migrating-tls-clients-managed-by-third-party-certificate-authorities-from-self-managed-apache-kafka-to-amazon-msk/)

#### Top Results

| Rank | Match | Title | Source | Score | Keywords |
|---:|---|---|---|---:|---|
| 1 | expected:3 | [Migrate third-party and self-managed Apache Kafka clusters to Amazon MSK Express brokers with Amazon MSK Replicator](https://aws.amazon.com/blogs/big-data/migrate-third-party-and-self-managed-apache-kafka-clusters-to-amazon-msk-express-brokers-with-amazon-msk-replicator/) | AWS / AWS Big Data Blog | 441.79 | AWS IAM, Amazon CloudWatch, Amazon MSK, Amazon S3, Amazon VPC, Apache Kafka |
| 2 | expected:3 | [Migrating TLS Clients managed by third-party Certificate Authorities from self-managed Apache Kafka to Amazon MSK](https://aws.amazon.com/blogs/big-data/migrating-tls-clients-managed-by-third-party-certificate-authorities-from-self-managed-apache-kafka-to-amazon-msk/) | AWS / AWS Big Data Blog | 374.23 | AWS IAM, Amazon EC2, Amazon MSK, Apache Kafka, Java, migration |
| 3 | - | [Migrate to Apache Flink 2.2 on Amazon Managed Service for Apache Flink](https://aws.amazon.com/blogs/big-data/migrate-to-apache-flink-2-2-on-amazon-managed-service-for-apache-flink/) | AWS / AWS Big Data Blog | 321.81 | AWS CloudFormation, AWS IAM, Amazon CloudWatch, Amazon DynamoDB, Amazon OpenSearch Service, Amazon S3 |
| 4 | - | [[다시보기] 3월 우아한테크세미나｜실시간 음식배달 플랫폼에서 활용한 분산 이벤트 스트리밍](https://techblog.woowahan.com/7894/) | Woowa Brothers / Woowa Tech Blog | 307.35 | Apache Kafka, event-driven architecture, streaming data pipeline |
| 5 | - | [초보 개발자를 위한 Redis Cluster Migration 가이드라인](https://dev.gmarket.com/71) | Gmarket / Gmarket Tech Blog | 285.18 | Java, Node.js, Redis, Spring Boot, search, migration |
| 6 | - | [Sharded MySQL Cluster 도입 배경과 개발기 (부제: 우당탕탕 좌충우돌 개발기)](https://dev.gmarket.com/61) | Gmarket / Gmarket Tech Blog | 278.78 | Apache Kafka, JPA, JVM, Java, Kubernetes, Spring Boot |
| 7 | - | [엔지니어링 프로젝트 임팩트 산정하기](https://medium.com/wantedjobs/%EC%97%94%EC%A7%80%EB%8B%88%EC%96%B4%EB%A7%81-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EC%9E%84%ED%8C%A9%ED%8A%B8-%EC%82%B0%EC%A0%95%ED%95%98%EA%B8%B0-cfc2bf8574eb?source=rss----fb47eceee74c---4) | Wantedlab / Wantedlab Tech Blog | 257.41 | Apache Kafka, search, Change Data Capture, streaming data pipeline |
| 8 | - | [사용법과 함께 작성해본 좌충우돌 AWS DMS 사용기 - feat. RDS 통합 이야기](https://blog.banksalad.com/tech/dms/) | Banksalad / Banksalad Blog | 240.24 | Amazon RDS |
| 9 | - | [여기어때 이벤트 기반 통합 알림 플랫폼 구축기 Part 2. How?](https://techblog.gccompany.co.kr/%EC%97%AC%EA%B8%B0%EC%96%B4%EB%95%8C-%EC%9D%B4%EB%B2%A4%ED%8A%B8-%EA%B8%B0%EB%B0%98-%ED%86%B5%ED%95%A9-%EC%95%8C%EB%A6%BC-%ED%94%8C%EB%9E%AB%ED%8F%BC-%EA%B5%AC%EC%B6%95%EA%B8%B0-part-2-how-11f41bb2b5f2?source=rss----18356045d353---4) | GC Company / GC Company Tech Blog | 238.47 | Apache Kafka, Redis, migration, observability, event-driven architecture |
| 10 | - | [Delivering the Future, WOOWACON 2025](https://techblog.woowahan.com/24289/) | Woowa Brothers / Woowa Tech Blog | 237.31 | Apache Kafka, incident response, migration |

#### Top Result Details

##### 1. Migrate third-party and self-managed Apache Kafka clusters to Amazon MSK Express brokers with Amazon MSK Replicator

- match: expected relevance 3
- source: AWS / AWS Big Data Blog
- url: https://aws.amazon.com/blogs/big-data/migrate-third-party-and-self-managed-apache-kafka-clusters-to-amazon-msk-express-brokers-with-amazon-msk-replicator/
- technologies: AWS IAM, Amazon CloudWatch, Amazon MSK, Amazon S3, Amazon VPC, Apache Kafka
- problem keywords: high availability, migration, observability, performance optimization
- case summary: 외부 Apache Kafka 클러스터에서 Amazon MSK Express 브로커로의 데이터 마이그레이션 시 MSK Replicator를 활용해 양방향 복제와 소비자 그룹 오프셋 동기화를 구현하여 다운타임과 데이터 손실 없이 마이그레이션을 수행한 사례이다.
- problem: 기존 Apache Kafka 클러스터를 Amazon MSK Express로 마이그레이션할 때 MirrorMaker 2와 같은 오픈소스 도구의 복잡한 인프라 관리, 제한적인 양방향 복제 지원, 소비자 오프셋 동기화 부재로 인한 높은 다운타임과 데이터 중복 처리 위험이 존재했다.
- solution: MSK Replicator를 사용해 SASL/SCRAM 인증 기반의 외부 Kafka 클러스터와 Amazon MSK Express 간에 양방향 데이터 및 소비자 그룹 오프셋 복제를 설정하여, 애플리케이션을 순서에 상관없이 점진적으로 이전하고 문제가 발생 시 롤백도 가능하도록 하여 마이그레이션 복잡성과 위험을 크게 줄였다.

Highlights:

- title: Migrate third-party and self-managed **Apache Kafka** clusters to Amazon MSK Express brokers with Amazon
- caseSummary: 외부 **Apache Kafka** 클러스터에서 Amazon MSK Express 브로커로의 데이터 **마이그레이션** 시 MSK Replicator를 활용해 양방향 복제와 소비자 그룹 오프셋 동기화를
- caseProblem: 기존 **Apache Kafka** 클러스터를 Amazon MSK Express로 마이그레이션할 때 MirrorMaker 2와 같은 오픈소스 도구의 복잡한 인프라 관리, 제한적인 양방향 복제
- caseSolution: MSK Replicator를 사용해 SASL/SCRAM 인증 기반의 외부 **Kafka** 클러스터와 Amazon MSK Express 간에 양방향 데이터 및 소비자 그룹 오프셋 복제를 설정하여
- caseSolution: , 애플리케이션을 순서에 상관없이 점진적으로 이전하고 문제가 발생 시 롤백도 가능하도록 하여 **마이그레이션** 복잡성과 위험을 크게 줄였다.
- summary: In this post, we walk you through how to replicate **Apache Kafka** data from your external **Apache Kafka**

##### 2. Migrating TLS Clients managed by third-party Certificate Authorities from self-managed Apache Kafka to Amazon MSK

- match: expected relevance 3
- source: AWS / AWS Big Data Blog
- url: https://aws.amazon.com/blogs/big-data/migrating-tls-clients-managed-by-third-party-certificate-authorities-from-self-managed-apache-kafka-to-amazon-msk/
- technologies: AWS IAM, Amazon EC2, Amazon MSK, Apache Kafka, Java
- problem keywords: migration, performance optimization
- case summary: 기존 제3자 인증기관(CA)에서 발급한 클라이언트 TLS 인증서를 재발급 없이 AWS Amazon MSK로 마이그레이션하는 방법을 다룬 사례입니다.
- problem: 자체 관리하는 Apache Kafka에서 Amazon MSK로 이전 시, 기존 제3자 CA가 발급한 클라이언트 인증서를 AWS Private CA로 재발급하지 않고도 신뢰할 수 있도록 하는 인증서 관리 및 신뢰 체인 문제.
- solution: 기존 제3자 CA에서 중간 인증서(Intermediate CA)를 생성하여 AWS Certificate Manager(ACM) Private CA에 임포트하고, Amazon MSK 클러스터를 이 중간 CA와 연동하여 기존 클라이언트 인증서를 재발급 없이 신뢰하도록 구성하는 방법을 적용함.

Highlights:

- title: Migrating TLS Clients managed by third-party Certificate Authorities from self-managed **Apache Kafka** to
- summary: This solution enables an accelerated **migration** path by using your current third-party CA infrastructure
- content: Amazon Managed Streaming for **Apache Kafka** (Amazon MSK) is a fully managed streaming data service that handles **Apache Kafka** infrastructure and operations, so developers
- content: and DevOps managers can run **Apache Kafka** applications on AWS.

##### 3. Migrate to Apache Flink 2.2 on Amazon Managed Service for Apache Flink

- match: not expected
- source: AWS / AWS Big Data Blog
- url: https://aws.amazon.com/blogs/big-data/migrate-to-apache-flink-2-2-on-amazon-managed-service-for-apache-flink/
- technologies: AWS CloudFormation, AWS IAM, Amazon CloudWatch, Amazon DynamoDB, Amazon OpenSearch Service, Amazon S3, Apache Flink, Apache Kafka, Java, search
- problem keywords: migration, observability, performance optimization
- case summary: Amazon Managed Service for Apache Flink에서 Flink 1.x에서 2.2로 마이그레이션하며 Java 17 런타임, 향상된 RocksDB 상태 백엔드, SQL 기반 AI/ML 추론 기능을 도입하여 성능과 운영 효율성을 개선한 사례이다.
- problem: 기존 Flink 1.x 환경에서 Java 11 지원 종료, 느린 상태 백엔드 성능, 분산된 API 사용으로 인한 유지보수 어려움과 최신 기능 부재 문제가 있었다.
- solution: Flink 2.2로 업그레이드하여 Java 17과 Python 3.12 지원, RocksDB 8.10.0 적용, 새로운 SQL/테이블 API 기능 활용, 자동 롤백과 스냅샷 기능으로 안정적인 무중단 마이그레이션을 수행하였다.

Highlights:

- summary: this post, we explain what's new in Amazon Managed Service for Apache Flink 2.2, provide a guided **migration**
- content: This has state compatibility implications covered in the **migration** section.
- content: ), "Kinesis Source"); Update connector dependencies: The following AWS connectors have Flink 2.x-compatible releases: Connector Flink 2.x Artifact Version **Apache Kafka**


### ko-architecture-serverless - `서버리스`

- category: architecture
- intent: 한글 아키텍처 키워드로 serverless 관련 사례를 찾는다.
- total results: 53
- precision@5: 0.400
- recall@10: 1.000
- mrr: 0.500
- ndcg@10: 0.598

#### Expected URLs

- relevance 2: [Serverless ICYMI Q1 2026](https://aws.amazon.com/blogs/compute/serverless-icymi-q1-2026/)
- relevance 3: [Modernizing KYC with AWS serverless solutions and agentic AI for financial services](https://aws.amazon.com/blogs/architecture/modernizing-kyc-with-aws-serverless-solutions-and-agentic-ai-for-financial-services/)
- relevance 3: [Optimizing Compute-Intensive Serverless Workloads with Multi-threaded Rust on AWS Lambda](https://aws.amazon.com/blogs/compute/optimizing-compute-intensive-serverless-workloads-with-multi-threaded-rust-on-aws-lambda/)

#### Top Results

| Rank | Match | Title | Source | Score | Keywords |
|---:|---|---|---|---:|---|
| 1 | - | [Serverless ICYMI Q4 2025](https://aws.amazon.com/blogs/compute/serverless-icymi-q4-2025/) | AWS / AWS Compute Blog | 449.89 | AWS IAM, AWS Lambda, Amazon DynamoDB, Amazon EC2, Amazon EventBridge, Amazon S3 |
| 2 | expected:2 | [Serverless ICYMI Q1 2026](https://aws.amazon.com/blogs/compute/serverless-icymi-q1-2026/) | AWS / AWS Compute Blog | 428.52 | AWS CDK, AWS Lambda, Amazon DynamoDB, Amazon EC2, Amazon EventBridge, Java |
| 3 | expected:3 | [Optimizing Compute-Intensive Serverless Workloads with Multi-threaded Rust on AWS Lambda](https://aws.amazon.com/blogs/compute/optimizing-compute-intensive-serverless-workloads-with-multi-threaded-rust-on-aws-lambda/) | AWS / AWS Compute Blog | 347.52 | AWS CloudFormation, AWS IAM, AWS Lambda, Amazon CloudWatch, Node.js, observability |
| 4 | - | [.NET 10 runtime now available in AWS Lambda](https://aws.amazon.com/blogs/compute/net-10-runtime-now-available-in-aws-lambda/) | AWS / AWS Compute Blog | 326.47 | AWS CDK, AWS CloudFormation, AWS Lambda, Amazon EC2, migration, observability |
| 5 | - | [More room to build: serverless services now support payloads up to 1 MB](https://aws.amazon.com/blogs/compute/more-room-to-build-serverless-services-now-support-payloads-up-to-1-mb/) | AWS / AWS Compute Blog | 314.01 | AWS Lambda, Amazon CloudWatch, Amazon EventBridge, Amazon S3, Apache Kafka, Java |
| 6 | - | [Google Cloud Next 2024 참관 후기 2편 - Google Cloud Serverless for Java developer](https://tech.kakaopay.com/post/2024-google-cloud-next-2/) | Kakao Pay / Kakao Pay Tech Blog | 305.68 | Java, serverless |
| 7 | expected:3 | [Modernizing KYC with AWS serverless solutions and agentic AI for financial services](https://aws.amazon.com/blogs/architecture/modernizing-kyc-with-aws-serverless-solutions-and-agentic-ai-for-financial-services/) | AWS / AWS Architecture Blog | 299.57 | AWS Lambda, Amazon CloudWatch, Amazon DynamoDB, Amazon MSK, Amazon OpenSearch Service, Amazon S3 |
| 8 | - | [Building an end-to-end agentic SRE using AWS DevOps Agent](https://aws.amazon.com/blogs/devops/building-an-end-to-end-agentic-sre-using-aws-devops-agent/) | AWS / AWS DevOps Blog | 292.47 | AWS CDK, AWS Lambda, Amazon CloudWatch, Amazon EC2, Amazon EventBridge, Amazon VPC |
| 9 | - | [Building Memory-Intensive Apps with AWS Lambda Managed Instances](https://aws.amazon.com/blogs/compute/building-memory-intensive-apps-with-aws-lambda-managed-instances/) | AWS / AWS Compute Blog | 290.61 | AWS CloudFormation, AWS IAM, AWS Lambda, Amazon CloudWatch, Amazon EC2, Amazon S3 |
| 10 | - | [6,000 AWS accounts, three people, one platform: Lessons learned](https://aws.amazon.com/blogs/architecture/6000-aws-accounts-three-people-one-platform-lessons-learned/) | AWS / AWS Architecture Blog | 290.32 | AWS CloudFormation, AWS IAM, AWS Lambda, Amazon CloudWatch, Amazon DynamoDB, Amazon EC2 |

#### Top Result Details

##### 1. Serverless ICYMI Q4 2025

- match: not expected
- source: AWS / AWS Compute Blog
- url: https://aws.amazon.com/blogs/compute/serverless-icymi-q4-2025/
- technologies: AWS IAM, AWS Lambda, Amazon DynamoDB, Amazon EC2, Amazon EventBridge, Amazon S3, Amazon VPC, Apache Kafka, Java, LLM, Node.js, search
- problem keywords: observability, performance optimization
- case summary: AWS는 2025년 4분기 서버리스 기술 혁신을 통해 복잡한 상태 관리, 고성능 컨테이너 배포, API 응답 최적화, 이벤트 기반 아키텍처 개선 등 다양한 서버리스 애플리케이션 개발 문제를 해결했다.
- problem: 서버리스 애플리케이션에서 다단계 워크플로우 상태 관리, 고성능 및 예측 가능한 컴퓨팅 자원 확보, API 응답 지연 문제, 멀티테넌시 데이터 격리, 이벤트 기반 애플리케이션 개발 복잡성 등이 주요 도전 과제였다.
- solution: AWS Lambda Durable Functions를 통해 상태를 자동 체크포인트하며 장기 실행 워크플로우를 지원하고, Lambda Managed Instances로 EC2 유연성을 서버리스 운영과 결합했다. Amazon ECS Express Mode는 컨테이너 배포를 간소화하고, API Gateway는 스트리밍 응답과 ALB 프라이빗 통합으로 API 성능과 보안을 강화했다. EventBridge의 시각적 룰 빌더는 이벤트 기반 개발 생산성을 높였다.

Highlights:

- title: **Serverless** ICYMI Q4 2025
- caseSummary: AWS는 2025년 4분기 **서버리스** 기술 혁신을 통해 복잡한 상태 관리, 고성능 컨테이너 배포, API 응답 최적화, 이벤트 기반 아키텍처 개선 등 다양한 **서버리스** 애플리케이션 개발
- caseProblem: **서버리스** 애플리케이션에서 다단계 워크플로우 상태 관리, 고성능 및 예측 가능한 컴퓨팅 자원 확보, API 응답 지연 문제, 멀티테넌시 데이터 격리, 이벤트 기반 애플리케이션 개발 복잡성
- caseSolution: Lambda Durable Functions를 통해 상태를 자동 체크포인트하며 장기 실행 워크플로우를 지원하고, Lambda Managed Instances로 EC2 유연성을 **서버리스**
- summary: Stay current with the latest **serverless** innovations that can transform your applications.
- summary: In this 31st quarterly recap, discover the most impactful AWS **serverless** launches, features, and resources

##### 2. Serverless ICYMI Q1 2026

- match: expected relevance 2
- source: AWS / AWS Compute Blog
- url: https://aws.amazon.com/blogs/compute/serverless-icymi-q1-2026/
- technologies: AWS CDK, AWS Lambda, Amazon DynamoDB, Amazon EC2, Amazon EventBridge, Java, search
- problem keywords: high availability, observability, performance optimization
- case summary: AWS는 2026년 1분기 서버리스 혁신을 통해 AWS Lambda 내 내구 함수, .NET 10 런타임 지원, 페이로드 크기 확대, AI 통합 도구, 다중 계정 및 리전 간 DynamoDB 복제 등 다양한 기능을 발표하여 서버리스 애플리케이션의 내결함성, 확장성, 운영 효율성을 크게 향상시켰다.
- problem: 서버리스 애플리케이션에서 복잡한 워크플로우 관리, 대용량 이벤트 데이터 처리, 고가용성 및 장애 복구, AI 통합, 그리고 다중 계정 및 리전 환경에서 데이터 복제와 배포 자동화가 어려웠다.
- solution: AWS Lambda 내구 함수로 다중 단계 워크플로우의 체크포인트 및 오류 복구 자동화, 페이로드 크기 1MB 확대로 풍부한 이벤트 컨텍스트 지원, .NET 10 런타임 도입으로 성능 및 시작 시간 개선, AI 모델과 도구를 통합한 개발 지원, DynamoDB 다중 계정 및 리전 복제로 데이터 복원력 강화, Step Functions TestState API로 CI/CD 내 워크플로우 검증, EventBridge 스케줄러 메트릭 제공으로 리소스 관리 용이성 제고 등 다양한 기능을 도입했다.

Highlights:

- title: **Serverless** ICYMI Q1 2026
- caseSummary: AWS는 2026년 1분기 **서버리스** 혁신을 통해 AWS Lambda 내 내구 함수, .NET 10 런타임 지원, 페이로드 크기 확대, AI 통합 도구, 다중 계정 및 리전 간 DynamoDB
- caseSummary: 복제 등 다양한 기능을 발표하여 **서버리스** 애플리케이션의 내결함성, 확장성, 운영 효율성을 크게 향상시켰다.
- caseProblem: **서버리스** 애플리케이션에서 복잡한 워크플로우 관리, 대용량 이벤트 데이터 처리, 고가용성 및 장애 복구, AI 통합, 그리고 다중 계정 및 리전 환경에서 데이터 복제와 배포 자동화가
- summary: Stay current with the latest **serverless** innovations that can improve your applications.
- summary: In this 32nd quarterly recap, discover the most impactful AWS **serverless** launches, features, and resources

##### 3. Optimizing Compute-Intensive Serverless Workloads with Multi-threaded Rust on AWS Lambda

- match: expected relevance 3
- source: AWS / AWS Compute Blog
- url: https://aws.amazon.com/blogs/compute/optimizing-compute-intensive-serverless-workloads-with-multi-threaded-rust-on-aws-lambda/
- technologies: AWS CloudFormation, AWS IAM, AWS Lambda, Amazon CloudWatch, Node.js
- problem keywords: observability, performance optimization
- case summary: AWS Lambda에서 Rust를 사용해 멀티스레딩을 구현하여 CPU 집약적 서버리스 워크로드의 성능을 4~6배 향상시킨 사례이다.
- problem: AWS Lambda에서 메모리 할당에 따라 최대 6개의 vCPU가 제공되지만, 단일 스레드로 동작하는 코드가 멀티코어를 활용하지 못해 자원을 낭비하고 성능이 제한되는 문제.
- solution: Rust의 Rayon 라이브러리를 활용해 멀티스레딩을 구현하고, Lambda 함수의 콜드 스타트 시점에 스레드 풀을 초기화하여 병렬 처리로 CPU 집약적 작업(예: bcrypt 해싱)을 수행함으로써 멀티코어를 효율적으로 활용했다.

Highlights:

- title: Optimizing Compute-Intensive **Serverless** Workloads with Multi-threaded Rust on AWS Lambda
- caseSummary: AWS Lambda에서 Rust를 사용해 멀티스레딩을 구현하여 CPU 집약적 **서버리스** 워크로드의 성능을 4~6배 향상시킨 사례이다.
- summary: Customers use AWS Lambda to build **Serverless** applications for a wide variety of use cases, from simple
- summary: MB of memory, you can now tackle compute-intensive tasks that were previously challenging in a **Serverless**
- content: Customers use AWS Lambda to build **Serverless** applications for a wide variety of use cases, from simple API backends to complex data processing pipelines.
- content: choice for many workloads, and with support for up to 10,240 MB of memory, you can now tackle compute-intensive tasks that were previously challenging in a **Serverless**


### ko-tech-eks-autoscaling - `EKS 오토스케일링`

- category: technology
- intent: 한글 검색어로 EKS 노드 그룹 오토스케일링, Pod 권한, 카나리 배포처럼 Kubernetes 운영 사례를 찾는다.
- total results: 29
- precision@5: 0.200
- recall@10: 1.000
- mrr: 1.000
- ndcg@10: 1.000

#### Expected URLs

- relevance 3: [Job 워크로드를 위한 EKS Node Group 오토스케일링 도입기](https://medium.com/daangn/job-%EC%9B%8C%ED%81%AC%EB%A1%9C%EB%93%9C%EB%A5%BC-%EC%9C%84%ED%95%9C-eks-node-group-%EC%98%A4%ED%86%A0%EC%8A%A4%EC%BC%80%EC%9D%BC%EB%A7%81-%EB%8F%84%EC%9E%85%EA%B8%B0-a6a28376d153?source=rss----4505f82a2dbd---4)

#### Top Results

| Rank | Match | Title | Source | Score | Keywords |
|---:|---|---|---|---:|---|
| 1 | expected:3 | [Job 워크로드를 위한 EKS Node Group 오토스케일링 도입기](https://medium.com/daangn/job-%EC%9B%8C%ED%81%AC%EB%A1%9C%EB%93%9C%EB%A5%BC-%EC%9C%84%ED%95%9C-eks-node-group-%EC%98%A4%ED%86%A0%EC%8A%A4%EC%BC%80%EC%9D%BC%EB%A7%81-%EB%8F%84%EC%9E%85%EA%B8%B0-a6a28376d153?source=rss----4505f82a2dbd---4) | Daangn / Daangn Tech Blog | 393.57 | Amazon EC2, Amazon EKS, Amazon VPC, Istio, Kubernetes, cost optimization |
| 2 | - | [AI-powered event response for Amazon EKS](https://aws.amazon.com/blogs/architecture/ai-powered-event-response-for-amazon-eks/) | AWS / AWS Architecture Blog | 295.01 | AWS CDK, AWS CloudFormation, AWS IAM, Amazon CloudWatch, Amazon EKS, Java |
| 3 | - | [How Generali Malaysia optimizes operations with Amazon EKS](https://aws.amazon.com/blogs/architecture/how-generali-malaysia-optimizes-operations-with-amazon-eks/) | AWS / AWS Architecture Blog | 281.15 | AWS IAM, Amazon CloudWatch, Amazon EC2, Amazon EKS, Kubernetes, cost optimization |
| 4 | - | [Optimizing storage performance for Amazon EKS on AWS Outposts](https://aws.amazon.com/blogs/compute/optimizing-storage-performance-for-amazon-eks-on-aws-outposts/) | AWS / AWS Compute Blog | 268.70 | AWS IAM, Amazon CloudWatch, Amazon EKS, Amazon S3, Kubernetes, cost optimization |
| 5 | - | [Spark on Kubernetes로 이관하기](https://techblog.woowahan.com/10291/) | Woowa Brothers / Woowa Tech Blog | 268.41 | AWS Glue, AWS IAM, Amazon EKS, Amazon S3, Kubernetes, migration |
| 6 | - | [우아한 Cloud FinOps 여정](https://techblog.woowahan.com/22855/) | Woowa Brothers / Woowa Tech Blog | 239.43 | Amazon CloudWatch, Amazon EC2, Amazon EKS, Amazon ElastiCache, Amazon OpenSearch Service, Amazon RDS |
| 7 | - | [EKS Bottlerocket AMI에서 DCGM 오류로 GPU 노드 반복 교체 문제 해결기](https://tech.inflab.com/20250827-bottlerocket-ami-gpu-issue/) | Inflab / Inflab Tech Blog | 230.45 | Amazon EC2, Amazon EKS, Kubernetes, observability |
| 8 | - | [Deloitte optimizes EKS environment provisioning and achieves 89% faster testing environments using Amazon EKS and vCluster](https://aws.amazon.com/blogs/architecture/deloitte-optimizes-eks-environment-provisioning-and-achieves-89-faster-testing-environments-using-amazon-eks-and-vcluster/) | AWS / AWS Architecture Blog | 230.14 | AWS IAM, Amazon EC2, Amazon EKS, Amazon VPC, Kubernetes, cost optimization |
| 9 | - | [How Kaltura Accelerates CI/CD Using AWS CodeBuild-hosted Runners](https://aws.amazon.com/blogs/devops/how-kaltura-accelerates-ci-cd-using-aws-codebuild-hosted-runners/) | AWS / AWS DevOps Blog | 225.97 | AWS IAM, Amazon CloudWatch, Amazon EKS, Amazon VPC, Kubernetes, migration |
| 10 | - | [배민 앱에도 AI 서비스가? AI 서비스와 MLOps 도입기](https://techblog.woowahan.com/11582/) | Woowa Brothers / Woowa Tech Blog | 217.94 | Amazon EKS, observability |

#### Top Result Details

##### 1. Job 워크로드를 위한 EKS Node Group 오토스케일링 도입기

- match: expected relevance 3
- source: Daangn / Daangn Tech Blog
- url: https://medium.com/daangn/job-%EC%9B%8C%ED%81%AC%EB%A1%9C%EB%93%9C%EB%A5%BC-%EC%9C%84%ED%95%9C-eks-node-group-%EC%98%A4%ED%86%A0%EC%8A%A4%EC%BC%80%EC%9D%BC%EB%A7%81-%EB%8F%84%EC%9E%85%EA%B8%B0-a6a28376d153?source=rss----4505f82a2dbd---4
- technologies: Amazon EC2, Amazon EKS, Amazon VPC, Istio, Kubernetes
- problem keywords: cost optimization, incident response, observability, performance optimization
- case summary: 당근은 중단이 어려운 Job 워크로드를 위한 AWS EKS Node Group에 오토스케일링을 도입하며, Bin-packing 스케줄링과 강제 종료 방지 Annotation 적용으로 비용 효율성과 안정성을 개선했다. 운영 중 발생한 kubelet 과부하, 이미지 풀 실패, EBS 볼륨 쓰로틀링, CNI IP 할당 지연 문제를 각각 설정 조정과 인프라 증설로 해결했다.
- problem: 중단이 어려운 장시간 실행 Job 워크로드가 EKS Node Group에서 고르게 분산되어 Node Scale-in이 어렵고, 고정된 Node 수 운영으로 비용 비효율과 처리 지연 문제가 발생했다. 또한 Bin-packing 적용 후 특정 Node에 Pod가 집중되면서 kubelet 과부하, 이미지 풀 병목, EBS 쓰로틀링, IP 할당 지연 등의 부하 문제가 발생했다.
- solution: Job 워크로드 전용 Node Group 분리 및 PodAffinity를 활용한 Bin-packing 스케줄링으로 Pod를 소수 Node에 집중 배치해 Scale-in 효율을 높이고, Cluster Autoscaler와 Karpenter Annotation으로 실행 중인 Job Pod의 강제 종료를 방지했다. kubelet maxPods 제한, registryPullQPS/registryBurst 상향, EBS IOPS/Throughput 증설, Host Network Mode 적용 등으로 부하 문제를 해결했다.

Highlights:

- title: Job 워크로드를 위한 **EKS** Node Group **오토스케일링** 도입기
- summary: **오토스케일링** 적용 후 지표 변화 위 그래프는 **오토스케일링** 적용 전후의 Job 워크로드용 Node Group의 시간별 Node 수를 나타내고 있어요.
- summary: 그래프를 통해 **오토스케일링** 적용 후 Node 수가 유동적으로 증감하는 것을 확인할 수 있어요.
- content: **오토스케일링** 도입 이후 적절한 Node 수가 자연스럽게 조정되었고, 이로 인해 Pod Pending 시간 감소와 Running 시간 단축 등 전반적인 성능 개선을 확인할 수 있었어요. 마무리 당근에서는 다양한 종류의 Job 워크로드가 AWS **EKS** 클러스터에서 실행되고 있어요.
- content: Job 워크로드를 위한 **EKS** Node Group **오토스케일링** 도입기 was originally published in 당근 테크 블로그 on Medium, where people are continuing the conversation by highlighting and responding

##### 2. AI-powered event response for Amazon EKS

- match: not expected
- source: AWS / AWS Architecture Blog
- url: https://aws.amazon.com/blogs/architecture/ai-powered-event-response-for-amazon-eks/
- technologies: AWS CDK, AWS CloudFormation, AWS IAM, Amazon CloudWatch, Amazon EKS, Java, Kubernetes, OpenTelemetry
- problem keywords: incident response, migration, observability, performance optimization
- case summary: AWS DevOps Agent를 활용해 Amazon EKS 클러스터 내 마이크로서비스의 이벤트를 AI 기반으로 자동 탐지 및 대응하는 사례로, 복잡한 Kubernetes 리소스 간 관계를 이해하고 신속한 근본 원인 분석을 지원한다.
- problem: 대규모 마이크로서비스 환경에서 수천 건의 이벤트 신호를 효과적으로 모니터링하고, 신속하고 정확한 근본 원인 분석 및 자동화된 사건 대응이 어려운 상황.
- solution: Amazon EKS와 통합된 AWS DevOps Agent를 배포하여 OpenTelemetry, CloudWatch, X-Ray 등 다양한 관찰 가능성 데이터를 AI와 머신러닝으로 분석하고, Kubernetes 리소스 간 의존성을 파악해 자동으로 이상 징후를 탐지하고 대응하는 시스템 구축.

Highlights:

- title: AI-powered event response for **Amazon EKS**
- caseSummary: AWS DevOps Agent를 활용해 **Amazon EKS** 클러스터 내 마이크로서비스의 이벤트를 AI 기반으로 자동 탐지 및 대응하는 사례로, 복잡한 Kubernetes 리소스 간
- content: Figure 1: This is an example of target architecture of how **Amazon EKS** workloads are deployed and how AWS DevOps agent can interact with the different managed services
- content: Amazon Elastic Kubernetes Service (**Amazon EKS**) cluster version 1.27 or later OpenTelemetry Operator installed for telemetry collection Amazon Managed Service for

##### 3. How Generali Malaysia optimizes operations with Amazon EKS

- match: not expected
- source: AWS / AWS Architecture Blog
- url: https://aws.amazon.com/blogs/architecture/how-generali-malaysia-optimizes-operations-with-amazon-eks/
- technologies: AWS IAM, Amazon CloudWatch, Amazon EC2, Amazon EKS, Kubernetes
- problem keywords: cost optimization, high availability, migration, observability, performance optimization
- case summary: Generali Malaysia는 Amazon EKS Auto Mode와 AWS 서비스 통합을 활용해 보험업계의 클라우드 전환과 디지털 서비스 수요 증가에 대응하며 운영 효율성, 보안, 비용 최적화를 달성했다.
- problem: 레거시 애플리케이션의 클라우드 마이그레이션과 다수 컨테이너화된 마이크로서비스의 확장에 따른 운영 복잡성, 비용 과다 지출, 보안 및 컴플라이언스 관리 어려움이 있었다.
- solution: Amazon EKS Auto Mode를 도입해 클러스터 인프라 자동 관리 및 확장, AWS IAM과 네트워크 정책을 통한 보안 강화, Amazon GuardDuty, Inspector, Network Firewall, Secrets Manager 등 AWS 보안 서비스와 통합하여 위협 탐지 및 비밀 관리 자동화, 비용 최적화를 위한 태그 기반 비용 할당과 Savings Plans 활용, Amazon Managed Grafana를 통한 세분화된 모니터링 대시보드 구축으로 운영 효율성과 신뢰성을 확보했다.

Highlights:

- title: How Generali Malaysia optimizes operations with **Amazon EKS**
- caseSummary: Generali Malaysia는 **Amazon EKS** Auto Mode와 AWS 서비스 통합을 활용해 보험업계의 클라우드 전환과 디지털 서비스 수요 증가에 대응하며 운영 효율성, 보안
- caseSolution: **Amazon EKS** Auto Mode를 도입해 클러스터 인프라 자동 관리 및 확장, AWS IAM과 네트워크 정책을 통한 보안 강화, Amazon GuardDuty, Inspector
- summary: In this post, we look at how Generali is using **Amazon EKS** Auto Mode and its integration with other AWS
- content: Previous experience of the Generali DevOps and Cloud team was also a strong factor in selecting **Amazon EKS**.
- content: If you’re interested in learning more about **Amazon EKS**, refer to **Amazon EKS** Best Practices Guide .


### ko-problem-observability - `옵저버빌리티`

- category: problem
- intent: 한글 검색어로 관측성, 모니터링, 로그 플랫폼 구축 사례를 찾는다.
- total results: 287
- precision@5: 0.200
- recall@10: 0.333
- mrr: 1.000
- ndcg@10: 0.674

#### Expected URLs

- relevance 3: [옵저버빌리티 Right-Sizing: 여기어때에서 기준을 만드는 법](https://techblog.gccompany.co.kr/%EC%98%B5%EC%A0%80%EB%B2%84%EB%B9%8C%EB%A6%AC%ED%8B%B0-right-sizing-%EC%97%AC%EA%B8%B0%EC%96%B4%EB%95%8C%EC%97%90%EC%84%9C-%EA%B8%B0%EC%A4%80%EC%9D%84-%EB%A7%8C%EB%93%9C%EB%8A%94-%EB%B2%95-8c9e1b3d3c97?source=rss----18356045d353---4)
- relevance 2: [일 41TB, 200억 건의 로그를 ClickStack으로 실시간 처리하기 - 호그와트 도서관 프로젝트](https://tech.kakaopay.com/post/pallas-v2-log-platform/)
- relevance 2: [비용, 성능, 안정성을 목표로 한 지능형 로그 파이프라인 도입](https://d2.naver.com/helloworld/0004394)

#### Top Results

| Rank | Match | Title | Source | Score | Keywords |
|---:|---|---|---|---:|---|
| 1 | expected:3 | [옵저버빌리티 Right-Sizing: 여기어때에서 기준을 만드는 법](https://techblog.gccompany.co.kr/%EC%98%B5%EC%A0%80%EB%B2%84%EB%B9%8C%EB%A6%AC%ED%8B%B0-right-sizing-%EC%97%AC%EA%B8%B0%EC%96%B4%EB%95%8C%EC%97%90%EC%84%9C-%EA%B8%B0%EC%A4%80%EC%9D%84-%EB%A7%8C%EB%93%9C%EB%8A%94-%EB%B2%95-8c9e1b3d3c97?source=rss----18356045d353---4) | GC Company / GC Company Tech Blog | 312.49 | JVM, Kubernetes, OpenTelemetry, cost optimization, observability, performance optimization |
| 2 | - | [옵저버빌리티: 로그라고해서 다 같은 로그가 아니다(1/2)](https://netmarble.engineering/observability-logging-a/) | Netmarble / Netmarble Tech Blog | 302.30 | Kubernetes, observability |
| 3 | - | [옵저버빌리티: 로그라고해서 다 같은 로그가 아니다(2/2)](https://netmarble.engineering/observability-logging-b/) | Netmarble / Netmarble Tech Blog | 294.85 | observability |
| 4 | - | [Enhancing network observability with new AWS Outposts racks LAG metrics](https://aws.amazon.com/blogs/compute/enhancing-network-observability-with-new-aws-outposts-racks-lag-metrics/) | AWS / AWS Compute Blog | 237.82 | AWS CloudFormation, AWS IAM, Amazon CloudWatch, high availability, observability |
| 5 | - | [AWS re:Invent 2023, 관심 세션을 중심으로 (2편): Cost Optimization, Observability](https://tech.kakaopay.com/post/2023-aws-reinvent-2/) | Kakao Pay / Kakao Pay Tech Blog | 237.82 | cost optimization, observability |
| 6 | - | [Unified observability in Amazon OpenSearch Service: metrics, traces, and AI agent debugging in a single interface](https://aws.amazon.com/blogs/big-data/unified-observability-in-amazon-opensearch-service-metrics-traces-and-ai-agent-debugging-in-a-single-interface/) | AWS / AWS Big Data Blog | 192.42 | AWS IAM, Amazon OpenSearch Service, LLM, OpenTelemetry, search, observability |
| 7 | - | [LLMOps로 확장하는 AI플랫폼 2.0](https://techblog.woowahan.com/22839/) | Woowa Brothers / Woowa Tech Blog | 186.20 | LLM, Redis, observability, performance optimization, streaming data pipeline |
| 8 | - | [Scaling to Infinity: 한계를 넘어서는 LY Corporation의 관측 가능성 플랫폼 진화기](https://techblog.lycorp.co.jp/ko/the-evolution-of-the-ly-observability-platform) | LY Corporation / LY Corporation Tech Blog | 180.83 | observability |
| 9 | - | [AI-powered event response for Amazon EKS](https://aws.amazon.com/blogs/architecture/ai-powered-event-response-for-amazon-eks/) | AWS / AWS Architecture Blog | 176.07 | AWS CDK, AWS CloudFormation, AWS IAM, Amazon CloudWatch, Amazon EKS, Java |
| 10 | - | [6,000 AWS accounts, three people, one platform: Lessons learned](https://aws.amazon.com/blogs/architecture/6000-aws-accounts-three-people-one-platform-lessons-learned/) | AWS / AWS Architecture Blog | 160.26 | AWS CloudFormation, AWS IAM, AWS Lambda, Amazon CloudWatch, Amazon DynamoDB, Amazon EC2 |

#### Top Result Details

##### 1. 옵저버빌리티 Right-Sizing: 여기어때에서 기준을 만드는 법

- match: expected relevance 3
- source: GC Company / GC Company Tech Blog
- url: https://techblog.gccompany.co.kr/%EC%98%B5%EC%A0%80%EB%B2%84%EB%B9%8C%EB%A6%AC%ED%8B%B0-right-sizing-%EC%97%AC%EA%B8%B0%EC%96%B4%EB%95%8C%EC%97%90%EC%84%9C-%EA%B8%B0%EC%A4%80%EC%9D%84-%EB%A7%8C%EB%93%9C%EB%8A%94-%EB%B2%95-8c9e1b3d3c97?source=rss----18356045d353---4
- technologies: JVM, Kubernetes, OpenTelemetry
- problem keywords: cost optimization, observability, performance optimization
- case summary: 여기어때컴퍼니는 Kubernetes 환경에서 옵저버빌리티 인프라의 Pod 리소스 요청(requests)과 제한(limits)을 실제 사용 패턴에 맞게 조정하는 Right-Sizing 기준을 수립하여 리소스 낭비를 줄이고 안정성을 확보했다.
- problem: Kubernetes 클러스터에서 Pod의 resources.requests 설정이 과다하거나 부족할 경우 클러스터 자원 낭비, OOMKill, CPU Throttling 등의 문제가 발생하며, 기존 성능 테스트 기반 산정 기준이 서비스 성장과 트래픽 변화에 맞지 않아 명확한 조정 정책과 기준이 필요했다.
- solution: OpenTelemetry와 Grafana LGTM 스택으로 수집된 메트릭 데이터를 활용해 P95 기준과 컴포넌트별 특성을 반영한 목표 사용률을 설정하고, 메모리와 CPU의 특성에 맞는 버퍼 전략을 적용하여 컴포넌트 유형별로 차등화된 Right-Sizing 기준을 수립하고 단계별 적용 및 검증을 통해 안정적으로 리소스를 최적화했다.

Highlights:

- title: **옵저버빌리티** Right-Sizing: 여기어때에서 기준을 만드는 법
- caseSummary: 여기어때컴퍼니는 Kubernetes 환경에서 **옵저버빌리티** 인프라의 Pod 리소스 요청(requests)과 제한(limits)을 실제 사용 패턴에 맞게 조정하는 Right-Sizing
- summary: **옵저버빌리티** 인프라의 노드 사용률을 점검하던 중 이런 의문이 들었습니다. “노드는 꽉 찬 것처럼 보이는데, 실제로 Pod들이 그만큼 쓰고 있는 건가?”
- summary: 여기어때에서 운영하고 있는 **옵저버빌리티** 스택은 역할에 따라 여러 컴포넌트로 구성됩니다.
- content: **옵저버빌리티** 인프라의 노드 사용률을 점검하던 중 이런 의문이 들었습니다. “노드는 꽉 찬 것처럼 보이는데, 실제로 Pod들이 그만큼 쓰고 있는 건가?” Kubernetes에서 resources.requests는 단순한 설정값이 아닙니다.
- content: 여기어때에서 운영하고 있는 **옵저버빌리티** 스택은 역할에 따라 여러 컴포넌트로 구성됩니다. 로그나 메트릭 데이터를 수신하고 저장하는 컴포넌트(Ingester)는 데이터를 일정량 메모리에 쌓았다가 주기적으로 디스크에 내려쓰는 방식으로 동작합니다.

##### 2. 옵저버빌리티: 로그라고해서 다 같은 로그가 아니다(1/2)

- match: not expected
- source: Netmarble / Netmarble Tech Blog
- url: https://netmarble.engineering/observability-logging-a/
- technologies: Kubernetes
- problem keywords: observability
- case summary: 넷마블은 수천 개의 VM과 수백 개의 Kubernetes 클러스터에서 200여 개의 서비스를 운영하며 복잡한 서비스 환경에서 효율적인 로그 관리와 옵저버빌리티를 구현하는 문제를 다룹니다.
- problem: 대규모 분산 환경에서 다양한 서비스와 인프라가 복잡하게 얽혀 있어 단순한 로그 수집만으로는 운영 및 문제 해결에 한계가 존재함.
- solution: 서비스별, 목적별로 로그를 구분하고, 로그의 특성과 역할에 맞는 체계적인 옵저버빌리티 전략을 수립하여 효율적인 모니터링과 문제 진단을 가능하게 함.

Highlights:

- title: **옵저버빌리티**: 로그라고해서 다 같은 로그가 아니다(1/2)
- caseSolution: 서비스별, 목적별로 로그를 구분하고, 로그의 특성과 역할에 맞는 체계적인 **옵저버빌리티** 전략을 수립하여 효율적인 모니터링과 문제 진단을 가능하게 함.
- summary: The post **옵저버빌리티**: 로그라고해서 다 같은 로그가 아니다(1/2) appeared first on 넷마블 기술 블로그 .

##### 3. 옵저버빌리티: 로그라고해서 다 같은 로그가 아니다(2/2)

- match: not expected
- source: Netmarble / Netmarble Tech Blog
- url: https://netmarble.engineering/observability-logging-b/
- technologies: -
- problem keywords: observability
- case summary: 넷마블은 레거시 서비스에 로깅 기술을 도입하면서 로그 품질 관리 미흡으로 인한 문제를 경험했고, 이를 개선하기 위한 로깅 품질 관리 방안을 모색했다.
- problem: 레거시 서비스에 옵저버빌리티를 위한 로깅 기술을 적용할 때 로그 품질 관리가 제대로 이루어지지 않아 예상치 못한 문제가 발생했다.
- solution: 로그 품질 관리 체계를 강화하고, 서비스 초기부터 일관된 로깅 정책을 적용하여 로그의 신뢰성과 활용도를 높이는 방식을 도입했다.

Highlights:

- title: **옵저버빌리티**: 로그라고해서 다 같은 로그가 아니다(2/2)
- summary: The post **옵저버빌리티**: 로그라고해서 다 같은 로그가 아니다(2/2) appeared first on 넷마블 기술 블로그 .


### ko-deployment-canary - `카나리 배포`

- category: architecture
- intent: 한글 검색어로 카나리 배포, Blue-Green 배포, Argo Rollouts, Spinnaker 적용 사례를 찾는다.
- total results: 292
- precision@5: 0.400
- recall@10: 1.000
- mrr: 1.000
- ndcg@10: 1.000

#### Expected URLs

- relevance 3: [EKS + ALB 환경에서 Argo Rollouts 503 에러 없는 카나리 배포 적용기](https://techblog.gccompany.co.kr/eks-alb-%ED%99%98%EA%B2%BD%EC%97%90%EC%84%9C-argo-rollouts-503-%EC%97%90%EB%9F%AC-%EC%97%86%EB%8A%94-%EC%B9%B4%EB%82%98%EB%A6%AC-%EB%B0%B0%ED%8F%AC-%EC%A0%81%EC%9A%A9%EA%B8%B0-689eedaf8d1a?source=rss----18356045d353---4)
- relevance 3: [Istio와 Spinnaker를 활용한 Blue-Green + Canary 자동 배포 전략 도입기](https://tech.devsisters.com/posts/blue-green-canary-deployment)

#### Top Results

| Rank | Match | Title | Source | Score | Keywords |
|---:|---|---|---|---:|---|
| 1 | expected:3 | [EKS + ALB 환경에서 Argo Rollouts 503 에러 없는 카나리 배포 적용기](https://techblog.gccompany.co.kr/eks-alb-%ED%99%98%EA%B2%BD%EC%97%90%EC%84%9C-argo-rollouts-503-%EC%97%90%EB%9F%AC-%EC%97%86%EB%8A%94-%EC%B9%B4%EB%82%98%EB%A6%AC-%EB%B0%B0%ED%8F%AC-%EC%A0%81%EC%9A%A9%EA%B8%B0-689eedaf8d1a?source=rss----18356045d353---4) | GC Company / GC Company Tech Blog | 558.55 | Amazon EKS, Amazon S3, Argo Rollouts, Kubernetes, incident response, observability |
| 2 | expected:3 | [Istio와 Spinnaker를 활용한 Blue-Green + Canary 자동 배포 전략 도입기](https://tech.devsisters.com/posts/blue-green-canary-deployment) | Devsisters / Devsisters Tech Blog | 184.08 | Argo Rollouts, Istio, JVM, Kubernetes, Redis, Spinnaker |
| 3 | - | [Kubernetes 클러스터에 애플리케이션 배포하기](https://medium.com/naver-cloud-platform/kubernetes-%ED%81%B4%EB%9F%AC%EC%8A%A4%ED%84%B0%EC%97%90-%EC%95%A0%ED%94%8C%EB%A6%AC%EC%BC%80%EC%9D%B4%EC%85%98-%EB%B0%B0%ED%8F%AC%ED%95%98%EA%B8%B0-494f653341ab?source=rss----c7f2bfeb6b98---4) | NAVER Cloud / NAVER Cloud Platform Tech Blog | 176.98 | Kubernetes, observability, canary deployment |
| 4 | - | [실험과 기능플래그를 위한 실험플랫폼 구축하기](https://techblog.woowahan.com/9935/) | Woowa Brothers / Woowa Tech Blog | 172.11 | AWS Glue, Amazon RDS, JVM, Java, Kotlin, Redis |
| 5 | - | [배달의민족 광고데이터 이관기](https://techblog.woowahan.com/14041/) | Woowa Brothers / Woowa Tech Blog | 164.47 | Amazon OpenSearch Service, Elasticsearch, JVM, search, cost optimization, migration |
| 6 | - | [쿠팡의 머신러닝 플랫폼을 통한 ML 개발 가속화](https://medium.com/coupang-engineering/%EC%BF%A0%ED%8C%A1%EC%9D%98-%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D-%ED%94%8C%EB%9E%AB%ED%8F%BC%EC%9D%84-%ED%86%B5%ED%95%9C-ml-%EA%B0%9C%EB%B0%9C-%EA%B0%80%EC%86%8D%ED%99%94-de29804148bb?source=rss----fb028911af07---4) | Coupang / Coupang Engineering Blog | 161.80 | Kubernetes, LLM, search, observability, canary deployment, streaming data pipeline |
| 7 | - | [별로 안 궁금했지만 막상 들어보니 은근 궁금했던 개발 이야기](https://techblog.woowahan.com/6042/) | Woowa Brothers / Woowa Tech Blog | 157.44 | observability, canary deployment |
| 8 | - | [웹 애플리케이션 페이지를 패키지로 개발해 본 경험](https://techblog.woowahan.com/16910/) | Woowa Brothers / Woowa Tech Blog | 146.62 | Node.js, React, canary deployment |
| 9 | - | [Choosing between Amazon ECS Blue/Green Native or AWS CodeDeploy in AWS CDK](https://aws.amazon.com/blogs/devops/choosing-between-amazon-ecs-blue-green-native-or-aws-codedeploy-in-aws-cdk/) | AWS / AWS DevOps Blog | 144.51 | AWS CDK, AWS CloudFormation, AWS Lambda, Amazon EC2, migration, canary deployment |
| 10 | - | [이젠 보내줄 때가 되었다. 대규모 트래픽의 C++ 시스템 Java로 전환하기](https://techblog.woowahan.com/20763/) | Woowa Brothers / Woowa Tech Blog | 124.01 | Java, Redis, Spring Boot, search, migration, observability |

#### Top Result Details

##### 1. EKS + ALB 환경에서 Argo Rollouts 503 에러 없는 카나리 배포 적용기

- match: expected relevance 3
- source: GC Company / GC Company Tech Blog
- url: https://techblog.gccompany.co.kr/eks-alb-%ED%99%98%EA%B2%BD%EC%97%90%EC%84%9C-argo-rollouts-503-%EC%97%90%EB%9F%AC-%EC%97%86%EB%8A%94-%EC%B9%B4%EB%82%98%EB%A6%AC-%EB%B0%B0%ED%8F%AC-%EC%A0%81%EC%9A%A9%EA%B8%B0-689eedaf8d1a?source=rss----18356045d353---4
- technologies: Amazon EKS, Amazon S3, Argo Rollouts, Kubernetes
- problem keywords: incident response, observability
- case summary: GC Company는 EKS와 ALB 환경에서 Argo Rollouts를 이용한 카나리 배포 시 발생하는 503 에러 문제를 Canary PingPong 전략으로 해결하고, 실제 운영 환경에서 무중단 배포를 검증했다.
- problem: EKS + ALB 환경에서 Argo Rollouts의 Blue/Green 및 기본 Canary 배포 시 Promote 단계에서 Service selector 변경으로 인해 ALB Target Group 재등록이 발생하고, 헬스체크 통과 전까지 약 30초간 503 에러가 발생하는 구조적 한계가 있었다.
- solution: Argo Rollouts v1.2의 Canary PingPong 전략을 적용하여 두 개의 Target Group을 고정하고, Promote 시 Service selector 변경 없이 ALB ForwardConfig의 weight만 교체하는 방식으로 503 에러를 근본적으로 제거하였다. 또한, PingPong 적용을 위한 3개 Service 구성과 Ingress 설정(use-annotation) 등 구체적인 설정 가이드를 제공하고, 다양한 시나리오 테스트를 통해 무중단 배포를 검증했다.

Highlights:

- title: EKS + ALB 환경에서 Argo Rollouts 503 에러 없는 **카나리 배포** 적용기
- caseSummary: GC Company는 EKS와 ALB 환경에서 Argo Rollouts를 이용한 **카나리 배포** 시 발생하는 503 에러 문제를 **Canary** PingPong 전략으로 해결하고, 실제 운영
- caseProblem: EKS + ALB 환경에서 Argo Rollouts의 Blue/Green 및 기본 **Canary** **배포** 시 Promote 단계에서 Service selector 변경으로 인해 ALB Target
- caseSolution: Argo Rollouts v1.2의 **Canary** PingPong 전략을 적용하여 두 개의 Target Group을 고정하고, Promote 시 Service selector 변경 없이
- summary: 이후 **카나리** 배포가 필요한 요건이 생겼습니다.
- summary: Phase 2 — **배포** : **canary** Pod 생성 후 weight를 10% → 30% → … 단계적으로 증가시킵니다.

##### 2. Istio와 Spinnaker를 활용한 Blue-Green + Canary 자동 배포 전략 도입기

- match: expected relevance 3
- source: Devsisters / Devsisters Tech Blog
- url: https://tech.devsisters.com/posts/blue-green-canary-deployment
- technologies: Argo Rollouts, Istio, JVM, Kubernetes, Redis, Spinnaker
- problem keywords: observability, performance optimization
- case summary: 데브시스터즈는 Kubernetes 환경에서 Istio와 Spinnaker를 활용해 Blue-Green과 Canary 배포 전략을 결합한 자동 무중단 배포 파이프라인을 도입하여 배포 안정성과 효율성을 크게 개선했다.
- problem: 기존 Rolling Update 방식은 배포 시 롤백 어려움, 신 서버 모니터링 및 워밍업 부족, 배포 시간 지연 등의 문제로 여러 게임 서버를 빈번히 업데이트하는 데 부담과 위험이 컸다.
- solution: Istio를 이용한 트래픽 가중치 제어로 Blue-Green 방식처럼 신 서버를 미리 프로비저닝하고, Canary 방식으로 일부 트래픽을 신 서버에 보내 모니터링 후 점진적으로 전환하는 자동화된 배포 파이프라인을 Spinnaker와 Helm으로 구축했다.

Highlights:

- title: Istio와 Spinnaker를 활용한 Blue-Green + **Canary** 자동 **배포** 전략 도입기
- caseSummary: 데브시스터즈는 Kubernetes 환경에서 Istio와 Spinnaker를 활용해 Blue-Green과 **Canary** **배포** 전략을 결합한 자동 무중단 **배포** 파이프라인을 도입하여 **배포**
- caseProblem: 기존 Rolling Update 방식은 **배포** 시 롤백 어려움, 신 서버 모니터링 및 워밍업 부족, **배포** 시간 지연 등의 문제로 여러 게임 서버를 빈번히 업데이트하는 데 부담과 위험이
- caseSolution: Istio를 이용한 트래픽 가중치 제어로 Blue-Green 방식처럼 신 서버를 미리 프로비저닝하고, **Canary** 방식으로 일부 트래픽을 신 서버에 보내 모니터링 후 점진적으로 전환하는
- caseSolution: 자동화된 **배포** 파이프라인을 Spinnaker와 Helm으로 구축했다.
- summary: 기존 **배포** 전략보다 더 효율적이고 안전한 자동 **배포** 전략을 실제 게임 서비스에 도입한 사례를 소개합니다.

##### 3. Kubernetes 클러스터에 애플리케이션 배포하기

- match: not expected
- source: NAVER Cloud / NAVER Cloud Platform Tech Blog
- url: https://medium.com/naver-cloud-platform/kubernetes-%ED%81%B4%EB%9F%AC%EC%8A%A4%ED%84%B0%EC%97%90-%EC%95%A0%ED%94%8C%EB%A6%AC%EC%BC%80%EC%9D%B4%EC%85%98-%EB%B0%B0%ED%8F%AC%ED%95%98%EA%B8%B0-494f653341ab?source=rss----c7f2bfeb6b98---4
- technologies: Kubernetes
- problem keywords: observability
- case summary: 네이버 클라우드 플랫폼의 Developer Tools를 활용해 Kubernetes 클러스터에 애플리케이션을 빌드, 배포, 자동화하는 DevOps 실습 사례를 다룹니다.
- problem: DevOps 환경 구축 시 소스 코드 관리, 빌드, 컨테이너 이미지 생성, Kubernetes 클러스터 배포 및 자동화 과정의 복잡성으로 인해 효율적인 개발 및 운영이 어려움.
- solution: SourceCommit, SourceBuild, SourceDeploy, SourcePipeline 4가지 Developer Tools를 연계하여 소스 코드 복사 및 관리, 도커 이미지 빌드, Kubernetes 클러스터에 롤링 업데이트 배포, CI/CD 자동화 파이프라인 구축을 통해 DevOps 전 과정을 자동화하고 안정적으로 운영함.

Highlights:

- caseSummary: 네이버 클라우드 플랫폼의 Developer Tools를 활용해 Kubernetes 클러스터에 애플리케이션을 빌드, **배포**, 자동화하는 DevOps 실습 사례를 다룹니다.
- caseProblem: DevOps 환경 구축 시 소스 코드 관리, 빌드, 컨테이너 이미지 생성, Kubernetes 클러스터 **배포** 및 자동화 과정의 복잡성으로 인해 효율적인 개발 및 운영이 어려움.
- caseSolution: SourceDeploy, SourcePipeline 4가지 Developer Tools를 연계하여 소스 코드 복사 및 관리, 도커 이미지 빌드, Kubernetes 클러스터에 롤링 업데이트 **배포**
- summary: **배포** 프로젝트 생성 [이미지 14] **배포** 프로젝트 기본 설정하기 (이름 설정) SourceDeploy 콘솔에서 [**배포** 프로젝트 생성] 버튼을 클릭하여 신규 **배포** 프로젝트를 생성합니다
- summary: [이미지 15] **배포** 환경 설정하기 (real stage 설정 화면) [이미지 16] **배포** 프로젝트 생성 전 최종 정보 확인하기 **배포** 시나리오 생성 **배포** 프로젝트를 생성한 이후 **배포**
- content: [이미지 18] **배포** 시나리오 생성 > 매니페스트 설정하기 **배포** 전략은 Rolling (롤링), 블루/그린, **Canary** (**카나리**) 를 제공합니다. 롤링 업데이트를 선택하여 애플리케이션이 점진적으로 업데이트 되도록 설정합니다. 최종 확인 이후 **배포** 시나리오의 생성을 완료합니다.


### ko-tech-search - `검색 개선`

- category: technology
- intent: 한글 검색어로 검색 기능 개선, 검색 시스템 설계, 검색 엔진 분석 사례를 찾는다.
- total results: 476
- precision@5: 0.000
- recall@10: 0.333
- mrr: 0.143
- ndcg@10: 0.174

#### Expected URLs

- relevance 3: [Vertex AI Search를 활용한 결과 없는 검색 개선하기](https://helloworld.kurly.com/blog/vertex-ai-search-nr/)
- relevance 3: [검색 성능 개선을 위한 Elasticsearch 인덱스 구조와 쿼리 최적화](https://techblog.woowahan.com/20161/)
- relevance 2: [네이버 통합검색 AIB 도입과 웹 성능 변화 분석](https://d2.naver.com/helloworld/4241703)
- relevance 3: [컬리 검색이 카프카를 들여다본 이야기 2](https://helloworld.kurly.com/blog/search-system-with-kafka-2/)
- relevance 2: [OpenSearch Analyzer를 활용한 검색기능 알아보기](https://tech.kakaopay.com/post/kakaopayins-opensearch-analyzer/)
- relevance 2: [30분만 투자하면 사용하는 API 문서 검색 엔진, Doxygen 외부 검색 설정하기](https://netmarble.engineering/doxygen-nginx-fcgiwrap/)

#### Top Results

| Rank | Match | Title | Source | Score | Keywords |
|---:|---|---|---|---:|---|
| 1 | - | [MongoDB Atlas Search 정렬이슈 해결기](https://tech.inflab.com/202211-mongodb-atlas-search/) | Inflab / Inflab Tech Blog | 318.13 | Amazon OpenSearch Service, Elasticsearch, Java, search, observability |
| 2 | - | [Full-text, exact-match, range, and hybrid search on Amazon ElastiCache](https://aws.amazon.com/blogs/database/enhanced-search-for-amazon-elasticache/) | AWS / AWS Database Blog | 240.09 | AWS IAM, Amazon EC2, Amazon ElastiCache, Amazon VPC, Redis, Valkey |
| 3 | - | [Real-time Service Configuration으로 Consul을 신주소 서비스에 적용한 사례](https://techblog.woowahan.com/2586/) | Woowa Brothers / Woowa Tech Blog | 232.80 | AWS IAM, Amazon VPC, Java, search, high availability |
| 4 | - | [Announcing aggregations on Amazon ElastiCache](https://aws.amazon.com/blogs/database/announcing-aggregations-on-amazon-elasticache/) | AWS / AWS Database Blog | 215.16 | AWS IAM, Amazon EC2, Amazon ElastiCache, Amazon VPC, Redis, Valkey |
| 5 | - | [SEO 주도 개발 실천기: 구글이 인정한 ‘좋은 URL’ 99% 달성 여정](https://medium.com/wantedjobs/seo-%EC%A3%BC%EB%8F%84-%EA%B0%9C%EB%B0%9C-%EC%8B%A4%EC%B2%9C%EA%B8%B0-%EA%B5%AC%EA%B8%80%EC%9D%B4-%EC%9D%B8%EC%A0%95%ED%95%9C-%EC%A2%8B%EC%9D%80-url-99-%EB%8B%AC%EC%84%B1-%EC%97%AC%EC%A0%95-7e494b56d39b?source=rss----fb47eceee74c---4) | Wantedlab / Wantedlab Tech Blog | 209.71 | search, performance optimization |
| 6 | - | [[AI 트렌드] 매출 성장의 비결로 떠오른 검색· 추천 기술, Seargest](https://www.upstage.ai/blog/ko/2023-ai-tech-trend-seargest) | Upstage / Upstage Blog | 180.55 | search |
| 7 | expected:2 | [네이버 통합검색 AIB 도입과 웹 성능 변화 분석](https://d2.naver.com/helloworld/4241703) | NAVER / NAVER D2 | 173.24 | search, performance optimization, streaming data pipeline |
| 8 | expected:3 | [검색 성능 개선을 위한 Elasticsearch 인덱스 구조와 쿼리 최적화](https://techblog.woowahan.com/20161/) | Woowa Brothers / Woowa Tech Blog | 169.57 | Elasticsearch, Spring Boot, search, migration, observability, performance optimization |
| 9 | - | [배민상회와 검색플랫폼 연동기](https://techblog.woowahan.com/11732/) | Woowa Brothers / Woowa Tech Blog | 167.76 | Amazon OpenSearch Service, Elasticsearch, search, observability, event-driven architecture |
| 10 | - | [실시간 인덱싱을 위한 Elasticsearch 구조를 찾아서](https://techblog.woowahan.com/7425/) | Woowa Brothers / Woowa Tech Blog | 166.30 | Elasticsearch, search, performance optimization |

#### Top Result Details

##### 1. MongoDB Atlas Search 정렬이슈 해결기

- match: not expected
- source: Inflab / Inflab Tech Blog
- url: https://tech.inflab.com/202211-mongodb-atlas-search/
- technologies: Amazon OpenSearch Service, Elasticsearch, Java, search
- problem keywords: observability
- case summary: MongoDB Atlas Search에서 정렬 성능 저하 문제를 경험하고, storedSource 옵션과 near operator, score function을 활용해 성능 개선과 고급 정렬 기능을 구현한 사례입니다.
- problem: MongoDB Atlas Search에서 $search 다음에 $sort를 사용하면 mongod가 많은 데이터를 조회하고 정렬하여 성능 저하가 발생하는 문제와, 다양한 정렬 기준(최신순, 답변많은순, 좋아요순)을 효율적으로 처리하는 어려움이 있었습니다.
- solution: storedSource 옵션으로 정렬 필드를 검색 인덱스에 저장해 mongot에서 정렬을 수행하거나, near operator와 score function을 활용해 mongot에서 필터링과 정렬을 함께 처리하는 방식을 적용하여 성능을 개선하고, score function을 이용해 복합 조건의 고급 정렬을 구현했습니다.

Highlights:

- title: MongoDB Atlas **Search** 정렬이슈 해결기
- caseProblem: MongoDB Atlas Search에서 $**search** 다음에 $sort를 사용하면 mongod가 많은 데이터를 조회하고 정렬하여 성능 저하가 발생하는 문제와, 다양한 정렬 기준(최신순
- caseSolution: storedSource 옵션으로 정렬 필드를 **검색** 인덱스에 저장해 mongot에서 정렬을 수행하거나, near operator와 score function을 활용해 mongot에서
- content: MongoDB Atlas **Search** 우선 검색엔진으로 사용한 기술에 대해 간략한 소개를 하겠습니다. Atlas **Search** 는 MongoDB full-managed 클라우드 서비스인 MongoDB Atlas 에서 제공하는 전문 **검색** 솔루션입니다.
- content: returnStoredSource 옵션을 **검색** 쿼리에 넣어서 요청합니다. db . question . aggregate ( [ { $**search** : { text : { query : "강의" , path : [ "title" , "body" , "writer.name" ] } , returnStoredSource

##### 2. Full-text, exact-match, range, and hybrid search on Amazon ElastiCache

- match: not expected
- source: AWS / AWS Database Blog
- url: https://aws.amazon.com/blogs/database/enhanced-search-for-amazon-elasticache/
- technologies: AWS IAM, Amazon EC2, Amazon ElastiCache, Amazon VPC, Redis, Valkey, search
- problem keywords: migration, performance optimization
- case summary: Amazon ElastiCache 9.0 버전에서 Valkey 엔진을 활용해 실시간 전체 텍스트, 정확 일치, 범위, 하이브리드 검색 기능을 구현하여 대규모 데이터에 대해 마이크로초 단위의 저지연 검색을 가능하게 한 사례이다.
- problem: 대규모 동적 데이터에 대해 별도의 검색 서비스 없이 캐시 내에서 저지연, 고처리량의 다양한 검색(전체 텍스트, 정확 일치, 범위, 벡터 유사도)을 지원해야 하는 상황.
- solution: ElastiCache 9.0의 Valkey 엔진을 사용해 해시 기반 문서 인덱싱과 텍스트, 태그, 숫자, 벡터 필드를 결합한 복합 검색 인덱스를 구축하고, 동기식 인덱싱과 멀티스레딩을 통해 마이크로초 단위 응답과 높은 QPS를 달성했다.

Highlights:

- title: Full-text, exact-match, range, and hybrid **search** on Amazon ElastiCache
- caseSummary: Amazon ElastiCache 9.0 버전에서 Valkey 엔진을 활용해 실시간 전체 텍스트, 정확 일치, 범위, 하이브리드 **검색** 기능을 구현하여 대규모 데이터에 대해 마이크로초
- caseProblem: 대규모 동적 데이터에 대해 별도의 **검색** 서비스 없이 캐시 내에서 저지연, 고처리량의 다양한 **검색**(전체 텍스트, 정확 일치, 범위, 벡터 유사도)을 지원해야 하는 상황.
- caseSolution: ElastiCache 9.0의 Valkey 엔진을 사용해 해시 기반 문서 인덱싱과 텍스트, 태그, 숫자, 벡터 필드를 결합한 복합 **검색** 인덱스를 구축하고, 동기식 인덱싱과 멀티스레딩을
- summary: New **search** capabilities are available in ElastiCache version 9.0 for Valkey.
- summary: In this post, we walk through the new **search** capabilities, show how they work together, and build a **search**

##### 3. Real-time Service Configuration으로 Consul을 신주소 서비스에 적용한 사례

- match: not expected
- source: Woowa Brothers / Woowa Tech Blog
- url: https://techblog.woowahan.com/2586/
- technologies: AWS IAM, Amazon VPC, Java, search
- problem keywords: high availability
- case summary: 배달의민족 주소 검색 서비스의 단일 장애점 문제를 해결하기 위해 Consul 기반 Real-time Service Configuration을 도입하여 외부 지도 API 간 트래픽을 실시간으로 전환하고 환경 설정을 동적으로 관리한 사례입니다.
- problem: 주소 검색 서비스가 A사 지도 API에 100% 의존하여 장애 발생 시 주문 불가 등 큰 서비스 장애가 발생하는 단일 장애점(SPOF) 문제와 레거시 시스템으로 인한 개선 어려움이 있었습니다.
- solution: B사 지도 API를 백업 서비스로 추가하고, ALB를 통한 트래픽 우선순위 전환을 구현했으며, Consul을 활용한 Real-time Service Configuration으로 Git 연동 환경 설정 변경 시 1분 이내에 클라이언트 서비스에 실시간 반영되도록 하여 장애 대응과 서비스 복원력을 강화했습니다.

Highlights:

- caseSummary: 배달의민족 주소 **검색** 서비스의 단일 장애점 문제를 해결하기 위해 Consul 기반 Real-time Service Configuration을 도입하여 외부 지도 API 간 트래픽을
- caseProblem: 주소 **검색** 서비스가 A사 지도 API에 100% 의존하여 장애 발생 시 주문 불가 등 큰 서비스 장애가 발생하는 단일 장애점(SPOF) 문제와 레거시 시스템으로 인한 **개선** 어려움이
- summary: 주소 **검색** 서비스를 개선하면서 Real-time Service Configuration으로 consul을 적용한 사례를 공유하고자 합니다.
- content: AS-IS 주소 **검색** 서비스 사용자의 주소(장소) 및 위치를 조회하는 시스템(PHP 레거시) A사 Map API(의존도 100%) POI 통합검색 API: 전자지도 위에 표시된 건물과 상점 등 **검색** 역지오 **검색** API: 위경도 좌표 -> 주소 단일 장애점(SPOF – Single Point
- content: B사 Map API geocode: 주소 -> 좌표 변환 API reverseGeocoding: 좌표 -> 주소 변환 API **search**: 지역별 업체 및 상호 **검색** API 따라서, B사 Map API 3개를 조합하여 A사의 Poi API와 같은 데이터를 내려주도록 작업을 해야 합니다.


### ko-data-log-platform - `로그 플랫폼`

- category: architecture
- intent: 한글 검색어로 대용량 로그 처리, 로그 파이프라인, 실시간 로그 플랫폼 사례를 찾는다.
- total results: 397
- precision@5: 0.600
- recall@10: 0.600
- mrr: 0.500
- ndcg@10: 0.438

#### Expected URLs

- relevance 3: [일 41TB, 200억 건의 로그를 ClickStack으로 실시간 처리하기 - 호그와트 도서관 프로젝트](https://tech.kakaopay.com/post/pallas-v2-log-platform/)
- relevance 3: [로그 파이프라인 개선기 - 기존 파이프라인 문제 정의 및 해결 방안 적용](https://tech.socarcorp.kr/data/2025/02/25/log-pipeline-revamp.html)
- relevance 2: [로그 데이터로 유저 이해하기](https://techblog.woowahan.com/2536/)
- relevance 3: [비용, 성능, 안정성을 목표로 한 지능형 로그 파이프라인 도입](https://d2.naver.com/helloworld/0004394)
- relevance 2: [Kotlin 환경에서 로그를 기록할 때 불필요한 문자열 연산을 방지하는 방법](https://tech.kakaopay.com/post/efficient-logging-with-kotlin/)

#### Top Results

| Rank | Match | Title | Source | Score | Keywords |
|---:|---|---|---|---:|---|
| 1 | - | [우아한테크캠프 7기: 데모데이 1위 팀의 로그 매니저 프로젝트를 소개합니다!](https://techblog.woowahan.com/19370/) | Woowa Brothers / Woowa Tech Blog | 174.41 | AWS Lambda, Amazon EC2, Amazon RDS, Amazon VPC, JPA, Java |
| 2 | expected:2 | [로그 데이터로 유저 이해하기](https://techblog.woowahan.com/2536/) | Woowa Brothers / Woowa Tech Blog | 170.73 | cost optimization, log platform |
| 3 | - | [실험과 기능플래그를 위한 실험플랫폼 구축하기](https://techblog.woowahan.com/9935/) | Woowa Brothers / Woowa Tech Blog | 152.64 | AWS Glue, Amazon RDS, JVM, Java, Kotlin, Redis |
| 4 | expected:3 | [로그 파이프라인 개선기 - 기존 파이프라인 문제 정의 및 해결 방안 적용](https://tech.socarcorp.kr/data/2025/02/25/log-pipeline-revamp.html) | SOCAR / SOCAR Tech Blog | 150.11 | AWS Lambda, Amazon MSK, Amazon S3, Apache Flink, Apache Kafka, Java |
| 5 | expected:3 | [비용, 성능, 안정성을 목표로 한 지능형 로그 파이프라인 도입](https://d2.naver.com/helloworld/0004394) | NAVER / NAVER D2 | 138.88 | Amazon OpenSearch Service, Apache Kafka, Java, search, observability, log platform |
| 6 | - | [지금 매출 얼마인가요?](https://tech.devsisters.com/posts/near-real-time) | Devsisters / Devsisters Tech Blog | 137.48 | Amazon S3, Apache Kafka, Elasticsearch, search, observability, log platform |
| 7 | - | [따끈따끈한 전사 로그 시스템 전환기: ELK Stack에서 Loki로 전환한 이유](https://techblog.woowahan.com/14505/) | Woowa Brothers / Woowa Tech Blog | 129.99 | Amazon S3, Elasticsearch, OpenTelemetry, search, cost optimization, incident response |
| 8 | - | [AI 데이터 분석가 ‘물어보새’ 등장 – 2부. Data Discovery](https://techblog.woowahan.com/18362/) | Woowa Brothers / Woowa Tech Blog | 128.98 | LLM, search, log platform |
| 9 | - | [쿠키런: 킹덤 데이터베이스 스토리지 레이어 복원기](https://tech.devsisters.com/posts/crk-launch-storage-postmortem) | Devsisters / Devsisters Tech Blog | 123.80 | Amazon EC2, Amazon RDS, incident response, observability, log platform |
| 10 | - | [2021 우아한형제들 경력 개발자 인터뷰 #2편](https://techblog.woowahan.com/5345/) | Woowa Brothers / Woowa Tech Blog | 118.37 | AWS IAM, Amazon CloudWatch, Amazon EC2, Amazon VPC, Elasticsearch, JVM |

#### Top Result Details

##### 1. 우아한테크캠프 7기: 데모데이 1위 팀의 로그 매니저 프로젝트를 소개합니다!

- match: not expected
- source: Woowa Brothers / Woowa Tech Blog
- url: https://techblog.woowahan.com/19370/
- technologies: AWS Lambda, Amazon EC2, Amazon RDS, Amazon VPC, JPA, Java, Node.js, Spring Boot
- problem keywords: performance optimization
- case summary: 우아한테크캠프 7기 팀이 Spring 기반 로그 매니저 'Log Bat'를 개발하며, 대량 로그 처리 시 발생하는 DB 커넥션 병목 문제를 버퍼링과 캐시 도입, 싱글 스레드 큐 구조 개선으로 해결하고 AWS Lambda 부하 테스트를 통해 성능 최적화를 이뤘다.
- problem: 다수의 클라이언트에서 발생하는 로그를 한 곳에 모아 빠르게 저장하고 조회하는 로그 관리 시스템을 구축하는 과정에서, 특히 DB 커넥션 풀 부족과 큐 락 경합으로 인한 병목 현상과 높은 동시성 부하 처리 문제에 직면했다.
- solution: JavaScript와 Java SDK에서 로그를 버퍼링해 배치 전송하도록 개선하고, DB 저장 시 Bulk Insert와 AppKey 검증 캐시 도입으로 DB 커넥션 사용을 최소화했으며, 큐 삽입을 싱글 스레드로 제한해 락 경합을 해소하는 파이프라인 구조를 적용했다. 또한 AWS Lambda 기반 부하 테스트로 병목 지점을 확인하고, 성능 최적화를 반복 수행했다.

Highlights:

- title: 우아한테크캠프 7기: 데모데이 1위 팀의 **로그** 매니저 프로젝트를 소개합니다!
- caseSummary: 우아한테크캠프 7기 팀이 Spring 기반 **로그** 매니저 '**Log** Bat'를 개발하며, 대량 **로그** 처리 시 발생하는 DB 커넥션 병목 문제를 버퍼링과 캐시 도입, 싱글 스레드 큐 구조
- caseProblem: 다수의 클라이언트에서 발생하는 로그를 한 곳에 모아 빠르게 저장하고 조회하는 **로그** 관리 시스템을 구축하는 과정에서, 특히 DB 커넥션 풀 부족과 큐 락 경합으로 인한 병목 현상과 높은
- content: 저희가 준비한 최종 프로젝트 ‘**Log** Bat’는 토이 프로젝트나 사이드 프로젝트를 진행할 때 추가적인 인프라 없이 간편하게 로그를 모아볼 수 있는 **로그** 매니저(**Log** Manager)입니다. 프로젝트 주제로 선정한 이유를 소개합니다.
- content: 예시로 사용자 100만 명이 있는 서비스 앱이 이 **로그** 시스템을 사용하게 될 경우, 100만 개의 서로 다른 인스턴스에서 **로그** 요청이 들어오게 됩니다.

##### 2. 로그 데이터로 유저 이해하기

- match: expected relevance 2
- source: Woowa Brothers / Woowa Tech Blog
- url: https://techblog.woowahan.com/2536/
- technologies: -
- problem keywords: cost optimization
- case summary: 우아한형제들은 앱 내 유저 행동을 이해하고 서비스 개선 인사이트를 도출하기 위해 로그 설계부터 수집, 품질 확보, 분석, 결과 전달까지 전 과정을 체계적으로 수행하였다. 특히 로그 데이터의 품질 확보와 분석 프레임 설정, 중복 데이터 처리 방식을 통해 현실적인 유저 행동 해석과 효율적 분석을 실현하였다.
- problem: 앱 내 유저 행동을 정확히 이해하고 서비스 개선에 필요한 인사이트를 도출하기 위해 로그 데이터를 설계·수집·분석하는 과정에서 데이터 품질 문제와 방대한 로그 데이터 탐색의 어려움, 중복 데이터 처리 문제에 직면하였다.
- solution: 앱 기능과 시나리오를 상세히 파악하여 체계적인 로그 설계 및 JSON 형태의 로그 수집 환경을 구축하고, 데이터 품질 검증 및 오류 수정에 집중하였다. 분석 목적에 맞는 프레임을 사전에 설정해 데이터 탐색의 방향성을 확보하고, 중복 로그는 인간 행동 패턴에 기반해 합리적으로 축약하여 해석하였다. 또한, 분석 결과는 이해하기 쉽고 명확하게 전달하여 실제 비즈니스 적용을 지원하였다.

Highlights:

- title: **로그** 데이터로 유저 이해하기
- caseSummary: 우아한형제들은 앱 내 유저 행동을 이해하고 서비스 개선 인사이트를 도출하기 위해 **로그** 설계부터 수집, 품질 확보, 분석, 결과 전달까지 전 과정을 체계적으로 수행하였다.
- caseSummary: 특히 **로그** 데이터의 품질 확보와 분석 프레임 설정, 중복 데이터 처리 방식을 통해 현실적인 유저 행동 해석과 효율적 분석을 실현하였다.
- caseProblem: 앱 내 유저 행동을 정확히 이해하고 서비스 개선에 필요한 인사이트를 도출하기 위해 **로그** 데이터를 설계·수집·분석하는 과정에서 데이터 품질 문제와 방대한 **로그** 데이터 탐색의 어려움,
- caseSolution: 앱 기능과 시나리오를 상세히 파악하여 체계적인 **로그** 설계 및 JSON 형태의 **로그** 수집 환경을 구축하고, 데이터 품질 검증 및 오류 수정에 집중하였다.
- summary: 이를 위해 **로그** 설계/수집/분석에 이르는 전반적 과정에 직/간접적으로 관여하고 있으며, 입사후 4개월간 경험한 내용과 생각을 공유하고자 합니다. 1.

##### 3. 실험과 기능플래그를 위한 실험플랫폼 구축하기

- match: not expected
- source: Woowa Brothers / Woowa Tech Blog
- url: https://techblog.woowahan.com/9935/
- technologies: AWS Glue, Amazon RDS, JVM, Java, Kotlin, Redis, Spring Boot
- problem keywords: observability, performance optimization
- case summary: 우아한형제들은 실험(AB 테스트)과 기능 플래그를 효과적으로 운영하기 위해 일관된 그룹 분배와 충돌 방지 기능을 갖춘 실험 플랫폼을 구축하였으며, Webflux 기반 비동기 서버 구현과 로그 처리 최적화 방안을 적용했다.
- problem: 서비스 내 다양한 실험과 기능 플래그를 통해 사용자 반응을 검증하고 안정적인 기능 배포를 해야 하는 상황에서, 사용자 그룹 분배의 일관성 보장과 실험 간 충돌 방지, 그리고 효율적인 이벤트 수집 및 결과 집계가 필요했다.
- solution: 10,000개의 슬롯 기반 해싱 알고리즘으로 사용자 그룹 분배의 일관성을 확보하고, 실험 대상 범위 설정으로 실험 간 충돌을 방지했다. 실험 플랫폼 어드민에서 실험과 기능 플래그를 관리하며, 이벤트 데이터는 데이터 플랫폼과 Airflow를 활용해 추출 및 집계한다. 그룹 분배 서버는 Webflux를 사용해 비동기 처리하며, 로그는 AsyncAppender와 neverBlock 옵션으로 비동기화해 이벤트 루프 스레드 차단을 방지했다.

Highlights:

- caseSummary: 우아한형제들은 실험(AB 테스트)과 기능 플래그를 효과적으로 운영하기 위해 일관된 그룹 분배와 충돌 방지 기능을 갖춘 실험 플랫폼을 구축하였으며, Webflux 기반 비동기 서버 구현과 **로그**
- caseSolution: 실험 **플랫폼** 어드민에서 실험과 기능 플래그를 관리하며, 이벤트 데이터는 데이터 플랫폼과 Airflow를 활용해 추출 및 집계한다.
- content: 실험 **플랫폼** 이벤트 데이터 추출 사내 다양한 서비스(배달의민족, B마트)와 이벤트 적재 API를 통해 쌓인 **로그** 정보를 기반으로 실험에 필요한 이벤트 데이터를 추출하고 실험 **플랫폼** 이벤트 테이블(Hive 테이블)에 적재합니다.
- content: 서비스별 **로그** 적재를 위한 dag의 task가 완료되었는지 Sensor를 통해 체크하고 대기합니다. 서비스별 **로그** 테이블에서 실험을 위한 데이터를 추출하는 작업을 진행하고 추출된 결과 데이터를 실험 **플랫폼** 이벤트 Hive 테이블로 적재합니다.


### ko-problem-jvm-latency - `JVM 응답 지연`

- category: problem
- intent: 한글 검색어로 JVM 웜업, 메모리 누수, 배포 직후 지연 같은 JVM 운영 문제 해결 사례를 찾는다.
- total results: 356
- precision@5: 0.400
- recall@10: 1.000
- mrr: 1.000
- ndcg@10: 0.834

#### Expected URLs

- relevance 3: [배포 직후 발생하는 응답 지연을 해결하기 위한 여정 (feat. JVM 웜업)](https://tech.kakaopay.com/post/jvm-warm-up/)
- relevance 2: [도움이 될수도 있는 JVM memory leak 이야기](https://techblog.woowahan.com/2628/)

#### Top Results

| Rank | Match | Title | Source | Score | Keywords |
|---:|---|---|---|---:|---|
| 1 | expected:2 | [도움이 될수도 있는 JVM memory leak 이야기](https://techblog.woowahan.com/2628/) | Woowa Brothers / Woowa Tech Blog | 367.34 | JVM, Java, migration, observability, performance optimization |
| 2 | expected:3 | [배포 직후 발생하는 응답 지연을 해결하기 위한 여정 (feat. JVM 웜업)](https://tech.kakaopay.com/post/jvm-warm-up/) | Kakao Pay / Kakao Pay Tech Blog | 333.29 | JVM, performance optimization |
| 3 | - | [[요기요 카오스 엔지니어링 (2)] 카오스 실험 결과 정리하기](https://techblog.yogiyo.co.kr/%EC%9A%94%EA%B8%B0%EC%9A%94-%EC%B9%B4%EC%98%A4%EC%8A%A4-%EC%97%94%EC%A7%80%EB%8B%88%EC%96%B4%EB%A7%81-2-%EC%B9%B4%EC%98%A4%EC%8A%A4-%EC%8B%A4%ED%97%98-%EA%B2%B0%EA%B3%BC-%EA%B3%B5%EC%9C%A0-7b09c0b2183b?source=rss----c1b33ccbbc42---4) | YOGIYO / YOGIYO Tech Blog | 310.74 | Amazon EKS, Istio, JVM, Redis, observability, performance optimization |
| 4 | - | [신규 포인트 시스템 전환기 #2 – 오픈 준비 단계](https://techblog.woowahan.com/2588/) | Woowa Brothers / Woowa Tech Blog | 283.95 | Amazon CloudWatch, Amazon RDS, JVM, Java, Redis, migration |
| 5 | - | [Java Logger의 또다른 식구, tinylog](https://dev.gmarket.com/67) | Gmarket / Gmarket Tech Blog | 267.42 | AWS Lambda, JVM, Java, Kotlin, Spring Boot, performance optimization |
| 6 | - | [Sharded MySQL Cluster 도입 배경과 개발기 (부제: 우당탕탕 좌충우돌 개발기)](https://dev.gmarket.com/61) | Gmarket / Gmarket Tech Blog | 244.58 | Apache Kafka, JPA, JVM, Java, Kubernetes, Spring Boot |
| 7 | - | [Istio와 Spinnaker를 활용한 Blue-Green + Canary 자동 배포 전략 도입기](https://tech.devsisters.com/posts/blue-green-canary-deployment) | Devsisters / Devsisters Tech Blog | 241.69 | Argo Rollouts, Istio, JVM, Kubernetes, Redis, Spinnaker |
| 8 | - | [Apache Flink + RocksDB 튜닝으로 광고 Frequency Capping 실시간 집계를 일주일까지 확장하기](https://toss.tech/article/flink-realtime-frequency-capping) | Toss / Toss Tech | 239.41 | Apache Flink, Apache Kafka, JVM, Java, Kubernetes, Redis |
| 9 | - | [JDBC setReadOnly 호출 이슈 해결기](https://tech.inflab.com/20240901-jdbc-set-readonly-issue/) | Inflab / Inflab Tech Blog | 239.01 | Amazon Aurora, JVM, Node.js, Spring Boot, observability |
| 10 | - | [Streamlined monitoring and debugging for Amazon EMR on EC2](https://aws.amazon.com/blogs/big-data/streamlined-monitoring-and-debugging-for-amazon-emr-on-ec2/) | AWS / AWS Big Data Blog | 237.02 | Amazon CloudWatch, Amazon EC2, Amazon S3, JVM, high availability, migration |

#### Top Result Details

##### 1. 도움이 될수도 있는 JVM memory leak 이야기

- match: expected relevance 2
- source: Woowa Brothers / Woowa Tech Blog
- url: https://techblog.woowahan.com/2628/
- technologies: JVM, Java
- problem keywords: migration, observability, performance optimization
- case summary: Woowa Brothers의 주문중계 API에서 RestTemplate 사용 시 Netflix ServoMetrics가 URL 패턴을 고유 키로 수집하면서 발생한 JVM 메모리 누수 문제를 분석하고, pathVariable 바인딩 및 ServoMetrics 비활성화로 해결한 사례입니다.
- problem: 주문중계 API에서 트래픽이 많지 않은 상황에서도 응답 지연과 FullGC가 반복되며 메모리 누수가 발생하는 현상이 발견되었고, 원인을 코드나 일반적인 의심 라이브러리에서 찾기 어려웠습니다.
- solution: Heapdump 분석을 통해 Netflix ServoMetrics가 RestTemplate 호출 시 URL을 문자열 결합으로 사용하여 다양한 패턴을 고유 키로 수집하며 메모리 누수가 발생함을 확인, URL pathVariable 바인딩 방식으로 호출을 변경하고 ServoMetrics를 비활성화하거나 의존성에서 제외하여 문제를 해결했습니다.

Highlights:

- title: 도움이 될수도 있는 **JVM** memory leak 이야기
- caseSummary: Woowa Brothers의 주문중계 API에서 RestTemplate 사용 시 Netflix ServoMetrics가 URL 패턴을 고유 키로 수집하면서 발생한 **JVM** 메모리 누수
- caseProblem: 주문중계 API에서 트래픽이 많지 않은 상황에서도 **응답** 지연과 FullGC가 반복되며 메모리 누수가 발생하는 현상이 발견되었고, 원인을 코드나 일반적인 의심 라이브러리에서 찾기 어려웠습니다
- summary: 도움이 될지도 모르는 **JVM** memory leak 얘기인데 제목을 뭐라고 하지? 안녕하세요. 배민 플랫폼실 주문중계 시스템팀 오민철입니다.
- content: 주문중계 api에 문제가 발생했어요. 12월 중순쯤 트래픽이 많지 않았으나 api **응답** **지연** 이 발생했습니다. 응답이 느린 api의 코드를 살펴봤지만, 특이점을 찾을 수 없었습니다. 장애로 번지기 전에 해결하고자 환경 복제 후 트래픽을 새로운 서버로 이관했습니다.
- content: PARALLEL GC -> G1GC 변경하고 **JVM** 메모리 옵션 추가 JDK8의 기본 GC는 PARALLEL GC 입니다. 그래서 이 부분을 G1GC 로 변경하면서 **JVM** 메모리 옵션도 추가하기로 했습니다.

##### 2. 배포 직후 발생하는 응답 지연을 해결하기 위한 여정 (feat. JVM 웜업)

- match: expected relevance 3
- source: Kakao Pay / Kakao Pay Tech Blog
- url: https://tech.kakaopay.com/post/jvm-warm-up/
- technologies: JVM
- problem keywords: performance optimization
- case summary: 카카오페이 굿딜 서비스에서 배포 직후 발생하는 JVM 웜업 문제로 인한 응답 지연을 해결한 사례입니다.
- problem: 배포 직후 JVM이 충분히 웜업되지 않아 초기 요청에 응답 지연이 발생하는 문제를 겪었습니다.
- solution: JVM 웜업 과정을 사전에 실행하거나 최적화하여 배포 후 즉시 안정적인 응답 성능을 확보하는 방식을 도입했습니다.

Highlights:

- title: 배포 직후 발생하는 **응답** 지연을 해결하기 위한 여정 (feat. **JVM** 웜업)
- caseSummary: 카카오페이 굿딜 서비스에서 배포 직후 발생하는 **JVM** 웜업 문제로 인한 **응답** 지연을 해결한 사례입니다.
- caseProblem: 배포 직후 JVM이 충분히 웜업되지 않아 초기 요청에 **응답** 지연이 발생하는 문제를 겪었습니다.
- caseSolution: **JVM** 웜업 과정을 사전에 실행하거나 최적화하여 배포 후 즉시 안정적인 **응답** 성능을 확보하는 방식을 도입했습니다.
- summary: 굿딜 서비스를 운영하며 마주친 배포 직후 **응답** **지연** 문제를 해결하기 위한 과정을 공유하고자 합니다.

##### 3. [요기요 카오스 엔지니어링 (2)] 카오스 실험 결과 정리하기

- match: not expected
- source: YOGIYO / YOGIYO Tech Blog
- url: https://techblog.yogiyo.co.kr/%EC%9A%94%EA%B8%B0%EC%9A%94-%EC%B9%B4%EC%98%A4%EC%8A%A4-%EC%97%94%EC%A7%80%EB%8B%88%EC%96%B4%EB%A7%81-2-%EC%B9%B4%EC%98%A4%EC%8A%A4-%EC%8B%A4%ED%97%98-%EA%B2%B0%EA%B3%BC-%EA%B3%B5%EC%9C%A0-7b09c0b2183b?source=rss----c1b33ccbbc42---4
- technologies: Amazon EKS, Istio, JVM, Redis
- problem keywords: observability, performance optimization
- case summary: 요기요는 Stage 환경에서 AWS FIS를 활용해 Pod 네트워크 지연과 외부 API 장애를 주입하는 카오스 엔지니어링 실험을 수행하여, Redis 연결 병목과 Istio의 빠른 실패 처리 영향, 그리고 멤버십 서비스의 장애 내성을 분석했다.
- problem: 24/7 운영되는 멤버십 서비스에서 네트워크 지연과 외부 API 장애가 발생했을 때 서비스 처리량 저하, 장애 전파, 사용자 경험 저하 문제를 파악하고 개선점을 찾는 것이 필요했다.
- solution: 운영 환경과 유사한 Stage 환경에서 Locust로 트래픽을 재현하며 Pod 네트워크 지연(250ms, 500ms)과 외부 API 차단 장애를 주입하고, 인프라, 애플리케이션 로그, Istio 로그, 클라이언트 지표를 종합 분석해 Redis 연결 리소스 부족, Istio의 Unhealthy Upstream Host 처리, 장애 영향 범위 및 개선 포인트를 도출했다.

Highlights:

- caseSolution: 운영 환경과 유사한 Stage 환경에서 Locust로 트래픽을 재현하며 Pod 네트워크 **지연**(250ms, 500ms)과 외부 API 차단 장애를 주입하고, 인프라, 애플리케이션 로그
- summary: Locust는 응답을 받으면 해당 **응답** 시간을 기준으로 RPS를 조정합니다.
- summary: Check CPU usage of the **JVM**. Try to increase nettyThreads setting.
- content: Locust는 응답을 받으면 해당 **응답** 시간을 기준으로 RPS를 조정합니다. 그런데 RPS가 이 정도로 요동친다는 점은 일반적인 “**지연** 증가”만으로는 설명이 어려워, 뒤에서 추가 분석을 통해 원인을 더 살펴보겠습니다. 3.
- content: Check CPU usage of the **JVM**. Try to increase nettyThreads setting.


### ko-game-server - `게임 서버`

- category: technology
- intent: 한글 검색어로 게임 서버 개발, Scala 게임 서버, 게임 서비스 장애 회고 사례를 찾는다.
- total results: 41
- precision@5: 0.400
- recall@10: 0.667
- mrr: 1.000
- ndcg@10: 0.884

#### Expected URLs

- relevance 3: [데브시스터즈 엔지니어링 데이 - 게임 서버 돌아보기](https://tech.devsisters.com/posts/2025-engineering-day-game-server)
- relevance 3: [게임 서버 개발에 스칼라 사용하기](https://tech.devsisters.com/posts/scala-for-game-server-development-kr)
- relevance 2: [쿠키런: 킹덤 길드 업데이트 이후 서비스 이슈 되돌아보기](https://tech.devsisters.com/posts/crk-hot-range-postmortem)

#### Top Results

| Rank | Match | Title | Source | Score | Keywords |
|---:|---|---|---|---:|---|
| 1 | expected:3 | [게임 서버 개발에 스칼라 사용하기](https://tech.devsisters.com/posts/scala-for-game-server-development-kr) | Devsisters / Devsisters Tech Blog | 379.93 | Apache Kafka, Java, Redis |
| 2 | expected:3 | [데브시스터즈 엔지니어링 데이 - 게임 서버 돌아보기](https://tech.devsisters.com/posts/2025-engineering-day-game-server) | Devsisters / Devsisters Tech Blog | 358.77 | incident response |
| 3 | - | [게임 서버 시스템을 위한 JDBC와 Timeout 이해하기](https://netmarble.engineering/jdbc-timeout-for-game-server/) | Netmarble / Netmarble Tech Blog | 349.73 | search |
| 4 | - | [게임 서버 시스템을 위한 HikariCP 옵션 및 권장 설정](https://netmarble.engineering/hikaricp-options-optimization-for-game-server/) | Netmarble / Netmarble Tech Blog | 334.94 |  |
| 5 | - | [Scala for Game Server Development](https://tech.devsisters.com/posts/scala-for-game-server-development) | Devsisters / Devsisters Tech Blog | 253.52 | Apache Kafka, Redis |
| 6 | - | [새로운 팀의 코드베이스 적응기: 내 코드로 만들어가는 과정](https://tech.devsisters.com/posts/adapt-to-new-codebase) | Devsisters / Devsisters Tech Blog | 248.31 |  |
| 7 | - | [[Windows 컨테이너] 4: 베이스 이미지, 격리 방식에 대한 이해](https://tech.devsisters.com/posts/windows-container-basics) | Devsisters / Devsisters Tech Blog | 228.00 | Amazon EC2, Kubernetes, migration |
| 8 | - | [PerfView를 활용한 .NET GC 프로파일링](https://netmarble.engineering/profiling-dotnet-gc-with-perfview/) | Netmarble / Netmarble Tech Blog | 125.36 |  |
| 9 | - | [Istio와 Spinnaker를 활용한 Blue-Green + Canary 자동 배포 전략 도입기](https://tech.devsisters.com/posts/blue-green-canary-deployment) | Devsisters / Devsisters Tech Blog | 105.58 | Argo Rollouts, Istio, JVM, Kubernetes, Redis, Spinnaker |
| 10 | - | [타입스크립트스럽게 성능과 생산성 두 마리 토끼 모두 잡기](https://tech.devsisters.com/posts/typescript-ish-way-to-improve-performance) | Devsisters / Devsisters Tech Blog | 77.85 | Node.js |

#### Top Result Details

##### 1. 게임 서버 개발에 스칼라 사용하기

- match: expected relevance 3
- source: Devsisters / Devsisters Tech Blog
- url: https://tech.devsisters.com/posts/scala-for-game-server-development-kr
- technologies: Apache Kafka, Java, Redis
- problem keywords: -
- case summary: Devsisters의 쿠키런: 킹덤 게임 서버 개발에 스칼라를 도입하여 정적 타입 시스템과 DSL을 활용해 게임 로직의 정확성, 동시성 문제 해결, 보일러플레이트 감소, 안전한 리팩토링을 실현한 사례입니다.
- problem: 게임 서버는 복잡하고 빠르게 변화하는 게임 로직을 정확히 구현해야 하며, 다수 동시 접속자 처리와 확장성 문제, 그리고 지속적인 기능 추가에 따른 코드 유지보수 어려움이 존재했습니다.
- solution: 스칼라의 강력한 정적 타입 시스템과 refined, newtype 라이브러리를 활용해 타입 안전성을 강화하고, 도메인 특화 언어(DSL)를 만들어 비즈니스 로직을 제한된 연산만 수행하도록 하여 오류 가능성을 줄였습니다. 또한, 매크로와 컴파일러 플러그인을 이용해 프로토콜 버퍼 타입 변환과 GraphQL 스키마 자동 생성 등 보일러플레이트 코드를 줄였으며, ZIO 기반의 파이버를 활용해 동시성 문제를 효율적으로 처리했습니다.

Highlights:

- title: **게임 서버** 개발에 스칼라 사용하기
- caseSummary: Devsisters의 쿠키런: 킹덤 **게임 서버** 개발에 스칼라를 도입하여 정적 타입 시스템과 DSL을 활용해 **게임** 로직의 정확성, 동시성 문제 해결, 보일러플레이트 감소, 안전한 리팩토링을
- summary: Scala가 **게임 서버** 개발에 왜 좋을까요? 그 이유를 알아봅니다.
- content: 스튜디오 킹덤 팀은 스칼라 프로그래밍 언어 (이하 스칼라)를 사용하여 인기 **게임** <쿠키런: 킹덤> **게임** 서버를 만들었습니다. 스칼라는 다른 프로그래밍 언어들보다 덜 알려졌지만, 그래도 우리가 만든 **게임** 서버에는 정말 잘 맞는 언어라고 생각합니다.
- content: 그리고 cookieDataIds 필드 대신 다른 이름을 사용하여 **게임 서버** 코드를 이해하기 쉽게 만들었습니다. 아래 타입들 사이를 변환하기 위해 각각의 Transformer 들이 필요할 것입니다.

##### 2. 데브시스터즈 엔지니어링 데이 - 게임 서버 돌아보기

- match: expected relevance 3
- source: Devsisters / Devsisters Tech Blog
- url: https://tech.devsisters.com/posts/2025-engineering-day-game-server
- technologies: -
- problem keywords: incident response
- case summary: 데브시스터즈는 대규모 트래픽을 처리하는 게임 서버의 안정성과 성능 문제를 함수형 프로그래밍 기반 Scala 백엔드와 Unity 에셋 번들 최적화로 해결한 사례를 공유했다.
- problem: 전 세계 수천만 유저가 이용하는 게임 서버에서 안정적인 라이브 서비스 제공과 모바일 데이터 사용량 최소화라는 두 가지 주요 기술적 도전을 해결해야 했다.
- solution: Scala 함수형 프로그래밍으로 명료하고 확장성 높은 리얼타임 게임 서버를 구현하고, Unity 에셋 번들에 바이너리 패치를 적용해 리소스 업데이트 시 다운로드 용량과 CDN 비용을 크게 줄였다.

Highlights:

- title: 데브시스터즈 엔지니어링 데이 - **게임 서버** 돌아보기
- content: 이번 글에서는 2025년 9월 25일에 진행했던 <제3회 데브시스터즈 엔지니어링 데이 - **게임 서버**>를 소개합니다.
- content: 지난 3번의 행사를 통해 저희는 Infra/SRE, 데이터, **게임 서버** 등 데브시스터즈의 기술 분야에 대한 깊이 있는 이야기를 나누었습니다. 매번 세션이 끝난 후 보내주시는 여러 질문과 피드백 덕분에 저희도 더 성장할 수 있었습니다.

##### 3. 게임 서버 시스템을 위한 JDBC와 Timeout 이해하기

- match: not expected
- source: Netmarble / Netmarble Tech Blog
- url: https://netmarble.engineering/jdbc-timeout-for-game-server/
- technologies: search
- problem keywords: -
- case summary: 넷마블은 게임 서버 시스템에서 JDBC와 타임아웃 설정의 중요성을 분석하고, 기존 WAS-DB 최적화 권장 설정과 다른 게임 서버 특화 설정 방안을 제시했다.
- problem: 기존 JDBC 커넥션 풀과 타임아웃 설정 권장 사항이 주로 WAS와 DB 기반 시스템에 맞춰져 있어, 게임 서버 시스템에서는 적합하지 않은 문제 발생.
- solution: 게임 서버의 특성을 고려한 HikariCP 커넥션 풀과 타임아웃 설정 최적화 방안을 도입하여 안정성과 성능을 개선함.

Highlights:

- title: **게임 서버** 시스템을 위한 JDBC와 Timeout 이해하기
- caseSummary: 넷마블은 **게임 서버** 시스템에서 JDBC와 타임아웃 설정의 중요성을 분석하고, 기존 WAS-DB 최적화 권장 설정과 다른 **게임 서버** 특화 설정 방안을 제시했다.
- caseProblem: 기존 JDBC 커넥션 풀과 타임아웃 설정 권장 사항이 주로 WAS와 DB 기반 시스템에 맞춰져 있어, **게임 서버** 시스템에서는 적합하지 않은 문제 발생.
- summary: 즉, **게임 서버** 시스템을 위한 권장... The post **게임 서버** 시스템을 위한 JDBC와 Timeout 이해하기 appeared first on 넷마블 기술 블로그 .


### ko-event-driven-commerce - `이벤트 기반 상품 조회`

- category: architecture
- intent: 한글 검색어로 이벤트 기반 아키텍처가 커머스, 알림, 상품 조회에 적용된 사례를 찾는다.
- total results: 818
- precision@5: 0.200
- recall@10: 0.333
- mrr: 1.000
- ndcg@10: 0.674

#### Expected URLs

- relevance 3: [쿠폰, 어디에 쓸 수 있어요? - 이벤트 기반 적용 상품 조회 시스템 구축](https://medium.com/29cm/%EC%BF%A0%ED%8F%B0-%EC%96%B4%EB%94%94%EC%97%90-%EC%93%B8-%EC%88%98-%EC%9E%88%EC%96%B4%EC%9A%94-%EC%9D%B4%EB%B2%A4%ED%8A%B8-%EA%B8%B0%EB%B0%98-%EC%A0%81%EC%9A%A9-%EC%83%81%ED%92%88-%EC%A1%B0%ED%9A%8C-%EC%8B%9C%EC%8A%A4%ED%85%9C-%EA%B5%AC%EC%B6%95-4dc35eb97c1f?source=rss----fbd022693005---4)
- relevance 2: [여기어때 이벤트 기반 통합 알림 플랫폼 구축기 Part 1. Why?](https://techblog.gccompany.co.kr/%EC%97%AC%EA%B8%B0%EC%96%B4%EB%95%8C-%EC%9D%B4%EB%B2%A4%ED%8A%B8-%EA%B8%B0%EB%B0%98-%ED%86%B5%ED%95%A9-%EC%95%8C%EB%A6%BC-%ED%94%8C%EB%9E%AB%ED%8F%BC-%EA%B5%AC%EC%B6%95%EA%B8%B0-part-1-why-3d2961d1e849?source=rss----18356045d353---4)
- relevance 2: [여기어때 이벤트 기반 통합 알림 플랫폼 구축기 Part 2. How?](https://techblog.gccompany.co.kr/%EC%97%AC%EA%B8%B0%EC%96%B4%EB%95%8C-%EC%9D%B4%EB%B2%A4%ED%8A%B8-%EA%B8%B0%EB%B0%98-%ED%86%B5%ED%95%A9-%EC%95%8C%EB%A6%BC-%ED%94%8C%EB%9E%AB%ED%8F%BC-%EA%B5%AC%EC%B6%95%EA%B8%B0-part-2-how-11f41bb2b5f2?source=rss----18356045d353---4)

#### Top Results

| Rank | Match | Title | Source | Score | Keywords |
|---:|---|---|---|---:|---|
| 1 | expected:3 | [쿠폰, 어디에 쓸 수 있어요? — 이벤트 기반 적용 상품 조회 시스템 구축](https://medium.com/29cm/%EC%BF%A0%ED%8F%B0-%EC%96%B4%EB%94%94%EC%97%90-%EC%93%B8-%EC%88%98-%EC%9E%88%EC%96%B4%EC%9A%94-%EC%9D%B4%EB%B2%A4%ED%8A%B8-%EA%B8%B0%EB%B0%98-%EC%A0%81%EC%9A%A9-%EC%83%81%ED%92%88-%EC%A1%B0%ED%9A%8C-%EC%8B%9C%EC%8A%A4%ED%85%9C-%EA%B5%AC%EC%B6%95-4dc35eb97c1f?source=rss----fbd022693005---4) | 29CM / 29CM TEAM | 649.71 | Apache Kafka, Elasticsearch, search, Change Data Capture, event-driven architecture |
| 2 | - | [Building event-driven architecture for member system](https://techblog.woowahan.com/10320/) | Woowa Brothers / Woowa Tech Blog | 633.61 | high availability, performance optimization, event-driven architecture |
| 3 | - | [Mastering millisecond latency and millions of events: The event-driven architecture behind the Amazon Key Suite](https://aws.amazon.com/blogs/architecture/mastering-millisecond-latency-and-millions-of-events-the-event-driven-architecture-behind-the-amazon-key-suite/) | AWS / AWS Architecture Blog | 431.27 | AWS CDK, AWS IAM, Amazon EventBridge, migration, observability, performance optimization |
| 4 | - | [Build a multi-tenant configuration system with tagged storage patterns](https://aws.amazon.com/blogs/architecture/build-a-multi-tenant-configuration-system-with-tagged-storage-patterns/) | AWS / AWS Architecture Blog | 337.92 | AWS CloudFormation, AWS IAM, AWS Lambda, Amazon CloudWatch, Amazon DynamoDB, Amazon ElastiCache |
| 5 | - | [Modernizing KYC with AWS serverless solutions and agentic AI for financial services](https://aws.amazon.com/blogs/architecture/modernizing-kyc-with-aws-serverless-solutions-and-agentic-ai-for-financial-services/) | AWS / AWS Architecture Blog | 321.80 | AWS Lambda, Amazon CloudWatch, Amazon DynamoDB, Amazon MSK, Amazon OpenSearch Service, Amazon S3 |
| 6 | - | [VLOps:Event-driven MLOps & Omni-Evaluator](https://d2.naver.com/helloworld/0931890) | NAVER / NAVER D2 | 158.53 | observability, event-driven architecture |
| 7 | - | [postgres_fdw로 마이그레이션 생산성 높이기](https://techblog.woowahan.com/20371/) | Woowa Brothers / Woowa Tech Blog | 155.93 | Amazon RDS, migration, performance optimization, event-driven architecture |
| 8 | - | [(youtube)Event Streaming 도입과 앞으로의 활용](https://medium.com/29cm/youtube-event-streaming-%EB%8F%84%EC%9E%85%EA%B3%BC-%EC%95%9E%EC%9C%BC%EB%A1%9C%EC%9D%98-%ED%99%9C%EC%9A%A9-806f2002586a?source=rss----fbd022693005---4) | 29CM / 29CM TEAM | 143.44 | event-driven architecture |
| 9 | - | [[배민스토어] 배민스토어에 이벤트 기반 아키텍처를 곁들인…](https://techblog.woowahan.com/13101/) | Woowa Brothers / Woowa Tech Blog | 142.64 | Amazon DynamoDB, Apache Kafka, Kotlin, Redis, search, high availability |
| 10 | - | [오픈마켓 여행 플랫폼의 실전 API 연동 노하우](https://dev.gmarket.com/115) | Gmarket / Gmarket Tech Blog | 141.19 | performance optimization, event-driven architecture |

#### Top Result Details

##### 1. 쿠폰, 어디에 쓸 수 있어요? — 이벤트 기반 적용 상품 조회 시스템 구축

- match: expected relevance 3
- source: 29CM / 29CM TEAM
- url: https://medium.com/29cm/%EC%BF%A0%ED%8F%B0-%EC%96%B4%EB%94%94%EC%97%90-%EC%93%B8-%EC%88%98-%EC%9E%88%EC%96%B4%EC%9A%94-%EC%9D%B4%EB%B2%A4%ED%8A%B8-%EA%B8%B0%EB%B0%98-%EC%A0%81%EC%9A%A9-%EC%83%81%ED%92%88-%EC%A1%B0%ED%9A%8C-%EC%8B%9C%EC%8A%A4%ED%85%9C-%EA%B5%AC%EC%B6%95-4dc35eb97c1f?source=rss----fbd022693005---4
- technologies: Apache Kafka, Elasticsearch, search
- problem keywords: -
- case summary: 29CM은 복잡한 쿠폰과 상품 매핑 조건을 실시간으로 반영하는 이벤트 기반 시스템을 구축하여, 사용자에게 쿠폰 적용 가능 상품 목록을 빠르고 정확하게 제공하는 기능을 성공적으로 구현했다.
- problem: 쿠폰과 상품 간 복잡한 매핑 및 실시간 변경 사항을 반영해 사용자에게 쿠폰 적용 가능 상품을 정확하고 신속하게 조회할 수 있는 시스템이 부재했다.
- solution: Kafka 기반 이벤트 드리븐 아키텍처를 활용해 쿠폰과 상품 변경 이벤트를 실시간 처리하고, 반정규화 테이블에 쿠폰-상품 적용 가능 정보를 저장하며, 이를 Debezium CDC와 Elasticsearch 인덱싱으로 연동해 빠른 검색과 필터링을 지원하는 시스템을 설계·구현했다.

Highlights:

- title: — **이벤트 기반 적용 상품 조회** 시스템 구축
- caseSummary: 29CM은 복잡한 쿠폰과 **상품** 매핑 조건을 실시간으로 반영하는 **이벤트** **기반** 시스템을 구축하여, 사용자에게 쿠폰 적용 가능 **상품** 목록을 빠르고 정확하게 제공하는 기능을 성공적으로 구현했다
- caseProblem: 쿠폰과 **상품** 간 복잡한 매핑 및 실시간 변경 사항을 반영해 사용자에게 쿠폰 적용 가능 상품을 정확하고 신속하게 조회할 수 있는 시스템이 부재했다.
- caseSolution: Kafka **기반** **이벤트** 드리븐 아키텍처를 활용해 쿠폰과 **상품** 변경 이벤트를 실시간 처리하고, 반정규화 테이블에 쿠폰-**상품** 적용 가능 정보를 저장하며, 이를 Debezium CDC와
- summary: — **이벤트 기반 적용 상품 조회** 시스템 구축 안녕하세요, 29CM Commerce Core Engineering 에서 Sale Pricing 팀으로 일하고 있는 백엔드 개발자 조한석이라고
- summary: 그래서 지금까지 사용자들은 쿠폰 사용처를 찾기 위해 일일이 **상품** 페이지를 방문하며 확인해야 했습니다. 🥲 2025년 2월, 마침내 오랜 숙원과 같았던 쿠폰 적용 가능 **상품** 목록 **조회**

##### 2. Building event-driven architecture for member system

- match: not expected
- source: Woowa Brothers / Woowa Tech Blog
- url: https://techblog.woowahan.com/10320/
- technologies: -
- problem keywords: high availability, performance optimization
- case summary: 배민 회원 시스템에서 급격한 트래픽 증가와 단일 DB 한계로 인해 마이크로서비스 아키텍처와 이벤트 기반 아키텍처를 도입하여 시스템 안정성과 느슨한 결합을 달성한 사례이다.
- problem: 단일 프로젝트로 시작한 배민 회원 시스템이 주문 증가에 따른 트래픽 폭증으로 단일 DB 처리 한계에 봉착하고, 시스템 오류가 빈번해져 안정화가 필요했다.
- solution: 마이크로서비스 아키텍처로 시스템을 분리하고, 이벤트 기반 아키텍처를 적용하여 도메인 간 결합도를 낮추고 비동기 메시징(AWS SNS-SQS)을 활용해 업무 로직과 부수 정책을 분리하여 확장성과 유지보수성을 확보했다.

Highlights:

- title: Building **event-driven architecture** for member system
- caseSummary: 배민 회원 시스템에서 급격한 트래픽 증가와 단일 DB 한계로 인해 마이크로서비스 아키텍처와 **이벤트** **기반** 아키텍처를 도입하여 시스템 안정성과 느슨한 결합을 달성한 사례이다.
- caseSolution: 마이크로서비스 아키텍처로 시스템을 분리하고, **이벤트** **기반** 아키텍처를 적용하여 도메인 간 결합도를 낮추고 비동기 메시징(AWS SNS-SQS)을 활용해 업무 로직과 부수 정책을 분리하여
- content: From a macroscopic perspective, it seems **event-driven architecture** is now a somewhat familiar concept, but **event-driven architecture** is still a new thing from a
- content: This is how **event-driven architecture** is built in the member system.

##### 3. Mastering millisecond latency and millions of events: The event-driven architecture behind the Amazon Key Suite

- match: not expected
- source: AWS / AWS Architecture Blog
- url: https://aws.amazon.com/blogs/architecture/mastering-millisecond-latency-and-millions-of-events-the-event-driven-architecture-behind-the-amazon-key-suite/
- technologies: AWS CDK, AWS IAM, Amazon EventBridge
- problem keywords: migration, observability, performance optimization
- case summary: Amazon Key 팀은 기존의 긴밀하게 결합된 모놀리식 시스템을 Amazon EventBridge 기반의 이벤트 중심 아키텍처로 전환하여 밀리초 단위 지연 시간과 수백만 건의 이벤트를 안정적으로 처리하는 확장 가능하고 유연한 시스템을 구축했다.
- problem: 기존 시스템은 서비스 간 긴밀한 결합과 느슨한 이벤트 스키마, 비효율적인 이벤트 라우팅으로 인해 시스템 안정성과 확장성에 심각한 제약이 있었으며, 단일 장애점이 전체 서비스에 영향을 미치는 문제가 발생했다.
- solution: 단일 이벤트 버스와 멀티 계정 구조를 도입해 서비스별 독립성과 중앙 집중식 거버넌스를 확보하고, 스키마 저장소와 클라이언트 라이브러리, 구독자 구성 라이브러리를 개발해 이벤트 스키마 관리, 검증, 표준화된 구독자 인프라 구축을 통해 개발 생산성과 시스템 신뢰성을 크게 향상시켰다.

Highlights:

- title: Mastering millisecond latency and millions of events: The **event-driven architecture** behind the Amazon
- caseSummary: Amazon Key 팀은 기존의 긴밀하게 결합된 모놀리식 시스템을 Amazon EventBridge 기반의 **이벤트** 중심 아키텍처로 전환하여 밀리초 단위 지연 시간과 수백만 건의 이벤트를
- caseProblem: 기존 시스템은 서비스 간 긴밀한 결합과 느슨한 **이벤트** 스키마, 비효율적인 **이벤트** 라우팅으로 인해 시스템 안정성과 확장성에 심각한 제약이 있었으며, 단일 장애점이 전체 서비스에 영향을
- caseSolution: 단일 **이벤트** 버스와 멀티 계정 구조를 도입해 서비스별 독립성과 중앙 집중식 거버넌스를 확보하고, 스키마 저장소와 클라이언트 라이브러리, 구독자 구성 라이브러리를 개발해 **이벤트** 스키마
- summary: to modernize their architecture, transforming a tightly coupled monolithic system into a resilient, **event**-**driven**
- summary: The post covers our solutions for managing **event** schemas at scale, handling multiple service integrations


### ko-problem-data-consistency - `낙관적 락`

- category: problem
- intent: 한글 검색어로 동시성 상황에서 데이터 정합성을 유지하는 방법과 낙관적 락 적용 사례를 찾는다.
- total results: 2
- precision@5: 0.200
- recall@10: 1.000
- mrr: 1.000
- ndcg@10: 1.000

#### Expected URLs

- relevance 3: [뱅크샐러드가 게임을 만들 때 데이터 정합성을 유지하는 법 (feat. 낙관적 락)](https://blog.banksalad.com/tech/banksalad-optimistic-lock/)

#### Top Results

| Rank | Match | Title | Source | Score | Keywords |
|---:|---|---|---|---:|---|
| 1 | expected:3 | [뱅크샐러드가 게임을 만들 때 데이터 정합성을 유지하는 법 (feat. 낙관적 락)](https://blog.banksalad.com/tech/banksalad-optimistic-lock/) | Banksalad / Banksalad Blog | 469.49 |  |
| 2 | - | [프로모션 시스템 엿보기: 파일럿 프로젝트](https://techblog.woowahan.com/10795/) | Woowa Brothers / Woowa Tech Blog | 85.57 | JPA, Redis, Spring Boot, search |

#### Top Result Details

##### 1. 뱅크샐러드가 게임을 만들 때 데이터 정합성을 유지하는 법 (feat. 낙관적 락)

- match: expected relevance 3
- source: Banksalad / Banksalad Blog
- url: https://blog.banksalad.com/tech/banksalad-optimistic-lock/
- technologies: -
- problem keywords: -
- case summary: 뱅크샐러드는 게임 개발 과정에서 데이터 정합성 문제를 낙관적 락(Optimistic Lock) 기법을 활용해 해결한 사례를 다룬다.
- problem: 게임 내에서 다수의 동시 사용자로 인해 발생하는 데이터 충돌과 정합성 문제를 어떻게 관리할지에 대한 고민이 있었다.
- solution: 낙관적 락을 적용하여 데이터 충돌 시점에만 재시도를 통해 정합성을 유지하고, 성능 저하 없이 동시성 문제를 해결했다.

Highlights:

- title: **낙관적 락**)
- caseSummary: 뱅크샐러드는 게임 개발 과정에서 데이터 정합성 문제를 **낙관적 락**(Optimistic Lock) 기법을 활용해 해결한 사례를 다룬다.

##### 2. 프로모션 시스템 엿보기: 파일럿 프로젝트

- match: not expected
- source: Woowa Brothers / Woowa Tech Blog
- url: https://techblog.woowahan.com/10795/
- technologies: JPA, Redis, Spring Boot, search
- problem keywords: -
- case summary: 우아한형제들 배민푸드서비스 개발팀에서 신입 개발자가 파일럿 프로젝트로 프로모션 시스템 API 서버를 Spring Webflux와 R2DBC 기반으로 구현하며 요구사항 분석, ERD 설계, 비동기 트랜잭션 관리, 복잡한 쿼리 최적화, 동시성 문제 대응 경험을 공유한다.
- problem: 프로모션 시스템에서 마케터별 복잡한 쿠폰 지급 조건과 대량 사용자 요청을 효율적으로 처리하며, 쿠폰 발급 이력과 참여 제한, 동시성 문제를 해결해야 하는 상황이었다.
- solution: Spring Webflux와 R2DBC를 활용해 비동기 논블로킹 API 서버를 구축하고, Reactor Context를 이용한 비동기 트랜잭션 관리를 적용했으며, 복잡한 조인 쿼리를 통해 N+1 문제를 해결하고, 동시성 문제를 고려한 참여 이력 조회 및 쿠폰 발급 로직을 구현했다.

Highlights:

- content: 이를 해결하기 위한 방법으로 메시지 큐나 Redis를 이용한 글로벌 락과 같은 방법도 있겠지만 파일럿 프로젝트이기에 WAS, DB 이외에 추가적인 인프라 리소스를 활용하지 않고, 코드 레벨 혹은 DB만을 가지고 해결이 가능한 비관적 **락**, **낙관적 락** 2가지 방법을 고려하였습니다.
- content: 이러한 비관적 락은 DB row에 Exclusive Lock 을 걸기에 속도가 많이 저하되는 문제가 있지만, **낙관적** 락을 사용하지 않은 이유는 다음과 같습니다. 개인적으로 **낙관적** 락은 “선착순 1명”과 같이 여러 요청 중 하나의 요청만을 성공시켜야 할 때 적절한 방법이라고 생각합니다.


### ko-architecture-pr-preview - `PR Preview Argo CD Linkerd`

- category: architecture
- intent: 한글/영문 혼합 검색어로 QA 병목을 줄이기 위한 PR Preview 환경과 GitOps 기반 배포 사례를 찾는다.
- total results: 202
- precision@5: 0.400
- recall@10: 1.000
- mrr: 1.000
- ndcg@10: 0.932

#### Expected URLs

- relevance 3: [Argo CD, Linkerd 기반 QA 병목 제거: PR Preview 환경 구축](https://tech.inflab.com/20251121-pr-preview/)
- relevance 2: [EKS + ALB 환경에서 Argo Rollouts 503 에러 없는 카나리 배포 적용기](https://techblog.gccompany.co.kr/eks-alb-%ED%99%98%EA%B2%BD%EC%97%90%EC%84%9C-argo-rollouts-503-%EC%97%90%EB%9F%AC-%EC%97%86%EB%8A%94-%EC%B9%B4%EB%82%98%EB%A6%AC-%EB%B0%B0%ED%8F%AC-%EC%A0%81%EC%9A%A9%EA%B8%B0-689eedaf8d1a?source=rss----18356045d353---4)

#### Top Results

| Rank | Match | Title | Source | Score | Keywords |
|---:|---|---|---|---:|---|
| 1 | expected:3 | [Argo CD, Linkerd 기반 QA 병목 제거: PR Preview 환경 구축](https://tech.inflab.com/20251121-pr-preview/) | Inflab / Inflab Tech Blog | 509.64 | Kubernetes, cost optimization, migration, observability |
| 2 | - | [CI 소요시간을 최대 4.6배 개선하는 방법](https://tech.inflab.com/20231101-optimizing-ci-pipeline/) | Inflab / Inflab Tech Blog | 47.09 | AWS Lambda, Amazon EC2, Amazon S3, Node.js, observability, serverless |
| 3 | - | [누구나 찾아볼 수 있는 중고거래 서버 LLM 릴리즈 노트 도입기](https://medium.com/daangn/%EB%88%84%EA%B5%AC%EB%82%98-%EC%B0%BE%EC%95%84%EB%B3%BC-%EC%88%98-%EC%9E%88%EB%8A%94-%EC%A4%91%EA%B3%A0%EA%B1%B0%EB%9E%98-%EC%84%9C%EB%B2%84-llm-%EB%A6%B4%EB%A6%AC%EC%A6%88-%EB%85%B8%ED%8A%B8-%EB%8F%84%EC%9E%85%EA%B8%B0-93afe203d766?source=rss----4505f82a2dbd---4) | Daangn / Daangn Tech Blog | 42.84 | Java, LLM |
| 4 | expected:2 | [EKS + ALB 환경에서 Argo Rollouts 503 에러 없는 카나리 배포 적용기](https://techblog.gccompany.co.kr/eks-alb-%ED%99%98%EA%B2%BD%EC%97%90%EC%84%9C-argo-rollouts-503-%EC%97%90%EB%9F%AC-%EC%97%86%EB%8A%94-%EC%B9%B4%EB%82%98%EB%A6%AC-%EB%B0%B0%ED%8F%AC-%EC%A0%81%EC%9A%A9%EA%B8%B0-689eedaf8d1a?source=rss----18356045d353---4) | GC Company / GC Company Tech Blog | 42.18 | Amazon EKS, Amazon S3, Argo Rollouts, Kubernetes, incident response, observability |
| 5 | - | [ODW #1: AI로 리뷰 정체를 해소하다 - PR 리뷰 지원과 사내 워크숍으로 리뷰 문화 바꾸기](https://techblog.lycorp.co.jp/ko/resolving-pr-review-bottlenecks-with-ai-and-transforming-review-culture) | LY Corporation / LY Corporation Tech Blog | 42.07 |  |
| 6 | - | [라이더스 개발팀 모바일에서 CI/CD 도입](https://techblog.woowahan.com/2579/) | Woowa Brothers / Woowa Tech Blog | 41.33 | search |
| 7 | - | [AWX를 이용한 CI/CD Pipeline: Pylon](https://tech.kakaopay.com/post/sre-re-pylon/) | Kakao Pay / Kakao Pay Tech Blog | 41.33 |  |
| 8 | - | [Yarn Classic에서 Pnpm으로 전환하기 with TurboRepo](https://medium.com/wantedjobs/yarn-classic%EC%97%90%EC%84%9C-pnpm%EC%9C%BC%EB%A1%9C-%EC%A0%84%ED%99%98%ED%95%98%EA%B8%B0-with-turborepo-7c0c37cb3f9e?source=rss----fb47eceee74c---4) | Wantedlab / Wantedlab Tech Blog | 40.67 | AWS Lambda, React, migration, serverless |
| 9 | - | [https://www.upstage.ai/blog/ko/solar-pro-2-preview-introduction](https://www.upstage.ai/blog/ko/solar-pro-2-preview-introduction) | Upstage / Upstage Blog | 40.55 |  |
| 10 | - | [Linger 로 오버헤드 줄이기](https://dev.gmarket.com/26) | Gmarket / Gmarket Tech Blog | 40.21 | Apache Kafka |

#### Top Result Details

##### 1. Argo CD, Linkerd 기반 QA 병목 제거: PR Preview 환경 구축

- match: expected relevance 3
- source: Inflab / Inflab Tech Blog
- url: https://tech.inflab.com/20251121-pr-preview/
- technologies: Kubernetes
- problem keywords: cost optimization, migration, observability
- case summary: 인프랩은 Kubernetes, Argo CD ApplicationSet, Linkerd를 활용해 PR 별 독립된 QA Preview 환경을 자동 생성 및 트래픽 라우팅하여 개발 병목을 해소했다.
- problem: 단일 QA 환경으로 인해 여러 개발자가 동시에 기능 테스트를 진행할 수 없고, 배포 충돌과 높은 커뮤니케이션 비용이 발생하는 병목 현상이 있었다.
- solution: Argo CD ApplicationSet으로 PR마다 자동으로 격리된 테스트 환경을 생성하고, Linkerd의 HTTPRoute를 이용한 쿠키 기반 트래픽 라우팅으로 기존 도메인 유지하면서 PR 환경으로 트래픽을 분기해 병렬 QA를 가능하게 했다.

Highlights:

- title: **Argo** **CD**, **Linkerd** 기반 QA 병목 제거: **PR** **Preview** 환경 구축
- caseSummary: 인프랩은 Kubernetes, **Argo** **CD** ApplicationSet, **Linkerd를** 활용해 **PR** 별 독립된 QA **Preview** 환경을 자동 생성 및 트래픽 라우팅하여 개발 병목을
- caseSolution: **Argo** **CD** ApplicationSet으로 PR마다 자동으로 격리된 테스트 환경을 생성하고, **Linkerd의** HTTPRoute를 이용한 쿠키 기반 트래픽 라우팅으로 기존 도메인 유지하면서
- caseSolution: **PR** 환경으로 트래픽을 분기해 병렬 QA를 가능하게 했다.
- content: 이를 해결하기 위해 **Argo** **CD** ApplicationSet 의 동적 환경 생성 능력과 **Linkerd** 의 트래픽 라우팅 기능을 조합했습니다. 1. **Argo** **CD** ApplicationSet: 동적 환경 생성 PR마다 자동으로 환경을 만들려면 두 가지 조건이 필요했습니다.
- content: 이제 개발자가 PR에 라벨만 붙이면, **Argo** CD가 알아서 inflearn-courses-fe-**pr**-<번호> 와 같은 이름의 Application을 생성하고 배포를 시작합니다. **Preview** 환경은 기능 테스트가 목적이므로 개발/운영 환경과 동일한 스펙일 필요가 없습니다.

##### 2. CI 소요시간을 최대 4.6배 개선하는 방법

- match: not expected
- source: Inflab / Inflab Tech Blog
- url: https://tech.inflab.com/20231101-optimizing-ci-pipeline/
- technologies: AWS Lambda, Amazon EC2, Amazon S3, Node.js
- problem keywords: observability
- case summary: 인프랩은 모노레포 기반 대규모 프로젝트에서 CI 파이프라인의 의존성 설치 및 빌드 시간을 최대 4.6배 단축하기 위해 pnpm과 turborepo 도입, 그리고 Jenkins 기반 캐시 볼륨 마운트 최적화를 적용했다.
- problem: 모노레포 프로젝트가 커지면서 의존성 설치와 빌드 시간이 급증해 PR 리뷰 및 배포 지연 문제가 발생했고, 기존 순차적 빌드와 의존성 캐시 미활용으로 CI 효율이 떨어졌다.
- solution: pnpm으로 의존성 설치 방식을 개선해 디스크 I/O를 줄이고 turborepo를 도입해 증분 빌드 및 병렬 실행, 원격 캐싱을 활용했으며, Jenkins CI 환경에서 캐시 볼륨 마운트를 통해 브랜치 간 의존성 캐시 공유를 구현해 설치 시간을 97% 단축했다.

Highlights:

- caseProblem: 모노레포 프로젝트가 커지면서 의존성 설치와 빌드 시간이 급증해 **PR** 리뷰 및 배포 지연 문제가 발생했고, 기존 순차적 빌드와 의존성 캐시 미활용으로 CI 효율이 떨어졌다.
- summary: 여러분은 혹시 CI 파이프라인이 너무 오래 동작해서 **PR** 리뷰에 영향을 받은 적 있으신가요? 프로젝트 규모가 커질수록 늘어나는 CI/**CD**…
- content: 여러분은 혹시 CI 파이프라인이 너무 오래 동작해서 **PR** 리뷰에 영향을 받은 적 있으신가요? 프로젝트 규모가 커질수록 늘어나는 CI / **CD** 파이프라인의 소요시간으로 고민한 적이 있으신가요? 이번 글에서 소요시간을 최대 4.6배 까지 개선할 수 있었던 노하우를 공유해 드리겠습니다.
- content: 이로 인해 rallit_frontend 의 **PR**#15242, **PR**#15243 모두 같은 경로( /tmp/.pnpm-store )를 바라보게 됩니다.

##### 3. 누구나 찾아볼 수 있는 중고거래 서버 LLM 릴리즈 노트 도입기

- match: not expected
- source: Daangn / Daangn Tech Blog
- url: https://medium.com/daangn/%EB%88%84%EA%B5%AC%EB%82%98-%EC%B0%BE%EC%95%84%EB%B3%BC-%EC%88%98-%EC%9E%88%EB%8A%94-%EC%A4%91%EA%B3%A0%EA%B1%B0%EB%9E%98-%EC%84%9C%EB%B2%84-llm-%EB%A6%B4%EB%A6%AC%EC%A6%88-%EB%85%B8%ED%8A%B8-%EB%8F%84%EC%9E%85%EA%B8%B0-93afe203d766?source=rss----4505f82a2dbd---4
- technologies: Java, LLM
- problem keywords: -
- case summary: 당근마켓 중고거래 서버에서 배포 내역을 비개발자도 쉽게 이해할 수 있도록 LLM과 기존 도구를 활용해 자동 요약 및 릴리즈 노트 생성 파이프라인을 구축한 사례입니다.
- problem: 배포 시점과 변경 내용을 개발자만 이해 가능한 git log와 PR 목록에서 일일이 확인해야 하는 비효율과, 기술 용어가 비개발자에게 전달되지 않아 팀 전체 커뮤니케이션 비용이 증가하는 문제를 겪었습니다.
- solution: GitHub Actions와 Rails 기반 rake task로 배포 시점에 PR 목록과 설명을 Notion에 정형화해 저장하고, 사내 GenAI 플랫폼인 Prompt Studio를 통해 LLM으로 비개발자도 이해할 수 있는 릴리즈 노트를 자동 생성하는 2단계 파이프라인을 구축했습니다. PR description은 AI 요약 도구(CodeRabbit)로 사전 정제하여 LLM 토큰 비용과 품질 문제를 해결했고, 프롬프트를 코드 외부에서 관리해 용어 변환과 분류 규칙을 지속적으로 개선했습니다.

Highlights:

- caseProblem: 배포 시점과 변경 내용을 개발자만 이해 가능한 git log와 **PR** 목록에서 일일이 확인해야 하는 비효율과, 기술 용어가 비개발자에게 전달되지 않아 팀 전체 커뮤니케이션 비용이 증가하는
- caseSolution: GitHub Actions와 Rails 기반 rake task로 배포 시점에 **PR** 목록과 설명을 Notion에 정형화해 저장하고, 사내 GenAI 플랫폼인 Prompt Studio를
- caseSolution: **PR** description은 AI 요약 도구(CodeRabbit)로 사전 정제하여 LLM 토큰 비용과 품질 문제를 해결했고, 프롬프트를 코드 외부에서 관리해 용어 변환과 분류 규칙을
- summary: “**PR** 하나가 어떤 기능을 적용·수정했고 어떻게 바뀌었는지”를 **PR** 단위로 정리한 문서가 그 형태예요.
- summary: 여기서 **PR** 본문은 GitHub에서 다시 가져오는 게 아니라, Stage 1에서 이미 Notion **PR** DB에 저장해둔 본문을 그대로 읽어요.
- content: 여기서 **PR** 본문은 GitHub에서 다시 가져오는 게 아니라, Stage 1에서 이미 Notion **PR** DB에 저장해둔 본문을 그대로 읽어요. **PR** 정보를 한 번만 가져오면 그다음부터는 Notion이 우리 데이터 소스가 되는 거예요.


### ko-problem-s3-cdn-cost - `S3 비용 이미지 CDN 최적화`

- category: problem
- intent: 한글 검색어로 S3 보관 비용, 이미지 CDN 트래픽, CloudFront 비용 효율화 사례를 찾는다.
- total results: 119
- precision@5: 0.400
- recall@10: 1.000
- mrr: 1.000
- ndcg@10: 0.918

#### Expected URLs

- relevance 3: [Amazon S3 보관 비용과 이미지 CDN 트래픽 최적화](https://tech.inflab.com/20251029-optimize-s3/)
- relevance 2: [CloudFront의 숨은 힘: 캐싱 없이도 극대화 되는 성능과 비용 효율성](https://medium.com/wantedjobs/cloudfront%EC%9D%98-%EC%88%A8%EC%9D%80-%ED%9E%98-%EC%BA%90%EC%8B%B1-%EC%97%86%EC%9D%B4%EB%8F%84-%EA%B7%B9%EB%8C%80%ED%99%94-%EB%90%98%EB%8A%94-%EC%84%B1%EB%8A%A5%EA%B3%BC-%EB%B9%84%EC%9A%A9-%ED%9A%A8%EC%9C%A8%EC%84%B1-44f66701d1eb?source=rss----fb47eceee74c---4)

#### Top Results

| Rank | Match | Title | Source | Score | Keywords |
|---:|---|---|---|---:|---|
| 1 | expected:3 | [Amazon S3 보관 비용과 이미지 CDN 트래픽 최적화](https://tech.inflab.com/20251029-optimize-s3/) | Inflab / Inflab Tech Blog | 382.98 | AWS Lambda, Amazon S3, search, cost optimization, observability |
| 2 | - | [Optimize Amazon S3 Tables queries with Amazon Redshift](https://aws.amazon.com/blogs/big-data/optimize-amazon-s3-tables-queries-with-amazon-redshift/) | AWS / AWS Big Data Blog | 287.25 | AWS Glue, AWS IAM, Amazon S3, Apache Iceberg, migration, observability |
| 3 | - | [AWS re:Invent 2024 Recap: Database, Storage](https://tech.kakaopay.com/post/aws-reinvent-2024-database-and-storage/) | Kakao Pay / Kakao Pay Tech Blog | 255.24 | Amazon Aurora, Amazon S3 |
| 4 | - | [Enable real-time mainframe analytics with Precisely Connect and Amazon S3](https://aws.amazon.com/blogs/big-data/enable-real-time-mainframe-analytics-with-precisely-connect-and-amazon-s3/) | AWS / AWS Big Data Blog | 252.53 | AWS Glue, Amazon MSK, Amazon RDS, Amazon S3, Apache Iceberg, migration |
| 5 | expected:2 | [CloudFront의 숨은 힘: 캐싱 없이도 극대화 되는 성능과 비용 효율성](https://medium.com/wantedjobs/cloudfront%EC%9D%98-%EC%88%A8%EC%9D%80-%ED%9E%98-%EC%BA%90%EC%8B%B1-%EC%97%86%EC%9D%B4%EB%8F%84-%EA%B7%B9%EB%8C%80%ED%99%94-%EB%90%98%EB%8A%94-%EC%84%B1%EB%8A%A5%EA%B3%BC-%EB%B9%84%EC%9A%A9-%ED%9A%A8%EC%9C%A8%EC%84%B1-44f66701d1eb?source=rss----fb47eceee74c---4) | Wantedlab / Wantedlab Tech Blog | 246.71 | Amazon EC2, Amazon S3, cost optimization, performance optimization |
| 6 | - | [Query billion-scale vectors with SQL: Integrating Amazon S3 Vectors and Aurora PostgreSQL](https://aws.amazon.com/blogs/database/query-billion-scale-vectors-with-sql-integrating-amazon-s3-vectors-and-aurora-postgresql/) | AWS / AWS Database Blog | 238.76 | AWS CloudFormation, AWS IAM, AWS Lambda, Amazon Aurora, Amazon CloudWatch, Amazon RDS |
| 7 | - | [How to use streamlined permissions for Amazon S3 Tables and Iceberg materialized views](https://aws.amazon.com/blogs/big-data/how-to-use-streamlined-permissions-for-amazon-s3-tables-and-iceberg-materialized-views/) | AWS / AWS Big Data Blog | 234.30 | AWS CloudFormation, AWS Glue, AWS IAM, Amazon S3, Apache Iceberg, serverless |
| 8 | - | [데이터 분석 라이브러리 개발기 (2) - 통합 테스팅과 문서화를 동시에 잡는 방법](https://tech.devsisters.com/posts/testing-devplay-analytics-library) | Devsisters / Devsisters Tech Blog | 227.95 | Amazon S3, Java |
| 9 | - | [스타트업 엔지니어의 AWS 비용 최적화 경험기](https://tech.inflab.com/20240227-finops-for-startup/) | Inflab / Inflab Tech Blog | 224.49 | AWS CDK, AWS CloudFormation, AWS Lambda, Amazon Aurora, Amazon CloudWatch, Amazon DynamoDB |
| 10 | - | [Streamlined monitoring and debugging for Amazon EMR on EC2](https://aws.amazon.com/blogs/big-data/streamlined-monitoring-and-debugging-for-amazon-emr-on-ec2/) | AWS / AWS Big Data Blog | 191.31 | Amazon CloudWatch, Amazon EC2, Amazon S3, JVM, high availability, migration |

#### Top Result Details

##### 1. Amazon S3 보관 비용과 이미지 CDN 트래픽 최적화

- match: expected relevance 3
- source: Inflab / Inflab Tech Blog
- url: https://tech.inflab.com/20251029-optimize-s3/
- technologies: AWS Lambda, Amazon S3, search
- problem keywords: cost optimization, observability
- case summary: 인프랩은 Amazon S3의 보관 비용과 CDN 이미지 트래픽 비용을 줄이기 위해 S3 Intelligent-Tiering 스토리지 클래스 도입과 Lambda@Edge 기반 이미지 리사이저 및 AVIF 포맷 변환을 적용하여 비용 절감과 사용자 경험 개선을 달성했다.
- problem: 대량의 VOD 영상과 이미지 파일을 Amazon S3에 저장하면서 스토리지 보관 비용과 CDN 트래픽 비용이 급증해 비용 최적화가 필요했다.
- solution: S3 Intelligent-Tiering을 도입해 자동으로 접근 빈도에 따라 스토리지 클래스를 전환하고, Lambda@Edge를 활용해 CloudFront 엣지에서 이미지 리사이징과 AVIF 포맷 변환을 수행하여 CDN 트래픽을 줄였다. 또한, S3 Inventory와 CopyObject API를 활용해 비용 효율적으로 스토리지 클래스를 전환했다.

Highlights:

- title: **Amazon S3** 보관 비용과 이미지 CDN 트래픽 최적화
- summary: 인프랩은 최근 **Amazon S3** 보관 비용과 CDN 트래픽을 최적화하는 성과를 달성했습니다.
- content: 인프랩은 최근 **Amazon S3** 보관 비용과 **CDN** 트래픽을 최적화하는 성과를 달성했습니다. **S3** Intelligent-Tiering 스토리지 클래스 도입과, **CDN** 응답 **이미지** AVIF·MP4 포맷 변환 지원에 관한 내용입니다.
- content: 만약 객체 보관 패턴을 잘 알기 어려운 경우라면 **S3** Inventory 도 활용해보시기를 권해 드립니다. **이미지** **CDN** 트래픽 **최적화** 왜 비용이 많이 나오는가? 영상 보관 뿐만 아니라, 서비스 곳곳에서 사용되는 이미지의 **CDN** 응답 트래픽도 최적화의 대상이었습니다.

##### 2. Optimize Amazon S3 Tables queries with Amazon Redshift

- match: not expected
- source: AWS / AWS Big Data Blog
- url: https://aws.amazon.com/blogs/big-data/optimize-amazon-s3-tables-queries-with-amazon-redshift/
- technologies: AWS Glue, AWS IAM, Amazon S3, Apache Iceberg
- problem keywords: migration, observability, performance optimization
- case summary: Amazon Redshift와 S3 Tables를 활용한 Apache Iceberg 테이블 쿼리 성능 및 사용성 최적화 사례로, 외부 스키마 생성, 물리적 뷰 활용, 데이터 파일 컴팩션 전략 조정을 통해 쿼리 속도와 비용 효율을 개선했다.
- problem: S3 Tables의 Apache Iceberg 테이블을 Amazon Redshift로 쿼리할 때, 반복 쿼리 시 매번 S3 데이터를 스캔하고 복잡한 3파트 테이블 참조 구문으로 인해 BI 도구 및 사용자 접근성이 떨어지며, 비효율적인 데이터 파일 레이아웃으로 쿼리 성능 저하가 발생했다.
- solution: Lake Formation 리소스 링크를 활용해 외부 스키마를 생성하여 쿼리 구문을 2파트로 단순화하고, 물리적 뷰(materialized views)를 만들어 반복 쿼리 시 로컬 저장소에서 결과를 읽도록 하며, S3 Tables의 컴팩션 전략(자동, binpack, sort, z-order)을 쿼리 패턴에 맞게 조정해 데이터 파일 레이아웃을 최적화했다.

Highlights:

- title: Optimize **Amazon S3** Tables queries with Amazon Redshift
- caseSummary: **Amazon Redshift와 S3** Tables를 활용한 Apache Iceberg 테이블 쿼리 성능 및 사용성 최적화 사례로, 외부 스키마 생성, 물리적 뷰 활용, 데이터 파일 컴팩션
- content: **Amazon S3** Tables with Amazon Redshift gives you a powerful combination for analytical workloads on Apache Iceberg tables.
- content: To learn more, see the **Amazon S3** Tables documentation , Materialized views in Amazon Redshift , and S3 Tables maintenance .

##### 3. AWS re:Invent 2024 Recap: Database, Storage

- match: not expected
- source: Kakao Pay / Kakao Pay Tech Blog
- url: https://tech.kakaopay.com/post/aws-reinvent-2024-database-and-storage/
- technologies: Amazon Aurora, Amazon S3
- problem keywords: -
- case summary: AWS re:Invent 2024에서 발표된 Amazon Aurora DSQL과 Amazon S3 Tables를 활용한 데이터베이스 및 스토리지 혁신 사례를 소개합니다.
- problem: 대규모 데이터베이스와 스토리지 환경에서 성능과 확장성을 개선할 필요가 있었습니다.
- solution: Amazon Aurora DSQL과 Amazon S3 Tables를 도입하여 데이터 처리 효율성과 저장소 관리 최적화를 달성했습니다.

Highlights:

- caseSummary: AWS re:Invent 2024에서 발표된 Amazon Aurora DSQL과 **Amazon S3** Tables를 활용한 데이터베이스 및 스토리지 혁신 사례를 소개합니다.
- caseSolution: Amazon Aurora DSQL과 **Amazon S3** Tables를 도입하여 데이터 처리 효율성과 저장소 관리 최적화를 달성했습니다.
- summary: AWS re:Invent 2024에서 새롭게 공개한 Amazon Aurora DSQL과 **Amazon S3** Tables를 소개합니다.


### ko-problem-bottlerocket-gpu - `Bottlerocket GPU 노드 교체`

- category: problem
- intent: 한글/영문 혼합 검색어로 EKS Bottlerocket GPU 노드 운영 문제와 이미지 캐싱 최적화 사례를 찾는다.
- total results: 148
- precision@5: 0.400
- recall@10: 1.000
- mrr: 1.000
- ndcg@10: 1.000

#### Expected URLs

- relevance 3: [EKS Bottlerocket AMI에서 DCGM 오류로 GPU 노드 반복 교체 문제 해결기](https://tech.inflab.com/20250827-bottlerocket-ami-gpu-issue/)
- relevance 2: [EKS Bottlerocket에서 이미지 캐싱으로 Pull 시간 줄이기](https://tech.inflab.com/20250421-bottlerocket-volume-image-cache/)

#### Top Results

| Rank | Match | Title | Source | Score | Keywords |
|---:|---|---|---|---:|---|
| 1 | expected:3 | [EKS Bottlerocket AMI에서 DCGM 오류로 GPU 노드 반복 교체 문제 해결기](https://tech.inflab.com/20250827-bottlerocket-ami-gpu-issue/) | Inflab / Inflab Tech Blog | 431.23 | Amazon EC2, Amazon EKS, Kubernetes, observability |
| 2 | expected:2 | [EKS Bottlerocket에서 이미지 캐싱으로 Pull 시간 줄이기](https://tech.inflab.com/20250421-bottlerocket-volume-image-cache/) | Inflab / Inflab Tech Blog | 63.47 | AWS CloudFormation, Amazon EC2, Amazon EKS, Amazon S3, Kubernetes, cost optimization |
| 3 | - | [쿠팡의 머신러닝 플랫폼을 통한 ML 개발 가속화](https://medium.com/coupang-engineering/%EC%BF%A0%ED%8C%A1%EC%9D%98-%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D-%ED%94%8C%EB%9E%AB%ED%8F%BC%EC%9D%84-%ED%86%B5%ED%95%9C-ml-%EA%B0%9C%EB%B0%9C-%EA%B0%80%EC%86%8D%ED%99%94-de29804148bb?source=rss----fb028911af07---4) | Coupang / Coupang Engineering Blog | 42.55 | Kubernetes, LLM, search, observability, canary deployment, streaming data pipeline |
| 4 | - | [AI 플랫폼 GPU 도입부터 Kubeflow까지 도입기](https://tech.kakaopay.com/post/ai-platform/) | Kakao Pay / Kakao Pay Tech Blog | 42.47 |  |
| 5 | - | [EKS Anywhere 구축기](https://techblog.woowahan.com/10221/) | Woowa Brothers / Woowa Tech Blog | 42.39 | AWS CloudFormation, AWS IAM, Amazon CloudWatch, Amazon EC2, Amazon EKS, Amazon S3 |
| 6 | - | [Kurly만의 MLOps 구축하기 - 초석 다지기](https://helloworld.kurly.com/blog/first-mlops/) | Kurly / Kurly Tech Blog | 42.33 |  |
| 7 | - | [변화에 유연한 HTTP 클라이언트 만들기](https://tech.inflab.com/20230723-pure-http-client/) | Inflab / Inflab Tech Blog | 41.37 | JVM, Node.js |
| 8 | - | [디자인 생산성을 높이는 피그마 플러그인을 만들어보자 2부: 개발 편](https://techblog.woowahan.com/21850/) | Woowa Brothers / Woowa Tech Blog | 41.16 | Amazon S3, React, search |
| 9 | - | [하마터면 못생겨질 뻔했다 - 토스 프론트 2 제작기](https://toss.tech/article/toss_front) | Toss / Toss Tech | 40.95 |  |
| 10 | - | [Meet Coupang’s Machine Learning Platform](https://medium.com/coupang-engineering/meet-coupangs-machine-learning-platform-cd00e9ccc172?source=rss----fb028911af07---4) | Coupang / Coupang Engineering Blog | 40.51 | Kubernetes, LLM, search, observability, performance optimization, canary deployment |

#### Top Result Details

##### 1. EKS Bottlerocket AMI에서 DCGM 오류로 GPU 노드 반복 교체 문제 해결기

- match: expected relevance 3
- source: Inflab / Inflab Tech Blog
- url: https://tech.inflab.com/20250827-bottlerocket-ami-gpu-issue/
- technologies: Amazon EC2, Amazon EKS, Kubernetes
- problem keywords: observability
- case summary: Amazon EKS Bottlerocket AMI 환경에서 NVIDIA DCGM 라이브러리 누락으로 인해 GPU 노드가 AcceleratedHardwareReady=False 상태가 되어 Karpenter의 Node Auto-Repair 기능이 반복적으로 노드를 교체하는 문제를 해결한 사례입니다.
- problem: Bottlerocket AMI 기반 EKS 클러스터에서 GPU 노드가 정상 생성 후 약 10분 내에 DCGM 라이브러리 누락 오류로 AcceleratedHardwareReady 상태가 False가 되어 Karpenter가 노드를 비정상으로 판단, 반복 교체하는 문제가 발생했습니다.
- solution: 근본 원인인 DCGM 라이브러리 누락 문제는 Bottlerocket AMI 특성상 직접 수정이 어려워, 임시로 Karpenter의 Node Auto-Repair 기능을 비활성화하여 GPU 노드의 반복 교체를 막고 안정적인 GPU 워크로드 운영을 유지했습니다.

Highlights:

- title: EKS **Bottlerocket** AMI에서 DCGM 오류로 **GPU** **노드** 반복 **교체** 문제 해결기
- caseSummary: Amazon EKS **Bottlerocket** AMI 환경에서 NVIDIA DCGM 라이브러리 누락으로 인해 **GPU** 노드가 AcceleratedHardwareReady=False 상태가
- caseProblem: **Bottlerocket** AMI 기반 EKS 클러스터에서 **GPU** 노드가 정상 생성 후 약 10분 내에 DCGM 라이브러리 누락 오류로 AcceleratedHardwareReady 상태가
- caseSolution: 근본 원인인 DCGM 라이브러리 누락 문제는 **Bottlerocket** AMI 특성상 직접 수정이 어려워, 임시로 Karpenter의 Node Auto-Repair 기능을 비활성화하여
- caseSolution: **GPU** 노드의 반복 교체를 막고 안정적인 **GPU** 워크로드 운영을 유지했습니다.
- summary: 최근 인프런의 ”클린 코더스: 실전 객체 지향 프로그래밍과 TDD 마스터 클래스” 강의 영상 업스케일링 작업을 위해 **GPU** 클러스터를 운영하던 중, 예상치 못한 문제에 직면했습니다.

##### 2. EKS Bottlerocket에서 이미지 캐싱으로 Pull 시간 줄이기

- match: expected relevance 2
- source: Inflab / Inflab Tech Blog
- url: https://tech.inflab.com/20250421-bottlerocket-volume-image-cache/
- technologies: AWS CloudFormation, Amazon EC2, Amazon EKS, Amazon S3, Kubernetes
- problem keywords: cost optimization, performance optimization
- case summary: 인프랩은 AWS EKS의 Bottlerocket OS 환경에서 대용량 컨테이너 이미지의 pull 시간을 줄이기 위해 이미지가 캐시된 EBS 볼륨 스냅샷을 활용하는 방식을 도입하여 컨테이너 시작 시간을 15분에서 10초 이내로 단축하고 비용을 70% 이상 절감했다.
- problem: Spot 인스턴스 환경에서 대용량 컨테이너 이미지를 자주 pull해야 하면서 이미지 다운로드 및 압축 해제에 수분이 소요되어 EC2 및 네트워크 자원 낭비와 컨테이너 시작 지연 문제가 발생했다.
- solution: Bottlerocket OS의 운영체제와 컨테이너 데이터를 분리하는 구조를 활용해 이미지가 저장된 컨테이너 데이터 볼륨을 EBS 스냅샷으로 생성하고, 신규 노드 생성 시 해당 스냅샷을 기반으로 볼륨을 복원하여 이미지 pull 과정을 생략하는 캐시 전략을 적용했다. 또한, 스냅샷 볼륨의 lazy loading 문제를 해결하기 위해 EBS gp3 볼륨의 IOPS와 throughput을 높여 초기 파일 로드 시간을 단축했다.

Highlights:

- title: EKS **Bottlerocket에서** 이미지 캐싱으로 Pull 시간 줄이기
- caseSummary: 인프랩은 AWS EKS의 **Bottlerocket** OS 환경에서 대용량 컨테이너 이미지의 pull 시간을 줄이기 위해 이미지가 캐시된 EBS 볼륨 스냅샷을 활용하는 방식을 도입하여 컨테이너
- caseSolution: **Bottlerocket** OS의 운영체제와 컨테이너 데이터를 분리하는 구조를 활용해 이미지가 저장된 컨테이너 데이터 볼륨을 EBS 스냅샷으로 생성하고, 신규 **노드** 생성 시 해당 스냅샷을
- caseSolution: 또한, 스냅샷 볼륨의 lazy loading 문제를 해결하기 위해 EBS **gp3** 볼륨의 IOPS와 throughput을 높여 초기 파일 로드 시간을 단축했다.
- content: **Bottlerocket** OS 우선, **Bottlerocket** 은 AWS에서 컨테이너 호스팅에 최적화하여 제작한 Linux 기반의 오픈소스 운영체제입니다. 환경 구축시 **Bottlerocket을** 사용한 이유는 다음과 같습니다.
- content: snapshotID : { snapshot - id } # 필요한 로드 성능에 따라 값 조정 iops : 3000 # **gp3** 기본값 3000 throughput : 750 # **gp3** 기본값 125MiB/s 마무리 이번 개선 작업을 통해 **Bottlerocket의** 구조적 장점과 EBS 스냅샷을

##### 3. 쿠팡의 머신러닝 플랫폼을 통한 ML 개발 가속화

- match: not expected
- source: Coupang / Coupang Engineering Blog
- url: https://medium.com/coupang-engineering/%EC%BF%A0%ED%8C%A1%EC%9D%98-%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D-%ED%94%8C%EB%9E%AB%ED%8F%BC%EC%9D%84-%ED%86%B5%ED%95%9C-ml-%EA%B0%9C%EB%B0%9C-%EA%B0%80%EC%86%8D%ED%99%94-de29804148bb?source=rss----fb028911af07---4
- technologies: Kubernetes, LLM, search
- problem keywords: observability
- case summary: 쿠팡은 머신러닝 개발의 복잡성과 시간 소모 문제를 해결하기 위해 통합 ML 플랫폼을 구축하여 개발 속도와 운영 효율성을 크게 향상시켰다.
- problem: 기존 ML 개발은 데이터 준비, 분산 훈련, 모델 배포 등에서 복잡한 설정과 높은 엔지니어링 요구로 인해 개발 및 적용 시간이 길고 비용이 많이 들었다.
- solution: 쿠팡은 관리형 Jupyter Notebook, 피처 스토어, 컨테이너 기반 모델 훈련 및 추론, Kubernetes 기반 배포, 모니터링, 하이브리드 온프레미스-클라우드 인프라를 통합한 ML 플랫폼을 도입하여 개발과 배포를 표준화하고 자동화했다.

Highlights:

- summary: 쿠팡은 다중 **GPU를** 사용한 학습으로 모델 훈련 작업 속도를 크게 향상시켰습니다.
- summary: 이를 통해 다양한 모델 프레임워크, 런타임 및 하드웨어(CPU 및 **GPU** 서빙 포함)를 폭넓게 지원합니다.
- content: 트레이닝 클러스터의 **GPU** 사용률 모니터링 훈련에는 대용량 메모리가 있는 인스턴스, **GPU와** 같은 가속기, 분산 훈련을 위한 **노드** 간 고대역폭 연결, 그리고 훈련 데이터 및 모델 체크포인트와 같은 출력 아티팩트를 저장하기 위한 공유 스토리지 클러스터가 필요합니다.
- content: A100 **GPU의** 다중 **GPU** 분산 훈련을 통해 이전 세대의 GPU들과 훈련 전략에 비해 버트(BERT)의 훈련 속도가 10배 향상되었습니다.


### ko-tech-redis-stream - `Redis Stream`

- category: technology
- intent: Redis Stream과 Redis 운영, Kubernetes 구성, connection 이슈, cluster migration 사례를 찾는다.
- total results: 90
- precision@5: 0.800
- recall@10: 1.000
- mrr: 1.000
- ndcg@10: 0.914

#### Expected URLs

- relevance 3: [Redis Stream 적용기](https://dev.gmarket.com/113)
- relevance 3: [Redis New Connection 증가 이슈 돌아보기](https://techblog.woowahan.com/23121/)
- relevance 2: [Redis on Kubernetes 플랫폼을 구성해 나가기](https://tech.kakaopay.com/post/kakaopaysec-redis-on-kubernetes/)
- relevance 2: [DevOps 엔지니어의 Redis Test 분투기 - Part 1](https://helloworld.kurly.com/blog/redis-fight-part-1/)
- relevance 2: [초보 개발자를 위한 Redis Cluster Migration 가이드라인](https://dev.gmarket.com/71)
- relevance 2: [Redis Lua Script를 이용해서 API Rate Limiter개발](https://dev.gmarket.com/69)

#### Top Results

| Rank | Match | Title | Source | Score | Keywords |
|---:|---|---|---|---:|---|
| 1 | expected:3 | [Redis Stream 적용기](https://dev.gmarket.com/113) | Gmarket / Gmarket Tech Blog | 1209.54 | Apache Kafka, Redis, Redis Stream, Spring Boot, high availability, streaming data pipeline |
| 2 | - | [Server-Sent Events로 실시간 알림 전달하기](https://techblog.woowahan.com/23199/) | Woowa Brothers / Woowa Tech Blog | 626.94 | Apache Kafka, MQTT, Redis, Redis Stream, observability |
| 3 | expected:3 | [Redis New Connection 증가 이슈 돌아보기](https://techblog.woowahan.com/23121/) | Woowa Brothers / Woowa Tech Blog | 202.60 | Amazon ElastiCache, Redis, Spring Boot, Valkey, observability |
| 4 | expected:2 | [Redis on Kubernetes 플랫폼을 구성해 나가기](https://tech.kakaopay.com/post/kakaopaysec-redis-on-kubernetes/) | Kakao Pay / Kakao Pay Tech Blog | 202.60 | Kubernetes, Redis |
| 5 | expected:2 | [초보 개발자를 위한 Redis Cluster Migration 가이드라인](https://dev.gmarket.com/71) | Gmarket / Gmarket Tech Blog | 193.21 | Java, Node.js, Redis, Spring Boot, search, migration |
| 6 | expected:2 | [Redis Lua Script를 이용해서 API Rate Limiter개발](https://dev.gmarket.com/69) | Gmarket / Gmarket Tech Blog | 193.21 | Java, Redis |
| 7 | expected:2 | [DevOps 엔지니어의 Redis Test 분투기 - Part 1](https://helloworld.kurly.com/blog/redis-fight-part-1/) | Kurly / Kurly Tech Blog | 193.21 | Redis |
| 8 | - | [[배민스토어] 신입 개발자 배민스토어 6개월 생존기](https://techblog.woowahan.com/12987/) | Woowa Brothers / Woowa Tech Blog | 190.61 | Java, Kotlin, Redis, search, migration, event-driven architecture |
| 9 | - | [How Our Team Uses Kafka](https://techblog.woowahan.com/20078/) | Woowa Brothers / Woowa Tech Blog | 189.16 | Amazon S3, Apache Kafka, Java, Redis, performance optimization, Change Data Capture |
| 10 | - | [이제 Redis를 멈춰보겠습니다: @CacheEvict 파헤치기](https://techblog.woowahan.com/23138/) | Woowa Brothers / Woowa Tech Blog | 188.01 | Java, Redis, Spring Boot, incident response |

#### Top Result Details

##### 1. Redis Stream 적용기

- match: expected relevance 3
- source: Gmarket / Gmarket Tech Blog
- url: https://dev.gmarket.com/113
- technologies: Apache Kafka, Redis, Redis Stream, Spring Boot
- problem keywords: high availability
- case summary: Gmarket Data Product 팀은 대규모 사용자 세션 히스토리 데이터를 실시간으로 안정적이고 빠르게 처리하기 위해 Redis Stream을 도입하여 기존 Redis 기반 세션 저장소와 연계한 스트리밍 데이터 파이프라인을 구축했다.
- problem: 빅스마일데이 등 대규모 트래픽 급증 시 세션 히스토리 적재 및 처리 지연으로 인한 데이터 처리 병목 현상 발생과 기존 Redis Pub/Sub의 메시지 유실 및 중복 문제.
- solution: 기존 Redis 세션 저장소를 활용하면서 Kafka와 유사한 기능을 제공하는 Redis Stream을 도입해 consumer group 기반 병렬 처리 구조를 구현하고, 메시지 처리 완료 확인(ack) 및 미처리 메시지 재처리 로직을 추가해 데이터 일관성과 고가용성을 확보함.

Highlights:

- title: **Redis Stream** 적용기
- caseSummary: Gmarket Data Product 팀은 대규모 사용자 세션 히스토리 데이터를 실시간으로 안정적이고 빠르게 처리하기 위해 **Redis** Stream을 도입하여 기존 **Redis** 기반 세션
- caseProblem: 빅스마일데이 등 대규모 트래픽 급증 시 세션 히스토리 적재 및 처리 지연으로 인한 데이터 처리 병목 현상 발생과 기존 **Redis** Pub/Sub의 메시지 유실 및 중복 문제.
- caseSolution: 기존 **Redis** 세션 저장소를 활용하면서 Kafka와 유사한 기능을 제공하는 **Redis** Stream을 도입해 consumer group 기반 병렬 처리 구조를 구현하고, 메시지 처리
- summary: 이번에 제가 소개해드릴 내용은 팀 내 session Info data 적재 및 API 서비스 구축에 적용한 **Redis** Stream에 대한 이야기입니다.
- content: **Redis Stream** flow 먼저 Post Processor에서 트래픽 데이터를 가공/처리한 후, app에서 정의한 streamKey를 통해서 생성한 session 객체를 캡슐화해서 **Redis Stream** 메시지로 발행합니다.

##### 2. Server-Sent Events로 실시간 알림 전달하기

- match: not expected
- source: Woowa Brothers / Woowa Tech Blog
- url: https://techblog.woowahan.com/23199/
- technologies: Apache Kafka, MQTT, Redis, Redis Stream
- problem keywords: observability
- case summary: 배달의민족 주문접수 프로그램에서 기존 MQTT 기반 알림 시스템의 보안, 네트워크 방화벽, Webview 지원 문제를 해결하기 위해 AWS IoT와 Server-Sent Events(SSE)를 도입하여 안정적이고 확장 가능한 실시간 알림 전달 체계를 구축한 사례입니다.
- problem: 기존 MQTT 기반 알림 시스템은 Zero Payload 메시지 전달, 보안 미흡, 네트워크 방화벽 차단, Webview 환경 지원 불가 등의 문제로 인해 대규모 사용자 증가에 따른 빠르고 안정적인 알림 전송이 어려웠습니다.
- solution: AWS IoT를 활용해 MQTT 브로커 보안과 메시지 정형화를 적용하고, Webview 및 방화벽 문제 해결을 위해 HTTP 기반 단방향 실시간 통신인 Server-Sent Events(SSE)를 도입했습니다. 메시지 전달은 Kafka 브로커를 통한 모든 서버 구독 방식으로 확장성과 메시지 순서 보장, 유실 방지를 구현했으며, 중복 연결 방지, 수신 확인(CommitEvent) 및 비즈니스 로직 기반 재전송으로 신뢰성을 높였습니다. 또한 클라이언트 Polling을 제거하고 서버에서 필요한 외부 API 호출을 대체하여 네트워크 비용을 절감했습니다.

Highlights:

- content: 장점: 직접 전달 : 연결된 서버에만 메시지를 보내므로 불필요한 네트워크 홉 최소화 레이턴시 최적화 : 브로커를 거치지 않아 상대적으로 빠른 전달 가능 단점: 세션 추적 복잡도 클라이언트가 어느 서버에 연결되어 있는지 별도 관리 필요 **Redis** 등 세션 저장소 구축 및 실시간 동기화 필요
- content: 메시지 브로커 최적화 현재 Kafka를 사용 중이지만, SSE 특성에 더 적합한 브로커 검토 **Redis** Streams, NATS 등 대안 기술 PoC 진행 예정 2.

##### 3. Redis New Connection 증가 이슈 돌아보기

- match: expected relevance 3
- source: Woowa Brothers / Woowa Tech Blog
- url: https://techblog.woowahan.com/23121/
- technologies: Amazon ElastiCache, Redis, Spring Boot, Valkey
- problem keywords: observability
- case summary: 우아한형제들은 Redis 신규 커넥션 증가 문제를 Lettuce 커넥션 풀과 Elasticache 타임아웃 설정 간 상호작용에서 발생한 커넥션 재생성 이슈로 진단하고, 커넥션 풀 전략 변경과 IDLE 커넥션 정리 설정을 통해 문제를 해결하였다.
- problem: Redis 신규 커넥션 생성 수가 예상과 달리 자정 이후에도 줄어들지 않고 오히려 증가하는 현상이 발생하여 서비스 지연 가능성이 우려되었다.
- solution: Lettuce 커넥션 풀의 기본 LIFO 전략을 FIFO로 변경하여 커넥션 재사용을 개선하고, 커넥션 풀의 IDLE 커넥션에 대해 eviction 설정을 추가하여 Elasticache의 100초 타임아웃으로 인한 커넥션 끊김 후 재연결 문제를 완화하였다.

Highlights:

- title: **Redis** New Connection 증가 이슈 돌아보기
- caseSummary: 우아한형제들은 **Redis** 신규 커넥션 증가 문제를 Lettuce 커넥션 풀과 Elasticache 타임아웃 설정 간 상호작용에서 발생한 커넥션 재생성 이슈로 진단하고, 커넥션 풀 전략
- caseProblem: **Redis** 신규 커넥션 생성 수가 예상과 달리 자정 이후에도 줄어들지 않고 오히려 증가하는 현상이 발생하여 서비스 지연 가능성이 우려되었다.
- summary: **Redis** 관련 지표를 모니터링 하던 중 신규 커넥션 생성이 많은 현상을 발견하였습니다.
- content: Redis를 사용하는 데 있어 Spring data **Redis** 설정뿐 아니라 **Redis** OSS Parameter까지 다양한 설정을 확인해야 한다는 점을 배우게 된 계기가 되었습니다. 이 글이 관련된 문제를 확인하고 계신 다른 분들께 도움이 되었기를 바랍니다.
- content: 참고 문서 https://docs.spring.io/spring-data/**redis**/reference/**redis**/drivers.html#redis:connectors:connection **Redis** OSS 2.6.13 parameters https://commons.apache.org/proper


### ko-tech-kubernetes-operator - `쿠버네티스 오퍼레이터 Java`

- category: technology
- intent: 쿠버네티스 오퍼레이터를 Java 또는 Golang으로 구현하거나 적용한 사례를 찾는다.
- total results: 352
- precision@5: 0.600
- recall@10: 1.000
- mrr: 1.000
- ndcg@10: 0.980

#### Expected URLs

- relevance 3: [쿠버네티스 오퍼레이터를 Java로 개발해보기](https://dev.gmarket.com/112)
- relevance 2: [쿠버네티스 오퍼레이터를 Golang으로 개발해보기](https://dev.gmarket.com/102)
- relevance 2: [쿠버네티스 오퍼레이터 적용하기](https://dev.gmarket.com/65)

#### Top Results

| Rank | Match | Title | Source | Score | Keywords |
|---:|---|---|---|---:|---|
| 1 | expected:3 | [쿠버네티스 오퍼레이터를 Java로 개발해보기](https://dev.gmarket.com/112) | Gmarket / Gmarket Tech Blog | 393.82 | Java, Kubernetes, Spring Boot |
| 2 | expected:2 | [쿠버네티스 오퍼레이터를 Golang으로 개발해보기](https://dev.gmarket.com/102) | Gmarket / Gmarket Tech Blog | 371.20 | Java, Kubernetes, Spring Boot |
| 3 | - | [Kubernetes 클러스터에 애플리케이션 배포하기](https://medium.com/naver-cloud-platform/kubernetes-%ED%81%B4%EB%9F%AC%EC%8A%A4%ED%84%B0%EC%97%90-%EC%95%A0%ED%94%8C%EB%A6%AC%EC%BC%80%EC%9D%B4%EC%85%98-%EB%B0%B0%ED%8F%AC%ED%95%98%EA%B8%B0-494f653341ab?source=rss----c7f2bfeb6b98---4) | NAVER Cloud / NAVER Cloud Platform Tech Blog | 292.86 | Kubernetes, observability, canary deployment |
| 4 | expected:2 | [쿠버네티스 오퍼레이터 적용하기](https://dev.gmarket.com/65) | Gmarket / Gmarket Tech Blog | 286.72 | Amazon S3, Kubernetes, Redis, search, incident response, migration |
| 5 | - | [Java Enum 활용기](https://techblog.woowahan.com/2527/) | Woowa Brothers / Woowa Tech Blog | 275.10 | JPA, Java, search |
| 6 | - | [Redis on Kubernetes 플랫폼을 구성해 나가기](https://tech.kakaopay.com/post/kakaopaysec-redis-on-kubernetes/) | Kakao Pay / Kakao Pay Tech Blog | 262.04 | Kubernetes, Redis |
| 7 | - | [막내 개발자의 Sell POD PD 생활](https://dev.gmarket.com/11) | Gmarket / Gmarket Tech Blog | 261.22 | Apache Kafka, Elasticsearch, JPA, Java, Kubernetes, Spring Boot |
| 8 | - | [쿠버네티스를 이용해 테스팅 환경 구현해보기](https://techblog.woowahan.com/2562/) | Woowa Brothers / Woowa Tech Blog | 253.24 | Amazon EC2, Amazon S3, Amazon VPC, JVM, Java, Kubernetes |
| 9 | - | [테라폼을 통해 Ncloud Kubernetes Service 클러스터 구축하기](https://medium.com/naver-cloud-platform/cbe27e197a97?source=rss----c7f2bfeb6b98---4) | NAVER Cloud / NAVER Cloud Platform Tech Blog | 249.26 | AWS IAM, Amazon VPC, Kubernetes |
| 10 | - | [AI-powered event response for Amazon EKS](https://aws.amazon.com/blogs/architecture/ai-powered-event-response-for-amazon-eks/) | AWS / AWS Architecture Blog | 246.51 | AWS CDK, AWS CloudFormation, AWS IAM, Amazon CloudWatch, Amazon EKS, Java |

#### Top Result Details

##### 1. 쿠버네티스 오퍼레이터를 Java로 개발해보기

- match: expected relevance 3
- source: Gmarket / Gmarket Tech Blog
- url: https://dev.gmarket.com/112
- technologies: Java, Kubernetes, Spring Boot
- problem keywords: -
- case summary: Gmarket은 Java Operator SDK와 fabric8 Kubernetes Client를 활용해 Java 기반 쿠버네티스 오퍼레이터를 개발하는 과정을 소개하며, Spring Boot 환경에서 CRD, Reconciler, Dependent Resource를 구현하는 방법을 상세히 다룹니다.
- problem: 국내에서 Golang보다 Java 수요가 높아 Java 환경에서 쿠버네티스 오퍼레이터를 개발하는 방법과 아키텍처를 이해하고자 하는 상황.
- solution: Java Operator SDK를 기반으로 fabric8 Kubernetes Client를 활용해 Spring Boot 프로젝트 내에서 CRD Spec/Status, Primary Resource, Dependent Resources(Deployment, Service, Ingress) 및 Reconciler를 구현하고, Operator를 구성하여 쿠버네티스 클러스터에 배포 및 테스트하는 방법을 적용.

Highlights:

- title: **쿠버네티스** 오퍼레이터를 Java로 개발해보기
- caseSummary: Gmarket은 **Java** Operator SDK와 fabric8 **Kubernetes** Client를 활용해 **Java** 기반 **쿠버네티스** 오퍼레이터를 개발하는 과정을 소개하며, Spring
- caseProblem: 국내에서 Golang보다 **Java** 수요가 높아 **Java** 환경에서 **쿠버네티스** 오퍼레이터를 개발하는 방법과 아키텍처를 이해하고자 하는 상황.
- caseSolution: **Java** Operator SDK를 기반으로 fabric8 **Kubernetes** Client를 활용해 Spring Boot 프로젝트 내에서 CRD Spec/Status, Primary
- caseSolution: Resource, Dependent Resources(Deployment, Service, Ingress) 및 Reconciler를 구현하고, Operator를 구성하여 **쿠버네티스**
- summary: 이전 포스트: **쿠버네티스** 오퍼레이터를 Golang으로 개발해보기 안녕하세요.Cloud Strategy팀 박규민입니다.

##### 2. 쿠버네티스 오퍼레이터를 Golang으로 개발해보기

- match: expected relevance 2
- source: Gmarket / Gmarket Tech Blog
- url: https://dev.gmarket.com/102
- technologies: Java, Kubernetes, Spring Boot
- problem keywords: -
- case summary: Gmarket은 Golang 기반 Operator SDK를 활용해 쿠버네티스 오퍼레이터를 직접 개발하고, 로컬 kind 클러스터에 배포하여 Spring Boot 애플리케이션을 커스텀 리소스로 관리하는 사례를 소개한다.
- problem: 쿠버네티스에서 커스텀 리소스를 통해 복잡한 애플리케이션 배포 및 관리를 자동화하고자 하는 상황에서, 오퍼레이터 개발과 배포 방법에 대한 실무적 이해가 필요했다.
- solution: Golang Operator SDK와 Kubebuilder를 사용해 Petclinic이라는 커스텀 리소스 정의(CRD)와 컨트롤러를 생성하고, Deployment, Service, Ingress 리소스를 자동으로 생성·관리하는 오퍼레이터를 구현했다. 로컬 kind 클러스터에 배포하여 실제 동작을 검증했다.

Highlights:

- title: **쿠버네티스** 오퍼레이터를 Golang으로 개발해보기
- caseSummary: Gmarket은 Golang 기반 Operator SDK를 활용해 **쿠버네티스** 오퍼레이터를 직접 개발하고, 로컬 kind 클러스터에 배포하여 Spring Boot 애플리케이션을 커스텀
- caseProblem: 쿠버네티스에서 커스텀 리소스를 통해 복잡한 애플리케이션 배포 및 관리를 자동화하고자 하는 상황에서, **오퍼레이터** 개발과 배포 방법에 대한 실무적 이해가 필요했다.
- summary: 이번 포스트는 **쿠버네티스** 오퍼레이터를 직접 구현해 보고, 개발한 오퍼레이터를 로컬 **쿠버네티스** 클러스터에 적용하는 과정까지 설명드리려고 합니다.
- summary: 예전에 지형님이 소개했었던 **쿠버네티스** **오퍼레이터** 적용하기를 본 독자들이 있을 겁니다.
- content: 이번 포스트는 **쿠버네티스** 오퍼레이터를 직접 구현해 보고, 개발한 오퍼레이터를 로컬 **쿠버네티스** 클러스터에 적용하는 과정까지 설명드리려고 합니다. 예전에 지형님이 소개했었던 **쿠버네티스** **오퍼레이터** 적용하기 를 본 독자들이 있을 겁니다.

##### 3. Kubernetes 클러스터에 애플리케이션 배포하기

- match: not expected
- source: NAVER Cloud / NAVER Cloud Platform Tech Blog
- url: https://medium.com/naver-cloud-platform/kubernetes-%ED%81%B4%EB%9F%AC%EC%8A%A4%ED%84%B0%EC%97%90-%EC%95%A0%ED%94%8C%EB%A6%AC%EC%BC%80%EC%9D%B4%EC%85%98-%EB%B0%B0%ED%8F%AC%ED%95%98%EA%B8%B0-494f653341ab?source=rss----c7f2bfeb6b98---4
- technologies: Kubernetes
- problem keywords: observability
- case summary: 네이버 클라우드 플랫폼의 Developer Tools를 활용해 Kubernetes 클러스터에 애플리케이션을 빌드, 배포, 자동화하는 DevOps 실습 사례를 다룹니다.
- problem: DevOps 환경 구축 시 소스 코드 관리, 빌드, 컨테이너 이미지 생성, Kubernetes 클러스터 배포 및 자동화 과정의 복잡성으로 인해 효율적인 개발 및 운영이 어려움.
- solution: SourceCommit, SourceBuild, SourceDeploy, SourcePipeline 4가지 Developer Tools를 연계하여 소스 코드 복사 및 관리, 도커 이미지 빌드, Kubernetes 클러스터에 롤링 업데이트 배포, CI/CD 자동화 파이프라인 구축을 통해 DevOps 전 과정을 자동화하고 안정적으로 운영함.

Highlights:

- title: **Kubernetes** 클러스터에 애플리케이션 배포하기
- caseSummary: 네이버 클라우드 플랫폼의 Developer Tools를 활용해 **Kubernetes** 클러스터에 애플리케이션을 빌드, 배포, 자동화하는 DevOps 실습 사례를 다룹니다.
- caseProblem: DevOps 환경 구축 시 소스 코드 관리, 빌드, 컨테이너 이미지 생성, **Kubernetes** 클러스터 배포 및 자동화 과정의 복잡성으로 인해 효율적인 개발 및 운영이 어려움.
- caseSolution: , SourceBuild, SourceDeploy, SourcePipeline 4가지 Developer Tools를 연계하여 소스 코드 복사 및 관리, 도커 이미지 빌드, **Kubernetes**
- summary: **Kubernetes** 클러스터에 애플리케이션 배포하기 — 네이버 클라우드 플랫폼 Developer Tools (개발자 도구) 활용 실습 DevOps의 중요도가 높아지면서 네이버 클라우드
- summary: 이용해 네이버 클라우드 플랫폼의 **Kubernetes** Service 클러스터에 배포할 수 있습니다.


### ko-tech-document-parse - `문서 파싱 Document Parse`

- category: technology
- intent: Document Parse, Document AI, 문서 파싱 기술을 실제 업무 자동화에 적용한 사례를 찾는다.
- total results: 304
- precision@5: 0.600
- recall@10: 1.000
- mrr: 1.000
- ndcg@10: 0.974

#### Expected URLs

- relevance 3: [Document Parse Enhanced \| 복잡한 문서를 실제 업무에 바로 활용하는 새로운 문서 파싱 방식](https://www.upstage.ai/blog/ko/document-parse-enhanced)
- relevance 3: [복잡한 문서를 지능형 데이터로, 강력한 문서 파싱 기술 - 업스테이지 도큐먼트 파스(Document Parse)](https://www.upstage.ai/blog/ko/introduce-upstage-document-parse)
- relevance 2: [Document AI로 문서 검토 한방에 끝내기](https://tech.kakaopay.com/post/ifkakao2024-document-ai/)

#### Top Results

| Rank | Match | Title | Source | Score | Keywords |
|---:|---|---|---|---:|---|
| 1 | expected:3 | [Document Parse Enhanced \| 복잡한 문서를 실제 업무에 바로 활용하는 새로운 문서 파싱 방식](https://www.upstage.ai/blog/ko/document-parse-enhanced) | Upstage / Upstage Blog | 354.20 | LLM, search, performance optimization |
| 2 | expected:3 | [복잡한 문서를 지능형 데이터로, 강력한 문서 파싱 기술 - 업스테이지 도큐먼트 파스(Document Parse)](https://www.upstage.ai/blog/ko/introduce-upstage-document-parse) | Upstage / Upstage Blog | 348.77 | LLM, search |
| 3 | - | [https://www.upstage.ai/blog/ko/langchain-llamaindex-latest-updates](https://www.upstage.ai/blog/ko/langchain-llamaindex-latest-updates) | Upstage / Upstage Blog | 107.57 | LLM |
| 4 | - | [전처리가 AI 에이전트 성공률을 좌우한다 \| 광고심의 자동화 사례](https://www.upstage.ai/blog/ko/ai-agent-preprocessing-pipeline-success) | Upstage / Upstage Blog | 56.77 | search |
| 5 | expected:2 | [Document AI로 문서 검토 한방에 끝내기](https://tech.kakaopay.com/post/ifkakao2024-document-ai/) | Kakao Pay / Kakao Pay Tech Blog | 50.95 |  |
| 6 | - | [AI 프로젝트 하는데 Document Parse를 안 쓴다고?! 정확하고 효율적인 데이터 전처리 및 자산화를 위한 필수 솔루션!](https://www.upstage.ai/blog/ko/introduction-upstage-document-parse2) | Upstage / Upstage Blog | 49.11 | LLM, search |
| 7 | - | [Layout Analyzer를 소개합니다.](https://www.upstage.ai/blog/ko/introducing-layout-analysis) | Upstage / Upstage Blog | 47.14 | LLM |
| 8 | - | [Orchestrating large-scale document processing with AWS Step Functions and Amazon Bedrock batch inference](https://aws.amazon.com/blogs/compute/orchestrating-large-scale-document-processing-with-aws-step-functions-and-amazon-bedrock-batch-inference/) | AWS / AWS Compute Blog | 46.77 | AWS CDK, AWS CloudFormation, AWS IAM, AWS Lambda, Amazon DynamoDB, Amazon EventBridge |
| 9 | - | [Securing client confidentiality at scale: Automated data discovery and governed analytics for legal workloads](https://aws.amazon.com/blogs/big-data/securing-client-confidentiality-at-scale-automated-data-discovery-and-governed-analytics-for-legal-workloads/) | AWS / AWS Big Data Blog | 45.37 | AWS Glue, AWS IAM, AWS Lambda, Amazon EventBridge, Amazon S3, search |
| 10 | - | [https://www.upstage.ai/blog/ko/upstage-console-faq-series-1](https://www.upstage.ai/blog/ko/upstage-console-faq-series-1) | Upstage / Upstage Blog | 45.33 |  |

#### Top Result Details

##### 1. Document Parse Enhanced | 복잡한 문서를 실제 업무에 바로 활용하는 새로운 문서 파싱 방식

- match: expected relevance 3
- source: Upstage / Upstage Blog
- url: https://www.upstage.ai/blog/ko/document-parse-enhanced
- technologies: LLM, search
- problem keywords: performance optimization
- case summary: 업스테이지의 Document Parse Enhanced는 복잡한 시각 요소가 포함된 문서를 안정적으로 구조화하여 금융, 제조, 공공 등 엔터프라이즈 환경에서 대량 문서 처리와 업무 자동화를 지원한다.
- problem: 기존 텍스트 중심 문서 파싱 방식은 선이 없는 테이블, 멀티페이지 표, 차트, 도표, 체크박스 등 시각적 복잡성이 높은 문서에서 정확한 구조 인식과 일관된 결과를 제공하지 못함.
- solution: 높은 OCR 정확도와 비주얼 그라운딩에 Vision Language Model을 결합한 확장 모드(Enhanced mode)를 도입해 복잡한 테이블 구조, 멀티페이지 병합, 차트 및 도표의 정형화와 자연어 설명 생성, 체크박스 인식을 개선하여 기존 API 변경 없이 업무 흐름에 바로 적용 가능하도록 설계함.

Highlights:

- title: **Document** **Parse** Enhanced | 복잡한 문서를 실제 업무에 바로 활용하는 새로운 **문서** **파싱** 방식
- caseSummary: 업스테이지의 **Document** **Parse** Enhanced는 복잡한 시각 요소가 포함된 문서를 안정적으로 구조화하여 금융, 제조, 공공 등 엔터프라이즈 환경에서 대량 **문서** 처리와 업무
- caseProblem: 기존 텍스트 중심 **문서** **파싱** 방식은 선이 없는 테이블, 멀티페이지 표, 차트, 도표, 체크박스 등 시각적 복잡성이 높은 문서에서 정확한 구조 인식과 일관된 결과를 제공하지 못함.
- summary: **Document** **Parse** Enhanced는 표, 차트, 도표, 체크박스 등 시각적으로 복잡한 문서를 정확하게 구조화해 실제 업무 워크플로우에 바로 활용할 수 있는 업스테이지의 **문서**
- summary: **파싱** 확장 모드입니다.
- content: **Document** **Parse** Enhanced는 어떻게 동작하나요 **Document** **Parse** Enhanced는 **Document** **Parse가** 이미 갖추고 있는 두 가지 핵심 강점, 즉 높은 OCR 정확도 와 안정적인 비주얼 그라운딩 을 기반으로 합니다.

##### 2. 복잡한 문서를 지능형 데이터로, 강력한 문서 파싱 기술 - 업스테이지 도큐먼트 파스(Document Parse)

- match: expected relevance 3
- source: Upstage / Upstage Blog
- url: https://www.upstage.ai/blog/ko/introduce-upstage-document-parse
- technologies: LLM, search
- problem keywords: -
- case summary: 업스테이지 도큐먼트 파스는 복잡한 문서 내 텍스트, 표, 이미지 등의 데이터를 자동으로 고속·고정확도로 추출해 기업의 디지털 전환과 AI 활용을 지원하는 문서 파싱 솔루션이다.
- problem: 기업들은 세로 긴 이미지, 중첩 표, 다중 페이지 표 통합, 이미지 내 캡션 추출 등 복잡한 문서 처리 문제로 업무 효율성과 생산성 저하를 겪고 있다.
- solution: 업스테이지 도큐먼트 파스는 다양한 문서 형식에서 텍스트와 구조를 정확히 분석해 HTML 등 구조화된 데이터로 변환하며, 대용량 문서도 1분 내 처리하는 고속·고정확도 파싱 기술을 제공한다. 또한 LLM과 RAG 기반 AI 시스템에 즉시 적용 가능해 응답 정확도를 높인다.

Highlights:

- title: 복잡한 문서를 지능형 데이터로, 강력한 **문서** **파싱** 기술 - 업스테이지 도큐먼트 파스(**Document** **Parse**)
- caseSummary: 업스테이지 도큐먼트 파스는 복잡한 **문서** 내 텍스트, 표, 이미지 등의 데이터를 자동으로 고속·고정확도로 추출해 기업의 디지털 전환과 AI 활용을 지원하는 **문서** **파싱** 솔루션이다.
- caseProblem: 기업들은 세로 긴 이미지, 중첩 표, 다중 페이지 표 통합, 이미지 내 캡션 추출 등 복잡한 **문서** 처리 문제로 업무 효율성과 생산성 저하를 겪고 있다.
- caseSolution: 업스테이지 도큐먼트 파스는 다양한 **문서** 형식에서 텍스트와 구조를 정확히 분석해 HTML 등 구조화된 데이터로 변환하며, 대용량 문서도 1분 내 처리하는 고속·고정확도 **파싱** 기술을 제공한다
- content: 복잡한 문서를 지능형 데이터로, 강력한 **문서** **파싱** 기술 - 업스테이지 도큐먼트 파스(**Document** **Parse**) 2025년은 AI가 우리의 일상과 업무에서 핵심 기술로 자리 잡는 해가 될 전망입니다.
- content: 텍스트, 표, 이미지까지 복잡한 **문서** 속 데이터를 자동으로 추출하는 도큐먼트 파스 (**Document** **Parse**) **파싱**(Parsing)은 컴퓨터 과학 및 프로그래밍에서 특정 형식으로 구성된 데이터를 분석하고 그 의미를 이해하는 과정으로 해석할 수 있습니다.

##### 3. https://www.upstage.ai/blog/ko/langchain-llamaindex-latest-updates

- match: not expected
- source: Upstage / Upstage Blog
- url: https://www.upstage.ai/blog/ko/langchain-llamaindex-latest-updates
- technologies: LLM
- problem keywords: -
- case summary: 업스테이지는 LangChain과 LlamaIndex 통합을 통해 AI 기반 문서 정보 추출과 대화형 LLM 활용을 개선하는 업데이트를 제공했다. 이를 통해 비정형 문서에서 핵심 정보를 추출하고, 다양한 파라미터 조절로 생성 모델의 응답 품질과 형식을 제어할 수 있다.
- problem: 비정형 문서에서 핵심 정보를 효과적으로 추출하고, LLM 기반 대화 시스템에서 출력의 무작위성, 반복성, 응답 형식 등을 세밀하게 제어하는 기술적 요구가 있었다.
- solution: LangChain과 LlamaIndex에 업스테이지의 Universal 및 Prebuilt Information Extraction 기능을 통합하여, 추가 학습 없이 다양한 문서에서 핵심 정보를 추출할 수 있게 했고, LLM 대화에서 temperature, top_p, frequency_penalty, presence_penalty, response_format 등의 파라미터를 지원하여 출력 품질과 형식을 맞춤 설정할 수 있도록 했다.

Highlights:

- caseSummary: 업스테이지는 LangChain과 LlamaIndex 통합을 통해 AI 기반 **문서** 정보 추출과 대화형 LLM 활용을 개선하는 업데이트를 제공했다.
- content: **Document** **Parse** 에서 chart_recognition 파라미터를 사용하실 수 있습니다. chart_recognition 파라미터는 차트 인식 사용 여부를 나타내는 boolean 값입니다. true로 설정할 시 차트 인식률이 올라갑니다. Default 값은 true입니다.
- content: Information Extraction 이란 단순히 문서를 디지털화하는 것을 넘어서, 비정형 **문서**(unstructured **documents**)에서 핵심 정보를 식별하고 추출하여, 그 중요한 정보들을 데이터베이스와 같은 정형화된 형식(structured formats)으로 저장하는 과정을


### ko-architecture-data-pipeline - `데이터 파이프라인`

- category: architecture
- intent: 한글 검색어로 데이터 파이프라인 설계, 분석 데이터 배포, 기본 원칙 사례를 찾는다.
- total results: 722
- precision@5: 0.600
- recall@10: 0.750
- mrr: 1.000
- ndcg@10: 0.834

#### Expected URLs

- relevance 3: [데이터 분석가가 직접 정의, 배포, 관리하는 뱅크샐러드 데이터 파이프라인](https://blog.banksalad.com/tech/datapipe/)
- relevance 3: [데이터 파이프라인 기본 원리와 원칙은 시간이 지나도 유효해야 한다(1/2)](https://netmarble.engineering/data-pipeline-design-principles-a/)
- relevance 3: [데이터 파이프라인 기본 원리와 원칙은 시간이 지나도 유효해야 한다(2/2)](https://netmarble.engineering/data-pipeline-design-principles-b/)
- relevance 2: [분석 데이터를 프로덕션에서 쉽게 사용할 수 없을까?](https://blog.banksalad.com/tech/dataserving/)

#### Top Results

| Rank | Match | Title | Source | Score | Keywords |
|---:|---|---|---|---:|---|
| 1 | expected:3 | [데이터 분석가가 직접 정의, 배포, 관리하는 뱅크샐러드 데이터 파이프라인](https://blog.banksalad.com/tech/datapipe/) | Banksalad / Banksalad Blog | 440.86 | streaming data pipeline |
| 2 | - | [[여의도 43층 사람들] Data Engineer 에게 무엇이든 물어보세요!](https://blog.banksalad.com/pnc/team-interview-de/) | Banksalad / Banksalad Blog | 377.14 |  |
| 3 | expected:3 | [데이터 파이프라인 기본 원리와 원칙은 시간이 지나도 유효해야 한다(2/2)](https://netmarble.engineering/data-pipeline-design-principles-b/) | Netmarble / Netmarble Tech Blog | 373.66 | streaming data pipeline |
| 4 | expected:3 | [데이터 파이프라인 기본 원리와 원칙은 시간이 지나도 유효해야 한다(1/2)](https://netmarble.engineering/data-pipeline-design-principles-a/) | Netmarble / Netmarble Tech Blog | 373.66 | streaming data pipeline |
| 5 | - | [데브시스터즈 엔지니어링 데이 - Data 돌아보기](https://tech.devsisters.com/posts/2025-engineering-day-data) | Devsisters / Devsisters Tech Blog | 338.58 | LLM, incident response, log platform, streaming data pipeline |
| 6 | - | [Building unified data pipelines with Apache Iceberg and Apache Flink](https://aws.amazon.com/blogs/big-data/building-unified-data-pipelines-with-apache-iceberg-and-apache-flink/) | AWS / AWS Big Data Blog | 326.63 | AWS Glue, AWS IAM, Amazon CloudWatch, Amazon EC2, Amazon S3, Amazon VPC |
| 7 | - | [게임별 다양한 지표 추출을 위한 데이터 적재 파이프라인, Bigwave](https://netmarble.engineering/data-pipeline-bigwave/) | Netmarble / Netmarble Tech Blog | 322.28 |  |
| 8 | - | [Getting started with Change Data Capture in Amazon Aurora DSQL](https://aws.amazon.com/blogs/database/getting-started-with-change-data-capture-in-amazon-aurora-dsql/) | AWS / AWS Database Blog | 306.49 | AWS IAM, AWS Lambda, Amazon Aurora, Apache Kafka, React, search |
| 9 | - | [[인턴십] 2026 NAVER AI CHALLENGE를 소개합니다.](https://d2.naver.com/news/7477295) | NAVER / NAVER D2 | 286.93 | search, streaming data pipeline |
| 10 | - | [LINE 서비스의 대규모 광고 데이터를 처리하기 위한 Spark on Kubernetes 적용기](https://techblog.lycorp.co.jp/ko/processing-large-scale-data-with-spark-on-kubernetes) | LY Corporation / LY Corporation Tech Blog | 285.93 | Kubernetes, streaming data pipeline |

#### Top Result Details

##### 1. 데이터 분석가가 직접 정의, 배포, 관리하는 뱅크샐러드 데이터 파이프라인

- match: expected relevance 3
- source: Banksalad / Banksalad Blog
- url: https://blog.banksalad.com/tech/datapipe/
- technologies: -
- problem keywords: -
- case summary: 뱅크샐러드는 데이터 분석가가 직접 데이터 파이프라인을 정의, 배포, 관리할 수 있도록 하여 데이터 처리의 효율성과 자율성을 높였다.
- problem: 데이터 분석가가 데이터 파이프라인 개발과 운영에 직접 참여하기 어려워 데이터 처리 속도와 유연성이 떨어지는 문제.
- solution: 분석가가 직접 파이프라인을 설계하고 배포할 수 있는 플랫폼을 구축해 데이터 파이프라인의 자율적 관리와 신속한 운영을 가능하게 함.

Highlights:

- title: **데이터** 분석가가 직접 정의, 배포, 관리하는 뱅크샐러드 **데이터 파이프라인**
- caseSummary: 뱅크샐러드는 **데이터** 분석가가 직접 **데이터** 파이프라인을 정의, 배포, 관리할 수 있도록 하여 **데이터** 처리의 효율성과 자율성을 높였다.
- caseProblem: **데이터** 분석가가 **데이터 파이프라인** 개발과 운영에 직접 참여하기 어려워 **데이터** 처리 속도와 유연성이 떨어지는 문제.
- caseSolution: 분석가가 직접 파이프라인을 설계하고 배포할 수 있는 플랫폼을 구축해 **데이터** 파이프라인의 자율적 관리와 신속한 운영을 가능하게 함.

##### 2. [여의도 43층 사람들] Data Engineer 에게 무엇이든 물어보세요!

- match: not expected
- source: Banksalad / Banksalad Blog
- url: https://blog.banksalad.com/pnc/team-interview-de/
- technologies: -
- problem keywords: -
- case summary: 뱅크샐러드의 Data Engineer가 데이터 파이프라인 구축과 운영에서 직면하는 문제와 해결 방안을 공유한다.
- problem: 대규모 금융 데이터를 효율적으로 수집, 처리, 분석하기 위한 안정적이고 확장 가능한 데이터 인프라 구축의 어려움.
- solution: 클라우드 기반 데이터 플랫폼과 자동화된 ETL 파이프라인을 활용하여 데이터 품질을 확보하고, 실시간 데이터 처리 및 모니터링 체계를 도입함.

Highlights:

- title: [여의도 43층 사람들] **Data** Engineer 에게 무엇이든 물어보세요!
- caseSummary: 뱅크샐러드의 **Data** Engineer가 **데이터 파이프라인** 구축과 운영에서 직면하는 문제와 해결 방안을 공유한다.
- caseProblem: 대규모 금융 데이터를 효율적으로 수집, 처리, 분석하기 위한 안정적이고 확장 가능한 **데이터** 인프라 구축의 어려움.
- caseSolution: 클라우드 기반 **데이터** 플랫폼과 자동화된 ETL 파이프라인을 활용하여 **데이터** 품질을 확보하고, 실시간 **데이터** 처리 및 모니터링 체계를 도입함.
- summary: 뱅크샐러드 **Data** Engineer는 무슨 일을 하나요? 뱅크샐러드 **Data** Engineer…

##### 3. 데이터 파이프라인 기본 원리와 원칙은 시간이 지나도 유효해야 한다(2/2)

- match: expected relevance 3
- source: Netmarble / Netmarble Tech Blog
- url: https://netmarble.engineering/data-pipeline-design-principles-b/
- technologies: -
- problem keywords: -
- case summary: 넷마블은 데이터 파이프라인의 복잡도를 관리하기 위해 소스 타입, 데이터 형태, 가공 방식, 전달 채널, 운영 도구 등 다양한 요소를 체계적으로 분석하고 공통 특성을 도출하는 원칙을 적용했다.
- problem: 데이터 파이프라인 시스템이 다양한 소스와 데이터 형태, 가공 방식 등으로 인해 복잡도가 증가하여 관리와 확장이 어려운 상황이었다.
- solution: 각 요소별 다양성을 면밀히 검토하고, 개별 케이스의 공통 특성과 의미를 추출하는 기본 원리와 원칙을 수립하여 시스템 복잡도를 효과적으로 관리했다.

Highlights:

- title: **데이터 파이프라인** 기본 원리와 원칙은 시간이 지나도 유효해야 한다(2/2)
- caseSummary: 넷마블은 **데이터** 파이프라인의 복잡도를 관리하기 위해 소스 타입, **데이터** 형태, 가공 방식, 전달 채널, 운영 도구 등 다양한 요소를 체계적으로 분석하고 공통 특성을 도출하는 원칙을
- caseProblem: **데이터 파이프라인** 시스템이 다양한 소스와 **데이터** 형태, 가공 방식 등으로 인해 복잡도가 증가하여 관리와 확장이 어려운 상황이었다.
- summary: **데이터 파이프라인** 시스템 복잡도를 관리하기 위해 아래와 같은 요소를 고려해야 합니다.
- summary: 소스 타입, **데이터** 형태, 가공 방식, 전달 채널, 운영 도구 등 각 고려 사항으로 언급한 다양성을 검토한 후에는 개별 케이스가 갖는 공통적인 특성이나 의미를 추출해야 합니다.


### ko-tech-aws-dms - `AWS DMS RDS 통합`

- category: technology
- intent: AWS DMS와 RDS를 이용한 데이터베이스 통합, 마이그레이션, 운영 경험을 찾는다.
- total results: 48
- precision@5: 0.400
- recall@10: 1.000
- mrr: 1.000
- ndcg@10: 0.974

#### Expected URLs

- relevance 3: [사용법과 함께 작성해본 좌충우돌 AWS DMS 사용기 - feat. RDS 통합 이야기](https://blog.banksalad.com/tech/dms/)
- relevance 1: [[다시보기] 2월 우아한테크세미나: 우아한형제들의 RDS Aurora Graviton2 성능 이슈 해결 사례와 RDS를 모니터링하는 방법](https://techblog.woowahan.com/10645/)

#### Top Results

| Rank | Match | Title | Source | Score | Keywords |
|---:|---|---|---|---:|---|
| 1 | expected:3 | [사용법과 함께 작성해본 좌충우돌 AWS DMS 사용기 - feat. RDS 통합 이야기](https://blog.banksalad.com/tech/dms/) | Banksalad / Banksalad Blog | 454.55 | Amazon RDS |
| 2 | - | [Connect to Amazon RDS for Db2 from your laptop](https://aws.amazon.com/blogs/database/connect-to-amazon-rds-for-db2-from-your-laptop/) | AWS / AWS Database Blog | 274.49 | AWS IAM, Amazon EC2, Amazon RDS, Amazon S3, Amazon VPC |
| 3 | - | [Upgrade strategies for Amazon RDS for MySQL 8.0 to 8.4](https://aws.amazon.com/blogs/database/upgrade-strategies-for-amazon-rds-for-mysql-8-0-to-8-4/) | AWS / AWS Database Blog | 262.97 | Amazon Aurora, Amazon CloudWatch, Amazon RDS, Amazon S3, migration, observability |
| 4 | expected:1 | [[다시보기] 2월 우아한테크세미나: 우아한형제들의 RDS Aurora Graviton2 성능 이슈 해결 사례와 RDS를 모니터링하는 방법](https://techblog.woowahan.com/10645/) | Woowa Brothers / Woowa Tech Blog | 255.21 | Amazon Aurora, Amazon RDS, observability, performance optimization, streaming data pipeline |
| 5 | - | [Migrating Amazon RDS for PostgreSQL to Amazon Aurora using seeded logical replication](https://aws.amazon.com/blogs/database/migrating-amazon-rds-for-postgresql-to-amazon-aurora-using-seeded-logical-replication/) | AWS / AWS Database Blog | 251.01 | AWS IAM, Amazon Aurora, Amazon CloudWatch, Amazon RDS, Amazon VPC, high availability |
| 6 | - | [Best practices for upgrading Amazon RDS for MySQL 8.0 to 8.4 with prechecks, Blue/Green, and rollback](https://aws.amazon.com/blogs/database/best-practices-for-upgrading-amazon-rds-for-mysql-8-0-to-8-4-with-prechecks-blue-green-and-rollback/) | AWS / AWS Database Blog | 228.87 | AWS IAM, Amazon Aurora, Amazon EC2, Amazon RDS, Amazon VPC, Java |
| 7 | - | [Troubleshoot Amazon RDS for Oracle to Amazon Redshift DMS migrations with AWS DevOps Agent](https://aws.amazon.com/blogs/database/troubleshoot-amazon-rds-for-oracle-to-amazon-redshift-dms-migrations-with-aws-devops-agent/) | AWS / AWS Database Blog | 226.30 | AWS IAM, AWS Lambda, Amazon CloudWatch, Amazon EventBridge, Amazon RDS, incident response |
| 8 | - | [실험과 기능플래그를 위한 실험플랫폼 구축하기](https://techblog.woowahan.com/9935/) | Woowa Brothers / Woowa Tech Blog | 191.15 | AWS Glue, Amazon RDS, JVM, Java, Kotlin, Redis |
| 9 | - | [쿠키런: 킹덤 데이터베이스 스토리지 레이어 복원기](https://tech.devsisters.com/posts/crk-launch-storage-postmortem) | Devsisters / Devsisters Tech Blog | 191.15 | Amazon EC2, Amazon RDS, incident response, observability, log platform |
| 10 | - | [PostgreSQL Vacuum에 대한 거의 모든 것](https://techblog.woowahan.com/9478/) | Woowa Brothers / Woowa Tech Blog | 191.15 | Amazon Aurora, Amazon RDS, observability |

#### Top Result Details

##### 1. 사용법과 함께 작성해본 좌충우돌 AWS DMS 사용기 - feat. RDS 통합 이야기

- match: expected relevance 3
- source: Banksalad / Banksalad Blog
- url: https://blog.banksalad.com/tech/dms/
- technologies: Amazon RDS
- problem keywords: -
- case summary: AWS DMS를 활용해 RDS 통합 과정에서 발생한 문제와 해결 경험을 공유하며, AWS DMS의 기본 사용법과 실무 적용 방안을 소개한다.
- problem: 기존 데이터베이스를 AWS RDS로 통합하는 과정에서 데이터 마이그레이션과 동기화 문제를 해결해야 하는 상황이었다.
- solution: AWS DMS(Data Migration Service)를 사용해 데이터 마이그레이션을 자동화하고, 실시간 데이터 동기화를 구현하여 안정적인 RDS 통합 환경을 구축했다.

Highlights:

- title: 사용법과 함께 작성해본 좌충우돌 **AWS** **DMS** 사용기 - feat. **RDS** **통합** 이야기
- caseSolution: **AWS** **DMS**(Data Migration Service)를 사용해 데이터 마이그레이션을 자동화하고, 실시간 데이터 동기화를 구현하여 안정적인 **RDS** **통합** 환경을 구축했다.

##### 2. Connect to Amazon RDS for Db2 from your laptop

- match: not expected
- source: AWS / AWS Database Blog
- url: https://aws.amazon.com/blogs/database/connect-to-amazon-rds-for-db2-from-your-laptop/
- technologies: AWS IAM, Amazon EC2, Amazon RDS, Amazon S3, Amazon VPC
- problem keywords: -
- case summary: AWS Systems Manager Session Manager를 활용해 사설 서브넷 내 Amazon RDS for Db2에 노트북에서 안전하게 접속하는 방법을 Terraform 기반 인프라 배포와 포트 포워딩 구성으로 구현한 사례입니다.
- problem: 사설 서브넷에 배포된 Amazon RDS for Db2 인스턴스에 인터넷 노출 없이 안전하고 관리 가능한 방식으로 로컬 노트북에서 접속하는 문제.
- solution: AWS SSM Session Manager를 이용해 EC2 배스천 호스트와의 암호화된 터널을 구축하고, Terraform으로 인프라를 자동화하며 포트 포워딩을 통해 로컬에서 RDS에 접속하는 방식을 적용함으로써 SSH 키 관리와 공개 IP 노출 없이 보안과 운영 편의성을 확보.

Highlights:

- title: Connect to **Amazon RDS** for Db2 from your laptop
- caseSummary: AWS Systems Manager Session Manager를 활용해 사설 서브넷 내 **Amazon RDS** for Db2에 노트북에서 안전하게 접속하는 방법을 Terraform 기반
- caseProblem: 사설 서브넷에 배포된 **Amazon RDS** for Db2 인스턴스에 인터넷 노출 없이 안전하고 관리 가능한 방식으로 로컬 노트북에서 접속하는 문제.
- summary: In this post, we demonstrate how to connect to **Amazon RDS** for Db2 from your laptop using AWS SSM, covering
- content: About the authors Vikram S Khatri Vikram is a Senior Engineer for **Amazon RDS** for Db2.
- content: He works with the **Amazon RDS** team, focusing on commercial database engines like Oracle and Db2.

##### 3. Upgrade strategies for Amazon RDS for MySQL 8.0 to 8.4

- match: not expected
- source: AWS / AWS Database Blog
- url: https://aws.amazon.com/blogs/database/upgrade-strategies-for-amazon-rds-for-mysql-8-0-to-8-4/
- technologies: Amazon Aurora, Amazon CloudWatch, Amazon RDS, Amazon S3
- problem keywords: migration, observability, performance optimization
- case summary: Amazon RDS for MySQL 8.0에서 8.4로의 주요 버전 업그레이드 시점에 맞춰, 지원 종료 일정, 확장 지원 비용, 업그레이드 방법과 사전 점검 및 롤백 전략을 포함한 최적의 업그레이드 전략을 제시한다.
- problem: MySQL 8.0의 표준 지원 종료에 따른 보안 및 기능 유지 필요성과, 주요 버전 업그레이드 시 발생할 수 있는 애플리케이션 호환성 문제 및 다운타임 우려가 존재한다.
- solution: AWS RDS의 사전 점검 자동화, Blue/Green 배포를 통한 무중단 업그레이드, 스냅샷 복원을 이용한 테스트 및 롤백 전략을 활용하여 안정적이고 유연한 업그레이드 수행 방안을 제공한다. 또한, 확장 지원 옵션으로 지원 기간 연장과 비용 예측을 가능하게 한다.

Highlights:

- title: Upgrade strategies for **Amazon RDS** for MySQL 8.0 to 8.4
- caseSummary: **Amazon RDS** for MySQL 8.0에서 8.4로의 주요 버전 업그레이드 시점에 맞춰, 지원 종료 일정, 확장 지원 비용, 업그레이드 방법과 사전 점검 및 롤백 전략을 포함한
- content: How **Amazon RDS** for MySQL performs a major version upgrade When a major version upgrade is invoked on the console or via the AWS CLI or **Amazon RDS** API, **Amazon RDS**
- content: She focuses on **Amazon RDS** and Amazon Aurora databases.
