from config import db, app
from models.models import Illness
from .illnesses_data import illnesses_data

with app.app_context():
  for illness in illnesses_data:
    Illness.create_row(name=illness)
