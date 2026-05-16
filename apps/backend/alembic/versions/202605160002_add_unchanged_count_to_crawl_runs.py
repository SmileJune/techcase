"""add unchanged count to crawl runs

Revision ID: 202605160002
Revises: 202605160001
Create Date: 2026-05-16 00:02:00

"""
from collections.abc import Sequence

import sqlalchemy as sa

from alembic import op

revision: str = "202605160002"
down_revision: str | None = "202605160001"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.add_column(
        "crawl_runs",
        sa.Column("unchanged_count", sa.Integer(), server_default="0", nullable=False),
    )


def downgrade() -> None:
    op.drop_column("crawl_runs", "unchanged_count")
