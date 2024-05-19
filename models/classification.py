from sqlalchemy.orm import validates
from config import db


class Classification(db.Model):
  __tablename__ = 'classifications'

  id = db.Column(db.Integer, primary_key=True)
  classification = db.Column(db.String, nullable=False)
