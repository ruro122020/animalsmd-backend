from flask_restful import Resource
from config import api
from flask import request, session
from models.models import Cart, User, Product
from marshmallow_schemas.cart import cart_schema, cart_schema_many
from marshmallow_schemas.product import product_schema

#IMPORTANT MESSAGE: This resource hold the products in the carts

class CartResource(Resource):
  def get(self):
    carts = Cart.query.filter_by(user_id=session.get('user_id')).order_by(Cart.id).all()
   
    if not carts:
      return {
      "status":'failed',
      "error": {"message":"There are no products in user's cart"},
      "code": 400
      }
    
    serialized_carts = cart_schema_many.dump(carts)

    return {
      "status": "success",
      "data": serialized_carts,
      "code": 200
    }
  
  def post(self):
    json = request.get_json()
    
    if json:
      try:
        #check if user exist
        user = User.query.filter_by(id=json.get('user_id')).first()
        if not user:
          return {
            "status":"failed",
            "error": {"message": "user does not exist"}, 
            "code": 404
            }
        #check if product exist
        product = Product.query.filter_by(id = json.get('product_id')).first()
        if not product:
          return {
            "status":"failed",
            "error": {"message": "product does not exist"},
            "code": 400
          }
        
        #check if product already exist in user's cart
        if product in user.cart_products:          
          return {
            "status": "failed",
            "error": {"message":"Product already exist in user's cart"},
            "code": 403
            }
        
        cart = Cart.create_row(user, product, json.get('quantity'))
        return {
          "status":"success",
          "data": cart_schema.dump(cart),
          "code": 200
          }
      except Exception as e:
        return {
          "status":"failed",
          "error":{"message": str(e)},
          "code": 404
          }
    return {
      "status": "failed",
      "error": {"message": "Cart Not Added"},
      "code": 400
      }
  
  #this delete is if you want to delete all the products in carts table
  def delete(self):
    user_session_id = session.get('user_id')
    if user_session_id:
      carts = Cart.query.filter_by(user_id = user_session_id).all()
      if carts:
        for cart in carts:
          cart.delete_db()
        return {
          "status": "success",
          "message":"Cart Successfully Deleted!",
          "code":200
        }
    return {
      "status": "failed",
      "error": {"message": "Products don't exist"},
      "code": 400
      }
    

api.add_resource(CartResource, '/user/cart', endpoint='user_cart')