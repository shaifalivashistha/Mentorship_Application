from flask.helpers import flash
from flask.templating import render_template
from flask_restful import Resource, Api
from flask_restful import fields, marshal_with
from flask_restful import reqparse
from .models import User
from . import db
from flask import current_app as app
import werkzeug
from flask import abort, redirect, url_for
from werkzeug.security import generate_password_hash
#from validation import AlreadyExists
import random

user_post_args = reqparse.RequestParser()
user_post_args.add_argument('fname', type=str , location='form')
user_post_args.add_argument('lname', type=str , location='form')
user_post_args.add_argument('email', type=str , location='form')
user_post_args.add_argument('username', type=str , location='form')
user_post_args.add_argument('password' , location='form')
user_post_args.add_argument('role', type=str , location='form')
user_post_args.add_argument('subjects', type=str , location='form')
user_post_args.add_argument('linkedin', type=str , location='form')

class UserAPI(Resource):
    def post(self):
        args = user_post_args.parse_args()
        u = User.query.filter_by(username=args['username']).first()
        if u:
            flash('Username is already in use.', category='error')
            return redirect('/register')
        elif len(args['username']) < 6:
            flash('Username is too short.', category='error')
            return redirect('/register')
        elif len(args['password']) < 6:
            flash('Password is too short.', category='error')
            return redirect('/register')
        
        new_user = User(
                fname=args['fname'],
                lname=args['lname'],
                email=args['email'],
                username=args['username'], 
                password = generate_password_hash(args['password'], method='sha256'),
                role=args['role'],
                subjects = args['subjects'],
                linkedin=args['linkedin'])
        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect('/login')
        except:
            return redirect('/register')
    def get(self, username):
        u = User.query.filter_by(username=username).first()
        return{
            "username": u.username,
        }

