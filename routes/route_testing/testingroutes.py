from itertools import product
from flask import request, session
from flask_restful import Resource
from config import app, db, api
from marshmallow_schemas.medication import medication_schema, medication_schema_many
from marshmallow_schemas.illness import illness_schema
from models.models import Illness
from models.models import Medication
from models.models import Product, User
from marshmallow_schemas.product import product_schema
from models.models import Cart
from marshmallow_schemas.cart import cart_schema_many
from marshmallow_schemas.users import user_schema
from marshmallow_schemas.illness import illness_schema
from marshmallow_schemas.illnessproduct import illness_product
from models.models import IllnessProduct

class TestingRoute(Resource):
  def get(self):
    illness = IllnessProduct.query.filter_by(illness_id = 6).first()

    print('illness product')
    return illness_product.dump(illness)
    


api.add_resource(TestingRoute,'/test')