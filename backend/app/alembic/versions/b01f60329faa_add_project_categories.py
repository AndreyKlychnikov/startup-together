"""Add project categories

Revision ID: b01f60329faa
Revises: f3a680f7328e
Create Date: 2021-09-03 20:22:02.225193

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b01f60329faa'
down_revision = 'f3a680f7328e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('project_category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('value', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_project_category_id'), 'project_category', ['id'], unique=False)
    op.create_table('project_category_association',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('project_id', sa.Integer(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['project_category.id'], ),
    sa.ForeignKeyConstraint(['project_id'], ['project.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('category_id', 'project_id', name='project_category_uniq')
    )
    op.create_index(op.f('ix_project_category_association_id'), 'project_category_association', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_project_category_association_id'), table_name='project_category_association')
    op.drop_table('project_category_association')
    op.drop_index(op.f('ix_project_category_id'), table_name='project_category')
    op.drop_table('project_category')
    # ### end Alembic commands ###
