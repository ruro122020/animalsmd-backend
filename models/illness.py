from config import db
from sqlalchemy.orm import validates
from sqlalchemy.ext.hybrid import hybrid_property

class Illness(db.Model):
  __tablename__ = 'illnesses'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, nullable=False)
  
  #relationship with illnesses table
  illness_symptom = db.relationship('IllnessSymptom', back_populates='illness', cascade="all, delete-orphan")

  @hybrid_property
  def symptoms(self):
    return []
  @classmethod
  def create_row(cls, name):
    illness = cls(name = name)
    illness.save_db()
    return illness
  
  def save_db(self):
    db.session.add(self)
    db.session.commit()

  def update_db(self, new_values):
    for key, value in new_values.items():
      setattr(self, key, value)
    db.session.commit()

  def delete_db(self):
    db.session.delete(self)
    db.session.commit()