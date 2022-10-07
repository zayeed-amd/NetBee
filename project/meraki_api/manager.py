# import requests
# from requests.auth import HTTPBasicAuth
# method = "get"
# url = "https://xxxxx"
# auth = HTTPBasicAuth(apiKey, secret)
# rsp = requests.request(method, url, headers=None, auth=auth)
from enum import Enum

# https://blog.networktocode.com/post/using-python-requests-with-rest-apis/
# https://developer.cisco.com/meraki/api-latest/#!delete-organization-action-batch


import requests
import os
from project.meraki_api.dashboard import get_api_key

class APIRef(Enum):
    vlan = {'Get Network Appliance Vlan': '/networks/{networkId}/appliance/vlans', 'put': {}}


class MerakiApi:
    def __init__(self, api_version=1, api_key=None):
        self.base_uri = None
        self.api_key = None
        if api_version == 1:
            self.base_uri = "https://api.meraki.com/api/v1"
        else:
            self.base_uri = "https://api.meraki.com/api/v0"

        if api_key:
            self.api_key = api_key
        else:
            self.api_key = get_api_key()

        # Set the custom header to include the API key
        self.headers = {'X-Cisco-Meraki-API-Key': self.api_key}

    def get(self, uri):
        # Get a list of organizations
        uri = fr'{self.base_uri}/{uri}'
        print(uri)
        response = requests.get(uri, headers=self.headers)
        # print(response.content)

        if response.status_code == 200:
            return response.json()

        return response


m = MerakiApi()
orgs = m.get('organizations')
print(orgs)

