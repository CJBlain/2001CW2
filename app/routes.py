from flask import Blueprint, request, jsonify
from models import db, Trail, Route, TrailFeature, TrailOwnership, User


main = Blueprint('main', __name__)

# ----------- TRAIL endpoints -----------
@main.route('/trails', methods=['GET'])
def get_trails():
    trails = Trail.query.all()
    return jsonify([trail.to_dict() for trail in trails])

@main.route('/trails', methods=['POST'])
def add_trail():
    data = request.get_json()
    new_trail = Trail(
        TrailName=data['TrailName'],
        TrailSummary=data['TrailSummary'],
        TrailDescription=data['TrailDescription'],
        Difficulty=data['Difficulty'],
        Location=data['Location'],
        Length=data['Length'],
        Elavationgain=data['Elavationgain']
    )
    db.session.add(new_trail)
    db.session.commit()
    return jsonify(new_trail.to_dict()), 201

@main.route('/trails/<int:id>', methods=['GET'])
def get_trail(id):
    trail = Trail.query.get_or_404(id)
    return jsonify(trail.to_dict())

@main.route('/trails/<int:id>', methods=['PUT'])
def update_trail(id):
    trail = Trail.query.get_or_404(id)
    data = request.get_json()
    trail.TrailName = data.get('TrailName', trail.TrailName)
    trail.TrailSummary = data.get('TrailSummary', trail.TrailSummary)
    trail.TrailDescription = data.get('TrailDescription', trail.TrailDescription)
    trail.Difficulty = data.get('Difficulty', trail.Difficulty)
    trail.Location = data.get('Location', trail.Location)
    trail.Length = data.get('Length', trail.Length)
    trail.Elavationgain = data.get('Elavationgain', trail.Elavationgain)

    db.session.commit()
    return jsonify(trail.to_dict())

@main.route('/trails/<int:id>', methods=['DELETE'])
def delete_trail(id):
    trail = Trail.query.get_or_404(id)
    db.session.delete(trail)
    db.session.commit()
    return '', 204

# ----------- ROUTE endpoints -----------
@main.route('/routes', methods=['GET'])
def get_routes():
    routes = Route.query.all()
    return jsonify([route.to_dict() for route in routes])

@main.route('/routes', methods=['POST'])
def add_route():
    data = request.get_json()
    new_route = Route(
        TrailID=data['TrailID'],
        RouteID=data['RouteID'],
        RouteType=data['RouteType']
    )
    db.session.add(new_route)
    db.session.commit()
    return jsonify(new_route.to_dict()), 201

@main.route('/routes/<int:id>', methods=['GET'])
def get_route(id):
    route = Route.query.get_or_404(id)
    return jsonify(route.to_dict())

@main.route('/routes/<int:id>', methods=['PUT'])
def update_route(id):
    route = Route.query.get_or_404(id)
    data = request.get_json()
    route.TrailID = data.get('TrailID', route.TrailID)
    route.RouteID = data.get('RouteID', route.RouteID)
    route.RouteType = data.get('RouteType', route.RouteType)

    db.session.commit()
    return jsonify(route.to_dict())

@main.route('/routes/<int:id>', methods=['DELETE'])
def delete_route(id):
    route = Route.query.get_or_404(id)
    db.session.delete(route)
    db.session.commit()
    return '', 204

# ----------- TRAILFEATURE endpoints -----------
@main.route('/trailfeatures', methods=['GET'])
def get_trail_features():
    trail_features = TrailFeature.query.all()
    return jsonify([feature.to_dict() for feature in trail_features])

@main.route('/trailfeatures', methods=['POST'])
def add_trail_feature():
    data = request.get_json()
    new_feature = TrailFeature(
        TrailID=data['TrailID'],
        FeatureName=data['FeatureName']
    )
    db.session.add(new_feature)
    db.session.commit()
    return jsonify(new_feature.to_dict()), 201

@main.route('/trailfeatures/<int:id>', methods=['GET'])
def get_trail_feature(id):
    feature = TrailFeature.query.get_or_404(id)
    return jsonify(feature.to_dict())

@main.route('/trailfeatures/<int:id>', methods=['PUT'])
def update_trail_feature(id):
    feature = TrailFeature.query.get_or_404(id)
    data = request.get_json()
    feature.TrailID = data.get('TrailID', feature.TrailID)
    feature.FeatureName = data.get('FeatureName', feature.FeatureName)

    db.session.commit()
    return jsonify(feature.to_dict())

@main.route('/trailfeatures/<int:id>', methods=['DELETE'])
def delete_trail_feature(id):
    feature = TrailFeature.query.get_or_404(id)
    db.session.delete(feature)
    db.session.commit()
    return '', 204

# ----------- TRAILOWNERSHIP endpoints -----------
@main.route('/trailownerships', methods=['GET'])
def get_trail_ownerships():
    trail_ownerships = TrailOwnership.query.all()
    return jsonify([ownership.to_dict() for ownership in trail_ownerships])

@main.route('/trailownerships', methods=['POST'])
def add_trail_ownership():
    data = request.get_json()
    new_ownership = TrailOwnership(
        TrailID=data['TrailID'],
        UserID=data['UserID'],
        OwnershipDate=data['OwnershipDate']
    )
    db.session.add(new_ownership)
    db.session.commit()
    return jsonify(new_ownership.to_dict()), 201

@main.route('/trailownerships/<int:id>', methods=['GET'])
def get_trail_ownership(id):
    ownership = TrailOwnership.query.get_or_404(id)
    return jsonify(ownership.to_dict())

@main.route('/trailownerships/<int:id>', methods=['PUT'])
def update_trail_ownership(id):
    ownership = TrailOwnership.query.get_or_404(id)
    data = request.get_json()
    ownership.TrailID = data.get('TrailID', ownership.TrailID)
    ownership.UserID = data.get('UserID', ownership.UserID)
    ownership.OwnershipDate = data.get('OwnershipDate', ownership.OwnershipDate)

    db.session.commit()
    return jsonify(ownership.to_dict())

@main.route('/trailownerships/<int:id>', methods=['DELETE'])
def delete_trail_ownership(id):
    ownership = TrailOwnership.query.get_or_404(id)
    db.session.delete(ownership)
    db.session.commit()
    return '', 204

# ----------- USER endpoints -----------
@main.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

@main.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    new_user = User(
        Username=data['Username'],
        Email=data['Email'],
        PasswordHash=data['PasswordHash'],
        Role=data['Role']
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.to_dict()), 201

@main.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify(user.to_dict())

@main.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    user = User.query.get_or_404(id)
    data = request.get_json()
    user.Username = data.get('Username', user.Username)
    user.Email = data.get('Email', user.Email)
    user.PasswordHash = data.get('PasswordHash', user.PasswordHash)
    user.Role = data.get('Role', user.Role)

    db.session.commit()
    return jsonify(user.to_dict())

@main.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return '', 204
