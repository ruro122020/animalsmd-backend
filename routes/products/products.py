from flask_restful import Resource
from config import api
from models.models import Product
from marshmallow_schemas.product import product_schema_many
class Products(Resource):
  def get(self):
    products = Product.query.all()
    if not products:
      return {
      "status": "failed",
      "error":{"message": "Products do not exist"},
      "code": 400
    }, 400
    
    return {
      "status": "success",
      "data": product_schema_many.dump(products),
      "code": 200
    }, 200


api.add_resource(Products, '/products', endpoint='products')