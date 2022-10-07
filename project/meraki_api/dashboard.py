# https://docs.google.com/presentation/d/1f0ja-N4gy6OZbIK91LoTz2FXgdmPlyhsgiw7TUTFq_8/edit#slide=id.g14b4003b687_0_195
# https://developer.cisco.com/meraki/api/#!get-network-vlan
# https://account.meraki.com/login/dashboard_login?email=&password_login=true

import meraki
from sqlalchemy.exc import PendingRollbackError

from project import db
from flask_login import current_user
from project.models import Api


def get_api_key():

    api = None
    try:
        api = db.session.query(Api).filter(Api.user_id == current_user.id).first()
    except PendingRollbackError:
        db.session.rollback()
        api = db.session.query(Api).filter(Api.user_id == current_user.id).first()
    except AttributeError:
        pass

    if api:
        return api.api_key

    api_key = "8646ff4c4c17f1db3b6fce47c97a8c0aaad828af"
    print(f"Could not get an API key from Database for this user, using: {api_key}")
    return api_key


def get_dashboard():
    dashboard = meraki.DashboardAPI(api_key=get_api_key(), output_log=False, print_console=False)
    return dashboard


# d = get_dashboard()
# d.switch.getDeviceSwitchPorts()
# p = d.switch.getOrganizationSwitchPortsBySwitch('549236')
# print(p)
# x = d.switch.get
# print(x)
# x = d.switch.getDeviceSwitchPorts('Q2GW-2BWP-FQHX')
# print(x)

# d.sm.getNetworkSmUsers()
# d.networks.

