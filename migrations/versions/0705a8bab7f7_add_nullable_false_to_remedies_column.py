"""add nullable=False to remedies column

Revision ID: 0705a8bab7f7
Revises: e7f07af1b436
Create Date: 2024-06-21 12:26:45.284805

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0705a8bab7f7'
down_revision = 'e7f07af1b436'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('illnesses', schema=None) as batch_op:
        batch_op.alter_column('remedies',
               existing_type=sa.VARCHAR(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('illnesses', schema=None) as batch_op:
        batch_op.alter_column('remedies',
               existing_type=sa.VARCHAR(),
               nullable=True)

    # ### end Alembic commands ###
