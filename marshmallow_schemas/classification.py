from config import ma
from models.models import Classification

class ClassificationSchema(ma.Schema):
  class Meta:
    model = Classification
    load_instance = True
    fields = ['id','classification']



classification_schema = ClassificationSchema()