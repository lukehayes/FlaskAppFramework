import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from app.database import Database

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods = ['GET', 'POST'])
def register():

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = Database()
        error = None

        if not username:
            error = 'The username is missing.'
        if not password:
            error = 'The password is missing.'

        if error is None:
            print("Running database queries...")

    return render_template('auth/register.html')


@bp.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        db = Database()
        error = None

        print(generate_password_hash("password"))

        query = 'SELECT * FROM users WHERE username = "{}"'.format(username)
        print(query)

        user = db.raw_query(
            'SELECT * FROM users WHERE username = "developer"')

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

        flash(error)
    return render_template('auth/login.html')

