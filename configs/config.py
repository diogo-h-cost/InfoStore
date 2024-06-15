from flask_sqlalchemy import SQLAlchemy

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///produtos.sqlite3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

db = SQLAlchemy()