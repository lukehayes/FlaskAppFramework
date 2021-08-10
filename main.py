from flask import Flask, url_for, request, render_template
from app.database import Database
import pprint

app = Flask(__name__)

db = Database()

@app.route("/")
def index():
    data = db.all("data")
    return render_template("hello.html", d = data)

@app.route("/about")
def about():
    return "About"

# with app.test_request_context():
    # print("Loaded")
    # # pprint.pprint(vars(request))
    # print("Current Path: " + request.path)

