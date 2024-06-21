from flask import request, session
from flask_restful import Resource
from config import app, db, api
from marshmallow_schemas.medication import medication_schema, medication_schema_many
from marshmallow_schemas.illness import illness_schema
from models.models import Illness
from models.models import Medication

class TestingRoute(Resource):
  def get(self):
    illness = Illness.query.first()
    return illness_schema.dump(illness)
    


api.add_resource(TestingRoute,'/test')