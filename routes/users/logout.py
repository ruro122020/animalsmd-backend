from flask import request, session
from flask_restful import Resource
from config import app, db, api

class Logout(Resource):
  def delete(self):
    if session.get('user_id'):
      session['user_id'] = None
      return {}, 204
    
    return {'error': 'not logged in'}, 401

api.add_resource(Logout, '/logout', endpoint='logout')