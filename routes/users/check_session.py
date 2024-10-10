from flask import request, session
from flask_restful import Resource
from config import app, db, api
from models.models import User
from marshmallow_schemas.users import user_schema

class CheckSession(Resource):
  def get(self):
    
    if not session.get('user_id'):
      return {
        "status":"failed",
        "error":{"message": "User Not logged in"},
        "code": 401
      }
    
    user = User.query.filter(User.id == session.get('user_id')).first()
    return {
      "status": "success",
      "data": user_schema.dump(user),
      "code": 200
    }
  

api.add_resource(CheckSession, '/check_session')