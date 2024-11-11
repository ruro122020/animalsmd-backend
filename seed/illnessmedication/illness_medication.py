from config import app
from models import illnessclassification
from .illnesses_medications_data import illness_medication_data
from models.models import IllnessMedication, Illness, Medication

def convert_data(list):
  new_data = {}
  for dict in list:
    new_data[dict.get('illness')] = dict.get('medications')
  return new_data

def retrieve_record(attribute, name, list):
  for instance in list:
    if getattr(instance, attribute) == name:
      return instance
  return None
    

def has_record(attribute, medication_id, list):
  for instance in list:
    if getattr(instance, attribute) == medication_id:
      return True
  return False

def retrieve_all_records(model):
  return model.query.all()

def create_records_in_db(illness, medications):
  illness_medication_collection = retrieve_all_records(IllnessMedication)
  medications_collection = retrieve_all_records(Medication)
  illnesses_collection = retrieve_all_records(Illness)
  for medication_name in medications:
    medication_instance = retrieve_record('name', medication_name, medications_collection)
    exist = has_record('medication_id', medication_instance.id, illness_medication_collection)
    if not exist:
      illness_instance = retrieve_record('name', illness, illnesses_collection)
      IllnessMedication.create_row(illness_instance, medication_instance)



def seed_illness_medications_table():
  with app.app_context():
    new_illness_medication_data = convert_data(illness_medication_data)
    for illness, medications in new_illness_medication_data.items():
      create_records_in_db(illness, medications)



        
seed_illness_medications_table()
