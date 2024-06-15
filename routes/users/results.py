from flask import request, session
from flask_restful import Resource
from config import api, db
from models.models import Symptom, IllnessSymptom, Illness
from sqlalchemy import func
from marshmallow_schemas.illness import illness_schema 

#implement considering species type

"""
 Now that I have a list of illness:
  - create illnessclassifications 
  - seed data in illnessclassifications
  - query the speciesclassifications table to find the classification of the species 
  - use classification's id to query the illnessclassifications table, return all illness that matched the classification_id
  - compare the returned list from illnessclassification to the illness_list
"""
class Results(Resource):
  def post(self):
    #get symptoms from the request body
    symptoms = request.get_json().get("symptoms")
    print('petInfo', request.get_json())
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

    print('illnesses', illnesses)
    illness_list = []
    #even though count is not being used, it is setup this way so that illness won't be a tuple that includes
    #the count
    for illness, count in illnesses:
      illness_list.append(illness_schema.dump(illness))

    return illness_list, 200

    


api.add_resource(Results, '/results', endpoint='results')