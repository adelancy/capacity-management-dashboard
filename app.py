from flask import Flask
from extensions import init_extensions
from blueprints.compute import compute


def create_app(config_filename=None):
    app = Flask(__name__)
    app.register_blueprint(compute)
    init_extensions(app)

    if config_filename is not None:
        app.config.from_pyfile(config_filename)

    return app

if __name__ == "__main__":
    create_app().run()
