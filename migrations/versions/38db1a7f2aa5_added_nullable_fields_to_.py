"""added nullable fields to illnessesclassification table

Revision ID: 38db1a7f2aa5
Revises: f972285a3221
Create Date: 2024-08-04 15:07:07.357656

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '38db1a7f2aa5'
down_revision = 'f972285a3221'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('illnessesclassifications', schema=None) as batch_op:
        batch_op.alter_column('illness_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('classification_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('illnessesclassifications', schema=None) as batch_op:
        batch_op.alter_column('classification_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('illness_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###