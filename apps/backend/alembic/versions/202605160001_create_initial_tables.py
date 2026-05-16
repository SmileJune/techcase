"""create initial tables

Revision ID: 202605160001
Revises:
Create Date: 2026-05-16 00:01:00

"""
from collections.abc import Sequence

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

revision: str = "202605160001"
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table(
        "sources",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("slug", sa.String(length=160), nullable=False),
        sa.Column("company_name", sa.String(length=160), nullable=False),
        sa.Column("feed_url", sa.Text(), nullable=False),
        sa.Column("site_url", sa.Text(), nullable=True),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("enabled", sa.Boolean(), server_default="true", nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_sources")),
        sa.UniqueConstraint("feed_url", name=op.f("uq_sources_feed_url")),
        sa.UniqueConstraint("slug", name=op.f("uq_sources_slug")),
    )
    op.create_index(op.f("ix_sources_slug"), "sources", ["slug"], unique=False)

    op.create_table(
        "articles",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("source_id", sa.Uuid(), nullable=False),
        sa.Column("title", sa.Text(), nullable=False),
        sa.Column("url", sa.Text(), nullable=False),
        sa.Column("canonical_url", sa.Text(), nullable=True),
        sa.Column("author", sa.String(length=255), nullable=True),
        sa.Column("published_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("summary", sa.Text(), nullable=True),
        sa.Column("content_text", sa.Text(), nullable=True),
        sa.Column("content_html", sa.Text(), nullable=True),
        sa.Column("language", sa.String(length=20), nullable=True),
        sa.Column("raw_metadata", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column("collected_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("indexed_at", sa.DateTime(timezone=True), nullable=True),
        sa.ForeignKeyConstraint(
            ["source_id"],
            ["sources.id"],
            name=op.f("fk_articles_source_id_sources"),
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_articles")),
        sa.UniqueConstraint("canonical_url", name=op.f("uq_articles_canonical_url")),
        sa.UniqueConstraint("url", name=op.f("uq_articles_url")),
    )
    op.create_index(op.f("ix_articles_published_at"), "articles", ["published_at"], unique=False)
    op.create_index(op.f("ix_articles_source_id"), "articles", ["source_id"], unique=False)
    op.create_index(
        "ix_articles_source_id_published_at",
        "articles",
        ["source_id", "published_at"],
        unique=False,
    )

    op.create_table(
        "crawl_runs",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("source_id", sa.Uuid(), nullable=False),
        sa.Column("status", sa.String(length=40), nullable=False),
        sa.Column(
            "started_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column("finished_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("fetched_count", sa.Integer(), server_default="0", nullable=False),
        sa.Column("created_count", sa.Integer(), server_default="0", nullable=False),
        sa.Column("updated_count", sa.Integer(), server_default="0", nullable=False),
        sa.Column("failed_count", sa.Integer(), server_default="0", nullable=False),
        sa.Column("error_message", sa.Text(), nullable=True),
        sa.Column("metadata", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.ForeignKeyConstraint(
            ["source_id"],
            ["sources.id"],
            name=op.f("fk_crawl_runs_source_id_sources"),
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_crawl_runs")),
    )
    op.create_index(op.f("ix_crawl_runs_source_id"), "crawl_runs", ["source_id"], unique=False)
    op.create_index(op.f("ix_crawl_runs_started_at"), "crawl_runs", ["started_at"], unique=False)
    op.create_index(op.f("ix_crawl_runs_status"), "crawl_runs", ["status"], unique=False)

    op.create_table(
        "article_keywords",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("article_id", sa.Uuid(), nullable=False),
        sa.Column("keyword", sa.String(length=255), nullable=False),
        sa.Column("keyword_type", sa.String(length=80), nullable=False),
        sa.Column("confidence", sa.Float(), nullable=True),
        sa.Column("matched_by", sa.String(length=80), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["article_id"],
            ["articles.id"],
            name=op.f("fk_article_keywords_article_id_articles"),
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_article_keywords")),
        sa.UniqueConstraint(
            "article_id",
            "keyword",
            "keyword_type",
            name="uq_article_keywords_article_id_keyword_type",
        ),
    )
    op.create_index(
        op.f("ix_article_keywords_article_id"), "article_keywords", ["article_id"], unique=False
    )
    op.create_index(
        op.f("ix_article_keywords_keyword"), "article_keywords", ["keyword"], unique=False
    )
    op.create_index(
        op.f("ix_article_keywords_keyword_type"), "article_keywords", ["keyword_type"], unique=False
    )
    op.create_index(
        "ix_article_keywords_keyword_type_keyword",
        "article_keywords",
        ["keyword_type", "keyword"],
        unique=False,
    )


def downgrade() -> None:
    op.drop_index("ix_article_keywords_keyword_type_keyword", table_name="article_keywords")
    op.drop_index(op.f("ix_article_keywords_keyword_type"), table_name="article_keywords")
    op.drop_index(op.f("ix_article_keywords_keyword"), table_name="article_keywords")
    op.drop_index(op.f("ix_article_keywords_article_id"), table_name="article_keywords")
    op.drop_table("article_keywords")

    op.drop_index(op.f("ix_crawl_runs_status"), table_name="crawl_runs")
    op.drop_index(op.f("ix_crawl_runs_started_at"), table_name="crawl_runs")
    op.drop_index(op.f("ix_crawl_runs_source_id"), table_name="crawl_runs")
    op.drop_table("crawl_runs")

    op.drop_index("ix_articles_source_id_published_at", table_name="articles")
    op.drop_index(op.f("ix_articles_source_id"), table_name="articles")
    op.drop_index(op.f("ix_articles_published_at"), table_name="articles")
    op.drop_table("articles")

    op.drop_index(op.f("ix_sources_slug"), table_name="sources")
    op.drop_table("sources")
