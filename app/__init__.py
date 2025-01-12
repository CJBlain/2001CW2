
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Load the configuration from the config.py file
    app.config.from_object('config')  # This loads the configuration from config.py

    db.init_app(app)

    # Register your blueprints, models, etc. here

    return app