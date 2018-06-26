"""user tokens

Revision ID: 4260dcfc57c1
Revises: 50f38482415b
Create Date: 2018-06-26 05:12:48.120630

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4260dcfc57c1'
down_revision = '50f38482415b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('token', sa.String(length=32), nullable=True))
    op.add_column('user', sa.Column('token_expiration', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_user_token'), 'user', ['token'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_token'), table_name='user')
    op.drop_column('user', 'token_expiration')
    op.drop_column('user', 'token')
    # ### end Alembic commands ###
