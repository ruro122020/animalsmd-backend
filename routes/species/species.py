from flask import request, session
from flask_restful import Resource
from config import app, db, api
from models.models import Species, SpeciesClassification
from sqlalchemy.exc import IntegrityError
from marshmallow_schemas.species import species_schema
from marshmallow_schemas.speciesclassification import species_classification_schema

class SpeciesByType(Resource):
  def get(self, type_name):
    species = Species.query.filter(Species.type_name == type_name).first()
    species_classification = SpeciesClassification.query.filter(SpeciesClassification.species_id == species.id).first()
    species_classification_schema.dump(species_classification)



    #stopping here to build more tables to query more data for this route. 
    return species_classification_schema.dump(species_classification)


api.add_resource(SpeciesByType, '/species/<type_name>')