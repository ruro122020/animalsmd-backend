from flask import request, session
from flask_restful import Resource
from config import app, db, api
from marshmallow_schemas.medication import medication_schema, medication_schema_many


from models.models import Medication
class TestingRoute(Resource):
  def get(self):
    medication = Medication.query.first()
    return medication_schema.dump(medication)
    


api.add_resource(TestingRoute,'/test')