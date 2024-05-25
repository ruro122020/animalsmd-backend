from config import app, db
from models.models import Symptom


symptoms = [
  'severe vomiting, often containing blood',
  'bloody diarrhea',
  'lethargy',
  'weekness',
  'high fever',
  'lack of appetite',
  'nasal discharge(pus-like)',
  'seizures',
  'paralysis',
  'persistent cough, especially during exercise',
  'difficulty breathing',
  'rapid breathing',
  'fainting',
  'jaundice',
  'severe abdominal pain',
  'dehydration',
  'distended abdomen(often appearing swollen or tight)',
  'unproductive attempts to vomit',
  'straining to urinate',
  'inability to urinate',
  'blood in urine',
  'excessive thirst',
  'excessive urination',
]
with app.app_context():

  created_symptoms = list()
  for element in symptoms:
    symptom = Symptom(name=element)
    created_symptoms.append(symptom)
  
  db.session.add_all(created_symptoms)
  db.session.commit()