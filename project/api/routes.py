import flask_login
from flask import Blueprint, render_template, redirect, request
from flask_login import login_required

# from project.app_object import app
from project import db
from project.models import Permission, User, Api

# from werkzeug.security import generate_password_hash, check_password_hash
# from flask_login import login_user, logout_user, login_required
api = Blueprint('api', __name__)
# db = SQLAlchemy(app)


@api.route('/api', methods=['GET', 'POST'])
@login_required
def index():
    if request.method == "POST":
        api_provider = request.form["api_provider"]
        api_username = request.form["api_username"]
        api_password = request.form["api_password"]
        api_key = request.form["api_key"]
        # user = request.form["role_desc"]
        if not api_provider:
            return render_template(template_name_or_list='errors.html', errors="api_provider is empty")
        new_api = Api(api_provider=api_provider, api_username=api_username, api_key=api_key, user_id=flask_login.current_user.id, api_password=api_password)
        try:
            db.session.add(new_api)
            db.session.commit()
            db.session.close()
            return redirect('/api')  # or redirect(url_for("index"))
        except Exception as e:
            return f"There is an error accepting your input: {e}"
        finally:
            db.session.close()
    else:
        api = Api.query.order_by(Api.date_created).all()
        return render_template(template_name_or_list='api.html', api=api, user=flask_login.current_user)


@api.route('/errors', methods=['GET'])
def errors(err):
    return err


@api.route('/api/delete/<int:id>')
@login_required
def delete(id):
    api = Api.query.get_or_404(id)
    try:
        if flask_login.current_user.permission_id != 4:
            return "Error"
        # db.session.close()
        db.session.delete(api)
        db.session.commit()
        return redirect('/api')
    except:
        return "Error due to exception"
    finally:
        # db.session.close()
        pass


@api.route('/api/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update(id):
    task = Permission.query.get_or_404(id)
    if request.method == "POST":
        task.content = request.form['content']
    else:
        return render_template(template_name_or_list='update_api.html', task=task)

    try:
        db.session.commit()
        return redirect('/api')
    finally:
        pass