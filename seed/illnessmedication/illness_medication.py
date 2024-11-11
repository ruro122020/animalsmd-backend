from config import app
from .illnesses_medications_data import illness_medication_data
from models.models import IllnessMedication, Illness, Medication

#STEPS
#STEP 1 - complete
# --- create a function to convert the data structure to something like the following:
#{
#  'respiratory infection': ['enrofloxacin (Baytril)', 'ceftazidime (Fortaz)']
#}

# Once data structure is converted, iterate through it
#for illness, medications in converted_data:
#for medication in medications:
#check if medication exist in IllnessMedication
# --- create a function to check if medication exist in illnessMedication table
#if medication exist, do nothing
#if medication doesn't exist then create the record


def convert_data(list):
  new_data = {}
  for dict in list:
    new_data[dict.get('illness')] = dict.get('medications')
  return new_data

def retrieve_record(attribute, name, list):
  for instance in list:
    if getattr(instance, attribute) == name:
      return instance
    

def has_record(attribute, medication_id, list):
  for instance in list:
    if getattr(instance, attribute) == medication_id:
      return True
  return False


def seed_illness_medications_table():
  with app.app_context():
    #query the database to get all the record in illness_medication
    illness_medication_collection = IllnessMedication.query.all()
    medications_collection = Medication.query.all()
    new_illness_medication_data = convert_data(illness_medication_data)

    for illness, medications in new_illness_medication_data.items():
      for medication_name in medications:
        #iterate through medications_collection to find the medication instance so we have access to medication id
        #--- create a function to return the medication instance
        # iterate through illness_medication_collection to check if medication exist 
        #---create a function to check if medication exist in the illness_medication_collection
        #create record if medication id is not found in illness_medication_collection
        # - to create the record we need the illness and medication instance
        pass


        
seed_illness_medications_table()



























































  # with app.app_context():
  #   for illness_name, medications in illness_medication_data.items():
  #     #get illness from illnesses table
  #     illness = Illness.query.filter_by(name=illness_name).first()
  #     #check if illness ID is in illnessmedication table
  #     illness_exist = IllnessMedication.query.filter_by(illness_id = illness.id).first()
  #     if not illness_exist:
  #       for medication_name in medications:
  #         #get medication from medications table
  #         medication = Medication.query.filter_by(name=medication_name).first()
  #         #create row
  #         IllnessMedication.create_row(illness, medication)