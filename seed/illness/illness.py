from config import db, app
from models.models import Illness
from .illnesses_data import illnesses_data

#helpers

def has_illness(illness):
  illness_db = Illness.query.filter_by(name=illness).first()
  return illness_db

#############

def addToPopulatedTable():
  with app.app_context():
    for illness, description in illnesses_data.items():
      if bool(has_illness(illness)):
        Illness.create_row(name=illness, description=description)

def seed_empty_table():
  with app.app_context():
    for illness, description in illnesses_data.items():
      Illness.create_row(name=illness, description=description)


seed_empty_table()
