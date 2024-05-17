from config import ma
from models.models import User


class UserSchema(ma.Schema):
  class Meta:
    model = User
    load_instance = True

  id = ma.Integer()
  name = ma.String()
  email = ma.String()
  username = ma.String()




user_schema = UserSchema()