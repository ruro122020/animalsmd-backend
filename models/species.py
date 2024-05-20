# from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from config import db


class Species(db.Model):
  __tablename__ = 'species'

  id = db.Column(db.Integer, primary_key=True)
  type = db.Column(db.String, nullable=False)

  #relationships
  species_classification = db.relationship('SpeciesClassification', back_populates='species')