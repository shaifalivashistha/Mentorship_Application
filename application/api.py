# from flask.helpers import flash
# from flask.templating import render_template
# from flask_restful import Resource, Api
# from flask_restful import fields, marshal_with
# from flask_restful import reqparse
# from .models import User
# from . import db
# from flask import current_app as app
# import werkzeug
# from flask import abort, redirect, url_for
# from werkzeug.security import generate_password_hash

# # from validation import AlreadyExists
# import random

# user_post_args = reqparse.RequestParser()
# user_post_args.add_argument("fname", type=str)
# user_post_args.add_argument("lname", type=str)
# user_post_args.add_argument("email", type=str)
# user_post_args.add_argument("username", type=str)
# user_post_args.add_argument("password", type=str)
# user_post_args.add_argument("role", type=str)

# user_fields = {
#     "fname": fields.String,
#     "lname": fields.String,
#     "email": fields.String,
#     "username": fields.String,
#     "password": fields.String,
#     "role": fields.String,
# }


# class UserAPI(Resource):
#     @marshal_with(user_fields)
#     def post(self):
#         print("in user api print")
#         print(user_post_args.parse_args())
#         args = user_post_args.parse_args()
#         print("abcd")
#         u = User.query.filter_by(username=args["username"]).first()
#         print(u)
#         if u:
#             flash("Username is already in use.", category="error")
#             return redirect("/register")
#         elif len(args["username"]) < 6:
#             flash("Username is too short.", category="error")
#             return redirect("/register")
#         elif len(args["password"]) < 6:
#             flash("Password is too short.", category="error")
#             return redirect("/register")
#         print("checks passed")
#         new_user = User(
#             fname=args["fname"],
#             lname=args["lname"],
#             email=args["email"],
#             username=args["username"],
#             password=generate_password_hash(args["password"], method="sha256"),
#             role=args["role"],
#         )
#         try:
#             db.session.add(new_user)
#             db.session.commit()
#             return redirect("/login")
#         except:
#             return redirect("/register")

#     def get(self, username):
#         u = User.query.filter_by(username=username).first()
#         return {
#             "username": u.username,
#         }

from flask import flash, render_template, jsonify, abort, redirect, url_for
from flask import current_app as app

from flask_restful import Resource, Api, fields, marshal_with, reqparse

import werkzeug
from werkzeug.security import generate_password_hash

from .models import User
from .database import db

# from validation import AlreadyExists
import random

user_post_args = reqparse.RequestParser()
user_post_args.add_argument("fname", location="form", type=str)
user_post_args.add_argument("lname", location="form", type=str)
user_post_args.add_argument("email", location="form", type=str)
user_post_args.add_argument("username", location="form", type=str)
user_post_args.add_argument("password", location="form", type=str)
user_post_args.add_argument("role", location="form", type=str)

user_fields = {
    "fname": fields.String,
    "lname": fields.String,
    "email": fields.String,
    "username": fields.String,
    "password": fields.String,
    "role": fields.String,
}


# class UserAPI(Resource):
#     @marshal_with(user_fields)
#     def post(self):
#         print("in user api print")
#         print(user_post_args.parse_args())
#         args = user_post_args.parse_args()
#         print("abcd")
#         u = User.query.filter_by(username=args["username"]).first()
#         print(u)
#         if u:
#             flash("Username is already in use.", category="error")
#             return redirect("/register")
#         elif len(args["username"]) < 6:
#             print("username len short")
#             flash("Username should be more than 6 characters", category="error")
#             print("HEy")
#             return render_template("register.html")
#         elif len(args["password"]) < 6:
#             flash("Password is too short.", category="error")
#             return redirect("/register")
#         print("checks passed")
#         new_user = User(
#             fname=args["fname"],
#             lname=args["lname"],
#             email=args["email"],
#             username=args["username"],
#             password=generate_password_hash(args["password"], method="sha256"),
#             role=args["role"],
#         )
#         try:
#             db.session.add(new_user)
#             db.session.commit()
#             return redirect("/login")
#         except:
#             return redirect("/register")

#     def get(self, username):
#         u = User.query.filter_by(username=username).first()
#         return {
#             "username": u.username,
#         }


class UserAPI(Resource):
    def post(self):
        args = user_post_args.parse_args()
        print(args["username"])
        fname = args.get("fname")
        lname = args.get("lname")
        email = args.get("email")
        username = args.get("username")
        passw = args.get("password")
        role = args.get("role")
        print(username)
        check = User.query.filter_by(username=username).first()
        if check:
            flash("Username is already in use.", category="error")
            return redirect("/register")
        elif len(args["username"]) < 6:
            flash("Username is too short.", category="error")
            return redirect("/register")
        elif len(args["password"]) < 6:
            flash("Password is too short.", category="error")
            return redirect("/register")
        print("checks passed")
        new_user = User(
            fname=fname,
            lname=lname,
            email=email,
            username=username,
            password=generate_password_hash(passw, method="sha256"),
            role=role,
        )
        try:
            db.session.add(new_user)
            db.session.commit()
            print("user commit successful")
            return redirect("/login")
        except:
            print("user commit fail")
            return redirect("/register")


# class UserAPI(Resource):
#     def post(self):
#         args = user_post_args.parse_args()

#         fname = args.get("fname")
#         lname = args.get("lname")
#         email = args.get("email")
#         username = args.get("username")
#         passw = args.get("password")
#         role = args.get("role")
#         check = User.query.filter_by(email=email).first()
#         print(check)
#         if check:
#             flash("email you entered already belongs to an account. Try another email.")
#             return redirect(url_for("controllers.register"))
#         else:
#             # If user does not exists check these
#             if username != "":
#                 if email:
#                     if passw:
#                         new_user = User(
#                             fname=fname,
#                             lname=lname,
#                             email=email,
#                             username=username,
#                             role=role,
#                             password=passw,
#                         )
#                         # User.create_user(
#                         #     email=email,
#                         #     username=user_name,
#                         #     password=hash_password(passw),
#                         # )
#                         db.session.add(new_user)
#                         db.session.commit()
#                         data = User.query.filter_by(email=email).first()

#                         return redirect(url_for("controllers.login"))

#                     else:
#                         return jsonify(
#                             "Password cannot be empty. Please enter a valid Password"
#                         )
#                 else:
#                     return jsonify("email cannot be empty. Please Enter email")
#             else:
#                 return jsonify("Name cannot be empty. Please enter a valid name")


# @marshal_with(user_fields)
# def get(self, id=None):
#     if id:
#         user_data = User.query.filter_by(id=id).first()
#         return user_data
#     else:
#         data = User.query.all()
#         return data


# from flask.helpers import flash
# from flask.templating import render_template
# from flask_restful import Resource, Api
# from flask_restful import fields, marshal_with
# from flask_restful import reqparse
# from .models import User
# from . import db
# from flask import current_app as app
# import werkzeug
# from flask import abort, redirect, url_for
# from werkzeug.security import generate_password_hash

# # from validation import AlreadyExists
# import random

# user_post_args = reqparse.RequestParser()
# user_post_args.add_argument("fname", location="form")
# user_post_args.add_argument("lname", location="form")
# user_post_args.add_argument("email", location="form")
# user_post_args.add_argument("username", location="form")
# user_post_args.add_argument("password", location="form")
# user_post_args.add_argument("role", location="form")


# class UserAPI(Resource):
#     def post(self):
#         args = user_post_args.parse_args()
#         u = User.query.filter_by(username=args["username"]).first()
#         if u:
#             flash("Username is already in use.", category="error")
#             return redirect("/register")
#         elif len(args["username"]) < 6:
#             flash("Username is too short.", category="error")
#             return redirect("/register")
#         elif len(args["password"]) < 6:
#             flash("Password is too short.", category="error")
#             return redirect("/register")

#         new_user = User(
#             fname=args["fname"],
#             lname=args["lname"],
#             email=args["email"],
#             username=args["username"],
#             password=generate_password_hash(args["password"], method="sha256"),
#             role=args["role"],
#         )
#         try:
#             db.session.add(new_user)
#             db.session.commit()
#             return redirect("/login")
#         except:
#             return redirect("/register")

#     def get(self, username):
#         u = User.query.filter_by(username=username).first()
#         return {
#             "username": u.username,
#         }
