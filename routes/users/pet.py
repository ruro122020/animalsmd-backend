from flask import request, session
from flask_restful import Resource
from config import app, db, api
from models.models import Pet
from utils.authenticate import authenticate
from marshmallow_schemas.pet import pet_schema_many


class Pets(Resource):
  def get(self):
    user_pets = Pet.query.filter_by(user_id = session.get('user_id')).all()
    return pet_schema_many.dump(user_pets), 200
    


api.add_resource(Pets, '/pets', endpoint='pets')