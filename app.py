from flask import Flask


import Users, Teams
from Database.db import mongo


def create_app(config_object="config.settings"):

    app = Flask(__name__)
    app.config.from_object(config_object)
    Users.init_app(app)
    Teams.init_app(app)
    mongo.init_app(app)

    return app