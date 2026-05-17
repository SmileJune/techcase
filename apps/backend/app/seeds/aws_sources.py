from dataclasses import dataclass


@dataclass(frozen=True)
class SourceSeed:
    name: str
    slug: str
    company_name: str
    feed_url: str | None
    site_url: str
    description: str
    collection_strategy: str = "rss"
    pagination_strategy: str = "none"
    content_strategy: str = "feed_only"
    language: str | None = None
    country: str | None = None
    trust_level: str = "official"
    enabled: bool = True


AWS_SOURCES: tuple[SourceSeed, ...] = (
    SourceSeed(
        name="AWS Architecture Blog",
        slug="aws-architecture-blog",
        company_name="AWS",
        feed_url="https://aws.amazon.com/blogs/architecture/feed/",
        site_url="https://aws.amazon.com/blogs/architecture/",
        description="AWS architecture patterns and technical case studies.",
        language="en",
        country="global",
    ),
    SourceSeed(
        name="AWS Database Blog",
        slug="aws-database-blog",
        company_name="AWS",
        feed_url="https://aws.amazon.com/blogs/database/feed/",
        site_url="https://aws.amazon.com/blogs/database/",
        description="AWS database migration, operations, and optimization cases.",
        language="en",
        country="global",
    ),
    SourceSeed(
        name="AWS Compute Blog",
        slug="aws-compute-blog",
        company_name="AWS",
        feed_url="https://aws.amazon.com/blogs/compute/feed/",
        site_url="https://aws.amazon.com/blogs/compute/",
        description="AWS compute, serverless, and container workload cases.",
        language="en",
        country="global",
    ),
    SourceSeed(
        name="AWS Big Data Blog",
        slug="aws-big-data-blog",
        company_name="AWS",
        feed_url="https://aws.amazon.com/blogs/big-data/feed/",
        site_url="https://aws.amazon.com/blogs/big-data/",
        description="AWS analytics, streaming, and data pipeline cases.",
        language="en",
        country="global",
    ),
    SourceSeed(
        name="AWS DevOps Blog",
        slug="aws-devops-blog",
        company_name="AWS",
        feed_url="https://aws.amazon.com/blogs/devops/feed/",
        site_url="https://aws.amazon.com/blogs/devops/",
        description="AWS DevOps, CI/CD, IaC, and operational automation cases.",
        language="en",
        country="global",
    ),
)

KOREAN_TECH_BLOG_SOURCES: tuple[SourceSeed, ...] = (
    SourceSeed(
        name="Toss Tech",
        slug="toss-tech",
        company_name="Toss",
        feed_url="https://toss.tech/rss.xml",
        site_url="https://toss.tech",
        description="Toss engineering stories and product technology cases.",
        language="ko",
        country="KR",
    ),
    SourceSeed(
        name="NAVER D2",
        slug="naver-d2",
        company_name="NAVER",
        feed_url="https://d2.naver.com/d2.atom",
        site_url="https://d2.naver.com",
        description="NAVER engineering, frontend, backend, AI, and platform technology cases.",
        language="ko",
        country="KR",
    ),
    SourceSeed(
        name="Kakao Tech",
        slug="kakao-tech",
        company_name="Kakao",
        feed_url="https://tech.kakao.com/feed/",
        site_url="https://tech.kakao.com",
        description="Kakao engineering, AI, frontend, backend, and service technology cases.",
        language="ko",
        country="KR",
    ),
    SourceSeed(
        name="Woowa Tech Blog",
        slug="woowa-tech-blog",
        company_name="Woowa Brothers",
        feed_url="https://techblog.woowahan.com/feed/",
        site_url="https://techblog.woowahan.com",
        description="Woowa Brothers engineering, product, data, AI, and platform technology cases.",
        pagination_strategy="wordpress_paged",
        language="ko",
        country="KR",
    ),
    SourceSeed(
        name="Daangn Tech Blog",
        slug="daangn-tech-blog",
        company_name="Daangn",
        feed_url="https://medium.com/feed/daangn",
        site_url="https://medium.com/daangn",
        description="Daangn engineering and product technology stories.",
        language="ko",
        country="KR",
    ),
    SourceSeed(
        name="LY Corporation Tech Blog",
        slug="ly-corporation-tech-blog",
        company_name="LY Corporation",
        feed_url="https://techblog.lycorp.co.jp/ko/feed/index.xml",
        site_url="https://techblog.lycorp.co.jp/ko",
        description="LY Corporation engineering, platform, frontend, backend, and AI cases.",
        language="ko",
        country="KR",
    ),
    SourceSeed(
        name="Kakao Pay Tech Blog",
        slug="kakaopay-tech-blog",
        company_name="Kakao Pay",
        feed_url="https://tech.kakaopay.com/rss.xml",
        site_url="https://tech.kakaopay.com",
        description="Kakao Pay engineering, fintech, data, platform, and reliability cases.",
        language="ko",
        country="KR",
    ),
    SourceSeed(
        name="SOCAR Tech Blog",
        slug="socar-tech-blog",
        company_name="SOCAR",
        feed_url="https://tech.socarcorp.kr/feed.xml",
        site_url="https://tech.socarcorp.kr",
        description="SOCAR mobility service engineering and data technology cases.",
        language="ko",
        country="KR",
    ),
    SourceSeed(
        name="Kurly Tech Blog",
        slug="kurly-tech-blog",
        company_name="Kurly",
        feed_url="https://helloworld.kurly.com/rss.xml",
        site_url="https://helloworld.kurly.com",
        description="Kurly commerce, logistics, data, backend, and platform engineering cases.",
        language="ko",
        country="KR",
    ),
    SourceSeed(
        name="GC Company Tech Blog",
        slug="gc-company-tech-blog",
        company_name="GC Company",
        feed_url="https://techblog.gccompany.co.kr/feed",
        site_url="https://techblog.gccompany.co.kr",
        description="GC Company engineering stories from the Yeogi Eottae service.",
        language="ko",
        country="KR",
    ),
    SourceSeed(
        name="YOGIYO Tech Blog",
        slug="yogiyo-tech-blog",
        company_name="YOGIYO",
        feed_url="https://techblog.yogiyo.co.kr/feed",
        site_url="https://techblog.yogiyo.co.kr",
        description="YOGIYO delivery platform engineering and product technology cases.",
        language="ko",
        country="KR",
    ),
    SourceSeed(
        name="MUSINSA Tech Blog",
        slug="musinsa-tech-blog",
        company_name="MUSINSA",
        feed_url="https://techblog.musinsa.com/feed",
        site_url="https://techblog.musinsa.com",
        description="MUSINSA fashion commerce, data, cloud, and engineering culture cases.",
        language="ko",
        country="KR",
    ),
    SourceSeed(
        name="29CM TEAM",
        slug="29cm-team",
        company_name="29CM",
        feed_url="https://medium.com/feed/29cm",
        site_url="https://medium.com/29cm",
        description="29CM product, engineering, data, and team stories.",
        language="ko",
        country="KR",
    ),
    SourceSeed(
        name="Devsisters Tech Blog",
        slug="devsisters-tech-blog",
        company_name="Devsisters",
        feed_url="https://tech.devsisters.com/rss.xml",
        site_url="https://tech.devsisters.com",
        description="Devsisters game, backend, data, platform, and engineering cases.",
        language="ko",
        country="KR",
    ),
    SourceSeed(
        name="NAVER Cloud Platform Tech Blog",
        slug="naver-cloud-platform-tech-blog",
        company_name="NAVER Cloud",
        feed_url="https://medium.com/feed/naver-cloud-platform",
        site_url="https://medium.com/naver-cloud-platform",
        description=(
            "NAVER Cloud Platform cloud, Kubernetes, DevOps, database, "
            "and infrastructure technology cases."
        ),
        language="ko",
        country="KR",
    ),
    SourceSeed(
        name="Zigbang Tech Blog",
        slug="zigbang-tech-blog",
        company_name="Zigbang",
        feed_url="https://medium.com/feed/zigbang",
        site_url="https://medium.com/zigbang",
        description=(
            "Zigbang real estate platform, backend, data, frontend, "
            "and product engineering cases."
        ),
        language="ko",
        country="KR",
    ),
    SourceSeed(
        name="Wantedlab Tech Blog",
        slug="wantedlab-tech-blog",
        company_name="Wantedlab",
        feed_url="https://medium.com/feed/wantedjobs",
        site_url="https://medium.com/wantedjobs",
        description=(
            "Wantedlab matching, recommendation, product engineering, backend, "
            "and data technology cases."
        ),
        language="ko",
        country="KR",
    ),
    SourceSeed(
        name="Coupang Engineering Blog",
        slug="coupang-engineering-blog",
        company_name="Coupang",
        feed_url="https://medium.com/feed/coupang-engineering",
        site_url="https://medium.com/coupang-engineering",
        description="Coupang commerce, logistics, backend, data, and platform engineering cases.",
        language="ko",
        country="KR",
    ),
    SourceSeed(
        name="Lunit Team Blog",
        slug="lunit-team-blog",
        company_name="Lunit",
        feed_url="https://medium.com/feed/lunit",
        site_url="https://medium.com/lunit",
        description="Lunit medical AI, machine learning, data, product, and engineering stories.",
        language="ko",
        country="KR",
    ),
    SourceSeed(
        name="Gmarket Tech Blog",
        slug="gmarket-tech-blog",
        company_name="Gmarket",
        feed_url="https://dev.gmarket.com/sitemap.xml",
        site_url="https://dev.gmarket.com",
        description=(
            "Gmarket commerce, search, backend, data, frontend, "
            "and platform engineering cases."
        ),
        collection_strategy="sitemap",
        content_strategy="article_fetch",
        language="ko",
        country="KR",
    ),
    SourceSeed(
        name="Netmarble Tech Blog",
        slug="netmarble-tech-blog",
        company_name="Netmarble",
        feed_url="https://netmarble.engineering/feed",
        site_url="https://netmarble.engineering",
        description=(
            "Netmarble game backend, large traffic, cloud, data, "
            "and platform engineering cases."
        ),
        pagination_strategy="wordpress_paged",
        language="ko",
        country="KR",
    ),
    SourceSeed(
        name="Banksalad Blog",
        slug="banksalad-blog",
        company_name="Banksalad",
        feed_url="https://blog.banksalad.com/rss.xml",
        site_url="https://blog.banksalad.com",
        description=(
            "Banksalad fintech, backend, frontend, data, product, "
            "and engineering technology cases."
        ),
        language="ko",
        country="KR",
    ),
    SourceSeed(
        name="Inflab Tech Blog",
        slug="inflab-tech-blog",
        company_name="Inflab",
        feed_url="https://tech.inflab.com/rss.xml",
        site_url="https://tech.inflab.com",
        description=(
            "Inflab education platform, backend, frontend, DevOps, "
            "cloud, and productivity engineering cases."
        ),
        language="ko",
        country="KR",
    ),
    SourceSeed(
        name="Upstage Blog",
        slug="upstage-blog",
        company_name="Upstage",
        feed_url="https://www.upstage.ai/sitemap.xml",
        site_url="https://www.upstage.ai",
        description=(
            "Upstage AI, LLM, document AI, machine learning, "
            "and product technology cases."
        ),
        collection_strategy="sitemap",
        content_strategy="article_fetch",
        language="ko",
        country="KR",
    ),
)

TECH_BLOG_SOURCES: tuple[SourceSeed, ...] = AWS_SOURCES + KOREAN_TECH_BLOG_SOURCES
