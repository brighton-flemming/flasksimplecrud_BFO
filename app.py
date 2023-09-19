# app.py
from flask import Flask
from flask_migrate import Migrate
from models import db
from routes import create_app

app = create_app()

# Configure Flask-Migrate
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///newdb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Migrate(app, db)

if __name__ == '__main__':
    app.run(debug=True)