from django.conf import settings
import requests


class WeatherResource:
    def __init__(self):
        self.uri = settings.ESTACAO_API_URI

    def get_weather_data(self):
        response = requests.get(self.uri)
        return response
