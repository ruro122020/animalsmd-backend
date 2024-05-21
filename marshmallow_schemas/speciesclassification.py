from config import ma
from models.models import SpeciesClassification
from flask_marshmallow.fields import fields


class SpeciesClassificationSchema(ma.Schema):
  class Meta:
    model = SpeciesClassification
    load_instance = True
    fields = ('id', 'classification', 'species')

  classification = fields.Nested("ClassificationSchema")
  species = fields.Nested("SpeciesSchema")
  id = ma.Integer()




species_classification_schema = SpeciesClassificationSchema()