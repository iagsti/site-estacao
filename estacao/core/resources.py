import requests
import numpy as np
from os import path
from urllib.parse import urljoin
from django.conf import settings
from requests.auth import HTTPBasicAuth


REQUEST_TIMEOUT = getattr(settings, 'API_REQUEST_TIMEOUT')


class UriManager:
    def generate_uri(self, step=1, version='v0', resource=''):
        self.make_date_range(step=step)
        self.generate_path(version=version, resource=resource)
        url = getattr(settings, 'API_URL')
        return urljoin(url, self.path)

    def generate_path(self, version='v0', resource=''):
        self.path = path.join(version, resource, self.date_range)

    def make_date_range(self, step=1):
        today = np.datetime64('today')
        date_delta = np.timedelta64(step, 'D')
        yesterday = today - date_delta
        self.date_range = path.join(str(yesterday), str(today))


class WeatherResource:
    def __init__(self):
        uri = getattr(settings, 'API_URL')
        self.uri = urljoin(uri, '/api/v0/current-conditions')
        user = getattr(settings, 'API_USER')
        paswd = getattr(settings, 'API_PASWD')
        self.auth = HTTPBasicAuth(username=user, password=paswd)

    def get_weather_data(self):
        try:
            response = requests.get(self.uri, timeout=REQUEST_TIMEOUT,
                                    auth=self.auth).json()

        except Exception:
            response = {
                "data": "-",
                "temperatura_ar": "-",
                "temperatura_ponto_orvalho": "-",
                "umidade_relativa": "-",
                "temperatura_min": "-",
                "temperatura_max": "-",
                "vento": "-",
                "pressao": "-",
                "visibilidade_min": "-",
                "visibilidade_max": "-",
                "nuvens_baixas": "-",
                "nuvens_medias": "-",
                "nuvens_altas": "-"
            }
        return response


class MeteogramTemperature(UriManager):
    def __init__(self):
        self.uri = settings.API_URL

    def temperature_min(self):
        uri = self.generate_uri(resource='temperatura-min')
        response = requests.get(uri, timeout=REQUEST_TIMEOUT)
        return response.json()

    def temperature_max(self):
        uri = self.generate_uri(resource='temperatura-max')
        response = requests.get(uri, timeout=REQUEST_TIMEOUT)
        return response.json()
