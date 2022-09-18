from datetime import datetime

import flask_login
# from itsdangerous.serializer import Serializer
# from sqlalchemy import insert
# from flask import Flask, current_app
from sqlalchemy.orm import backref
from sqlalchemy import create_engine

from project import login_manager
from flask_login import UserMixin
from sqlalchemy.sql import func
from project.app_object import db, app


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Role(db.Model):
    __tablename__ = "role"
    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(20), unique=True, nullable=False)
    role_desc = db.Column(db.String(200), nullable=True)
    date_created = db.Column(db.DateTime(timezone=True), server_default=func.now())
    db.Column('date_created', db.DateTime, onupdate=datetime.now)

    def __init__(self, role_name, role_desc=''):
        self.role_name = role_name
        self.role_desc = role_desc

    def __repr__(self):
        return f"Role {self.role_name}: {self.role_desc}"


class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)
    username = db.Column(db.String(40), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(200), nullable=False)
    role = db.relationship("Role", backref=backref("user", uselist=False))
    user_desc = db.Column(db.String(200), nullable=True)
    # date_created = db.Column(db.DateTime(), default=datetime.utcnow)
    date_created = db.Column(db.DateTime(timezone=True), server_default=func.now())

    # db.Column('date_created', db.DateTime, onupdate=datetime.now)

    def __init__(self, username, email, password, role_id):
        self.username = username
        self.email = email
        self.password = password
        self.role_id = role_id

    def __repr__(self):
        return f"User: {self.username}"


class Api(db.Model):
    __tablename__ = "api"
    id = db.Column(db.Integer, primary_key=True)
    api_provider = db.Column(db.String(40), nullable=False)
    api_username = db.Column(db.String(40), nullable=False)
    api_password = db.Column(db.String(40), nullable=False)
    api_key = db.Column(db.String(60), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship("User", backref=backref("api", uselist=False))
    date_created = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def __init__(self, api_provider, api_username, api_password, api_key, user_id):
        self.api_provider = api_provider
        self.api_username = api_username
        self.api_password = api_password
        self.api_key = api_key
        self.user_id = user_id

    def __repr__(self):
        return f"Api {self.id} {self.api_username}"


# class Profile(db.Model):
#     id = 1

# db.metadata.clear()
# app = create_app()
# app.app_context().push()

# user with app context
# db.create_all(app=create_app())

# db.create_all()
# print("done")
#
# user = User.query.filter_by(email="zayeed.cse@gmail.com").first()
# print(user.email)


# stmt = (
#     insert(Role).
#     values(role_name='Level 1', role_desc='Read Permission only')
# )

# print(stmt)

# role = Role(role_name='Admin', role_desc="Full Access")
# role = Role(role_name='Level 1', role_desc="Read")
# db.session.add(role)
# db.session.commit()

# user = User.query.get_or_404(2).filter(username='z')
# print(user.username)

# q = Session.query(User, Role).filter(
#          User.email == Document.author,
#     ).filter(
#          Document.name == DocumentPermissions.document,
#     ).filter(
#         User.email == 'someemail',
#     ).all()


# tutorialspoint.com/sqlalchemy/sqlalchemy_orm_building_relationship.htm
# engine = create_engine(app.config.get('SQLALCHEMY_DATABASE_URI'), echo=True)
# from sqlalchemy.orm import sessionmaker
# Session = sessionmaker(bind=engine)
# session = Session()
# # print(session)


# p = db.session.query(User, Role).filter(User.role_id == Role.id).filter(User.id == 2).all()
# print(p)

# api_info = db.session.query(Api, User).filter(Api.user_id == User.id).filter(User.id==2).all()
# print(api_info[0].Api.api_key)