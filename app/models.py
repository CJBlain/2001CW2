from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Trail(db.Model):
    __tablename__ = 'Trail'  # Corrected to match your specification
    
    TrailID = db.Column(db.Integer, primary_key=True)  # Primary key is TrailID
    trail_name = db.Column(db.String(100), nullable=False)  
    trail_summary = db.Column(db.String(200))  
    trail_description = db.Column(db.String(500)) 
    difficulty = db.Column(db.String(50))  
    location = db.Column(db.String(100))   
    length = db.Column(db.Float) 
    elevation_gain = db.Column(db.Float)  

    def __repr__(self):
        return f"<Trail {self.trail_name}>"

class Route(db.Model):
    __tablename__ = 'Route'  # Corrected to match your specification

    route_id = db.Column(db.Integer, primary_key=True)
    TrailID = db.Column(db.Integer, db.ForeignKey('Trail.TrailID'), nullable=False)  # Foreign key now correctly references Trail.TrailID
    route_type = db.Column(db.String(50))

    trail = db.relationship('Trail', backref=db.backref('routes', lazy=True), foreign_keys=[TrailID])  # Specify foreign_keys explicitly

    def __repr__(self):
        return f"<Route {self.route_id}>"
    
class TrailFeature(db.Model):
    __tablename__ = 'TrailFeature'  # Corrected to match your specification

    trail_feature_id = db.Column(db.Integer, primary_key=True)  
    TrailID = db.Column(db.Integer, db.ForeignKey('Trail.TrailID'), nullable=False)  # Foreign key now references TrailID
    feature_name = db.Column(db.String(100), nullable=False)  

    trail = db.relationship('Trail', backref=db.backref('features', lazy=True))

    def __repr__(self):
        return f"<TrailFeature {self.feature_name}>"
    
class TrailOwnership(db.Model):
    __tablename__ = 'TrailOwnership'  # Corrected to match your specification

    ownership_id = db.Column(db.Integer, primary_key=True)  
    TrailID = db.Column(db.Integer, db.ForeignKey('Trail.TrailID'), nullable=False)  # Foreign key now references TrailID
    user_id = db.Column(db.Integer, db.ForeignKey('Users.UserID'), nullable=False)  
    ownership_date = db.Column(db.Date)  

    trail = db.relationship('Trail', backref=db.backref('ownerships', lazy=True))
    user = db.relationship('User', backref=db.backref('owned_trails', lazy=True))

    def __repr__(self):
        return f"<TrailOwnership {self.ownership_id}>"
    

class User(db.Model):
    __tablename__ = 'Users'  # Corrected to match your specification

    user_id = db.Column(db.Integer, primary_key=True)  
    username = db.Column(db.String(100), nullable=False, unique=True)  
    email = db.Column(db.String(100), nullable=False, unique=True)  
    password_hash = db.Column(db.String(200), nullable=False)  
    role = db.Column(db.String(50), nullable=False)  

    def __repr__(self):
        return f"<User {self.user_id} - {self.username}>"
