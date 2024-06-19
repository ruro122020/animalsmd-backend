from flask import request, session, jsonify
from flask_restful import Resource
from config import app, db, api
from models.models import Pet

class PetByID(Resource):
  def delete(self, id):
    pet = Pet.query.filter_by(id=id).first()
    if pet:
      Pet.delete_db(pet)
      return {}, 200

    return {"error":'Pet does not exist'}
            



api.add_resource(PetByID, '/user/pets/<int:id>')