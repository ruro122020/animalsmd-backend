from .medications_data import medications_data
from config import app
from models.models import Medication

def seed_medications_table():
  with app.app_context():
    Medication.query.delete()

    for medication, description in medications_data.items():
      Medication.create_row(medication, description)
      

seed_medications_table()