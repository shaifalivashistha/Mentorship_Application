from flask import Flask
from flask_restful import Api
from flask_login import LoginManager, login_manager

from application.models import *
from application.database import db

from application.config import LocalDevelopmentConfig


app = None
api = None


def create_app():
    app = Flask(__name__)
    app.config.from_object(LocalDevelopmentConfig)

    db.init_app(app)
    app.app_context().push()

    api = Api(app)

    from .api import UserAPI

    api.add_resource(UserAPI, "/api/user", "/api/user/<string:username>")

    from .controllers import controllers

    app.register_blueprint(controllers, url_prefix="/")
    from .models import User

    login_manager = LoginManager()
    login_manager.login_view = "controllers.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    app.app_context().push()

    return app, api
