"""add content column to posts table

Revision ID: e442e1bcc103
Revises: 56640ba80740
Create Date: 2023-05-21 19:31:52.681585

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e442e1bcc103'
down_revision = '56640ba80740'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',sa.Column("content",sa.String(),nullable=False))


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
