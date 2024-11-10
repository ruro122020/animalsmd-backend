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



def seed_illness_classification():
 
  with app.app_context():
    for classification_name, illness_list in illness_classification_data.items():
      classification = Classification.query.filter_by(classification = classification_name).first()

      for illness_name in illness_list:
        illness = Illness.query.filter_by(name=illness_name).first()
        #in illnessclassification table each illness should be assigned to a classification id number
        #check if illness already exist in illnessesclassifications table 
        illness_exist = IllnessClassification.query.filter_by(illness_id = illness.id ).first()
        if not illness_exist:
          IllnessClassification.create_row(illness, classification)


# seed_illness_classification()  

#Steps
#we want to convert the data structure to be as follows:
#{
#   "reptile": ["scale rot"],
#   "ave":['avian flu',"psittacosis"],
#   "mammal": ["respiratory infection", "rabies", "canine distemper"]
# }
# ---create a function that will take in an list and convert it into the data structure above --- complete

#we need records of all the classifications, illnesses, and it's relationships that are in the 
#database. 
# ---create a function to returns a collection of classifications
# ---create a function to return a collection of illnesses
# ---create a function to return a collection of the relationship between illness and 
#classifications in illnessclasssification table

#we want check if that illness already exist in the illnessClassification table
# --- create a function to return true if illness exist or return false if illness does
#NOT exist

#we want to create a record in the illnessclassifications table
# #if the illness does NOT exist
# ---create a function to create the record



