from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user
# from flask_bcrypt import Bcrypt
from project.models import User
from project import bcrypt, db
from project.users.forms import LoginForm

# from flaskblog.users.utils import save_picture, send_reset_email

users_bp = Blueprint('users', __name__)


@users_bp.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash('Login Unsuccessful. Please check your email and password!', 'danger')
    return render_template('login.html', title='Login', form=form)


@users_bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.home'))
