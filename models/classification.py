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
    