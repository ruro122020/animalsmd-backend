from .medications_data import medications_data
from config import app
from models.models import Medication

def add_data_to_medications_table():
  with app.app_context():
    Medication.query.delete()

    for medication, description in medications_data.items():
      Medication.create_row(medication, description)
      

add_data_to_medications_table()