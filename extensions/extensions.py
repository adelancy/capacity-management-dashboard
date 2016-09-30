from restful import rest_api
from sql_alchemy import sqldb
from rest_api.endpoints import add_restful_endpoints

# Register the RestFul APIs
add_restful_endpoints(rest_api)


def init_extensions(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True  # Todo: Figure out what this enables
    sqldb.init_app(app)
    rest_api.init_app(app)



