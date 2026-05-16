from dataclasses import dataclass


@dataclass(frozen=True)
class SourceSeed:
    name: str
    slug: str
    company_name: str
    feed_url: str
    site_url: str
    description: str
    enabled: bool = True


AWS_SOURCES: tuple[SourceSeed, ...] = (
    SourceSeed(
        name="AWS Architecture Blog",
        slug="aws-architecture-blog",
        company_name="AWS",
        feed_url="https://aws.amazon.com/blogs/architecture/feed/",
        site_url="https://aws.amazon.com/blogs/architecture/",
        description="AWS architecture patterns and technical case studies.",
    ),
    SourceSeed(
        name="AWS Database Blog",
        slug="aws-database-blog",
        company_name="AWS",
        feed_url="https://aws.amazon.com/blogs/database/feed/",
        site_url="https://aws.amazon.com/blogs/database/",
        description="AWS database migration, operations, and optimization cases.",
    ),
    SourceSeed(
        name="AWS Compute Blog",
        slug="aws-compute-blog",
        company_name="AWS",
        feed_url="https://aws.amazon.com/blogs/compute/feed/",
        site_url="https://aws.amazon.com/blogs/compute/",
        description="AWS compute, serverless, and container workload cases.",
    ),
    SourceSeed(
        name="AWS Big Data Blog",
        slug="aws-big-data-blog",
        company_name="AWS",
        feed_url="https://aws.amazon.com/blogs/big-data/feed/",
        site_url="https://aws.amazon.com/blogs/big-data/",
        description="AWS analytics, streaming, and data pipeline cases.",
    ),
    SourceSeed(
        name="AWS DevOps Blog",
        slug="aws-devops-blog",
        company_name="AWS",
        feed_url="https://aws.amazon.com/blogs/devops/feed/",
        site_url="https://aws.amazon.com/blogs/devops/",
        description="AWS DevOps, CI/CD, IaC, and operational automation cases.",
    ),
)

