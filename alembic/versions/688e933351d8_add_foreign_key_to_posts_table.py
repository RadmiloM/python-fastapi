"""add foreign-key to posts table

Revision ID: 688e933351d8
Revises: 40f95fba248c
Create Date: 2023-05-21 19:47:28.115124

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '688e933351d8'
down_revision = '40f95fba248c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts",sa.Column("user_id",sa.Integer(),nullable=False))
    op.create_foreign_key('post_users_fk',source_table="posts", referent_table="users", local_cols=['user_id'],remote_cols=['id'],ondelete='CASCADE')



def downgrade() -> None:
    op.drop_constraint("post_users_fk",table_name="posts")
    op.drop_column("posts","user_id")
