import os
import sys

class Config:
    # SECRET_KEY = os.environ.get('SECRET_KEY')
    SECRET_KEY = "netbee-secret-key-001"
    # SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@localhost:3306/netbee' if sys.platform.startswith('win') else 'mysql://root@localhost:3306/netbee'
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///netbee'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    # https://github.com/apache/superset/issues/8207
    # sqlalchemy.exc.TimeoutError: QueuePool limit of size 10 overflow 10 reached, connection timed out
    SQLALCHEMY_ENGINE_OPTIONS = {
        "max_overflow": 15,
        "pool_pre_ping": True,
        "pool_recycle": 60 * 60,
        "pool_size": 30,
    }
