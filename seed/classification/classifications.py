from config import db, app
from models.models import Classification
from .classifications_data import classifications_data

with app.app_context():
  created_classification = list()

  for element in classifications_data:
    classification = Classification(classification=element)
    created_classification.append(classification)
  
  db.session.add_all(created_classification)
  db.session.commit()