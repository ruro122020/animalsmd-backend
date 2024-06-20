from config import db, app
from models.models import IllnessSymptom, Illness, Symptom
from .illnesses_symptoms_data import illness_symptom_data

with app.app_context():
  for illness in illness_symptom_data:
    illness_db = Illness.query.filter_by(name = illness).first()

    symptom_list_db = []
    #get id of symptoms array
    for symptom in illness_symptom_data[illness]:
      #query the database to get id of each symptom
      symptom_db = Symptom.query.filter_by(name=symptom).first()
      #add to symptom_list_db
      symptom_list_db.append(symptom_db)
    
    #iterate through symptoms_list_db and add a row to illness_symptoms table
    for symptom in symptom_list_db:
      IllnessSymptom.create_row(illness_db, symptom)