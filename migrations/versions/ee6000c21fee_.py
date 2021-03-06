"""empty message

Revision ID: ee6000c21fee
Revises: bab6943cc901
Create Date: 2019-10-06 11:39:32.284669

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ee6000c21fee'
down_revision = 'bab6943cc901'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('role', sa.String(length=128), nullable=True))
    op.drop_constraint('users_username_key', 'users', type_='unique')
    op.create_unique_constraint(None, 'users', ['phone'])
    op.drop_column('users', 'username')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('username', sa.VARCHAR(length=128), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'users', type_='unique')
    op.create_unique_constraint('users_username_key', 'users', ['username'])
    op.drop_column('users', 'role')
    # ### end Alembic commands ###
