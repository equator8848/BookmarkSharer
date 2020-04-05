import requests


def get_json(url, params={}, headers={}):
    return requests.get(url, params, header=dict({
                                                     'accept': 'application/json'
                                                 }.items() + headers.items())).json()
