import os

class Config:
    # Database connection string for MS SQL Server
    SQLALCHEMY_DATABASE_URI = (
        'mssql+pyodbc://CBlain:HjnF689+@DIST-6-505.uopnet.plymouth.ac.uk/COMP2001_CBlain'
        '?driver=ODBC+Driver+17+for+SQL+Server'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Optional: Disables Flask-SQLAlchemy's modification tracking
