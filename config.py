# Standard library imports

# Remote library imports
from flask import Flask
from flask_bcrypt import Bcrypt 
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flask_marshmallow import Marshmallow

import os

#enviroment variables
user = os.getenv('USER')
password = os.getenv('PASSWORD')
dbname = os.getenv('DBNAME')

# Local imports

# Instantiate app, set attributes
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user}:{password}@localhost:5432/{dbname}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False
#line below is not in use. Can be deleted, if needed
# app.config.update(SESSION_COOKIE_SAMESITE="None", SESSION_COOKIE_SECURE=True)

#session key configuration
app.secret_key= os.getenv('SECRET_KEY')

# Define metadata, instantiate db
metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})
db = SQLAlchemy(metadata=metadata)
migrate = Migrate(app, db)
# migrate.init_app(app, db, render_as_batch=True)
db.init_app(app)

# Instantiate Marshmellow
ma = Marshmallow(app)

# Instantiate Bcrypt
bcrypt = Bcrypt(app)

# Instantiate REST API
api = Api(app)

# Instantiate CORS
CORS(app)
#just in case cookies are not being set again. Try add this line to the line above. 
#, supports_credentials=True
