"""Add project membership model

Revision ID: 43e56e662091
Revises: 617ac90ecf21
Create Date: 2021-08-14 16:00:48.485579

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '43e56e662091'
down_revision = '617ac90ecf21'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('projectmembership',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('project_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['project_id'], ['project.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_projectmembership_id'), 'projectmembership', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_projectmembership_id'), table_name='projectmembership')
    op.drop_table('projectmembership')
    # ### end Alembic commands ###
