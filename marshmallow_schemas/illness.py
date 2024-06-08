from config import ma
from models.models import Illness
from flask_marshmallow.fields import fields

class IllnessSchema(ma.Schema):
  class Meta:
    model = Illness
    load_instance = True
    fields = ('id', 'name')


illness_schema = IllnessSchema()
illness_schema_many = IllnessSchema(many=True)