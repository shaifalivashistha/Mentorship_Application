from re import S
from flask import Blueprint, render_template, request, flash
from flask_login import login_user, logout_user, current_user
from flask_login.utils import login_required
from werkzeug.utils import redirect
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
import requests
from datetime import datetime

views = Blueprint("views", __name__)

BASE = 'http://127.0.0.1:5000'

@views.route('/dashboard', methods = ['GET', 'POST'])
@login_required
def home():
    if current_user.role == "Mentee":
        mentorlist = User.query.filter_by(role="Mentor").all()
        return render_template('dashboard.html' , name=current_user.username, mentorlist=mentorlist )
    else:
        menteelist = User.query.filter_by(role="Mentee").all()
        return render_template('dashboard_mentee.html' , name=current_user.username, menteelist=menteelist )

@views.route('/', methods=['GET'])
def landing():
    return render_template('landing.html')


@views.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user, remember=True)
                return redirect('/dashboard')
            else:
                flash('Password is incorrect.', category='error')
        else:
            flash('Username does not exist.', category='error')

    return render_template('login.html')




@views.route('/register', methods = ['GET', 'POST'])
def register():
    return render_template('register.html')


@views.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')