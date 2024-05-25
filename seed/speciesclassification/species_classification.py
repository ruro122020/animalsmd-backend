from config import db, app
from models.models import SpeciesClassification, Species, Classification
from .data import species_classification_data
from marshmallow_schemas.classification import classifications_schema_many
from marshmallow_schemas.species import species_schema_many

 
with app.app_context():
  pass


  # db.session.add_all(species_classifications)
  # db.session.commit()
# species_classification = SpeciesClassification(classification_id=1, species_id=2)
# db.session.add(species_classification)
# db.session.commit()