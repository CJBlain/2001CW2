from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Trail(db.model):
    __tablename__ = 'TRAIL'
    
    trail_id = db.Column(db.Integer, primary_key=True)  
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
    __tablename__ = 'route'

    route_id = db.Column(db.Integer, primary_key=True)  
    trail_id = db.Column(db.Integer, db.ForeignKey('trail.trail_id'), nullable=False)  
    route_type = db.Column(db.String(50))  

   
    trail = db.relationship('Trail', backref=db.backref('routes', lazy=True))

    def __repr__(self):
        return f"<Route {self.route_id}>"
    
class TrailFeature(db.Model):
    __tablename__ = 'trailfeature'

    trail_feature_id = db.Column(db.Integer, primary_key=True)  
    trail_id = db.Column(db.Integer, db.ForeignKey('trail.trail_id'), nullable=False)  
    feature_name = db.Column(db.String(100), nullable=False)  

    
    trail = db.relationship('Trail', backref=db.backref('features', lazy=True))

    def __repr__(self):
        return f"<TrailFeature {self.feature_name}>"
    
class TrailOwnership(db.Model):
    __tablename__ = 'trailownership'

    ownership_id = db.Column(db.Integer, primary_key=True)  
    trail_id = db.Column(db.Integer, db.ForeignKey('trail.trail_id'), nullable=False)  
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)  
    ownership_date = db.Column(db.Date)  

    
    trail = db.relationship('Trail', backref=db.backref('ownerships', lazy=True))
    user = db.relationship('User', backref=db.backref('owned_trails', lazy=True))

    def __repr__(self):
        return f"<TrailOwnership {self.ownership_id}>"
    

class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)  
    username = db.Column(db.String(100), nullable=False, unique=True)  
    email = db.Column(db.String(100), nullable=False, unique=True)  
    password_hash = db.Column(db.String(200), nullable=False)  
    role = db.Column(db.String(50), nullable=False)  

    def __repr__(self):
        return f"<User {self.user_id} - {self.username}>"