from flask import request, session, jsonify
from flask_restful import Resource
from config import app, db, api
from models.models import Pet
from marshmallow_schemas.pet import pet_schema


class PetByID(Resource):
  def get(self, id):
    pet = Pet.query.filter_by(id=id).first()
    if not pet:
      return {
        "status": "failed",
        "error": {"message":"pet does not exist"}
      }
    return {
      "status": "success",
      "data": pet_schema.dump(pet),
      "code": 200
    }, 200
  
  def delete(self, id):
    pet = Pet.query.filter_by(id=id).first()
    if not pet:
      return {
        "status": "failed",
        "error":{"message":'Pet does not exist'},
        "code": 400
      }, 400
    
    Pet.delete_db(pet)
    return {
      "status": "success",
      "message": "Pet has been deleted!",
      "code": 200
    }, 200
  
  def patch(self, id):
    pet = Pet.query.filter_by(id=id).first()
    pet_from_user = request.get_json()
    
    if not pet:
      return {
      "status": "failed",
      "error":{"message": "Pet does not exist"},
      "code": 400
    }, 400


    pet.update_db(pet_from_user)
    return {
      "status": "success",
      "data": pet_schema.dump(pet),
      "code": 200
    }, 200
      

api.add_resource(PetByID, '/user/pets/<int:id>', endpoint='user_pet_id')