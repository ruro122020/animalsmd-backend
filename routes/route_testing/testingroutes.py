from flask import request, session
from flask_restful import Resource
from config import app, db, api
from models.models import Species, Classification, Symptom, User, SpeciesClassification, SymptomClassification
from sqlalchemy.exc import IntegrityError
from marshmallow_schemas.species import species_schema
from marshmallow_schemas.classification import classification_schema, classifications_schema_many
from marshmallow_schemas.symptom import symptom_classification_schema
from marshmallow_schemas.symptom import symptom_classification_schema_many
from marshmallow_schemas.symptomsclassification import symptom_classification_schema_many, symptom_classification_schema

class TestingRoute(Resource):
  def get(self):
    symptoms_classification = SymptomClassification.query.all()
    return symptom_classification_schema_many.dump(symptoms_classification)
    pass


api.add_resource(TestingRoute,'/test')