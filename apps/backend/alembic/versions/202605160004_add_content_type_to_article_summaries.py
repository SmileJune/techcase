"""add content type to article summaries

Revision ID: 202605160004
Revises: 202605160003
Create Date: 2026-05-16 00:04:00

"""
from collections.abc import Sequence

import sqlalchemy as sa

from alembic import op

revision: str = "202605160004"
down_revision: str | None = "202605160003"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.add_column(
        "article_summaries",
        sa.Column("content_type", sa.String(length=80), nullable=True),
    )
    op.create_index(
        op.f("ix_article_summaries_content_type"),
        "article_summaries",
        ["content_type"],
        unique=False,
    )


def downgrade() -> None:
    op.drop_index(op.f("ix_article_summaries_content_type"), table_name="article_summaries")
    op.drop_column("article_summaries", "content_type")
