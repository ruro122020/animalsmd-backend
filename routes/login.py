from flask import request, session, jsonify
from flask_restful import Resource
from config import api
from models.models import User
from marshmallow_schemas.users import user_schema

class Login(Resource):
  def post(self):
    json = request.get_json()
    user = User.query.filter(User.username == json.get('username')).first()

    if user:
      if user.authenticate(json.get('password')):
        session['user_id'] = user.id
        return {
          "status": "success",
          "data": user_schema.dump(user),
          "code": 200
        }
      else:
        return {
          "status": 'failed',
          "error":{'message':'Invalid Credentials'},
          "code": 401
        }
    else:
      return {
        "status": "failed",
        "error":{'message': 'User does NOT exist'},
        "code": 400
      }


api.add_resource(Login, '/login', endpoint='login')