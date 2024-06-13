"""Delete usersspecies table

Revision ID: 310936181031
Revises: ff4ccdb91652
Create Date: 2024-06-04 18:44:02.977400

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '310936181031'
down_revision = 'ff4ccdb91652'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('usersspecies')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('usersspecies',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('age', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('weight', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('species_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['species_id'], ['species.id'], name='fk_usersspecies_species_id_species'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='fk_usersspecies_user_id_users'),
    sa.PrimaryKeyConstraint('id', name='usersspecies_pkey')
    )
    # ### end Alembic commands ###