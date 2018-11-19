"""empty message

Revision ID: 93f27311304c
Revises: e6977955e99b
Create Date: 2018-11-19 16:00:08.927321

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '93f27311304c'
down_revision = 'e6977955e99b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('time', sa.Time(), nullable=True),
    sa.Column('accX', sa.Float(), nullable=True),
    sa.Column('accY', sa.Float(), nullable=True),
    sa.Column('accZ', sa.Float(), nullable=True),
    sa.Column('gyroX', sa.Float(), nullable=True),
    sa.Column('gyroY', sa.Float(), nullable=True),
    sa.Column('gyroZ', sa.Float(), nullable=True),
    sa.Column('magX', sa.Float(), nullable=True),
    sa.Column('magY', sa.Float(), nullable=True),
    sa.Column('magZ', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('data')
    # ### end Alembic commands ###