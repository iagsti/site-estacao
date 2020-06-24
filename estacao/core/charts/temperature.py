import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth
from django.conf import settings
from bokeh.plotting import figure
from bokeh.embed import components


API_URL = getattr(settings, 'API_URL')


class Temperature():
    def plot(self, date_ini='2020-01-01', date_end='2020-02-01'):
        self.generate_uri(date_ini, date_end)
        self.load_data()
        self.extract_data(self.temperature_data)
        self.generate_components()
        self.set_components_attributes()

    def generate_uri(self, date_ini, date_end):
        uri = '{}/{}/{}/'.format(API_URL, date_ini, date_end)
        self.uri = uri

    def load_data(self):
        user = getattr(settings, 'API_USER')
        paswd = getattr(settings, 'API_PASWD')
        auth = HTTPBasicAuth(username=user, password=paswd)
        response = requests.get(self.uri, auth=auth)
        self.temperature_data = response.json()

    def extract_data(self, data):
        extracted = dict()
        extracted['date'] = [item['date'] for item in data['temp_min']]
        extracted['temp_min'] = [item['temp'] for item in data['temp_min']]
        self.extracted_data = extracted

    def generate_components(self):
        date = self.to_datetime(self.extracted_data['date'])
        temperature = self.extracted_data['temp_min']
        temp_figure = figure(x_axis_type='datetime')
        temp_figure.line(date, temperature, legend_label="Temp", line_width=1)
        script, div = components(temp_figure)
        self.components = {'script': script, 'div': div}

    def to_datetime(self, date_list):
        datetime_list = []
        for date in date_list:
            date_time = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
            datetime_list.append(date_time)
        return datetime_list

    def set_components_attributes(self):
        self.script = self.components.get('script')
        self.div = self.components.get('div')

    def get_script(self):
        return self.script

    def get_div(self):
        return self.div
