# flask packages
from flask import Flask, app
from flask_restful import Api
from flask_mongoengine import MongoEngine
# local packages
from api.routes import create_routes

# default mongodb configuration
default_config = {'MONGODB_SETTINGS': {
    'db': 'test_db2',
    'host': 'localhost',
    'port': 27017,
    'username': 'admin',
    'password': 'password',
    'authentication_source': 'admin'}}


def get_flask_app(config: dict = None) -> app.Flask:
    """
    Initializes Flask app with given configuration.
    Main entry point for wsgi (gunicorn) server.
    :param config: Configuration dictionary
    :return: app
    """
    # init flask
    flask_app = Flask(__name__)

    # configure app
    config = default_config if config is None else config
    flask_app.config.update(config)
    # init api and routes
    api = Api(app=flask_app)
    create_routes(api=api)
    # init mongoengine
    db = MongoEngine(app=flask_app)

    return flask_app


if __name__ == '__main__':
    # Main entry point when run in stand-alone mode.
    app = get_flask_app()
    app.run(debug=True)
