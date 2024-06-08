from config import db
from sqlalchemy.orm import validates
from sqlalchemy.ext.hybrid import hybrid_property

class Illness(db.Model):
  __tablename__ = 'illnesses'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, nullable=False)

  @classmethod
  def create_row(cls, name):
    name = cls(name = name)
    name.save_db()
    return name
  
  def save_db(self):
    db.session.add(self)
    db.session.commit()

  def update_db(self, new_values):
    for key, value in new_values.items():
      setattr(self, key, value)
    db.session.commit()

  def delete_db(self):
    db.session.delete(self)
    db.session.commit()