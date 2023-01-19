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

@app.route("/signup", methods=['GET', 'POST'])
def register():

    if request.method == 'POST':
        new_user = users(email=request.form['email'], password=request.form['password'])
        db.session.add(new_user)
        db.session.commit()

        return render_template("login.html")

    else:
        return render_template('signup.html')

@app.route("/login", methods = ["POST", "GET"])
def login():

    if request.method == 'POST':
        session.permanent = True
        email = request.form["email"]
        password = request.form["password"]

        found_user = users.query.filter_by(email=email, password=password).first()

        if found_user:
            session["email"] = email
            session["password"] = password
            return render_template("user.html", email = email, password = password)
        else:
            return render_template("signup.html")

    return render_template("login.html")

# @app.route("/user", methods=["POST", "GET"])
# def user():

    # if request.method == "GET":


if __name__ == "__main__":
    # with app.app_context():
    #     db.create_all() #this creates db if it doesnt already exist in our program
    app.run(debug = True)