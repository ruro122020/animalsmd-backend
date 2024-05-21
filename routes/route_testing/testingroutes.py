from flask import request, session
from flask_restful import Resource
from config import app, db, api
from models.models import Species, SpeciesClassification, Classification
from sqlalchemy.exc import IntegrityError
from marshmallow_schemas.species import species_schema
from marshmallow_schemas.speciesclassification import species_classification_schema
from marshmallow_schemas.classification import classification_schema

class TestingRoute(Resource):
  def get(self):
    classification = Classification.query.first()
    return classification_schema.dump(classification)



api.add_resource(TestingRoute,'/test')