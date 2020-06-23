import requests
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

    def load_data(self):
        response = requests.get(self.uri)
        self.temperature_data = response.json()

    def extract_data(self, data):
        extracted = dict()
        extracted['date'] = [item['date'] for item in data['temp_min']]
        extracted['temp_min'] = [item['temp'] for item in data['temp_min']]
        self.extracted_data = extracted

    def generate_components(self):
        temp_figure = figure()
        date = self.extracted_data['date']
        temperature = self.extracted_data['temp_min']
        temp_figure.line(date, temperature)
        script, div = components(temp_figure)
        self.components = {'script': script, 'div': div}

    def set_components_attributes(self):
        self.script = self.components.get('script')
        self.div = self.components.get('div')

    def generate_uri(self, date_ini, date_end):
        uri = '{}/{}/{}/'.format(API_URL, date_ini, date_end)
        self.uri = uri

    def get_script(self):
        return self.script

    def get_div(self):
        return self.div
