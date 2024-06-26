"""supabase database population

Revision ID: 2f4e8ec02b61
Revises: fc244b31410f
Create Date: 2024-06-19 17:32:57.081181

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2f4e8ec02b61'
down_revision = 'fc244b31410f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('classifications',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('classification', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('illnesses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('species',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type_name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('symptoms',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('_password_hash', sa.String(), nullable=False),
    sa.CheckConstraint('length(name) > 3', name='ck_user_name_length'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('illnessesclassifications',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('illness_id', sa.Integer(), nullable=True),
    sa.Column('classification_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['classification_id'], ['classifications.id'], name=op.f('fk_illnessesclassifications_classification_id_classifications')),
    sa.ForeignKeyConstraint(['illness_id'], ['illnesses.id'], name=op.f('fk_illnessesclassifications_illness_id_illnesses')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('illnessessymptoms',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('illness_id', sa.Integer(), nullable=True),
    sa.Column('symptom_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['illness_id'], ['illnesses.id'], name=op.f('fk_illnessessymptoms_illness_id_illnesses')),
    sa.ForeignKeyConstraint(['symptom_id'], ['symptoms.id'], name=op.f('fk_illnessessymptoms_symptom_id_symptoms')),
    sa.PrimaryKeyConstraint('id')
    )
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
    op.create_table('speciesclassifications',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('classification_id', sa.Integer(), nullable=True),
    sa.Column('species_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['classification_id'], ['classifications.id'], name=op.f('fk_speciesclassifications_classification_id_classifications')),
    sa.ForeignKeyConstraint(['species_id'], ['species.id'], name=op.f('fk_speciesclassifications_species_id_species')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('symptomsclassifications',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('classification_id', sa.Integer(), nullable=True),
    sa.Column('symptoms_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['classification_id'], ['classifications.id'], name=op.f('fk_symptomsclassifications_classification_id_classifications')),
    sa.ForeignKeyConstraint(['symptoms_id'], ['symptoms.id'], name=op.f('fk_symptomsclassifications_symptoms_id_symptoms')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('petsymptoms',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pet_id', sa.Integer(), nullable=True),
    sa.Column('symptom_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pet_id'], ['pets.id'], name=op.f('fk_petsymptoms_pet_id_pets')),
    sa.ForeignKeyConstraint(['symptom_id'], ['symptoms.id'], name=op.f('fk_petsymptoms_symptom_id_symptoms')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('petsymptoms')
    op.drop_table('symptomsclassifications')
    op.drop_table('speciesclassifications')
    op.drop_table('pets')
    op.drop_table('illnessessymptoms')
    op.drop_table('illnessesclassifications')
    op.drop_table('users')
    op.drop_table('symptoms')
    op.drop_table('species')
    op.drop_table('illnesses')
    op.drop_table('classifications')
    # ### end Alembic commands ###
