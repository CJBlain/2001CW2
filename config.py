import os

class Config:

    DB_USERNAME = 'CBlain'
    DB_PASSWORD = 'HjnF689+'
    DB_HOST = 'DIST-6-505.uopnet.plymouth.ac.uk'
    DB_NAME = 'COMP2001_CBlain'

    SQLALCHEMY_DATABASE_URI = (
        'mssql+pyodbc://CBlain:HjnF689+@DIST-6-505.uopnet.plymouth.ac.uk/COMP2001_CBlain'
        '?driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False  
