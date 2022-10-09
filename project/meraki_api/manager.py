# import requests
# from requests.auth import HTTPBasicAuth
# method = "get"
# url = "https://xxxxx"
# auth = HTTPBasicAuth(apiKey, secret)
# rsp = requests.request(method, url, headers=None, auth=auth)

# https://blog.networktocode.com/post/using-python-requests-with-rest-apis/
# https://developer.cisco.com/meraki/api-latest/#!delete-organization-action-batch

import requests

from project.meraki_api.dashboard import get_api_key


class ApiRef:
    def __int__(self):
        pass

    vlan = {'Get Network Appliance Vlan': '/networks/{networkId}/appliance/vlans', 'put': {}}

    class Get:
        pass

    class Put:
        pass

    class Delete:
        pass

    class Post:
        pass


class MerakiApi:
    def __init__(self, api_version=1, api_key=None):
        self.api_key = None
        self.host = "https://api.meraki.com"
        self.base_path = "/api/v1" if api_version == 1 else "/api/v0"
        self.base_uri = self.host + self.base_path
        self.api_key = api_key if api_key else get_api_key()

        # Set the custom header to include the API key
        self.headers = {'X-Cisco-Meraki-API-Key': self.api_key}

    def __get(self, uri):
        uri = fr'{self.base_uri}/{uri}'
        print(uri)
        return requests.get(uri, headers=self.headers)

    def get(self, uri, json=True):
        response = self.__get(uri)
        if json and response.status_code == 200:
            return response.json()

        return response


# m = MerakiApi()
# orgs = m.get('organizations', False)
# print(orgs.json())
# vlans = m.get(r'/networks/L_646829496481112152/vlans')

