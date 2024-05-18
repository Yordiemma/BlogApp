import os

class Config:
    SECRET_KEY = os.environ.get('95b6adf2c47453f4e54d602ddd02e9c5') or 'your_secret_key_here'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
