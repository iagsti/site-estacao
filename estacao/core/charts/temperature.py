from estacao.core.charts.chart import TempChart


class Temperature(TempChart):
    def make_uri(self):
        self.uri = self.generate_uri(resource='temperatura-min')

    def extract_data(self, data):
        try:
            extracted = dict()
            extracted['date'] = [item['data'] for item in data['temp_min']]
            extracted['temp_min'] = [item['temp'] for item in data['temp_min']]
        except KeyError:
            extracted = {'date': ['2020-06-25 13:00:00'], 'temp_min': ['0']}
        self.extracted_data = extracted


class TemperatureMax(TempChart):
    def make_uri(self):
        self.uri = self.generate_uri(resource='temperatura-max')

    def extract_data(self, data):
        try:
            extracted = dict()
            extracted['date'] = [item['data'] for item in data['temp_max']]
            extracted['temp_max'] = [item['temp'] for item in data['temp_max']]
        except KeyError:
            extracted = {'date': ['2020-06-25 13:00:00'], 'temp_max': ['0']}
        self.extracted_data = extracted
