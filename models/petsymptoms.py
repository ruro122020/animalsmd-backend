from sqlalchemy.orm import validates
from config import db
from sqlalchemy.ext.hybrid import hybrid_property


class PetSymptom(db.Model):
  __tablename__ = 'petsymptoms'

  id = db.Column(db.Integer, primary_key=True)
  pet_id = db.Column(db.Integer, db.ForeignKey('pets.id'))
  symptom_id = db.Column(db.Integer, db.ForeignKey('symptoms.id'))