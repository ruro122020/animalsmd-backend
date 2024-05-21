from sqlalchemy.orm import validates
from config import db


class Classification(db.Model):
  __tablename__ = 'classifications'

  id = db.Column(db.Integer, primary_key=True)
  classification = db.Column(db.String, nullable=False)

  #relationships
  #relationship between species and classification. This line points to SpeciesClassification association table
  species_classification = db.relationship('SpeciesClassification', back_populates='classification')
  #relationship between symptoms and classification. This line points to SymptomClassification association table
  symptom_classification = db.relationship('SymptomClassification', back_populates='classification')