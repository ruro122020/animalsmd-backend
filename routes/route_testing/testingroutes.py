from flask import request, session
from flask_restful import Resource
from config import app, db, api
from models.models import Species, Classification, Symptom, User, SpeciesClassification, SymptomClassification, Pet
from sqlalchemy.exc import IntegrityError
from marshmallow_schemas.species import species_schema
from marshmallow_schemas.classification import classification_schema, classifications_schema_many
from marshmallow_schemas.symptom import symptom_schema_many, symptom_schema
from marshmallow_schemas.symptomsclassification import symptom_classification_schema_many, symptom_classification_schema
from marshmallow_schemas.pet import pet_schema

class TestingRoute(Resource):
  def get(self):
    pet = Pet.query.filter_by(id=2).first()
    return pet_schema.dump(pet)
    


api.add_resource(TestingRoute,'/test')