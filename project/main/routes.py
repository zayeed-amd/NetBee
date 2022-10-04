import flask_login
from flask import render_template, request, Blueprint, send_from_directory
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


@main.route('/organizations/networks', methods=['POST'])
def networks_by_org():
    if request.method == "POST":
        orgs_selected = request.form.getlist('orgs')
        networks = list()
        for org_id in orgs_selected:
            nets = Organizations().get_all_networks(org_id)
            if isinstance(networks, list):
                for n in nets:
                    if isinstance(n, dict):
                        networks.append(n)
                    else:
                        return f"Error: Unexpected Data format {type(n)}, expected: dict"
            elif isinstance(nets, dict):
                networks.append(nets)
        return render_template('meraki/networks_by_orgs.html', networks=networks)

    return "Error: Method not allowed"


@main.route('/organizations/users', methods=['POST'])
def users_by_orgs():
    if request.method == "POST":
        orgs_selected = request.form.getlist('orgs')
        all_users = list()
        for org_id in orgs_selected:
            users = Organizations().get_all_users(org_id)
            if isinstance(all_users, list):
                for n in users:
                    if isinstance(n, dict):
                        all_users.append(n)
                    else:
                        return f"Error: Unexpected Data format {type(n)}, expected: dict"
            elif isinstance(users, dict):
                all_users.append(users)
        return render_template('meraki/users_by_orgs.html', users=all_users)

    return "Error: Method not allowed"


# @main.route("/static/<path:path>")
# def static_dir(path):
#     return send_from_directory("static", path)
