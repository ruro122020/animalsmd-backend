from config import ma
from models.models import Species
from flask_marshmallow.fields import fields

class SpeciesSchema(ma.Schema):
  class Meta:
    model = Species
    load_instance = True
    fields = ('id','type')

  species_classification = fields.Nested("SpeciesClassification")



species_schema = SpeciesSchema()
species_schema_many = SpeciesSchema(many=True)