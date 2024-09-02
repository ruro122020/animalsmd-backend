"""illnessproducts table created

Revision ID: dbab60ee122b
Revises: 9a70c610c424
Create Date: 2024-09-02 14:35:30.637572

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dbab60ee122b'
down_revision = '9a70c610c424'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('illnessesproducts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('illness_id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['illness_id'], ['illnesses.id'], name=op.f('fk_illnessesproducts_illness_id_illnesses')),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], name=op.f('fk_illnessesproducts_product_id_products')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('illnessesproducts')
    # ### end Alembic commands ###
