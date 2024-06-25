from itertools import product
from flask import request, session
from flask_restful import Resource
from config import app, db, api
from marshmallow_schemas.medication import medication_schema, medication_schema_many
from marshmallow_schemas.illness import illness_schema
from models.models import Illness
from models.models import Medication
from models.models import Product
from marshmallow_schemas.product import product_schema
class TestingRoute(Resource):
  def get(self):
    product = Product.query.first()
    return product_schema.dump(product)
    


api.add_resource(TestingRoute,'/test')