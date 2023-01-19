from flask import Flask, jsonify, redirect, url_for, render_template, request, make_response, session
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "ghjtyu"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3' #users is the name of the table that we will reference
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.permanent_session_lifetime = timedelta(minutes=5)
db = SQLAlchemy(app)

class users(db.Model):
    _id = db.Column("id",db.Integer, primary_key = True)
    email = db.Column("email", db.String(100))
    password = db.Column("password", db.String(100))

    def __init__(self, email, password):
        self.email = email
        self.password = password

