from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import DateTime, Float, ForeignKey, Index, String, UniqueConstraint, Uuid, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class ArticleKeyword(Base):
    __tablename__ = "article_keywords"
    __table_args__ = (
        UniqueConstraint(
            "article_id",
            "keyword",
            "keyword_type",
            name="uq_article_keywords_article_id_keyword_type",
        ),
        Index("ix_article_keywords_keyword_type_keyword", "keyword_type", "keyword"),
    )

    id: Mapped[UUID] = mapped_column(Uuid(as_uuid=True), primary_key=True, default=uuid4)
    article_id: Mapped[UUID] = mapped_column(
        Uuid(as_uuid=True),
        ForeignKey("articles.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    keyword: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    keyword_type: Mapped[str] = mapped_column(String(80), nullable=False, index=True)
    confidence: Mapped[float | None] = mapped_column(Float)
    matched_by: Mapped[str] = mapped_column(String(80), nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )

    article = relationship("Article", back_populates="keywords")
