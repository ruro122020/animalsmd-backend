from config import db, app
from models.models import IllnessClassification, Illness, Classification
from .illnesses_classifications_data import illness_classification_data


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


seed_illness_classification()  
