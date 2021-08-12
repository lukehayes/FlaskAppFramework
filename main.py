from flask import Flask, url_for, request, render_template, redirect, flash
from app.database import Database
import os
import pprint

app = Flask(__name__)
# Session need a secret key to work
app.config.update(SECRET_KEY=os.urandom(24))

db = Database()

@app.route("/")
def index():
    users = db.find("users", "developer")
    return render_template("hello.html", users = users)

@app.route("/login", methods=['GET', 'POST'])
def login():

    error = None

    if request.method == 'POST':
        userObject = db.find("users", request.form['username'])
        # Turn the sqlite.Row object into a dict
        user = dict(zip(userObject.keys(), userObject))

        if len(userObject) == 0:
            flash("User could not be found.")
            return redirect(url_for('login'))
        else:
            if request.form['password'] == user['password']:
                return render_template("hello.html", user = userObject)
                return redirect(url_for('index'))
            else:
                flash("The password was incorrect. Try again.")
                return redirect(url_for('login'))



    return render_template("login.html", error = error)

# with app.test_request_context():
    # print("Loaded")
    # # pprint.pprint(vars(request))
    # print("Current Path: " + request.path)

