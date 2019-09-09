"""
    This API is build around the API reference from the NS (Dutch Railways).
    You can find the full documentation over here: https://apiportal.ns.nl/docs/services/public-reisinformatie-api/operations/ApiV2StationsGet
    It is required to login with a free account from: https://apiportal.ns.nl/

    In this project there is an API-token included, but because of rate-limits or unauthorized access this can break easily.
    If that is the case, make sure you request your own (free) API-token, which you manage in your account on the website.

    Rate limit should be 5,000 requests per hour per OAuth token
"""

import requests
import json
import datetime

class NSApi:
    API_PATH = "https://gateway.apiportal.ns.nl/public-reisinformatie/api/v2/"
    API_TOKEN = "ecb91cb499714bffa3a6697597d89e32"

    def __init__(self):
        pass

    def get_request_headers(self):
        return {"Ocp-Apim-Subscription-Key": self.API_TOKEN}

    def get_train_stations(self):
        train_stations = []
        request = requests.get(self.API_PATH + "stations", headers=self.get_request_headers())

        if request.status_code != 200:
            print("Error with NS API:")
            print(request.content)
            return None

        data_json = json.loads(request.content)

        for json_station in data_json['payload']:
            # We only want dutch train stations
            if json_station['land'] != 'NL':
                continue

            # Add train station to array 'train_stations'
            train_stations.append({
                'id': json_station['UICCode'],
                'code': json_station['code'],
                'name': json_station['namen']['lang'],
                'location': {
                    'lat': json_station['lat'],
                    'lng': json_station['lng']
                }
            })

        return train_stations

    def get_disruptions(self):
        disruptions = []
        request = requests.get(self.API_PATH + "disruptions", headers=self.get_request_headers())

        if request.status_code != 200:
            print("Error with NS API:")
            print(request.content)
            return None

        data_json = json.loads(request.content)

        for json_disruptions in data_json['payload']:
            disruption_data = {
                'title': json_disruptions['titel'],
                'impact': json_disruptions['verstoring']['impact'] if 'impact' in json_disruptions['verstoring'] else None,
                'society': json_disruptions['verstoring']['maatschappij'] if 'impact' in json_disruptions['verstoring'] else None,
                'stations': []
            }

            if 'trajecten' in json_disruptions['verstoring']:
                for routes in json_disruptions['verstoring']['trajecten']:
                    for route_station in routes['stations']:
                        if route_station not in disruption_data:
                            disruption_data['stations'].append(route_station)

            disruptions.append(disruption_data)

        return disruptions

    def get_departures(self, station_id):
        departures = []
        request = requests.get(self.API_PATH + "departures?uicCode=" + station_id, headers=self.get_request_headers())

        if request.status_code != 200:
            print("Error with NS API:")
            print(request.content)
            return None

        data_json = json.loads(request.content)

        for json_departures in data_json['payload']['departures']:
            planned_timestamp = int(datetime.datetime.strptime(json_departures['plannedDateTime'], "%Y-%m-%dT%H:%M:%S%z").timestamp())
            actual_timestamp = int(datetime.datetime.strptime(json_departures['actualDateTime'], "%Y-%m-%dT%H:%M:%S%z").timestamp())

            departure_date = {
                'id': json_departures['product']['number'],
                'direction': json_departures['direction'],
                'delay_seconds': (actual_timestamp - planned_timestamp),
                'type': json_departures['trainCategory'],
                'stations': []
            }

            for trains in json_departures['routeStations']:
                departure_date['stations'].append(trains['uicCode'])

            departures.append(departure_date)

        return departures