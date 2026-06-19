import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Local DB (for testing)
    SQLALCHEMY_DATABASE_URI = (
    "mssql+pyodbc://hello:Aqwerty12345678@<server>.azure-backend-sql-test.database.windows.net:1433/test"
    "?driver=ODBC+Driver+17+for+SQL+Server")
