import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
from app.db import db
from config import Config

# Load environment variables from .env file
load_dotenv()

# Initialize the app and configurations
app = Flask(__name__)

app.config.from_object(Config)

# Initialize the database and migration
db.init_app(app)

migrate = Migrate(app, db)

# Import models
from app.models import Trail, Route, TrailFeature, TrailOwnership, User

# Define routes
@app.route('/')
def home():
    return "Welcome to the Trail App!"

@app.route('/trails', methods=['GET'])
def get_trails():
    trails = Trail.query.all()  # Fetch all trails from the database
    return jsonify([{
        'TrailID': trail.TrailID,
        'TrailName': trail.TrailName,
        'TrailSummary': trail.TrailSummary,
        'TrailDescription': trail.TrailDescription,
        'Difficulty': trail.Difficulty,
        'Location': trail.Location,
        'Length': trail.Length,
        'ElevationGain': trail.ElevationGain
    } for trail in trails])  # Return all trail data as JSON

@app.route('/routes', methods=['GET'])
def get_routes():
    routes = Route.query.all()  # Fetch all routes from the database
    return jsonify([{
        'RouteID': route.RouteID,
        'TrailID': route.TrailID,
        'RouteType': route.RouteType
    } for route in routes])

@app.route('/trailfeatures', methods=['GET'])
def get_trailfeatures():
    try:
        trailfeatures = TrailFeature.query.all()  # Fetch all trail features
        result = [
            {
                'TrailFeatureID': feature.TrailFeatureID,
                'TrailID': feature.TrailID,
                'FeatureName': feature.FeatureName
            }
            for feature in trailfeatures
        ]
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/trailownership', methods=['GET'])
def get_trailownership():
    try:
        ownerships = TrailOwnership.query.all()  # Fetch all trail ownership records
        result = [
            {
                'OwnershipID': ownership.OwnershipID,
                'UserID': ownership.UserID,
                'TrailID': ownership.TrailID,
                'OwnershipDate': ownership.OwnershipDate.strftime('%Y-%m-%d')  
            }
            for ownership in ownerships
        ]
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

@app.route('/users', methods=['GET'])
def get_users():
    try:
        users = User.query.all()  # Fetch all user records
        result = [
            {
                'UserID': user.UserID,
                'Username': user.Username,
                'Email': user.Email,
                'Role': user.Role
            }
            for user in users
        ]
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    
# Run the application
if __name__ == "__main__":
    app.run(debug=True)
