from flask import Flask, url_for, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("hello.html")

# with app.test_request_context():
    # print("Loaded")
    # # pprint.pprint(vars(request))
    # print("Current Path: " + request.path)

