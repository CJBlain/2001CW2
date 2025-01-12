from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Trail(db.model):
    __tablename__ = 'TRAIL'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    difficulty = db.Column(db.String(50), nullable=True)
    
    def __repr__(self):
        return f'<Trail {self.name}>'