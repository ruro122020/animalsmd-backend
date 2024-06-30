from flask_restful import Resource
from config import api
from flask import request

class Cart(Resource):

  def post(self):
    json = request.get_json()
    print('json', json)
    pass


api.add_resource(Cart, '/user/cart/', endpoint='user_cart')