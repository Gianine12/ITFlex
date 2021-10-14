from flask import Flask
from environs import Env
from flask_cors import CORS

from app.config import database, migrate
from app import views

env = Env()
env.read_env()

def create_app():
    app= Flask(__name__)
    CORS(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = env('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    database.init_app(app)
    migrate.init_app(app)
    views.init_app(app)

    return app
