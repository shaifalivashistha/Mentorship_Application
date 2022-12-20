from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager, login_manager
from flask_restful import Api


db = SQLAlchemy()
DB_NAME = "myData.db"
# DB_NAME = "project.sqlite3"
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'param'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    api = Api(app)
    from .api import UserAPI
    api.add_resource(UserAPI, '/api/user', '/api/user/<string:username>')
    from .views import views
    app.register_blueprint(views, url_prefix="/")
    from .models import User
    create_db(app)
    login_manager = LoginManager()
    login_manager.login_view = "views.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))


    return  app, api

def create_db(app):
    if not path.exists("seproject/"+ DB_NAME):
        db.create_all(app=app)
    print('DATABASE ALREADY EXISTS')