from flask_sqlalchemy import SQLAlchemy
from app.db import db


class Trail(db.Model):
    __tablename__ = 'Trail'
    __table_args__ = {'schema': 'CW2'}
    TrailID = db.Column(db.Integer, primary_key=True)
    TrailName = db.Column(db.String(120))
    TrailSummary = db.Column(db.String(500))
    TrailDescription = db.Column(db.Text)
    Difficulty = db.Column(db.String(50))
    Location = db.Column(db.String(120))
    Length = db.Column(db.Float)
    ElevationGain = db.Column(db.Float)

    def to_dict(self):
        return {
            'TrailID': self.TrailID,
            'TrailName': self.TrailName,
            'TrailSummary': self.TrailSummary,
            'TrailDescription': self.TrailDescription,
            'Difficulty': self.Difficulty,
            'Location': self.Location,
            'Length': self.Length,
            'ElevationGain': self.ElevationGain
        }

class Route(db.Model):
    __tablename__ = 'Route'
    __table_args__ = {'schema': 'CW2'}
    RouteID = db.Column(db.Integer, primary_key=True)
    TrailID = db.Column(db.Integer, db.ForeignKey('trail.id'))
    RouteType = db.Column(db.String(100))

    def to_dict(self):
        return {
            'TrailID': self.TrailID,
            'RouteID': self.RouteID,
            'RouteType': self.RouteType
        }

class TrailFeature(db.Model):
    __tablename__ = 'TrailFeature'
    __table_args__ = {'schema': 'CW2'}
    TrailFeatureID = db.Column(db.Integer, primary_key=True)
    TrailID = db.Column(db.Integer, db.ForeignKey('trail.id'))
    FeatureName = db.Column(db.String(120))

    def to_dict(self):
        return {
            'TrailFeatureID': self.id,
            'TrailID': self.TrailID,
            'FeatureName': self.FeatureName
        }

class TrailOwnership(db.Model):
    __tablename__ = 'TrailOwnership'
    __table_args__ = {'schema': 'CW2'}
    OwnershipID = db.Column(db.Integer, primary_key=True)
    TrailID = db.Column(db.Integer, db.ForeignKey('trail.id'))
    UserID = db.Column(db.Integer, db.ForeignKey('user.id'))
    OwnershipDate = db.Column(db.Date)

    def to_dict(self):
        return {
            'OwnershipID': self.id,
            'TrailID': self.TrailID,
            'UserID': self.UserID,
            'OwnershipDate': self.OwnershipDate
        }

class User(db.Model):
    __tablename__ = 'Users'
    __table_args__ = {'schema': 'CW2'}
    UserID = db.Column(db.Integer, primary_key=True)
    Username = db.Column(db.String(120))
    Email = db.Column(db.String(120))
    PasswordHash = db.Column(db.String(200))
    Role = db.Column(db.String(50))

    def to_dict(self):
        return {
            'UserID': self.id,
            'Username': self.Username,
            'Email': self.Email,
            'Role': self.Role
        }
