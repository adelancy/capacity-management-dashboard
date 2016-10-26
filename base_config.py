import os

basedir = os.path.abspath((os.path.dirname(__file__)))
_secret_key = os.urandom(24)


class BaseConfig(object):
    PROJECT = 'UHA Requirements & Current State Dashboard'
    DEBUG = False
    TESTING = False
    SECRET_KEY = _secret_key
    WTF_CSRF_SECRET_KEY = _secret_key


class TestingConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}'.format(os.path.join(basedir, 'test.db'))
    TESTING = True
    DEBUG = True


def get_configuration(name=''):
    if name.lower() in ['test', 'testing']:
        return TestingConfig
    return BaseConfig
