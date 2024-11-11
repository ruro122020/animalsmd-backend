from config import db, app
from models.models import IllnessClassification, Illness, Classification
from .illnesses_classifications_data import illness_classification_data

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

#get_full_records queries the database and returns an array of instances
def get_full_records(model):
  with app.app_context():
    return model.query.all()

#has_record will return a bool, it only checks if a record exist in a list of instances
def has_record(attribute, value, list):
  for instance in list:
    if getattr(instance, attribute) == value:
      return True
  return False

#retrieve_record will return an instance, it only returns 1 instance if it exist, None if it doesn't
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
