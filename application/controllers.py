from werkzeug.security import generate_password_hash, check_password_hash
from flask import current_app as app
from flask import Blueprint, request, session, jsonify, render_template, redirect, flash

from flask_login import login_user, logout_user, current_user
from flask_login.utils import login_required

# from flask_login import LoginManager, login_manager

from .models import *
from .database import *

import requests

controllers = Blueprint("controllers", __name__)
BASE = "http://127.0.0.1:5000"


# login_manager = LoginManager()
# login_manager.login_view = "controllers.login"
# login_manager.init_app(app)


# @login_manager.user_loader
# def load_user(id):
#     return User.query.get(int(id))


@app.before_first_request
def database():
    db.create_all()


@controllers.route("/dashboard", methods=["GET", "POST"])
@login_required
def home():
    data = requests.get(BASE + f"/api/deck/{current_user.username}")
    return render_template("dashboard.html")


@controllers.route("/", methods=["GET"])
def landing():
    return render_template("landing.html")


@controllers.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user, remember=True)
                return redirect("/dashboard")
            else:
                flash("Password is incorrect.", category="error")
        else:
            flash("Username does not exist.", category="error")

    return render_template("login.html")


@controllers.route("/register", methods=["GET", "POST"])
def register():
    return render_template("register.html")


@controllers.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/")
