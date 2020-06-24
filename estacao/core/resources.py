from django.conf import settings
import requests


class WeatherResource:
    def __init__(self):
        self.uri = settings.ESTACAO_API_URI

    def get_weather_data(self):
        response = requests.get(self.uri)
        return response


class MeteogramTemperature:
    def __init__(self):
        self.uri = settings.ESTACAO_API_URI

    def temperature_min(self):
        url = self.uri + '/temperature_min'
        response = requests.get(url)
        return response

    def temperature_max(self):
        url = self.uri + '/temperature_max'
        response = requests.get(url)
        return response
