from flask_security import UserMixin
from .database import db

# from flask_login import login_manager


# @login_manager.user_loader
# def load_user(id):
#     return User.query.get(int(id))


class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(30), nullable=False)
    lname = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(300), nullable=False)
    role = db.Column(db.String(30), nullable=False)


#     active = db.Column(db.Boolean())
#     fs_uniquifier = db.Column(db.String(255), unique=True, nullable=False)


# class Role(db.Model, RoleMixin):
#     __tablename__ = "role"
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), unique=True)
#     description = db.Column(db.String(300))


# class RolesUsers(db.Model):
#     __tablename__ = "roles_users"
#     id = db.Column(db.Integer(), primary_key=True)
#     user_id = db.Column("user_id", db.Integer(), db.ForeignKey("user.id"))
#     role_id = db.Column("role_id", db.Integer(), db.ForeignKey("role.id"))
