from flask_sqlalchemy import SQLAlchemy
import uuid

db = SQLAlchemy()

# User table
class User(db.Model):
   id = db.Column(db.String(), primary_key = True, default = lambda: str(uuid.uuid4()))
   username = db.Column(db.String())
   email = db.Column(db.String(), unique = True)