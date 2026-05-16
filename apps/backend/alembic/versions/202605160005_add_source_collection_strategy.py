"""add source collection strategy

Revision ID: 202605160005
Revises: 202605160004
Create Date: 2026-05-16 00:05:00

"""
from collections.abc import Sequence

import sqlalchemy as sa

from alembic import op

revision: str = "202605160005"
down_revision: str | None = "202605160004"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.alter_column("sources", "feed_url", existing_type=sa.Text(), nullable=True)
    op.add_column(
        "sources",
        sa.Column(
            "collection_strategy",
            sa.String(length=80),
            server_default="rss",
            nullable=False,
        ),
    )
    op.add_column(
        "sources",
        sa.Column(
            "pagination_strategy",
            sa.String(length=80),
            server_default="none",
            nullable=False,
        ),
    )
    op.add_column(
        "sources",
        sa.Column(
            "content_strategy",
            sa.String(length=80),
            server_default="feed_only",
            nullable=False,
        ),
    )
    op.add_column("sources", sa.Column("language", sa.String(length=20), nullable=True))
    op.add_column("sources", sa.Column("country", sa.String(length=80), nullable=True))
    op.add_column(
        "sources",
        sa.Column(
            "trust_level",
            sa.String(length=40),
            server_default="official",
            nullable=False,
        ),
    )
    op.create_index(
        op.f("ix_sources_collection_strategy"),
        "sources",
        ["collection_strategy"],
        unique=False,
    )


def downgrade() -> None:
    op.drop_index(op.f("ix_sources_collection_strategy"), table_name="sources")
    op.drop_column("sources", "trust_level")
    op.drop_column("sources", "country")
    op.drop_column("sources", "language")
    op.drop_column("sources", "content_strategy")
    op.drop_column("sources", "pagination_strategy")
    op.drop_column("sources", "collection_strategy")
    op.alter_column("sources", "feed_url", existing_type=sa.Text(), nullable=False)
