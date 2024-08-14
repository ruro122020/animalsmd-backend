from re import I
from flask import request, session
from flask_restful import Resource
from config import api, db
from models.models import Product, IllnessSymptom, Illness, IllnessClassification, SpeciesClassification, Pet
from sqlalchemy import func
from marshmallow_schemas.illness import illness_schema 
from marshmallow_schemas.illnesssymptom import illness_symptom_schema
from marshmallow_schemas.pet import pet_schema
from marshmallow_schemas.product import product_schema
import random
import ipdb

#The end goal is to return illness, medications, and products from results

def create_illnesses_ids_list(symptoms_list):
  #When query illness_symptoms, the same illness is returned for multiple symptoms
  #to avoid duplicate ids, we are using the set data structure
  illnesses_ids_set = set()
  for symptom in symptoms_list:
    illness = IllnessSymptom.query.filter_by(symptom_id=symptom.id).first()
    illnesses_ids_set.add(illness.illness.id)
  
  #To make it easier to work with the illness_ids_set
  #convert the illnesses_ids_set to a list
  return list(illnesses_ids_set)

def create_illness_list(classification_illness, illness_ids):
  #compare the returned list from IllnessesClassifications table to the illness_list
  illness_list = []
  for illness_classification in classification_illness:
    if illness_classification.illness_id in illness_ids:
      illness = Illness.query.filter_by(id=illness_classification.illness_id).first()
      illness_list.append(illness)
  return illness_list

def get_pets_classification_id(pet):
  #query the speciesclassifications table to find the classification id of the species 
  species_classification = SpeciesClassification.query.filter_by(species_id = pet.species_id).first()
  return species_classification.classification

def get_illnesses_based_on_pets_classification(pet_classification):
  #use classification's id to query the illnessclassifications table, return all illness that matched the classification_id
  return IllnessClassification.query.filter_by(classification_id = pet_classification.id).all()

def get_illness_medications_products(illness_list):
   
    for illness_obj in illness_list:
      #product list data structor needs to change to assign the products to its appropriate illness. 
      #currently all the products are being combined for each illness therefore not making the distinction
      #on which product belongs to which illness resulting in return the wrong products for each illness
      products_list = []
      breakpoint()
      for medication_obj in illness_obj.medications:
        #we only want to provide 2 or less products to user
        product = Product.query.filter_by(name=medication_obj.name).first()
          # print('product name', product.name)
        if product:
          products_list.append(product)
    # print(products_list)
    return products_list

def add_products_to_each_illness(serialized_illness_list, serialized_product_list):
      for illness_obj in serialized_illness_list:
        illness_obj["products"] = serialized_product_list
      return serialized_illness_list

class PetResults(Resource):
  def get(self, id):
    #get user's pet from database
    pet = Pet.query.filter_by(id=id).first()

    if not pet:
      return {"error": "pet id not found or pet does not exist"}, 400
    #Now we want to get all the illnesses that matches the symptoms id
    illness_ids = create_illnesses_ids_list(pet.symptoms)

    #Now we want to make sure that the illnesses belongs to the classification of the pet
    #for instance, if a user's pet is a dog and the dogs classification is a mammal, 
    #we don't want to return illnesses that belong to a reptile classification
    
    #get the pet's classification id
    pet_classification = get_pets_classification_id(pet)
    
    illnesses_based_on_pets_classification = get_illnesses_based_on_pets_classification(pet_classification)

    #this illness_list will be returned so it needs to be serialized 
    illness_list = create_illness_list(illnesses_based_on_pets_classification, illness_ids)
      
    #Now we want to get all the medications that are used for the illness(s)
    #Illness model has medications in its serialization rule

    #Now we want to get only 2 or less products that the user can purchase for their pet's illness
    products_list = get_illness_medications_products(illness_list)

    #Now we have to serialize the illness and products list to add the products list to the illness object
    #this decision was made because illnessproducts table still needs to be created for products to
    #be added to the illnesses table
    serialized_illness_list = [illness_schema.dump(illness) for illness in illness_list]
    serialized_product_list = [product_schema.dump(product) for product in products_list]

    results = add_products_to_each_illness(serialized_illness_list, serialized_product_list)
    
    if not results:
      return {"error":"No Results found"}, 404
    
    return results, 200

    


api.add_resource(PetResults, '/user/pets/<int:id>/results', endpoint='user_pet_results')