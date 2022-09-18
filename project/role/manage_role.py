import flask_login
from flask import Blueprint, render_template, redirect, request
from flask_login import login_required

# from project.app_object import app
from project import db
from project.models import Role, User

# from werkzeug.security import generate_password_hash, check_password_hash
# from flask_login import login_user, logout_user, login_required
role = Blueprint('role', __name__)
# db = SQLAlchemy(app)


@role.route('/role', methods=['GET', 'POST'])
@login_required
def index():
    if request.method == "POST":
        role_name = request.form["role_name"]
        role_desc = request.form["role_desc"]
        if not role_name:
            return render_template(template_name_or_list='errors.html', errors="Content is empty")
        new_role = Role(role_name=role_name, role_desc=role_desc)
        try:
            db.session.add(new_role)
            db.session.commit()
            db.session.close()
            return redirect('/role')  # or redirect(url_for("index"))
        except Exception as e:
            return f"There is an error accepting your input: {e}"
        finally:
            db.session.close()
    else:
        roles = Role.query.order_by(Role.date_created).all()
        # return str(roles)
        return render_template(template_name_or_list='role/role.html', roles=roles, user=flask_login.current_user)


@role.route('/errors', methods=['GET'])
def errors(err):
    return err


@role.route('/role/delete/<int:id>')
@login_required
def delete(id):
    role = Role.query.get_or_404(id)
    try:
        if not flask_login.current_user.role_id == 1:
            return "Error"
        # db.session.close()
        db.session.delete(role)
        db.session.commit()
        return redirect('/role')
    finally:
        db.session.close()


@role.route('/role/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update(id):
    task = Role.query.get_or_404(id)
    if request.method == "POST":
        task.content = request.form['content']
    else:
        return render_template(template_name_or_list='update.html', task=task)

    try:
        db.session.commit()
        return redirect('/role')
    finally:
        db.session.close()
