from config import db, app
from models.models import IllnessClassification, Illness, Classification
from .illnesses_classifications_data import illness_classification_data

with app.app_context():
  for classification_name in illness_classification_data:
    #query classification table for classification id 
    classification = Classification.query.filter_by(classification = classification_name).first()

   
    for illness_name in illness_classification_data[classification_name]:
      illness = Illness.query.filter_by(name=illness_name).first()
      #create a row in IllnessClassifications with the illness id and classification id
      IllnessClassification.create_row(illness, classification)    
