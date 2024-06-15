from flask import request, session
from flask_restful import Resource
from config import api

class Results(Resource):
  def get(self):
    
    pass


api.add_resource(Results, '/results', endpoint='results')