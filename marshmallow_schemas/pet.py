from config import ma
from models.models import Pet
from flask_marshmallow.fields import fields

class PetSchema(ma.Schema):
  class Meta:
    model = Pet
    load_instance = True
    
  id = ma.Integer()
  name=ma.String()
  age=ma.Integer()
  weight = ma.Integer()
  user_id= ma.Integer()
  pet_symptoms = fields.Nested("PetSymptomSchema")

pet_schema = PetSchema()
pet_schema_many = PetSchema(many=True)