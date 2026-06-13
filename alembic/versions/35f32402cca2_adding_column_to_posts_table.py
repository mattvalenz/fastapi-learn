"""adding column to posts table

Revision ID: 35f32402cca2
Revises: b6e6038f2460
Create Date: 2026-06-13 16:03:19.533336

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "35f32402cca2"
down_revision: Union[str, Sequence[str], None] = "b6e6038f2460"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    """Upgrade schema."""
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    """Downgrade schema."""
    pass
