# auth.py
# https://sebhastian.com/failed-building-wheel-mysql-python/
# https://texxl.com/python/cython/fatal-error-c1083-cannot-open-include-file-io-h-no-such-file-or-directory/
import flask_login
from flask import Blueprint, render_template, redirect, url_for, request, flash
# from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from project.models import User, Api, Permission
from project.app_object import db

prof = Blueprint('prof', __name__)


@prof.route('/profile')
@login_required
def profile():
    cur_user_id = flask_login.current_user.id
    user = User.query.get_or_404(flask_login.current_user.id)
    permission = db.session.query(Permission).filter(Permission.id == User.permission_id).filter(User.id == cur_user_id).first()
    api_info = db.session.query(Api, User).filter(Api.user_id == User.id).filter(User.id == cur_user_id).all()
    # print(permission)
    # for p in permission:
    #     print(p)
    return render_template('profile.html', user=user, permission=permission, api_info=api_info)


# @prof.route('/profile/delete/<int:id>')
# @login_required
# def delete(id):
#     role = Role.query.get_or_404(id)
#     try:
#         if not flask_login.current_user.role_id == 1:
#             return "Error"
#         # db.session.close()
#         db.session.delete(role)
#         db.session.commit()
#         return redirect('/role')
#     finally:
#         db.session.close()


@prof.route('/profile/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update(id):
    user = User.query.get_or_404(id)
    if request.method == "POST":
        user.username = request.form['username']
        user.password = request.form['password']
        user.image = request.form['image']
    else:
        return render_template(template_name_or_list='update.html', task=task)

    try:
        db.session.commit()
        return redirect('/role')
    finally:
        db.session.close()
