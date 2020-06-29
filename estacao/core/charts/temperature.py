import requests
import numpy as np
from requests.auth import HTTPBasicAuth
from django.conf import settings
from bokeh.plotting import figure
from bokeh.layouts import layout
from bokeh.embed import components
from estacao.core.resources import UriManager


API_URL = getattr(settings, 'API_URL')


class Temperature(UriManager):
    def __init__(self, date_ini=None, date_end=None):
        self.date_ini = date_ini
        self.date_end = date_end
        if not date_ini or not date_end:
            today = np.datetime64('today')
            datetime_delta = np.timedelta64(1, 'D')
            yesterday = today - datetime_delta
            self.date_ini = str(yesterday)
            self.date_end = str(today)

    def plot(self):
        self.make_uri()
        self.load_data()
        self.extract_data(self.temperature_data)
        self.generate_components()
        self.set_components_attributes()

    def make_uri(self):
        self.uri = self.generate_uri(resource='temperature_min')

    def load_data(self):
        try:
            user = getattr(settings, 'API_USER')
            paswd = getattr(settings, 'API_PASWD')
            auth = HTTPBasicAuth(username=user, password=paswd)
            response = requests.get(self.uri, auth=auth).json()
        except Exception:
            response = {'tem_min': [{'data': '2020-06-25 13:00:00', 'temp': '0'}]}
        self.temperature_data = response

    def extract_data(self, data):
        try:
            extracted = dict()
            extracted['date'] = [item['date'] for item in data['temp_min']]
            extracted['temp_min'] = [item['temp'] for item in data['temp_min']]
        except KeyError:
            extracted = {'date': ['2020-06-25 13:00:00'], 'temp_min': ['0']}
        self.extracted_data = extracted

    def generate_components(self):
        date = self.to_datetime(self.extracted_data['date'])
        temperature = self.extracted_data['temp_min']
        temp_figure = figure(x_axis_type='datetime', plot_height=300,
                             tools="pan,wheel_zoom,box_zoom,reset")
        temp_figure.toolbar.logo = None
        temp_figure.line(date, temperature)
        plot = layout([temp_figure], sizing_mode='stretch_width')
        script, div = components(plot)
        self.components = {'script': script, 'div': div}

    def to_datetime(self, date_list):
        datetime_list = []
        for date in date_list:
            date_time = np.datetime64(date)
            datetime_list.append(date_time)
        return datetime_list

    def set_components_attributes(self):
        self.script = self.components.get('script')
        self.div = self.components.get('div')

    def get_script(self):
        return self.script

    def get_div(self):
        return self.div
