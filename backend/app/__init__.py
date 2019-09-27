from flask import Flask
from app.api import bp as api_bp


def create_app(config_class=None):
    app = Flask(__name__)
    configure_app(app, config_class)
    configure_blueprints(app)
    return app


def configure_app(app, config_class):
    app.config.from_object(config_class)
    app.url_map.strict_slashes = False


def configure_blueprints(app):
    app.register_blueprint(api_bp, url_prefix="/api")


def configure_extensions(app):
    pass
