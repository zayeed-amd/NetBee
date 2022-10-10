import meraki

from project.meraki_api.dashboard import get_dashboard


# from meraki import Networks

class Organizations:
    def __init__(self):
        self.dashboard = None
        if not self.dashboard:
            self.dashboard = get_dashboard()

    def get_all(self):
        # dashboard.organizations.getOrganizationNetworks()
        return self.dashboard.organizations.getOrganizations()

    def get_all_networks(self, id):
        try:
            return self.dashboard.organizations.getOrganizationNetworks(id)
        except meraki.exceptions.APIError as e:
            print(e)
            return list()

    def get_all_networks_for_orgs(self):
        orgs = self.get_all()
        nets = list()
        for org in orgs:
            for k, v in org.items():
                if k == 'id':
                    networks = self.get_all_networks(v)
                    # print(networks)
                    for n in networks:
                        nets.append(n)
        # print(nets)
        return nets

    def get_all_users(self, id):
        orgs = self.get_all()
        # {'id': '646829496481090803', 'name': 'Test-org', 'url': 'https://n149.meraki.com/o/KsrL3cvc/manage/organization/overview',
        # 'api': {'enabled': True}, 'licensing': {'model': 'co-term'}, 'cloud': {'region': {'name': 'North America'}}}
        # users = dashboard.organizations.getOrganizationAdmins(organizationId='549236')
        users = self.dashboard.organizations.getOrganizationAdmins(organizationId=f"{id}")
        # print(users)
        # for u in users:
        #     print(u.keys())
        #     print(u['email'])

        return users


class Networks():
    def __init__(self):
        self.dashboard = None
        if not self.dashboard:
            self.dashboard = get_dashboard()

    def get_network(self, organization_id):
        return self.dashboard.networks.getNetwork(organization_id)

    def get_networks(self, org_ids):
        self.dashboard.organizations.getOrganizationNetworks()


# dashboard.switch.()
# try:
#     print(Organizations.get_all())
# except meraki.exceptions.APIError:
#     print("error")

#
# Networks.get_network()

# Organizations().get_all_networks_for_orgs()

# [{'id': 'L_646829496481105433', 'organizationId': '549236', 'name': 'DevNet Sandbox ALWAYS ON', 'productTypes': ['appliance', 'switch', 'wireless'], 'timeZone': 'America/Los_Angeles', 'tags': [], 'enrollmentString': None, 'url': 'https://n149.meraki.com/DevNet-Sandbox-A/n/EFZ1Davc/manage/usage/list', 'notes': '', 'isBoundToConfigTemplate': False}, {'id': 'L_646829496481110685', 'organizationId': '549236', 'name': 'Mike_test_vmx', 'productTypes': ['appliance', 'camera', 'cellularGateway', 'sensor', 'switch', 'wireless'], 'timeZone': 'America/Los_Angeles', 'tags': [], 'enrollmentString': None, 'url': 'https://n149.meraki.com/Mike_test_vmx-ap/n/H6qRqbvc/manage/usage/list', 'notes': None, 'isBoundToConfigTemplate': False}, {'id': 'L_646829496481111123', 'organizationId': '549236', 'name': 'PKC 3 Python Test', 'productTypes': ['appliance', 'camera', 'switch', 'wireless'], 'timeZone': 'America/Los_Angeles', 'tags': [], 'enrollmentString': None, 'url': 'https://n149.meraki.com/PKC-3-Python-Tes/n/su6Uobvc/manage/usage/list', 'notes': None, 'isBoundToConfigTemplate': False}, {'id': 'L_646829496481111455', 'organizationId': '549236', 'name': 'Cisco Meraki Test LAB Noa', 'productTypes': ['appliance', 'camera', 'switch', 'wireless'], 'timeZone': 'America/Los_Angeles', 'tags': [], 'enrollmentString': None, 'url': 'https://n149.meraki.com/Cisco-Meraki-Tes/n/tC0aDdvc/manage/usage/list', 'notes': None, 'isBoundToConfigTemplate': False}, {'id': 'L_646829496481111545', 'organizationId': '549236', 'name': 'yucansoft.co.uk', 'productTypes': ['appliance', 'camera', 'switch', 'wireless'], 'timeZone': 'America/Los_Angeles', 'tags': [], 'enrollmentString': None, 'url': 'https://n149.meraki.com/yucansoft.co.uk-/n/rjpG9dvc/manage/usage/list', 'notes': None, 'isBoundToConfigTemplate': False}, {'id': 'L_646829496481111792', 'organizationId': '549236', 'name': 'configTestNet', 'productTypes': ['appliance', 'camera', 'switch', 'wireless'], 'timeZone': 'America/Los_Angeles', 'tags': [], 'enrollmentString': None, 'url': 'https://n149.meraki.com/configTestNet-wi/n/yfBf0bvc/manage/usage/list', 'notes': None, 'isBoundToConfigTemplate': False}, {'id': 'L_646829496481111796', 'organizationId': '549236', 'name': 'CT_Test', 'productTypes': ['appliance', 'camera', 'switch', 'wireless'], 'timeZone': 'America/Los_Angeles', 'tags': [], 'enrollmentString': None, 'url': 'https://n149.meraki.com/CT_Test-camera/n/0yLDHdvc/manage/usage/list', 'notes': None, 'isBoundToConfigTemplate': False}, {'id': 'L_646829496481111843', 'organizationId': '549236', 'name': 'TEslag Networks', 'productTypes': ['appliance', 'camera', 'switch', 'wireless'], 'timeZone': 'America/Los_Angeles', 'tags': [], 'enrollmentString': None, 'url': 'https://n149.meraki.com/TEslag-Networks-/n/mRljRcvc/manage/usage/list', 'notes': None, 'isBoundToConfigTemplate': False}, {'id': 'L_646829496481111847', 'organizationId': '549236', 'name': 'JoelGonzalez', 'productTypes': ['appliance', 'camera', 'switch', 'wireless'], 'timeZone': 'America/Los_Angeles', 'tags': [], 'enrollmentString': None, 'url': 'https://n149.meraki.com/JoelGonzalez-wir/n/gmqoxbvc/manage/usage/list', 'notes': None, 'isBoundToConfigTemplate': False}, {'id': 'L_646829496481111849', 'organizationId': '549236', 'name': 'Teslag', 'productTypes': ['appliance', 'camera', 'switch', 'wireless'], 'timeZone': 'America/Los_Angeles', 'tags': [], 'enrollmentString': None, 'url': 'https://n149.meraki.com/Teslag-wireless/n/Xc70scvc/manage/usage/list', 'notes': None, 'isBoundToConfigTemplate': False}, {'id': 'L_646829496481111855', 'organizationId': '549236', 'name': 'Teslag-Networks', 'productTypes': ['appliance', 'camera', 'switch', 'wireless'], 'timeZone': 'America/Los_Angeles', 'tags': [], 'enrollmentString': None, 'url': 'https://n149.meraki.com/Teslag-Networks-/n/yhfWmavc/manage/usage/list', 'notes': '', 'isBoundToConfigTemplate': False}, {'id': 'L_646829496481111878', 'organizationId': '549236', 'name': 'DNENT3-xxxxxxx3columbia.edu', 'productTypes': ['appliance', 'camera', 'switch', 'wireless'], 'timeZone': 'America/Los_Angeles', 'tags': [], 'enrollmentString': None, 'url': 'https://n149.meraki.com/DNENT3-xxxxxxx3c/n/Nd8_Zavc/manage/usage/list', 'notes': None, 'isBoundToConfigTemplate': False}, {'id': 'L_646829496481111896', 'organizationId': '549236', 'name': 'KG-Network', 'productTypes': ['appliance', 'camera', 'switch', 'wireless'], 'timeZone': 'EST', 'tags': [], 'enrollmentString': None, 'url': 'https://n149.meraki.com/KG-Network-wirel/n/fXOvDavc/manage/usage/list', 'notes': '', 'isBoundToConfigTemplate': False}, {'id': 'L_646829496481111910', 'organizationId': '549236', 'name': 'DNENT1-jxxxxncisco.com', 'productTypes': ['appliance', 'camera', 'switch', 'wireless'], 'timeZone': 'America/Los_Angeles', 'tags': [], 'enrollmentString': None, 'url': 'https://n149.meraki.com/DNENT1-jxxxxncis/n/Vge96cvc/manage/usage/list', 'notes': None, 'isBoundToConfigTemplate': False}, {'id': 'L_646829496481111920', 'organizationId': '549236', 'name': 'DNSMB1-jxxxxxggmail.com', 'productTypes': ['appliance', 'camera', 'switch', 'wireless'], 'timeZone': 'America/Los_Angeles', 'tags': [], 'enrollmentString': None, 'url': 'https://n149.meraki.com/DNSMB1-jxxxxxggm/n/0TzYDcvc/manage/usage/list', 'notes': None, 'isBoundToConfigTemplate': False}, {'id': 'L_646829496481111922', 'organizationId': '549236', 'name': 'DNSMB4-gxxxxaunmsm.edu.pe', 'productTypes': ['appliance', 'camera', 'switch', 'wireless'], 'timeZone': 'America/Los_Angeles', 'tags': [], 'enrollmentString': None, 'url': 'https://n149.meraki.com/DNSMB4-gxxxxaunm/n/7suC-avc/manage/usage/list', 'notes': None, 'isBoundToConfigTemplate': False}, {'id': 'L_646829496481111924', 'organizationId': '549236', 'name': 'DNSMB2', 'productTypes': ['appliance', 'camera', 'switch', 'wireless'], 'timeZone': 'America/Los_Angeles', 'tags': [], 'enrollmentString': None, 'url': 'https://n149.meraki.com/DNSMB2-camera/n/Her8Ydvc/manage/usage/list', 'notes': None, 'isBoundToConfigTemplate': False}, {'id': 'L_646829496481111926', 'organizationId': '549236', 'name': 'DNSMB5', 'productTypes': ['appliance', 'camera', 'switch', 'wireless'], 'timeZone': 'America/Los_Angeles', 'tags': [], 'enrollmentString': None, 'url': 'https://n149.meraki.com/DNSMB5-wireless/n/U4CMXavc/manage/usage/list', 'notes': None, 'isBoundToConfigTemplate': False}, {'id': 'L_646829496481111927', 'organizationId': '549236', 'name': 'DNENT2-kxxxx9saskpolytech.ca', 'productTypes': ['appliance', 'camera', 'switch', 'wireless'], 'timeZone': 'America/Los_Angeles', 'tags': [], 'enrollmentString': None, 'url': 'https://n149.meraki.com/DNENT2-kxxxx9sas/n/PWeUncvc/manage/usage/list', 'notes': None, 'isBoundToConfigTemplate': False}, {'id': 'N_646829496481187875', 'organizationId': '549236', 'name': 'vmx_1.1_mike', 'productTypes': ['appliance'], 'timeZone': 'America/Los_Angeles', 'tags': [], 'enrollmentString': None, 'url': 'https://n149.meraki.com/vmx_1.1_mike/n/mBSfkbvc/manage/usage/list', 'notes': '', 'isBoundToConfigTemplate': False}, {'id': 'N_646829496481188321', 'organizationId': '549236', 'name': 'GLB_Network', 'productTypes': ['appliance'], 'timeZone': 'America/Los_Angeles', 'tags': [], 'enrollmentString': None, 'url': 'https://n149.meraki.com/GLB_Network/n/14KUcavc/manage/usage/list', 'notes': None, 'isBoundToConfigTemplate': False}, {'id': 'N_646829496481188541', 'organizationId': '549236', 'name': 'vmx_1.2_mike', 'productTypes': ['appliance'], 'timeZone': 'America/Los_Angeles', 'tags': [], 'enrollmentString': None, 'url': 'https://n149.meraki.com/vmx_1.2_mike/n/erllgavc/manage/usage/list', 'notes': None, 'isBoundToConfigTemplate': False}, {'id': 'N_646829496481188542', 'organizationId': '549236', 'name': 'vmx_1.3_mike', 'productTypes': ['appliance'], 'timeZone': 'America/Los_Angeles', 'tags': [], 'enrollmentString': None, 'url': 'https://n149.meraki.com/vmx_1.3_mike/n/bkWa_bvc/manage/usage/list', 'notes': None, 'isBoundToConfigTemplate': False}, {'id': 'N_646829496481189507', 'organizationId': '549236', 'name': 'CLUS-22', 'productTypes': ['camera'], 'timeZone': 'America/Los_Angeles', 'tags': [], 'enrollmentString': None, 'url': 'https://n149.meraki.com/CLUS-22/n/yRKR8cvc/manage/usage/list', 'notes': None, 'isBoundToConfigTemplate': False}]

orgs = Organizations().get_all()
print(orgs)

# exit()
y = Organizations().get_all_networks('549236')
#
# print(type(y))
for x in y:
    print(x)


# orgs_selected = ['646829496481090803', '646829496481090802', '549236']
# networks = list()
# for org_id in orgs_selected:
#     nets = Organizations().get_all_networks(org_id)
#     if isinstance(networks, list):
#         for n in nets:
#             networks.append(n)
#     elif isinstance(nets, dict):
#             networks.append(nets)
#
# for x in networks:
#     print(x)
# Organizations().get_all_users('549236')
