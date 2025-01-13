import pyodbc

DB_USERNAME = 'CBlain'  
DB_PASSWORD = 'HjnF689+'  
DB_HOST = 'DIST-6-505.uopnet.plymouth.ac.uk' 
DB_NAME = 'COMP2001_CBlain'  


conn_str = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={DB_HOST};DATABASE={DB_NAME};UID={DB_USERNAME};PWD={DB_PASSWORD};TrustServerCertificate=yes'

try:
    conn = pyodbc.connect(conn_str)
    print("Connection successful!")
    conn.close()  
except Exception as e:
    print(f"Error: {e}")
