from config import db, app
from models.models import Species

species = ['dog', 'cat', 'parrot', 'cockatiel', 'turtle', 'bearded dragon']

with app.app_context():
  created_species = list()
  for element in species:
    species=Species(type=element)
    created_species.append(species)

  db.session.add_all(created_species)
  db.session.commit()
 

