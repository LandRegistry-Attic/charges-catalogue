from flask import Flask
from flask.ext.script import Manager
from app import helloworld


def create_app():
    app = Flask(__name__)

    manager = Manager(app)

    app.register_blueprint(helloworld.blueprint)

    return app, manager
