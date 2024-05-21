from flask import request, session
from flask_restful import Resource
from config import app, db, api
from models.models import Species, SpeciesClassification
from sqlalchemy.exc import IntegrityError
from marshmallow_schemas.species import species_schema
from marshmallow_schemas.speciesclassification import species_classification_schema

class SpeciesByType(Resource):
  def get(self, type):
    species = Species.query.filter(Species.type == type).first()
    for s in species.species_classification:
      print(s.species_id)
      #somequery 
    return species_schema.dump(species)

api.add_resource(SpeciesByType, '/species/<type>')