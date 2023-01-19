from flask import Flask, jsonify, redirect, url_for, render_template, request, make_response, session
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "ghjtyu"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3' #users is the name of the table that we will reference
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.permanent_session_lifetime = timedelta(minutes=5)
db = SQLAlchemy(app)

