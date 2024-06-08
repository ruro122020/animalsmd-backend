"""create illnessessymptoms table

Revision ID: ec4f7976952e
Revises: c8ce45691617
Create Date: 2024-06-08 12:54:36.168085

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ec4f7976952e'
down_revision = 'c8ce45691617'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('illnessessymptoms',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('illness_id', sa.Integer(), nullable=True),
    sa.Column('symptom_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['illness_id'], ['illnesses.id'], name=op.f('fk_illnessessymptoms_illness_id_illnesses')),
    sa.ForeignKeyConstraint(['symptom_id'], ['symptoms.id'], name=op.f('fk_illnessessymptoms_symptom_id_symptoms')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('illnessessymptoms')
    # ### end Alembic commands ###
