from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#postgresql://[user]:[password]@[ip]/[dbname]
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres@46.101.194.177:5435/postgres' 
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, name, email):
        self.name=name
        self.email=emails

    def __repr__(self):
        return '<User %r>' % self.username   

from app import views