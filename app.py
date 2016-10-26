import os
from flask import Flask
from extensions import init_extensions
from blueprints.compute import compute, default, dashboard
import base_config


def create_app(config_filename=None, config_options_name=None):
    """
    Creates and returns the flask application object.

    :param config_filename: Filename with application configuration parameters
    :param config_options: Python module with the class options for configuring the application.
    :return: wsgi Flask application
    """
    app = Flask(__name__)

    # Todo: Move to a function or separate module for cleaner segregation of duties
    app.register_blueprint(compute)
    app.register_blueprint(default)
    init_extensions(app)

    default_configuration = base_config.get_configuration(config_options_name)
    print('Using {0} configuration'.format(default_configuration.__name__))
    app.config.from_object(default_configuration)
    if config_filename is not None:
        # Override base configuration parameters with more specific ones from a configuration file.
        app.config.from_pyfile(config_filename)
    return app

if __name__ == "__main__":
    create_app().run()
