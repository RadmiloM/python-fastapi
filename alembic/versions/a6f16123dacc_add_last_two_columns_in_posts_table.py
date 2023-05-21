"""add last two columns in posts table"

Revision ID: a6f16123dacc
Revises: 688e933351d8
Create Date: 2023-05-21 19:56:11.445466

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a6f16123dacc'
down_revision = '688e933351d8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column('published',sa.Boolean(),nullable=False,server_default='True'),)
    op.add_column('posts',sa.Column('created_at',sa.TIMESTAMP(timezone=True),nullable=False,server_default=sa.text('NOW()')))


def downgrade() -> None:
    op.drop_column("posts","published")
    op.drop_column("posts","created_at")
