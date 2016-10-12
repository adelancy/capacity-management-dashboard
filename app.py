from flask import Flask
from extensions import init_extensions
from blueprints.compute import compute, default, dashboard


def create_app(config_filename=None):
    app = Flask(__name__)
    app.register_blueprint(compute)
    app.register_blueprint(default)
    init_extensions(app)

    if config_filename is not None:
        app.config.from_object(config_filename)

    return app

if __name__ == "__main__":
    create_app().run()
