from config import db
from sqlalchemy.orm import validates
from sqlalchemy.ext.hybrid import hybrid_property

class SymptomClassification(db.Model):
  __tablename__ = 'symptomsclassifications'

  id = db.Column(db.Integer, primary_key=True)
  classification_id = db.Column(db.Integer, db.ForeignKey('classifications.id'))
  symptoms_id = db.Column(db.Integer, db.ForeignKey('symptoms.id'))

  classification = db.relationship('Classification', back_populates='symptom_classification')
  symptom = db.relationship('Symptom', back_populates='symptom_classification')

  #relationships

  
  @validates("classification_id")
  def validates_classification(self,key, classification_id):
    if classification_id is None:
      raise ValueError('classification must not be None')
    return classification_id
  
  @validates('symptom_id')
  def validate_symptom(self, key, symptom_id):
    if symptom_id is None:
      raise ValueError('symptom_id must not be None')
    return symptom_id
  
  @hybrid_property
  def classification_obj(self):
    return self._classification 
  
  @classification_obj.setter
  def classification_obj(self, value):
    from models.models import Classification
    if not isinstance(value, Classification):
      raise ValueError('value must be an instance of Classification')
    else:
      self._classification = value

  @hybrid_property
  def symptom_obj(self):
    return self._symptom
  
  @symptom_obj.setter
  def symptom_obj(self, value):
    from models.models import Symptom
    if not isinstance(value, Symptom):
      raise ValueError("value must be an instance of Symptom")
    else:
      self._symptom = value

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
    db.session.delete(self)
    db.session.commit()