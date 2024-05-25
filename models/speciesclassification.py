from config import db
from sqlalchemy.orm import validates

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
    from models.models import Classification
    if classification is None:
      raise ValueError('classification must not be None')
    #check if classification is an instance of Classification
    classification = Classification.query.filter_by(classification=classification).first()
    if not isinstance(classification, Classification):
      raise ValueError('classification must be an instance of Classification')
    
  
  @validates('species')
  def validate_species(self, key, species):
    from models.models import Species
    if species is None:
      raise ValueError('classification_id must not be None')
    #check if classification is an instance of Classification
    species = Species.query.filter_by(species=species).first()
    if not isinstance(species, Species):
      raise ValueError('species must be an instance of Species')
    
  @classmethod
  def create(cls, species, classification):
    species_classification = cls(classification_id=classification, species_id=species)
    species_classification.save()
    return species_classification
  
  def save(self):
    db.session.add(self)
    db.session.commit()