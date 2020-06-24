from django.shortcuts import render
from estacao.core.resources import WeatherResource
from estacao.core.charts.temperature import Temperature


def home(request):
    temp = Temperature()
    temp.plot()
    weather = WeatherResource()
    weather_data = weather.get_weather_data()
    context = {'conditions': weather_data.json(), 'temperature': temp}
    return render(request, 'home.html', context)
