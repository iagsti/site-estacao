from django.conf import settings
import requests


class WeatherResource:
    def __init__(self):
        self.uri = settings.API_URL

    def get_weather_data(self):
        try:
            response = requests.get(self.uri).json()
        except Exception:
            response = {
                "data": "-",
                "temperatura_ar": "-",
                "temperatura_orvalho": "-",
                "ur": "-",
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


class MeteogramTemperature:
    def __init__(self):
        self.uri = settings.API_URL

    def temperature_min(self):
        url = self.uri + '/temperature_min'
        response = requests.get(url)
        return response

    def temperature_max(self):
        url = self.uri + '/temperature_max'
        response = requests.get(url)
        return response
