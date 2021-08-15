"""Add accepted column to membership

Revision ID: d09dbc08bb6c
Revises: 43e56e662091
Create Date: 2021-08-14 18:43:48.298357

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd09dbc08bb6c'
down_revision = '43e56e662091'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('projectmembership', sa.Column('accepted', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('projectmembership', 'accepted')
    # ### end Alembic commands ###
