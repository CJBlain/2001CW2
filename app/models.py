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