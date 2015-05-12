from flask import Flask
from flask.ext.script import Manager
from app import api
from govuk_template.flask import assets


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    manager = Manager(app)

    static.register_assets(app)

    return app, manager
