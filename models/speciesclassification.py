from config import db

class SpeciesClassification(db.Model):
  __tablename__ = 'speciesclassifications'

  id = db.Column(db.Integer, primary_key=True)
  classification_id = db.Column(db.Integer, db.ForeignKey('classifications.id'))
  species_id = db.Column(db.Integer, db.ForeignKey('species.id'))

  
  #relationships
  classification = db.relationship('Classification', back_populates='species_classification')
  species = db.relationship('Species', back_populates='species_classification')