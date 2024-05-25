from sqlalchemy.orm import validates
from config import db
from sqlalchemy.ext.hybrid import hybrid_property


class Classification(db.Model):
  __tablename__ = 'classifications'

  id = db.Column(db.Integer, primary_key=True)
  classification = db.Column(db.String, nullable=False)

  #relationships
  #relationship between species and classification. This line points to SpeciesClassification association table
  species_classification = db.relationship('SpeciesClassification', back_populates='classification')
  #relationship between symptoms and classification. This line points to SymptomClassification association table
  symptom_classification = db.relationship('SymptomClassification', back_populates='classification')

  #hybrid_property is being used for the getter and setter 
  #because classification and species attributes are NOT columns
  #in the database and @validates, validates columns not instances
  @validates('classification')
  def validates_classification(self, key, classification):
    if classification is None or type(classification) != str:
      raise ValueError('classification must not be None. Must be of type string')

  @hybrid_property
  def species_classification_obj(self):
    return self._classification 
  
  @species_classification.setter
  def species_classification_obj(self, value):
    from models.models import SpeciesClassification
    if not isinstance(value, SpeciesClassification):
      raise ValueError('classification must be an instance of Classification')
    else:
      self._species_classification = value

    
  @classmethod
  def create_row(cls, classification):
    classification = cls(classification=classification)
    classification.save_db()
    return classification
  
  def save_db(self):
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
    