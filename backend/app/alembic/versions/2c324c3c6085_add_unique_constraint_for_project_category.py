"""Add unique constraint for project_category value

Revision ID: 2c324c3c6085
Revises: b01f60329faa
Create Date: 2021-09-04 10:40:27.744172

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "2c324c3c6085"
down_revision = "b01f60329faa"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, "project_category", ["value"])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "project_category", type_="unique")
    # ### end Alembic commands ###
