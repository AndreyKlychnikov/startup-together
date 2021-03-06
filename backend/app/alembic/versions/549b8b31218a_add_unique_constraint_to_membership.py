"""Add unique constraint to membership

Revision ID: 549b8b31218a
Revises: d09dbc08bb6c
Create Date: 2021-08-14 18:55:32.065468

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '549b8b31218a'
down_revision = 'd09dbc08bb6c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('membership_uniq', 'projectmembership', ['user_id', 'project_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('membership_uniq', 'projectmembership', type_='unique')
    # ### end Alembic commands ###
