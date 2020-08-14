from django.shortcuts import render
from bokeh.resources import CDN
from estacao.core.resources import WeatherResource
from estacao.core.charts.temperature import Temperature
from estacao.core.charts.pressao import Pressao


def home(request):
    temp = render_temperature_chart()
    weather_data = get_weather_data()
    pressao = render_pressao_chart()
    context = {
        'conditions': weather_data,
        'temperature': temp,
        'pressao': pressao,
        'bokehcdn': CDN.render()
    }
    return render(request, 'home.html', context)


def get_weather_data():
    weather = WeatherResource()
    weather_data = weather.get_weather_data()
    return weather_data.get('current')


def render_temperature_chart():
    temperature = Temperature()
    temperature.plot()
    return temperature


def render_pressao_chart():
    pressao = Pressao()
    pressao.plot_graph()
    return pressao
