"""add user table

Revision ID: 11a69755243b
Revises: 35f32402cca2
Create Date: 2026-06-13 16:14:55.638570

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "11a69755243b"
down_revision: Union[str, Sequence[str], None] = "35f32402cca2"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("password", sa.String(), nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
