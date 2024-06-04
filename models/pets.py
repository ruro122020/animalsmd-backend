from sqlalchemy.orm import validates
from config import db
from sqlalchemy.ext.hybrid import hybrid_property

class Pet(db.Model):
  __tablename__ = 'pets'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(), nullable=False)
  age = db.Column(db.Integer, nullable=False)
  weight = db.Column(db.Integer, nullable=False)
  species_id = db.Column(db.Integer, db.ForeignKey('species.id'), nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
