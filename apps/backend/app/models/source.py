from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import Boolean, DateTime, String, Text, Uuid, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Source(Base):
    __tablename__ = "sources"

    id: Mapped[UUID] = mapped_column(Uuid(as_uuid=True), primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    slug: Mapped[str] = mapped_column(String(160), nullable=False, unique=True, index=True)
    company_name: Mapped[str] = mapped_column(String(160), nullable=False)
    feed_url: Mapped[str | None] = mapped_column(Text, unique=True)
    site_url: Mapped[str | None] = mapped_column(Text)
    description: Mapped[str | None] = mapped_column(Text)
    collection_strategy: Mapped[str] = mapped_column(
        String(80), nullable=False, default="rss", server_default="rss"
    )
    pagination_strategy: Mapped[str] = mapped_column(
        String(80), nullable=False, default="none", server_default="none"
    )
    content_strategy: Mapped[str] = mapped_column(
        String(80), nullable=False, default="feed_only", server_default="feed_only"
    )
    language: Mapped[str | None] = mapped_column(String(20))
    country: Mapped[str | None] = mapped_column(String(80))
    trust_level: Mapped[str] = mapped_column(
        String(40), nullable=False, default="official", server_default="official"
    )
    enabled: Mapped[bool] = mapped_column(
        Boolean, nullable=False, default=True, server_default="true"
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now()
    )

    articles = relationship("Article", back_populates="source", cascade="all, delete-orphan")
    crawl_runs = relationship("CrawlRun", back_populates="source", cascade="all, delete-orphan")
