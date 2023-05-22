import requests

class Endpoint2:
    def __init__(self, url, port):
        self.url = url
        self.port = port

    def get_data(self):
        response = requests.get(f'{self.url}:{self.port}/data2', 
                 headers={'Accept': 'application/json'})
        return response
