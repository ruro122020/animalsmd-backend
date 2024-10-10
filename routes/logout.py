from flask import request, session
from flask_restful import Resource
from config import app, db, api

class Logout(Resource):
  def delete(self):

    if not session.get('user_id'):
      return {
        "status": "failed",
        "error":{"message": "not logged in"},
        "code": 401
      }
    
    session['user_id'] = None
    return {
      "status": "success",
      "message":"Logout Successful",
      "code":200
    }

api.add_resource(Logout, '/logout', endpoint='logout')