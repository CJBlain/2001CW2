import os
from flask import Flask, jsonify
from flask import request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
from app.db import db
from config import Config

#load environment files
load_dotenv()

#initializes the app
app = Flask(__name__)

app.config.from_object(Config)

#calls database
db.init_app(app)

migrate = Migrate(app, db)

#import models
from app.models import Trail, Route, TrailFeature, TrailOwnership, User    #imports tables from app.model

#defines routes
@app.route('/')
def home():
    return "Welcome to the Trail App!"

@app.route('/trails', methods=['GET'])          #imports data from trail table
def get_trails():
    trails = Trail.query.all() 
    return jsonify([{
        'TrailID': trail.TrailID,
        'TrailName': trail.TrailName,
        'TrailSummary': trail.TrailSummary,
        'TrailDescription': trail.TrailDescription,
        'Difficulty': trail.Difficulty,
        'Location': trail.Location,
        'Length': trail.Length,
        'ElevationGain': trail.ElevationGain
    } for trail in trails])  

@app.route('/trails', methods=['POST'])
def add_trail():
    try:
    
        data = request.get_json()
        
        if not data:
            return jsonify({"error": "No data provided"}), 400
        
        new_trail = Trail(
            TrailName=data['TrailName'],
            TrailSummary=data['TrailSummary'],
            TrailDescription=data['TrailDescription'],
            Difficulty=data['Difficulty'],
            Location=data['Location'],
            Length=data['Length'],
            ElevationGain=data['Elevationgain']
        )

        db.session.add(new_trail)
        db.session.commit()

        return jsonify(new_trail.to_dict()), 201

    except Exception as e:
        
        return jsonify({"error": str(e)}), 400
    
@app.route('/trails/<int:trail_id>', methods=['DELETE'])
def delete_trail(trail_id):
    try:
        # Find the trail by ID
        trail = Trail.query.get(trail_id)
        
        if not trail:
            return jsonify({'error': 'Trail not found'}), 404
        
        # Delete the trail
        db.session.delete(trail)
        db.session.commit()

        return jsonify({'message': f'Trail {trail_id} successfully deleted'}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400    


@app.route('/routes', methods=['GET'])      #gets the data from the routes table
def get_routes():
    routes = Route.query.all()  
    return jsonify([{
        'RouteID': route.RouteID,
        'TrailID': route.TrailID,
        'RouteType': route.RouteType
    } for route in routes])

@app.route('/trailfeatures', methods=['GET'])           #gets the data from trailfeatures table
def get_trailfeatures():
    try:
        trailfeatures = TrailFeature.query.all() 
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
    
@app.route('/trailownership', methods=['GET'])      #gets the data from the trailownership table
def get_trailownership():
    try:
        ownerships = TrailOwnership.query.all()  
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
    

@app.route('/users', methods=['GET'])     #gets teh data from the users table
def get_users():
    try:
        users = User.query.all()  
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
    

#runs the application
if __name__ == "__main__":
    app.run(debug=True)
