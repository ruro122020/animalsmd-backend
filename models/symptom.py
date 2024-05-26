from config import db
from sqlalchemy.orm import validates
from sqlalchemy.ext.hybrid import hybrid_property

class Symptom(db.Model):
  __tablename__ = 'symptoms'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, nullable=False)
  
  #relationships
  symptom_classification = db.relationship('SymptomClassification', back_populates='symptom')


  @validates('name')
  def validates_name (self, key, name):
    if name is None or type(name) == str:
      raise ValueError("name must not be None. Must be of a string")
    else:
      self._name = name

  @classmethod
  def create(cls, type_name):
    type_name = cls(type_name = type_name)
    type_name.save()
    return type_name
  
  def save(self):
    db.session.add(self)
    db.session.commit()

  def update_db(self, new_values):
    for new_value in new_values:
      setattr(self, new_value, new_values.get(new_value))

    db.session.add(self)
    db.session.commit()

  def delete_db(self):
    db.session.delete(self.id)
    db.session.commit()