from config import db, app
from models.models import Species
from .species_data import species_data

with app.app_context():
  #create species
  for element in species_data:
    species=Species(type_name=element)
    Species.create(species)
