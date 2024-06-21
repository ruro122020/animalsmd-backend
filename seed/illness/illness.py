from config import db, app
from models.models import Illness
from .illnesses_data import illnesses_data


def delete_illness_data():
  Illness.query.delete()
  db.engine.execute("ALTER SEQUENCE illnesses_id_seq RESTART WITH 1")
  
def seed_illness_table():
  with app.app_context():
    for illness, description_remedy_obj in illnesses_data.items():
      description = description_remedy_obj.get('description')
      remedy = description_remedy_obj.get('remedy')
      Illness.create_row(name=illness, description=description, remedy=remedy)

def update_illness_table():
    with app.app_context():
      for illness, description_remedy_obj in illnesses_data.items():
        illness = Illness.query.filter_by(name=illness).first()
        description = description_remedy_obj.get('description')
        remedy = description_remedy_obj.get('remedy')
        obj = {
          "illness": illness,
          "description": description,
          "remedy":remedy
        }
        illness.update_db(obj)



update_illness_table()