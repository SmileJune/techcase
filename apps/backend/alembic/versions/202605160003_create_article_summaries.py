"""create article summaries

Revision ID: 202605160003
Revises: 202605160002
Create Date: 2026-05-16 00:03:00

"""
from collections.abc import Sequence

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

revision: str = "202605160003"
down_revision: str | None = "202605160002"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table(
        "article_summaries",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("article_id", sa.Uuid(), nullable=False),
        sa.Column("summary_type", sa.String(length=80), nullable=False),
        sa.Column("language", sa.String(length=20), nullable=False),
        sa.Column("model", sa.String(length=120), nullable=False),
        sa.Column("prompt_version", sa.String(length=80), nullable=False),
        sa.Column("case_summary", sa.Text(), nullable=False),
        sa.Column("problem", sa.Text(), nullable=True),
        sa.Column("solution", sa.Text(), nullable=True),
        sa.Column("technologies", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column("architecture_keywords", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column("problem_keywords", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column("confidence", sa.Float(), nullable=True),
        sa.Column("raw_response", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
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
        sa.ForeignKeyConstraint(
            ["article_id"],
            ["articles.id"],
            name=op.f("fk_article_summaries_article_id_articles"),
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_article_summaries")),
        sa.UniqueConstraint(
            "article_id",
            "summary_type",
            "language",
            "prompt_version",
            name="uq_article_summaries_article_type_language_prompt",
        ),
    )
    op.create_index(
        "ix_article_summaries_article_type",
        "article_summaries",
        ["article_id", "summary_type"],
        unique=False,
    )
    op.create_index(
        op.f("ix_article_summaries_article_id"),
        "article_summaries",
        ["article_id"],
        unique=False,
    )
    op.create_index(
        op.f("ix_article_summaries_language"),
        "article_summaries",
        ["language"],
        unique=False,
    )
    op.create_index(
        op.f("ix_article_summaries_prompt_version"),
        "article_summaries",
        ["prompt_version"],
        unique=False,
    )
    op.create_index(
        op.f("ix_article_summaries_summary_type"),
        "article_summaries",
        ["summary_type"],
        unique=False,
    )


def downgrade() -> None:
    op.drop_index(op.f("ix_article_summaries_summary_type"), table_name="article_summaries")
    op.drop_index(op.f("ix_article_summaries_prompt_version"), table_name="article_summaries")
    op.drop_index(op.f("ix_article_summaries_language"), table_name="article_summaries")
    op.drop_index(op.f("ix_article_summaries_article_id"), table_name="article_summaries")
    op.drop_index("ix_article_summaries_article_type", table_name="article_summaries")
    op.drop_table("article_summaries")
