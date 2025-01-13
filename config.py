DB_USERNAME = 'CBlain'
DB_PASSWORD = 'HjnF689+'
DB_HOST = 'DIST-6-505.uopnet.plymouth.ac.uk'
DB_NAME = 'COMP2001_CBlain'

SQLALCHEMY_DATABASE_URI = f"mssql+pyodbc://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}?driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes"
SQLALCHEMY_TRACK_MODIFICATIONS = False
