# https://docs.google.com/presentation/d/1f0ja-N4gy6OZbIK91LoTz2FXgdmPlyhsgiw7TUTFq_8/edit#slide=id.g14b4003b687_0_195
# https://developer.cisco.com/meraki/api/#!get-network-vlan
# https://account.meraki.com/login/dashboard_login?email=&password_login=true

import meraki

sandbox_api = "0bcef274156a3fa883c058950bcd9f1446bf392d"  # do not delete
zac_api = "bab27aa19220dfab302ab6a68c3bd21bc8b00f7a"
dashboard = meraki.DashboardAPI(api_key=sandbox_api, output_log=False, print_console=False)



# dashboard.networks.get

# dashboard.switch.updateNetworkSwitchMtu()
