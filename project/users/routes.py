# auth.py
# https://sebhastian.com/failed-building-wheel-mysql-python/
# https://texxl.com/python/cython/fatal-error-c1083-cannot-open-include-file-io-h-no-such-file-or-directory/


from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required

from project.models import User
from project.app_object import db

auth = Blueprint('auth', __name__)
# db = SQLAlchemy(app)


@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False
    user = User.query.filter_by(email=email).first()
    # check if user actually exists
    # take the user supplied password, hash it, and compare it to the hashed password in database
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))  # if user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)
    return redirect(url_for('main.home'))


@auth.route('/signup')
def signup():
    return render_template('signup.html')


@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    username = request.form.get('name')
    password = request.form.get('password')

    email_exists = User.query.filter_by(email=email).first()  # if this returns a user, then the email already exists in database
    user_exists = User.query.filter_by(username=username).first()  # if this returns a user, then the email already exists in database

    if email_exists:  # if a user is found, we want to redirect back to signup page so user can try again
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))
    elif user_exists:
        flash('Username is already taken, please try another one!')
        return redirect(url_for('auth.signup'))

    # create new user with the form data. Hash the password so plaintext version isn't saved.
    new_user = User(email=email, username=username, password=generate_password_hash(password, method='sha256'), permission_id=1)

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()
    db.session.close()
    return redirect(url_for('auth.login'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

