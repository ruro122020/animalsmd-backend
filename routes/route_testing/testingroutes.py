from flask import request, session
from flask_restful import Resource
from config import app, db, api
from models.models import Species, Classification, Symptom, User, SpeciesClassification, SymptomClassification, Pet, PetSymptom, Illness, IllnessSymptom
from sqlalchemy.exc import IntegrityError
from marshmallow_schemas.species import species_schema
from marshmallow_schemas.classification import classification_schema, classifications_schema_many
from marshmallow_schemas.symptom import symptom_schema_many, symptom_schema
from marshmallow_schemas.symptomsclassification import symptom_classification_schema_many, symptom_classification_schema
from marshmallow_schemas.pet import pet_schema
from marshmallow_schemas.illness import illness_schema, illness_schema_many
from marshmallow_schemas.illnesssymptom import illness_symptom_schema_many
from marshmallow_schemas.medication import medication_schema, medication_schema_many
from models.models import Medication
class TestingRoute(Resource):
  def get(self):
    medication = Medication.query.first()
    return medication_schema.dump(medication)
    


api.add_resource(TestingRoute,'/test')