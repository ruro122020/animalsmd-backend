from config import db

class IllnessRemedy(db.Model):
  __tablename__ = 'illnessesremedies'


  id = db.Column(db.Integer, primary_key=True, nullable=False)
  illness_id = db.Column(db.Integer, db.ForeignKey('illnesses.id'), nullable=False)
  remedy = db.Column(db.String, nullable=False)

  #relationships
  illness = db.relationship('Illness', back_populates='remedy')

  @classmethod
  def create_row(cls, illness, remedy):
    illness_remedy = cls(illness=illness, remedy=remedy)
    illness_remedy.save_db()
    return illness_remedy
  
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
