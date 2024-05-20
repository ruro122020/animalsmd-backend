from flask import request, session
from flask_restful import Resource
from config import app, db, api
from models.models import Classification
from sqlalchemy.exc import IntegrityError
from marshmallow_schemas.species import species_schema
class SpeciesByType(Resource):

  def get(self):
    pass

api.add_resource(SpeciesByType, '/species')