"""empty message

Revision ID: 628064e1f23d
Revises: 081420648416
Create Date: 2021-11-24 12:17:14.277804

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '628064e1f23d'
down_revision = '081420648416'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('audio', sa.Column('audio_url', sa.String(length=256), nullable=False))
    op.drop_column('audio', 'audio_URI')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('audio', sa.Column('audio_URI', sa.VARCHAR(length=128), autoincrement=False, nullable=False))
    op.drop_column('audio', 'audio_url')
    # ### end Alembic commands ###
