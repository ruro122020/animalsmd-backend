from config import db, app
from models.models import IllnessClassification, Illness, Classification
from .illnesses_classifications_data import illness_classification_data
from marshmallow_schemas import classifications_schema_many
#Steps
#STEP 1 -- COMPLETE
#we want to convert the data structure to be as follows:
#{
#   "reptile": ["scale rot"],
#   "ave":['avian flu',"psittacosis"],
#   "mammal": ["respiratory infection", "rabies", "canine distemper"]
# }
# ---create a function that will take in an list and convert it into the data structure above --- 

#STEP 2 - COMPLETE
#we need records of all the classifications, illnesses, and it's relationships that are in the 
#database. 
# ---create a function to returns a collection of classifications
# ---create a function to return a collection of illnesses
# ---create a function to return a collection of the relationship between illness and 
#classifications in illnessclasssification table

#STEP 3 - COMPLETE
#we want check if that illness already exist in the illnessClassification table
# --- create a function to return true if illness exist or return false if illness does
#NOT exist

#STEP 4 - COMPLETE
#we want to create a record in the illnessclassifications table
# #if the illness does NOT exist
# ---create a function to create the record




#convert_data_to_dict function converts the list to the data structure below:
#{
#   "reptile": ["scale rot"],
#   "ave":['avian flu',"psittacosis"],
#   "mammal": ["respiratory infection", "rabies", "canine distemper"]
# }
def convert_data_to_dict(list):
  converted_obj = {}
  for obj in list:
      converted_obj[obj.get('classification')] = obj.get('illnesses')
  return converted_obj

def get_full_records(model):
  with app.app_context():
    return model.query.all()

#has_record will return a bool, it only checks if a record exist in a list
def has_record(attribute, value, list):
  for instance in list:
    if getattr(instance, attribute) == value:
      return True
  return False

def retrieve_record(attribute, value, list):
  for instance in list:
    if getattr(instance, attribute) == value:
      return instance
  return None
  

def seed_illness_classification():
  with app.app_context():
    convert_data = convert_data_to_dict(illness_classification_data)
    classifications_collection = get_full_records(Classification)
    illnesses_collection = get_full_records(Illness)
    illnessclassifications_collection = get_full_records(IllnessClassification)
    for classification, illnesses in convert_data.items():
      for illness in illnesses:
        illness_instance = retrieve_record('name', illness, illnesses_collection)
        if not has_record('illness_id', illness_instance.id, illnessclassifications_collection):
          classification_instance = retrieve_record('classification', classification, classifications_collection)
          IllnessClassification.create_row(illness_instance, classification_instance)

seed_illness_classification()  
