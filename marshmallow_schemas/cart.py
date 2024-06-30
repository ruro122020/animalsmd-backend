from config import ma
from models.models import Cart
from flask_marshmallow.fields import fields

class CartSchema(ma.Schema):
  class Meta:
    model = Cart
    load_instance=True
    field = ('id', 'quantity', 'user', 'products')

  user = fields.Nested('UserSchema')
  products = fields.List(fields.Nested('ProductSchema'))


cart_schema = CartSchema()
cart_schema_many = CartSchema(many=True)

