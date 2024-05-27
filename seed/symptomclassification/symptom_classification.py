from config import app, db
from models.models import Symptom, Classification, SymptomClassification
from .symptoms_classifications_data import symptoms_classifications_data

with app.app_context():
  for sypmtom_name, classification_names in symptoms_classifications_data.items():
    symptom = Symptom.query.filter_by(name=sypmtom_name.lower()).first()

    classification_db = []

    for classification_name in classification_names:
      classification = Classification.query.filter_by(classification = classification_name.lower()).first()
      classification_db.append(classification)

    for classification in classification_db:
      SymptomClassification.create(classification, symptom)
      