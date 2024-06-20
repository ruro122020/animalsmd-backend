from config import app, db
from models.models import Symptom
from .symptoms_data import symptoms_data


with app.app_context():
  for element in symptoms_data:
    Symptom.create_row(element)