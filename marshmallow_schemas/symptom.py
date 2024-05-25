from config import ma
from models.models import Symptom
from flask_marshmallow.fields import fields

class SymptomSchema(ma.Schema):
  class Meta:
    model = Symptom
    load_instance = True

  symptom_classification = fields.Nested('SymptomClassificationSchema')
  id = ma.Integer()
  name = ma.String()
  symptom = ma.String()

symptom__schema = SymptomSchema()
symptom__schema_many = SymptomSchema(many=True)