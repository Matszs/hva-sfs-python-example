"""
    Amsterdam Api description: https://api.data.amsterdam.nl/api/
"""

import requests
import json


class AmsterdamApi:
    API_PATH = "https://api.data.amsterdam.nl/"
    API_DATA_FORMAT = "/?format=json"

    def __init__(self):
        pass

    def perform_request(self, path):
        request = requests.get(self.API_PATH + path + self.API_DATA_FORMAT)
        if request.status_code == 200:
            return json.loads(request.content)
        return None

    def get_api_path(self):
        return self.API_PATH

    def get_trash_bins(self):
        data = self.perform_request("afval/v1/containers")

        if 'results' not in data:
            print("No 'results' in json")
            return None

        trash_bins = []
        for trash_bin in data['results']:
            trash_bins.append({
                'id': trash_bin['id'],
                'name': trash_bin['_display'],
                'type': trash_bin['waste_name'],
                'address': trash_bin['address'],
            })

        return trash_bins

    def get_monuments(self):
        data = self.perform_request("monumenten/monumenten")

        if 'results' not in data:
            print("No 'results' in json")
            return None

        monuments = []

        for monument in data['results']:
            monuments.append({
                'id': monument['monumentnummer'],
                'address': monument['_display']
            })

        return monuments
