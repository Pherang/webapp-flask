"""Corrected column name

Revision ID: 50f38482415b
Revises: d3fcdc2e6681
Create Date: 2018-06-22 07:23:46.981584

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '50f38482415b'
down_revision = 'd3fcdc2e6681'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    #op.add_column('task', sa.Column('description', sa.String(length=128), nullable=True))
    #op.drop_column('task', 'descriptuib')
    # ### end Alembic commands ###
    pass

def downgrade():
    pass
    # ### commands auto generated by Alembic - please adjust! ###
    #op.add_column('task', sa.Column('descriptuib', sa.VARCHAR(length=128), nullable=True))
    #op.drop_column('task', 'description')
    # ### end Alembic commands ###
