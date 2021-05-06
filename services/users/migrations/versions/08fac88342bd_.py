"""empty message

Revision ID: 08fac88342bd
Revises: 0f9f3a9988b2
Create Date: 2019-05-29 01:57:11.765408

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '08fac88342bd'
down_revision = '0f9f3a9988b2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password', sa.String(length=255), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'password')
    # ### end Alembic commands ###