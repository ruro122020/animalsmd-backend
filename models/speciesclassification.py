from config import db
from sqlalchemy.orm import validates
from models.models import Classification, Species

class SpeciesClassification(db.Model):
  __tablename__ = 'speciesclassifications'

  id = db.Column(db.Integer, primary_key=True)
  classification_id = db.Column(db.Integer, db.ForeignKey('classifications.id'))
  species_id = db.Column(db.Integer, db.ForeignKey('species.id'))

  
  #relationships
  classification = db.relationship('Classification', back_populates='species_classification')
  species = db.relationship('Species', back_populates='species_classification')


  @validates('classification')
  def validate_classification(self, key, classification):
    #check if classification is an instance of Classification
    classification = Classification.query.filter_by(classification=classification).first()
    if not isinstance(classification, Classification):
      raise ValueError('classification needs to be an instance of Classification')
    
  
  @validates('species')
  def validate_species(self, key, species):
    #check if classification is an instance of Classification
    species = Species.query.filter_by(species=species).first()
    if not isinstance(species, Species):
      raise ValueError('species needs to be an instance of Species')