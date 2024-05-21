from config import db

class Symptom(db.Model):
  __tablename__ = 'symptoms'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, nullable=False)
  
  #relationships
  symptom_classification = db.relationship('SymptomClassification', back_populates='symptom')