# https://docs.google.com/presentation/d/1f0ja-N4gy6OZbIK91LoTz2FXgdmPlyhsgiw7TUTFq_8/edit#slide=id.g14b4003b687_0_195
# https://developer.cisco.com/meraki/api/#!get-network-vlan
# https://account.meraki.com/login/dashboard_login?email=&password_login=true

import meraki
from sqlalchemy.exc import PendingRollbackError

from project import db
from flask_login import current_user
from project.models import Api


def get_dashboard():
    api_key = "ac84e73e2d143efa3eb1d098b884d02928be5e68"
    try:
        api = db.session.query(Api).filter(Api.user_id == current_user.id).first()
    except PendingRollbackError:
        db.session.rollback()
        api = db.session.query(Api).filter(Api.user_id == current_user.id).first()

    # if not api:
    #     raise KeyError(f"API key not found for user: {current_user.id}")

    if api:
        api_key = api.api_key
    dashboard = meraki.DashboardAPI(api_key=api_key, output_log=False, print_console=False)
    return dashboard


def get_dashboard_static():
    api_key = "ac84e73e2d143efa3eb1d098b884d02928be5e68"
    dashboard = meraki.DashboardAPI(api_key=api_key, output_log=False, print_console=False)
    return dashboard


# d = get_dashboard_static()
# d.switch.getDeviceSwitchPorts()
# p = d.switch.getOrganizationSwitchPortsBySwitch('549236')
# print(p)
# x = d.switch.get
# print(x)
