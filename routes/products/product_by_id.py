from config import api
from flask_restful import Resource
from models.models import Product
class ProductById(Resource):

  def get(self, id):
    product = Product.query.filter_by(id=id).first()
    print(product)
    pass

api.add_resource(ProductById, '/products/<int:id>', endpoint='')