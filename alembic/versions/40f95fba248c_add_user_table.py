"""add user table

Revision ID: 40f95fba248c
Revises: e442e1bcc103
Create Date: 2023-05-21 19:36:46.936792

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '40f95fba248c'
down_revision = 'e442e1bcc103'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id',sa.Integer(),nullable=False),
                    sa.Column('email',sa.String(),nullable=False),
                    sa.Column('password',sa.String(),nullable=False),
                    sa.Column('created_at',sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'),nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'))


def downgrade() -> None:
    op.drop_table("users")
