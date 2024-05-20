from config import db

class UsersSpecies(db.Model):
  __tablename__ = 'usersspecies'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, nullable=False)
  age = db.Column(db.Integer, nullable=False)
  weight = db.Column(db.Integer, nullable=False)
  species_id = db.Column(db.Integer, db.ForeignKey('species.id'))
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

  #relationships
