from flask import Flask, app
from flask_restful import Api
from flask_mongoengine import MongoEngine
from api.routes import create_routes
from flask_cors import CORS
from dotenv import load_dotenv
import os

"""
default_config = {'MONGODB_SETTINGS': {
    'db': 'slideland1',
    'host': 'localhost',
    'port': 27017,
    'username': 'admin',
    'password': 'password',
    'authentication_source': 'admin'}}
"""


def get_flask_app(config: dict = None) -> app.Flask:
    flask_app = Flask(__name__)
    DB_URI = os.environ.get("DB_URI")
    flask_app.config["MONGODB_HOST"] = DB_URI
    
    #config = default_config if config is None else config
    #flask_app.config.update(config)

    api = Api(app=flask_app)
    create_routes(api=api)
    db = MongoEngine(app=flask_app)
    return flask_app


if __name__ == '__main__':
    load_dotenv()
    app = get_flask_app()
    CORS(app)
    cors = CORS(app, resource={
        r"/*":{
            "origins":"*"
        }
    })
    app.run(debug=True)
