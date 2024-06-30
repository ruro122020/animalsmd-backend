from flask_restful import Resource
from config import api
from flask import request
from models.models import Cart
from marshmallow_schemas.cart import cart_schema

class Cart(Resource):

  def post(self):
    json = request.get_json()
    
    if json:
      print(json.get('user_id'))
      print(json.get('product_id'))
      print(json.get('quantity'))

      #validations have not been setup for cart so for right now the user's id and product id must be passed
      try:
        # cart = Cart.create_row(json.get('user_id'), json.get('product_id'), json.get('quantity'))
        # return cart_schema.dump(cart), 200
        print(Cart)
      except Exception as e:
        return {"error": str(e)}, 404
    return {"error": "Cart Not Added"}, 400



    

api.add_resource(Cart, '/user/cart', endpoint='user_cart')