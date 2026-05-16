from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.models.source import Source
from app.seeds.aws_sources import AWS_SOURCES, SourceSeed


def upsert_source(db: Session, seed: SourceSeed) -> bool:
    source = db.scalar(select(Source).where(Source.slug == seed.slug))
    created = source is None

    if source is None:
        source = Source(slug=seed.slug)
        db.add(source)

    source.name = seed.name
    source.company_name = seed.company_name
    source.feed_url = seed.feed_url
    source.site_url = seed.site_url
    source.description = seed.description
    source.enabled = seed.enabled

    return created


def seed_sources() -> tuple[int, int]:
    created_count = 0
    updated_count = 0

    with SessionLocal() as db:
        for seed in AWS_SOURCES:
            created = upsert_source(db, seed)
            if created:
                created_count += 1
            else:
                updated_count += 1

        db.commit()

    return created_count, updated_count


def main() -> None:
    created_count, updated_count = seed_sources()
    print(f"Seeded sources: created={created_count}, updated={updated_count}")


if __name__ == "__main__":
    main()

