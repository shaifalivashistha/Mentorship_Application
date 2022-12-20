from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True)
    fname = db.Column(db.String(30), nullable = False)
    lname = db.Column(db.String(30), nullable = False)
    email = db.Column(db.String(30), unique=True, nullable = False)
    username = db.Column(db.String(30), unique=True, nullable = False)
    password = db.Column(db.String(300), nullable=False)
    subjects = db.Column(db.String(30), nullable = True)
    role = db.Column(db.String(30), nullable = False)
    linkedin = db.Column(db.String, nullable = True)

