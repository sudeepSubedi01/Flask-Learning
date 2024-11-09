from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ipl.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Team(db.Model):
  __tablename__ = 'iplteams'
  id = db.Column(db.Integer, primary_key=True)
  team = db.Column(db.String, nullable=False, unique=True)
  state = db.Column(db.String, nullable=False)
  members = db.relationship('Player', backref='team')

  def __repr__(self):
    return f"Team('{self.id}','{self.team}','{self.state}')"
  
class Player(db.Model):
  __tablename__ = 'iplplayers'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, nullable=False)
  nationality = db.Column(db.String, nullable=False)
  team_id = db.Column(db.Integer, db.ForeignKey('iplteams.id'))

  def __repr__(self):
    return f"Team('{self.id}','{self.name}','{self.nationality}')"