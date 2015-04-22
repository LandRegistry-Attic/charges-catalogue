from flask import Flask
from flask.ext.script import Manager
from app import helloworld
from govuk_template.flask import assets


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    manager = Manager(app)

    app.register_blueprint(helloworld.blueprint)
    app.register_blueprint(assets.govuk_template, url_prefix='/template')

    return app, manager
