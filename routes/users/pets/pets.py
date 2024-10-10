from flask import request, session, jsonify
from flask_restful import Resource
from config import app, db, api
from models.models import Pet, User, Species, PetSymptom, Symptom
from utils.authenticate import authenticate
from marshmallow_schemas.pet import pet_schema_many, pet_schema

def get_user(user_id):
  """Fetch the user by ID."""
  return User.query.filter_by(id=user_id).first()


def get_species(species_name):
  """Fetch the species by type name."""
  return Species.query.filter_by(type_name = species_name).first()
 
def create_pet(pet, user, species):
  """Create a new pet row."""
  return Pet.create_row(name = pet.get('name'), age = pet.get('age'), weight=pet.get('weight'), user=user.id, species=species.id)#id's had to be passed cause Pet model has no validations yet. 

def add_pets_symptoms(user_pet, pet):
  """Add symptoms to the pet."""
  for symptom_name in user_pet.get('symptoms'):
    symptom = Symptom.query.filter_by(name = symptom_name).first()
    if symptom:
     PetSymptom.create_row(pet=pet, symptom=symptom)
    else:
      return {
        "status": "failed",
        "error":{"message": f"pet '{symptom_name}' symptom  does not exist"},
        "code": 400
      }
  return None

class Pets(Resource):
  def get(self):
    user_pets = Pet.query.filter_by(user_id = session.get('user_id')).order_by(Pet.id).all()
    return {
      "status": "success",
      "data": pet_schema_many.dump(user_pets),
      "code": 200
    }
    
  def post(self):
    user_pet = request.get_json()
    
    if not user_pet:
      return {
        "status":"failed",
        "error":{"message": 'User pet info missing'},
        "code": 400}
   
    pet_exist = Pet.query.filter_by(name=user_pet.get('name')).first()

    if pet_exist:
      return {
        "status": "failed",
        "error":{"message":"Pet already Exist"},
        "code": 409
        }

    user_id = session.get('user_id')
    species_name = user_pet.get('type')
    user = get_user(user_id)
    species = get_species(species_name.lower())
    
    if not user:
      return {
        "status":"failed",
        "error":{"message":"user of pet does not exist"},
        "code": 400}

    if not species:
      return {
        "status": "failed",
        "error":{"message":"species of pet does not exist"},
        "code": 400
      }

    pet = create_pet(user_pet, user, species)

    if not user_pet.get('symptoms'):
      return {
        "status": "failed",
        "error":{"message":"symptoms are missing"},
        "code": 400
      }
    #user_pet: is an object from the frontend
    #pet: is the object created in create_pet
    error_message = add_pets_symptoms(user_pet, pet)

    if error_message:
      return error_message
    
    return {
      "status": "success",
      "data": pet_schema.dump(pet),
      "code": 200
    }

api.add_resource(Pets, '/user/pets', endpoint='pets')