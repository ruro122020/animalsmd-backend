from config import ma
from models.models import Symptom
from flask_marshmallow.fields import fields

class SymptomClassificationSchema(ma.Schema):
  class Meta:
    model = Symptom
    load_instance = True
    fields = ('id', 'name', 'symptom_classification')


symptom_classification_schema = SymptomClassificationSchema()