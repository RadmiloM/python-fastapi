"""create posts table

Revision ID: 56640ba80740
Revises: 
Create Date: 2023-05-21 19:21:16.773503

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56640ba80740'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("posts", sa.Column('id',sa.Integer(),nullable=False,primary_key=True),
                    sa.Column('title', sa.String(),nullable=False))


def downgrade() -> None:
    op.drop_table("posts")
