from config import api
from flask_restful import Resource
from models.models import Product
from marshmallow_schemas.product import product_schema

class ProductById(Resource):

  def get(self, id):
    product = Product.query.filter_by(id=id).first()
    if product:
      return {
        "status": "success",
        "data": product_schema.dump(product),
        "code": 200
      }, 200

    return {
      "status": "failed",
      "error":{"message":"Product not found"},
      "code": 404
    }, 404
  
api.add_resource(ProductById, '/products/<int:id>', endpoint='')