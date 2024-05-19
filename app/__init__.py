from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Set the database URI - update the URI with your actual database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

db = SQLAlchemy(app)

from .routes import *  # Import routes from routes.py
