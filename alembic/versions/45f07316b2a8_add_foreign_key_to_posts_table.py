"""add foreign-key to posts table

Revision ID: 45f07316b2a8
Revises: 11a69755243b
Create Date: 2026-06-14 15:19:24.724457

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "45f07316b2a8"
down_revision: Union[str, Sequence[str], None] = "11a69755243b"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key(
        "posts_user_fk",
        source_table="posts",
        referent_table="users",
        local_cols=["owner_id"],
        remote_cols=["id"],
        ondelete="CASCADE",
    )

    """Upgrade schema."""
    pass


def downgrade() -> None:
    op.drop_constraint("posts_user_fk", table_name="posts")
    op.drop_column("posts", "owner_id")
    """Downgrade schema."""
    pass
