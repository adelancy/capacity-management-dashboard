import os

basedir = os.path.abspath((os.path.dirname(__file__)))


class BaseConfig(object):
    PROJECT = 'UHA Requirements & Current State Dashboard'
    DEBUG = False
    SECRET_KEY = os.urandom(24)


class TestingConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}'.format(os.path.join(basedir, 'test.db'))
    TESTING = True
    DEBUG = True
