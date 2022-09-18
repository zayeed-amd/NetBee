from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from project.config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)


# also can be initialized as
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cisco.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost:3306/netbee'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///netbee'
