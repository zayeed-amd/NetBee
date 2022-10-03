import meraki
from pprint import pprint as pp
from dashboard import dashboard

import csv

'''
Utility functions to be made as we go
'''


# This will get us all of our network ids
def getNetworkIDS(inventory):
    network_ids = set()  # a set keeps unique values

    for device in inventory:
        network_id = device["networkId"]
        if network_id is not None:
            network_ids.add(network_id)
    return network_ids


# This will output our inventory as a csv file for further reading
def dictToCSV(inventory):
    keys = inventory[0].keys()
    with open('inventory.csv', 'w', encoding='utf8', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=inventory[0].keys())
        dict_writer.writeheader()
        dict_writer.writerows(inventory)


# Start our API calls by creating a dashboard instance
# dashboard = meraki.DashboardAPI(api_key="aaabbbbccccdddd12345678")

# In order to access the modules, we need to use the __getattr__ function
# It will return to us an instance of that module
# Other modules include admins, base, clients, devices, networks, organizations, and ssids
organizations = dashboard.organizations.getOrganizations()

# Next we will get an inventory of our devices
inventory = dashboard.organizations.getOrganizations(1234567)
network_ids = getNetworkIDS(inventory)

print(network_ids)

for network_id in network_ids:
    print(network_id, ":")
    print(dashboard.vlans.getNetworkVlans(network_id))
