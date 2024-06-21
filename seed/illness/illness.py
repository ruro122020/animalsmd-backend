from config import db, app
from models.models import Illness
from .illnesses_data import illnesses_data


def delete_illness_data():
  Illness.query.delete()
  db.engine.execute("ALTER SEQUENCE illnesses_id_seq RESTART WITH 1")
  
def seed_illness_table():
  with app.app_context():
    for illness, description_remedies_obj in illnesses_data.items():
      description = description_remedies_obj.get('description')
      remedies = description_remedies_obj.get('remedies')
      Illness.create_row(name=illness, description=description, remedies=remedies)

def update_illness_table():
  for illness, description_remedies_obj in illnesses_data.items():
    illness = Illness.query.filter_by(name=illness).first()
    description = description_remedies_obj.get('description')
    remedies = description_remedies_obj.get('remedies')
    obj = {
      "illness": illness,
      "description": description,
      "remedies":remedies
    }
    illness.update_db(obj)



seed_illness_table()