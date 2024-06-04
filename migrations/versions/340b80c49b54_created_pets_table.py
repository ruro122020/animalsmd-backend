"""created pets table

Revision ID: 340b80c49b54
Revises: 310936181031
Create Date: 2024-06-04 18:59:29.430267

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '340b80c49b54'
down_revision = '310936181031'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('weight', sa.Integer(), nullable=False),
    sa.Column('species_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['species_id'], ['species.id'], name=op.f('fk_pets_species_id_species')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_pets_user_id_users')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pets')
    # ### end Alembic commands ###
