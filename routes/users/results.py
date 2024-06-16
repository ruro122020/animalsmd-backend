from flask import request, session
from flask_restful import Resource
from config import api, db
from models.models import Symptom, IllnessSymptom, Illness, IllnessClassification, SpeciesClassification, Species
from sqlalchemy import func
from marshmallow_schemas.illness import illness_schema 

#implement considering species type


class Results(Resource):
  def post(self):
    #get symptoms from the request body
    pet_info = request.get_json()
    symptoms = pet_info.get("symptoms")
    #if symptoms don't exist return an error message
    if not symptoms:
      return {"error":"Symptoms are missing"}, 400
      
    #create a list of sypmtom id's: e.g. [1,3]
    symptom_ids = []

    for symptom_name in symptoms:
      symptom = Symptom.query.filter_by(name=symptom_name).first()
      symptom_ids.append(symptom.id)

    #find and count the symptoms_id in IllnessSymptoms that match the id's in symptoms_ids list
    illnesses = db.session.query(
        Illness,
        func.count(IllnessSymptom.symptom_id).label('match_count')
    #join the illness table to the IllnessSymptom table
    ).join(IllnessSymptom).filter(
    #filter illnessSymptom table by symptom_id and return the rows that match in the symptom_ids list
        IllnessSymptom.symptom_id.in_(symptom_ids)
    #calculate the number of matching symptoms for each illness
    ).group_by(Illness.id).order_by(
      #sorts illness from the most matched to the least matched 
        db.desc('match_count')
    ).all()

    illness_ids_list = []
    #even though count is not being used, it is setup this way so that illness won't be a tuple that includes
    #the count
    for illness, count in illnesses:
      illness_ids_list.append(illness.id)

    """
     Now that I have a list of illness id's:
    - query the speciesclassifications table to find the classification id of the species 
    - use classification's id to query the illnessclassifications table, return all illness that matched the classification_id
    - compare the returned list from illnessclassification to the illness_list
    """

    #  - query the speciesclassifications table to find the classification id of the species 
    pet_type = pet_info.get('type')
    species = Species.query.filter_by(type_name = pet_type).first()
    species_classification = SpeciesClassification.query.filter_by(species_id = species.id).first()
    pet_classification = species_classification.classification

    #  - use classification's id to query the illnessclassifications table, return all illness that matched the classification_id
    illness_classifications = IllnessClassification.query.filter_by(classification_id = pet_classification.id).all()

    #  - compare the returned list from illnessclassification to the illness_list
    illness_list = []
    for illness_classification in illness_classifications:
      if illness_classification.illness_id in illness_ids_list:
        illness = Illness.query.filter_by(id=illness_classification.illness_id).first()
        illness_list.append(illness_schema.dump(illness))

    return illness_list, 200

    


api.add_resource(Results, '/results', endpoint='results')