from django.shortcuts import render
from estacao.core.resources import WeatherResource


def home(request):
    weather = WeatherResource()
    weather_data = weather.get_weather_data()
    context = {'conditions': weather_data.json()}
    return render(request, 'home.html', context)
