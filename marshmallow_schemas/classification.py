from config import ma
from models.models import Classification
from flask_marshmallow.fields import fields

class ClassificationSchema(ma.Schema):
  class Meta:
    model = Classification
    load_instance = True
    # fields = ('id','classification')
  
  id = ma.Integer()
  classification = ma.String()


classification_schema = ClassificationSchema()