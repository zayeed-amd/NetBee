import flask_login
from flask import Blueprint, render_template, redirect, request, url_for
from flask_login import login_required
from project import db
from project.models import Permission, User
from werkzeug.security import generate_password_hash  # check_password_hash

# from flask_login import login_user, logout_user, login_required

users_bp = Blueprint('users_bp', __name__)



@users_bp.route('/users', methods=['GET', 'POST'])
@login_required
def users():
    # users = User.query.order_by(User.username).all()
    # p = db.session.query(User, Permission).filter(Permission.id == User.role_id).filter(User.id == cur_user_id).all()
    # p = db.session.query(User, Permission).filter(Permission.id == User.permission_id).all()
    # p = db.session.query(Permission).filter(Permission.id == User.permission_id).all()
    # db.session.query(Permission.permission_name).filter(Permission.id == User.permission_id).all()

    if request.method == "POST":
        username = request.form.get('username')  # reads the name tag
        email = request.form.get('email')
        password = request.form.get('password')
        permission_id = request.form.get('permission_type')

        new_user = User(username=username, email=email, password=generate_password_hash(password, method='sha256'),
                        permission_id=permission_id)
        db.session.add(new_user)
        db.session.commit()
        # db.session.close()    # cannot cole the session here
        # return render_template(template_name_or_list='users/users.html')
        redirect(url_for('users_bp.users'))

    users_info = db.session.query(User, Permission).filter(Permission.id == User.permission_id).all()
    permissions = db.session.query(Permission).all()
    return render_template(template_name_or_list='users/users.html', users_info=users_info,
                           current_user=flask_login.current_user, permissions=permissions)


@users_bp.route('/users/delete/<int:id>')
@login_required
def delete(id):
    user = User.query.get_or_404(id)
    try:
        if flask_login.current_user.id == id:
            return "Error, cannot delete current user"
        db.session.delete(user)
        db.session.commit()
        return redirect(url_for('users_bp.users'))
    finally:
        pass


@users_bp.route('/users/edit/<int:id>', methods=['GET'])
@login_required
def edit(id):
    user = User.query.get_or_404(id)
    permissions = db.session.query(Permission).all()
    return render_template(template_name_or_list='users/edit.html', user=user, permissions=permissions)


@users_bp.route('/users/update', methods=['POST'])
@login_required
def update():
    # permissions = db.session.query(Permission).all()
    if request.method == "POST":
        # return str(request.form)
        id = request.form['id']
        user = User.query.get_or_404(id)
        user.username = request.form['username']
        user.email = request.form['email']
        user.password = generate_password_hash(request.form['password'], method='sha256')
        user.permission_id = request.form['permission_id']
        try:
            # return "Here"
            # db.session.update(user)
            db.session.commit()
            return redirect(url_for('users_bp.users'))
        finally:
            # db.session.close()
            pass
    else:
        return redirect(url_for('users_bp.users'))
