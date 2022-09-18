# to fix mysqldb module error
# import pymysql
# pymysql.install_as_MySQLdb()

# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail


from project.config import Config
from project.app_object import app, db


bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message_category = 'info'
mail = Mail()


def create_app():
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from project.users.routes import auth
    from project.users.profile import prof
    from project.main.routes import main
    from project.errors.handlers import errors
    from project.role.manage_role import role
    from project.api.routes import api
    app.register_blueprint(auth)
    app.register_blueprint(prof)
    app.register_blueprint(main)
    app.register_blueprint(errors)
    app.register_blueprint(role)
    app.register_blueprint(api)
    return app

