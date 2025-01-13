from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .routes import main


db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    
    app.config.from_object('config')  

    
    db.init_app(app)
    migrate.init_app(app, db) 

    
    with app.app_context():
        try:

            db.session.execute('SELECT 1')
            print("Database connection successful!")
        except Exception as e:
            print(f"Database connection failed: {e}")

    
    app.register_blueprint(main, url_prefix='/')

    return app


from app.models import Trail, Route, TrailFeature, TrailOwnership, User  
