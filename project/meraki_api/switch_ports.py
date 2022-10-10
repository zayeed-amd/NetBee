import meraki

api_key = "31df2ffcef12078fc5044058424d298f83da4f3f"


def get_dashboard():
    dashboard = meraki.DashboardAPI(api_key=api_key,
                                    output_log=False,
                                    print_console=False)
    return dashboard


d = get_dashboard()
netid = 'L_646829496481112155'

# Get the network details
network = d.networks.getNetwork(netid)
for k, v in network.items():
    print(f"{k}:{v}")
print('------------------------------------------------------')

# get all the devices for the given network
devices = d.networks.getNetworkDevices(netid)
for dev in devices:
    for k, v in dev.items():
        print(f"{k}:{v}")
    print('---------------------')

print('------------------------------------------------------')

# get the Ports the following switch serial #
serial = 'Q2GW-2WW9-LLZC'
ports = d.switch.getDeviceSwitchPorts(serial=serial)


for port in ports:
    print(port)


# Example output:
# id:L_646829496481112155
# organizationId:549236
# productTypes:['appliance', 'switch']
# url:https://n149.meraki.com/DNENT2-oxxxxxtgm/n/hrKLqavc/manage/usage/list
# name:DNENT2-oxxxxxtgmail.com
# timeZone:America/Los_Angeles
# enrollmentString:None
# tags:[]
# notes:None
# isBoundToConfigTemplate:False
# ------------------------------------------------------
# lat:37.4180951010362
# lng:-122.098531723022
# address:
# serial:Q2GW-2WW9-LLZC
# mac:34:56:fe:a5:8a:20
# lanIp:None
# url:https://n149.meraki.com/DNENT2-oxxxxxtgm/n/amgKpavc/manage/nodes/new_list/57548244093472
# networkId:L_646829496481112155
# tags:[]
# model:MS225-24P
# switchProfileId:None
# firmware:Not running configured version
# floorPlanId:None
# ---------------------
# lat:37.4180951010362
# lng:-122.098531723022
# address:
# serial:Q2PN-WWNM-JRAS
# mac:e0:55:3d:2b:ef:a0
# wan1Ip:None
# wan2Ip:None
# url:https://n149.meraki.com/DNENT2-oxxxxxtgm/n/Mb9G7cvc/manage/nodes/new_list/246656703131552
# networkId:L_646829496481112155
# tags:[]
# model:MX84
# firmware:Not running configured version
# floorPlanId:None
# ---------------------
# ------------------------------------------------------
# {'portId': '1', 'name': None, 'tags': [], 'enabled': True, 'poeEnabled': True, 'type': 'trunk', 'vlan': 1, 'voiceVlan': None, 'allowedVlans': 'all', 'isolationEnabled': False, 'rstpEnabled': True, 'stpGuard': 'disabled', 'linkNegotiation': 'Auto negotiate', 'portScheduleId': None, 'udld': 'Alert only', 'linkNegotiationCapabilities': ['Auto negotiate', '1 Gigabit full duplex (forced)', '100 Megabit (auto)', '100 Megabit half duplex (forced)', '100 Megabit full duplex (forced)', '10 Megabit (auto)', '10 Megabit half duplex (forced)', '10 Megabit full duplex (forced)'], 'accessPolicyType': 'Open'}
# {'portId': '2', 'name': None, 'tags': [], 'enabled': True, 'poeEnabled': True, 'type': 'trunk', 'vlan': 1, 'voiceVlan': None, 'allowedVlans': 'all', 'isolationEnabled': False, 'rstpEnabled': True, 'stpGuard': 'disabled', 'linkNegotiation': 'Auto negotiate', 'portScheduleId': None, 'udld': 'Alert only', 'linkNegotiationCapabilities': ['Auto negotiate', '1 Gigabit full duplex (forced)', '100 Megabit (auto)', '100 Megabit half duplex (forced)', '100 Megabit full duplex (forced)', '10 Megabit (auto)', '10 Megabit half duplex (forced)', '10 Megabit full duplex (forced)'], 'accessPolicyType': 'Open'}
# {'portId': '3', 'name': None, 'tags': [], 'enabled': True, 'poeEnabled': True, 'type': 'trunk', 'vlan': 1, 'voiceVlan': None, 'allowedVlans': 'all', 'isolationEnabled': False, 'rstpEnabled': True, 'stpGuard': 'disabled', 'linkNegotiation': 'Auto negotiate', 'portScheduleId': None, 'udld': 'Alert only', 'linkNegotiationCapabilities': ['Auto negotiate', '1 Gigabit full duplex (forced)', '100 Megabit (auto)', '100 Megabit half duplex (forced)', '100 Megabit full duplex (forced)', '10 Megabit (auto)', '10 Megabit half duplex (forced)', '10 Megabit full duplex (forced)'], 'accessPolicyType': 'Open'}
# {'portId': '4', 'name': None, 'tags': [], 'enabled': True, 'poeEnabled': True, 'type': 'trunk', 'vlan': 1, 'voiceVlan': None, 'allowedVlans': 'all', 'isolationEnabled': False, 'rstpEnabled': True, 'stpGuard': 'disabled', 'linkNegotiation': 'Auto negotiate', 'portScheduleId': None, 'udld': 'Alert only', 'linkNegotiationCapabilities': ['Auto negotiate', '1 Gigabit full duplex (forced)', '100 Megabit (auto)', '100 Megabit half duplex (forced)', '100 Megabit full duplex (forced)', '10 Megabit (auto)', '10 Megabit half duplex (forced)', '10 Megabit full duplex (forced)'], 'accessPolicyType': 'Open'}
# {'portId': '5', 'name': None, 'tags': [], 'enabled': True, 'poeEnabled': True, 'type': 'trunk', 'vlan': 1, 'voiceVlan': None, 'allowedVlans': 'all', 'isolationEnabled': False, 'rstpEnabled': True, 'stpGuard': 'disabled', 'linkNegotiation': 'Auto negotiate', 'portScheduleId': None, 'udld': 'Alert only', 'linkNegotiationCapabilities': ['Auto negotiate', '1 Gigabit full duplex (forced)', '100 Megabit (auto)', '100 Megabit half duplex (forced)', '100 Megabit full duplex (forced)', '10 Megabit (auto)', '10 Megabit half duplex (forced)', '10 Megabit full duplex (forced)'], 'accessPolicyType': 'Open'}
# {'portId': '6', 'name': None, 'tags': [], 'enabled': True, 'poeEnabled': True, 'type': 'trunk', 'vlan': 1, 'voiceVlan': None, 'allowedVlans': 'all', 'isolationEnabled': False, 'rstpEnabled': True, 'stpGuard': 'disabled', 'linkNegotiation': 'Auto negotiate', 'portScheduleId': None, 'udld': 'Alert only', 'linkNegotiationCapabilities': ['Auto negotiate', '1 Gigabit full duplex (forced)', '100 Megabit (auto)', '100 Megabit half duplex (forced)', '100 Megabit full duplex (forced)', '10 Megabit (auto)', '10 Megabit half duplex (forced)', '10 Megabit full duplex (forced)'], 'accessPolicyType': 'Open'}
# {'portId': '7', 'name': None, 'tags': [], 'enabled': True, 'poeEnabled': True, 'type': 'trunk', 'vlan': 1, 'voiceVlan': None, 'allowedVlans': 'all', 'isolationEnabled': False, 'rstpEnabled': True, 'stpGuard': 'disabled', 'linkNegotiation': 'Auto negotiate', 'portScheduleId': None, 'udld': 'Alert only', 'linkNegotiationCapabilities': ['Auto negotiate', '1 Gigabit full duplex (forced)', '100 Megabit (auto)', '100 Megabit half duplex (forced)', '100 Megabit full duplex (forced)', '10 Megabit (auto)', '10 Megabit half duplex (forced)', '10 Megabit full duplex (forced)'], 'accessPolicyType': 'Open'}
# {'portId': '8', 'name': None, 'tags': [], 'enabled': True, 'poeEnabled': True, 'type': 'trunk', 'vlan': 1, 'voiceVlan': None, 'allowedVlans': 'all', 'isolationEnabled': False, 'rstpEnabled': True, 'stpGuard': 'disabled', 'linkNegotiation': 'Auto negotiate', 'portScheduleId': None, 'udld': 'Alert only', 'linkNegotiationCapabilities': ['Auto negotiate', '1 Gigabit full duplex (forced)', '100 Megabit (auto)', '100 Megabit half duplex (forced)', '100 Megabit full duplex (forced)', '10 Megabit (auto)', '10 Megabit half duplex (forced)', '10 Megabit full duplex (forced)'], 'accessPolicyType': 'Open'}
# {'portId': '9', 'name': None, 'tags': [], 'enabled': True, 'poeEnabled': True, 'type': 'trunk', 'vlan': 1, 'voiceVlan': None, 'allowedVlans': 'all', 'isolationEnabled': False, 'rstpEnabled': True, 'stpGuard': 'disabled', 'linkNegotiation': 'Auto negotiate', 'portScheduleId': None, 'udld': 'Alert only', 'linkNegotiationCapabilities': ['Auto negotiate', '1 Gigabit full duplex (forced)', '100 Megabit (auto)', '100 Megabit half duplex (forced)', '100 Megabit full duplex (forced)', '10 Megabit (auto)', '10 Megabit half duplex (forced)', '10 Megabit full duplex (forced)'], 'accessPolicyType': 'Open'}
# {'portId': '10', 'name': None, 'tags': [], 'enabled': True, 'poeEnabled': True, 'type': 'trunk', 'vlan': 1, 'voiceVlan': None, 'allowedVlans': 'all', 'isolationEnabled': False, 'rstpEnabled': True, 'stpGuard': 'disabled', 'linkNegotiation': 'Auto negotiate', 'portScheduleId': None, 'udld': 'Alert only', 'linkNegotiationCapabilities': ['Auto negotiate', '1 Gigabit full duplex (forced)', '100 Megabit (auto)', '100 Megabit half duplex (forced)', '100 Megabit full duplex (forced)', '10 Megabit (auto)', '10 Megabit half duplex (forced)', '10 Megabit full duplex (forced)'], 'accessPolicyType': 'Open'}
# {'portId': '11', 'name': None, 'tags': [], 'enabled': True, 'poeEnabled': True, 'type': 'trunk', 'vlan': 1, 'voiceVlan': None, 'allowedVlans': 'all', 'isolationEnabled': False, 'rstpEnabled': True, 'stpGuard': 'disabled', 'linkNegotiation': 'Auto negotiate', 'portScheduleId': None, 'udld': 'Alert only', 'linkNegotiationCapabilities': ['Auto negotiate', '1 Gigabit full duplex (forced)', '100 Megabit (auto)', '100 Megabit half duplex (forced)', '100 Megabit full duplex (forced)', '10 Megabit (auto)', '10 Megabit half duplex (forced)', '10 Megabit full duplex (forced)'], 'accessPolicyType': 'Open'}
# {'portId': '12', 'name': None, 'tags': [], 'enabled': True, 'poeEnabled': True, 'type': 'trunk', 'vlan': 1, 'voiceVlan': None, 'allowedVlans': 'all', 'isolationEnabled': False, 'rstpEnabled': True, 'stpGuard': 'disabled', 'linkNegotiation': 'Auto negotiate', 'portScheduleId': None, 'udld': 'Alert only', 'linkNegotiationCapabilities': ['Auto negotiate', '1 Gigabit full duplex (forced)', '100 Megabit (auto)', '100 Megabit half duplex (forced)', '100 Megabit full duplex (forced)', '10 Megabit (auto)', '10 Megabit half duplex (forced)', '10 Megabit full duplex (forced)'], 'accessPolicyType': 'Open'}
# {'portId': '13', 'name': None, 'tags': [], 'enabled': True, 'poeEnabled': True, 'type': 'trunk', 'vlan': 1, 'voiceVlan': None, 'allowedVlans': 'all', 'isolationEnabled': False, 'rstpEnabled': True, 'stpGuard': 'disabled', 'linkNegotiation': 'Auto negotiate', 'portScheduleId': None, 'udld': 'Alert only', 'linkNegotiationCapabilities': ['Auto negotiate', '1 Gigabit full duplex (forced)', '100 Megabit (auto)', '100 Megabit half duplex (forced)', '100 Megabit full duplex (forced)', '10 Megabit (auto)', '10 Megabit half duplex (forced)', '10 Megabit full duplex (forced)'], 'accessPolicyType': 'Open'}
# {'portId': '14', 'name': None, 'tags': [], 'enabled': True, 'poeEnabled': True, 'type': 'trunk', 'vlan': 1, 'voiceVlan': None, 'allowedVlans': 'all', 'isolationEnabled': False, 'rstpEnabled': True, 'stpGuard': 'disabled', 'linkNegotiation': 'Auto negotiate', 'portScheduleId': None, 'udld': 'Alert only', 'linkNegotiationCapabilities': ['Auto negotiate', '1 Gigabit full duplex (forced)', '100 Megabit (auto)', '100 Megabit half duplex (forced)', '100 Megabit full duplex (forced)', '10 Megabit (auto)', '10 Megabit half duplex (forced)', '10 Megabit full duplex (forced)'], 'accessPolicyType': 'Open'}
# {'portId': '15', 'name': None, 'tags': [], 'enabled': True, 'poeEnabled': True, 'type': 'trunk', 'vlan': 1, 'voiceVlan': None, 'allowedVlans': 'all', 'isolationEnabled': False, 'rstpEnabled': True, 'stpGuard': 'disabled', 'linkNegotiation': 'Auto negotiate', 'portScheduleId': None, 'udld': 'Alert only', 'linkNegotiationCapabilities': ['Auto negotiate', '1 Gigabit full duplex (forced)', '100 Megabit (auto)', '100 Megabit half duplex (forced)', '100 Megabit full duplex (forced)', '10 Megabit (auto)', '10 Megabit half duplex (forced)', '10 Megabit full duplex (forced)'], 'accessPolicyType': 'Open'}
# {'portId': '16', 'name': None, 'tags': [], 'enabled': True, 'poeEnabled': True, 'type': 'trunk', 'vlan': 1, 'voiceVlan': None, 'allowedVlans': 'all', 'isolationEnabled': False, 'rstpEnabled': True, 'stpGuard': 'disabled', 'linkNegotiation': 'Auto negotiate', 'portScheduleId': None, 'udld': 'Alert only', 'linkNegotiationCapabilities': ['Auto negotiate', '1 Gigabit full duplex (forced)', '100 Megabit (auto)', '100 Megabit half duplex (forced)', '100 Megabit full duplex (forced)', '10 Megabit (auto)', '10 Megabit half duplex (forced)', '10 Megabit full duplex (forced)'], 'accessPolicyType': 'Open'}
# {'portId': '17', 'name': None, 'tags': [], 'enabled': True, 'poeEnabled': True, 'type': 'trunk', 'vlan': 1, 'voiceVlan': None, 'allowedVlans': 'all', 'isolationEnabled': False, 'rstpEnabled': True, 'stpGuard': 'disabled', 'linkNegotiation': 'Auto negotiate', 'portScheduleId': None, 'udld': 'Alert only', 'linkNegotiationCapabilities': ['Auto negotiate', '1 Gigabit full duplex (forced)', '100 Megabit (auto)', '100 Megabit half duplex (forced)', '100 Megabit full duplex (forced)', '10 Megabit (auto)', '10 Megabit half duplex (forced)', '10 Megabit full duplex (forced)'], 'accessPolicyType': 'Open'}
# {'portId': '18', 'name': None, 'tags': [], 'enabled': True, 'poeEnabled': True, 'type': 'trunk', 'vlan': 1, 'voiceVlan': None, 'allowedVlans': 'all', 'isolationEnabled': False, 'rstpEnabled': True, 'stpGuard': 'disabled', 'linkNegotiation': 'Auto negotiate', 'portScheduleId': None, 'udld': 'Alert only', 'linkNegotiationCapabilities': ['Auto negotiate', '1 Gigabit full duplex (forced)', '100 Megabit (auto)', '100 Megabit half duplex (forced)', '100 Megabit full duplex (forced)', '10 Megabit (auto)', '10 Megabit half duplex (forced)', '10 Megabit full duplex (forced)'], 'accessPolicyType': 'Open'}
# {'portId': '19', 'name': None, 'tags': [], 'enabled': True, 'poeEnabled': True, 'type': 'trunk', 'vlan': 1, 'voiceVlan': None, 'allowedVlans': 'all', 'isolationEnabled': False, 'rstpEnabled': True, 'stpGuard': 'disabled', 'linkNegotiation': 'Auto negotiate', 'portScheduleId': None, 'udld': 'Alert only', 'linkNegotiationCapabilities': ['Auto negotiate', '1 Gigabit full duplex (forced)', '100 Megabit (auto)', '100 Megabit half duplex (forced)', '100 Megabit full duplex (forced)', '10 Megabit (auto)', '10 Megabit half duplex (forced)', '10 Megabit full duplex (forced)'], 'accessPolicyType': 'Open'}
# {'portId': '20', 'name': None, 'tags': [], 'enabled': True, 'poeEnabled': True, 'type': 'trunk', 'vlan': 1, 'voiceVlan': None, 'allowedVlans': 'all', 'isolationEnabled': False, 'rstpEnabled': True, 'stpGuard': 'disabled', 'linkNegotiation': 'Auto negotiate', 'portScheduleId': None, 'udld': 'Alert only', 'linkNegotiationCapabilities': ['Auto negotiate', '1 Gigabit full duplex (forced)', '100 Megabit (auto)', '100 Megabit half duplex (forced)', '100 Megabit full duplex (forced)', '10 Megabit (auto)', '10 Megabit half duplex (forced)', '10 Megabit full duplex (forced)'], 'accessPolicyType': 'Open'}
# {'portId': '21', 'name': None, 'tags': [], 'enabled': True, 'poeEnabled': True, 'type': 'trunk', 'vlan': 1, 'voiceVlan': None, 'allowedVlans': 'all', 'isolationEnabled': False, 'rstpEnabled': True, 'stpGuard': 'disabled', 'linkNegotiation': 'Auto negotiate', 'portScheduleId': None, 'udld': 'Alert only', 'linkNegotiationCapabilities': ['Auto negotiate', '1 Gigabit full duplex (forced)', '100 Megabit (auto)', '100 Megabit half duplex (forced)', '100 Megabit full duplex (forced)', '10 Megabit (auto)', '10 Megabit half duplex (forced)', '10 Megabit full duplex (forced)'], 'accessPolicyType': 'Open'}
# {'portId': '22', 'name': None, 'tags': [], 'enabled': True, 'poeEnabled': True, 'type': 'trunk', 'vlan': 1, 'voiceVlan': None, 'allowedVlans': 'all', 'isolationEnabled': False, 'rstpEnabled': True, 'stpGuard': 'disabled', 'linkNegotiation': 'Auto negotiate', 'portScheduleId': None, 'udld': 'Alert only', 'linkNegotiationCapabilities': ['Auto negotiate', '1 Gigabit full duplex (forced)', '100 Megabit (auto)', '100 Megabit half duplex (forced)', '100 Megabit full duplex (forced)', '10 Megabit (auto)', '10 Megabit half duplex (forced)', '10 Megabit full duplex (forced)'], 'accessPolicyType': 'Open'}
# {'portId': '23', 'name': None, 'tags': [], 'enabled': True, 'poeEnabled': True, 'type': 'trunk', 'vlan': 1, 'voiceVlan': None, 'allowedVlans': 'all', 'isolationEnabled': False, 'rstpEnabled': True, 'stpGuard': 'disabled', 'linkNegotiation': 'Auto negotiate', 'portScheduleId': None, 'udld': 'Alert only', 'linkNegotiationCapabilities': ['Auto negotiate', '1 Gigabit full duplex (forced)', '100 Megabit (auto)', '100 Megabit half duplex (forced)', '100 Megabit full duplex (forced)', '10 Megabit (auto)', '10 Megabit half duplex (forced)', '10 Megabit full duplex (forced)'], 'accessPolicyType': 'Open'}
# {'portId': '24', 'name': None, 'tags': [], 'enabled': True, 'poeEnabled': True, 'type': 'trunk', 'vlan': 1, 'voiceVlan': None, 'allowedVlans': 'all', 'isolationEnabled': False, 'rstpEnabled': True, 'stpGuard': 'disabled', 'linkNegotiation': 'Auto negotiate', 'portScheduleId': None, 'udld': 'Alert only', 'linkNegotiationCapabilities': ['Auto negotiate', '1 Gigabit full duplex (forced)', '100 Megabit (auto)', '100 Megabit half duplex (forced)', '100 Megabit full duplex (forced)', '10 Megabit (auto)', '10 Megabit half duplex (forced)', '10 Megabit full duplex (forced)'], 'accessPolicyType': 'Open'}
# {'portId': '25', 'name': None, 'tags': [], 'enabled': True, 'poeEnabled': False, 'type': 'trunk', 'vlan': 1, 'voiceVlan': None, 'allowedVlans': 'all', 'isolationEnabled': False, 'rstpEnabled': True, 'stpGuard': 'disabled', 'linkNegotiation': 'Auto negotiate', 'portScheduleId': None, 'udld': 'Alert only', 'linkNegotiationCapabilities': ['Auto negotiate', '1 Gigabit full duplex (auto)', '1 Gigabit full duplex (forced)'], 'accessPolicyType': 'Open'}
# {'portId': '26', 'name': None, 'tags': [], 'enabled': True, 'poeEnabled': False, 'type': 'trunk', 'vlan': 1, 'voiceVlan': None, 'allowedVlans': 'all', 'isolationEnabled': False, 'rstpEnabled': True, 'stpGuard': 'disabled', 'linkNegotiation': 'Auto negotiate', 'portScheduleId': None, 'udld': 'Alert only', 'linkNegotiationCapabilities': ['Auto negotiate', '1 Gigabit full duplex (auto)', '1 Gigabit full duplex (forced)'], 'accessPolicyType': 'Open'}
# {'portId': '27', 'name': None, 'tags': [], 'enabled': True, 'poeEnabled': False, 'type': 'trunk', 'vlan': 1, 'voiceVlan': None, 'allowedVlans': 'all', 'isolationEnabled': False, 'rstpEnabled': True, 'stpGuard': 'disabled', 'linkNegotiation': 'Auto negotiate', 'portScheduleId': None, 'udld': 'Alert only', 'linkNegotiationCapabilities': ['Auto negotiate', '1 Gigabit full duplex (auto)', '1 Gigabit full duplex (forced)'], 'accessPolicyType': 'Open'}
# {'portId': '28', 'name': None, 'tags': [], 'enabled': True, 'poeEnabled': False, 'type': 'trunk', 'vlan': 1, 'voiceVlan': None, 'allowedVlans': 'all', 'isolationEnabled': False, 'rstpEnabled': True, 'stpGuard': 'disabled', 'linkNegotiation': 'Auto negotiate', 'portScheduleId': None, 'udld': 'Alert only', 'linkNegotiationCapabilities': ['Auto negotiate', '1 Gigabit full duplex (auto)', '1 Gigabit full duplex (forced)'], 'accessPolicyType': 'Open'}
# {'portId': '29', 'name': None, 'tags': [], 'enabled': True, 'poeEnabled': False, 'type': 'trunk', 'vlan': 1, 'voiceVlan': None, 'allowedVlans': 'all', 'isolationEnabled': False, 'rstpEnabled': True, 'stpGuard': 'disabled', 'linkNegotiation': 'Auto negotiate', 'portScheduleId': None, 'udld': 'Alert only', 'linkNegotiationCapabilities': ['Auto negotiate'], 'accessPolicyType': 'Open'}
# {'portId': '30', 'name': None, 'tags': [], 'enabled': True, 'poeEnabled': False, 'type': 'trunk', 'vlan': 1, 'voiceVlan': None, 'allowedVlans': 'all', 'isolationEnabled': False, 'rstpEnabled': True, 'stpGuard': 'disabled', 'linkNegotiation': 'Auto negotiate', 'portScheduleId': None, 'udld': 'Alert only', 'linkNegotiationCapabilities': ['Auto negotiate'], 'accessPolicyType': 'Open'}
#
# Process finished with exit code 0

