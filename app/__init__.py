import os
from flask import Flask, render_template

def create_app(test_config=None):

    # Flask Initialization
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'db.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    # Blueprint Initialization
    from . import auth
    app.register_blueprint(auth.bp)


    # Routes
    @app.route('/')
    def index():
        return render_template("index.html")

    return app
