from config import db

class SymptomClassification(db.Model):
  __tablename__ = 'symptomsclassifications'

  id = db.Column(db.Integer, primary_key=True)
  classification_id = db.Column(db.Integer, db.ForeignKey('classifications.id'))
  symptoms_id = db.Column(db.Integer, db.ForeignKey('symptoms.id'))

  classification = db.relationship('Classification', back_populates='symptom_classification')
  symptom = db.relationship('Symptom', back_populates='symptom_classification')