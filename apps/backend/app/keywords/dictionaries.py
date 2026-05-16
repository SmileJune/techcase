from dataclasses import dataclass


@dataclass(frozen=True)
class KeywordRule:
    keyword: str
    keyword_type: str
    aliases: tuple[str, ...]


KEYWORD_RULES = [
    KeywordRule("AWS Lambda", "aws_service", ("lambda", "aws lambda", "람다")),
    KeywordRule("Amazon DynamoDB", "aws_service", ("dynamodb", "amazon dynamodb", "다이나모db")),
    KeywordRule("Amazon EKS", "aws_service", ("eks", "amazon eks")),
    KeywordRule(
        "Amazon OpenSearch Service",
        "aws_service",
        ("opensearch", "amazon opensearch", "오픈서치"),
    ),
    KeywordRule("Amazon MSK", "aws_service", ("msk", "amazon msk")),
    KeywordRule("Amazon S3", "aws_service", ("s3", "amazon s3")),
    KeywordRule("AWS Glue", "aws_service", ("glue", "aws glue")),
    KeywordRule("Amazon Aurora", "aws_service", ("aurora", "amazon aurora", "오로라")),
    KeywordRule("Amazon RDS", "aws_service", ("rds", "amazon rds")),
    KeywordRule("Amazon ElastiCache", "aws_service", ("elasticache", "amazon elasticache")),
    KeywordRule("Amazon CloudWatch", "aws_service", ("cloudwatch", "amazon cloudwatch")),
    KeywordRule("Amazon EventBridge", "aws_service", ("eventbridge", "amazon eventbridge")),
    KeywordRule("AWS CloudFormation", "aws_service", ("cloudformation", "aws cloudformation")),
    KeywordRule("AWS CDK", "technology", ("cdk", "aws cdk")),
    KeywordRule("Apache Kafka", "technology", ("kafka", "apache kafka", "카프카")),
    KeywordRule("Apache Flink", "technology", ("flink", "apache flink", "플링크")),
    KeywordRule("Apache Iceberg", "technology", ("iceberg", "apache iceberg")),
    KeywordRule("OpenTelemetry", "technology", ("opentelemetry", "otel")),
    KeywordRule("Valkey", "technology", ("valkey",)),
    KeywordRule("Kubernetes", "technology", ("kubernetes", "k8s", "쿠버네티스")),
    KeywordRule(
        "serverless",
        "architecture",
        ("serverless", "serverless architecture", "serverless workloads", "서버리스"),
    ),
    KeywordRule(
        "streaming data pipeline",
        "architecture",
        (
            "streaming data pipeline",
            "streaming applications",
            "streaming cloudwatch metrics",
            "unified data pipelines",
            "real-time analytics",
            "real time analytics",
            "스트리밍",
            "데이터 파이프라인",
            "실시간 분석",
        ),
    ),
    KeywordRule(
        "Change Data Capture",
        "architecture",
        ("change data capture", "cdc", "logical replication", "변경 데이터 캡처"),
    ),
    KeywordRule(
        "cross-Region resilience",
        "architecture",
        ("cross-region resilience", "cross-region", "cross region", "multi-region", "멀티 리전"),
    ),
    KeywordRule(
        "event response",
        "architecture",
        ("event response", "incident response", "autonomous incident response"),
    ),
    KeywordRule(
        "observability",
        "problem",
        ("observability", "monitoring", "metrics", "traces", "debugging", "관측성", "모니터링"),
    ),
    KeywordRule(
        "cost optimization",
        "problem",
        (
            "cost optimization",
            "cost",
            "costs",
            "hidden costs",
            "cut inter-az cost",
            "optimizes operations",
            "비용 최적화",
            "비용 절감",
        ),
    ),
    KeywordRule(
        "migration",
        "problem",
        ("migration", "migrating", "migrate", "upgrade", "upgrading", "마이그레이션", "이관"),
    ),
    KeywordRule(
        "incident response",
        "problem",
        ("incident response", "incident investigation", "sre", "devops agent", "장애 대응"),
    ),
    KeywordRule(
        "performance optimization",
        "problem",
        ("performance", "high-performance", "latency", "throughput", "benchmark", "성능 최적화"),
    ),
    KeywordRule(
        "high availability",
        "problem",
        ("high availability", "fault-tolerant", "resilience", "disaster recovery", "고가용성"),
    ),
]
