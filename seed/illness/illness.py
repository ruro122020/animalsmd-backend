from config import db, app
from models.models import Illness
from .illnesses_data import illnesses_data


def seed_illness_table():
  with app.app_context():
    Illness.query.delete()

    for illness, description_remedies_obj in illnesses_data.items():
      description = illnesses_data[illness]
      Illness.create_row(name=illness, description=description)
  

seed_illness_table()