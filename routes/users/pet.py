from flask import request, session, jsonify
from flask_restful import Resource
from config import app, db, api
from models.models import Pet, User, Species, PetSymptom, Symptom
from utils.authenticate import authenticate
from marshmallow_schemas.pet import pet_schema_many


class Pets(Resource):
  def get(self):
    user_pets = Pet.query.filter_by(user_id = session.get('user_id')).all()
    return pet_schema_many.dump(user_pets), 200
    
  def post(self):
    user_pet = request.get_json()
    print('user_pet', user_pet)
    if user_pet:
      user = User.query.filter_by(id=session.get('user_id')).first()
      species = Species.query.filter_by(type_name = user_pet.get('type')).first()
      if user and species:
        pet = Pet.create_row(name = user_pet.get('name'), age = user_pet.get('age'), weight=user_pet.get('weight'), user=user.id, species=species.id)#id's had to be passed cause Pet model has no validations yet. 
        #add pet symptoms to petssymptoms table
        if user_pet.get('symptoms'):
          for symptom_name in user_pet.get('symptoms'):
            symptom = Symptom.query.filter_by(name = symptom_name).first()
            if symptom:
              pet_symptom = PetSymptom.create_row(pet=pet, symptom=symptom)
              print('pet_symptom', pet_symptom)
            else:
              return {"error": f"pet '{symptom_name}' symptom  does not exist"}, 400
        else:
          return {"error":"symptoms are missing"}, 400
      else:
        return {"error":"user or species of pet does not exist"}, 400
    else:
      return {'error': 'User pet info missing'}, 400
    return {}, 200

api.add_resource(Pets, '/user/pets', endpoint='pets')