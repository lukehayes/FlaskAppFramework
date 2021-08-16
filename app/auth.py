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
