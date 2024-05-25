from config import db, app
from models.models import SpeciesClassification, Species, Classification
from .species_classifications_data import species_classification_data

 
with app.app_context():
  for type in species_classification_data:
    #query species table for species
    species_query = Species.query.filter(Species.type == type).first()
    #query classification table for the classification
    classification = Classification.query.filter_by(classification = species_classification_data[type]).first()
    #create species_classification 
    SpeciesClassification.create(species_query, classification)
