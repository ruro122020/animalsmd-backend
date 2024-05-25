from config import db, app
from models.models import Classification


classifications = ['mammal', 'reptile', 'aves']


with app.app_context():
  created_classification = list()

  for element in classifications:
    classification = Classification(classification=element)
    created_classification.append(classification)
  
  db.session.add_all(created_classification)
  db.session.commit()