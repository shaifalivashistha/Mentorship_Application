import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = False

    SQLITE_DB_DIR = None
    SQLALCHEMY_DATABASE_URI = None
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    WTF_CSRF_ENABLED = False


class LocalDevelopmentConfig(Config):
    SQLITE_DB_DIR = os.path.join(basedir, "../db_directory")
    SQLALCHEMY_DATABASE_URI = "sqlite:///mentoring_app.sqlite3"

    DEBUG = True
    SECRET_KEY = "Th1s1sas3cr3tk3y"
    SECURITY_PASSWORD_SALT = "S3cr3tPassword"  # Read from ENV in your case
    SECURITY_CONFIRMABLE = False
    SECURITY_SEND_REGISTER_EMAIL = False
    SECURITY_UNAUTHORIZED_VIEW = None
    WTF_CSRF_ENABLED = False
