from config import app
from .illnesses_medications_data import illness_classification_data
from models.models import IllnessMedication, Illness, Medication

def seed_illness_medications_table():
  
  with app.app_context():
    for illness_name, medications in illness_classification_data.items():
      #get illness from illnesses table
      illness = Illness.query.filter_by(name=illness_name).first()
      for medication_name in medications:
        #get medication from medications table
        medication = Medication.query.filter_by(name=medication_name).first()
        #create row
        IllnessMedication.create_row(illness, medication)
        
seed_illness_medications_table()