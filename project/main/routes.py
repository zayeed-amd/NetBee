import flask_login
from flask import render_template, request, Blueprint
from flask_login import login_required

from project.meraki_api.organizations import Organizations

# {{url_for('main.about')}}
main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
@login_required
def home():
    # page = request.args.get('page', 1, type=int)
    # posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    # return str(flask_login.current_user.username)
    return render_template('index.html', user_info=flask_login.current_user)
    # return r"/home"


@main.route("/about")
def about():
    # return render_template('about.html', title='About')
    return r"/about "


@main.route('/organizations')
def organizations():
    return render_template('meraki/organizations.html', orgs=Organizations.get_all())


@main.route('/networks')
def networks():
    return render_template('meraki/networks.html', networks=Organizations().get_all_networks_for_orgs())