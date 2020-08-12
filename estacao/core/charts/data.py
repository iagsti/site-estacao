from .chart import Chart


class DataTemperature(Chart):
    def __init__(self, resource=None, data_index=None, date_ini=None,
                 date_end=None):
        super().__init__(date_ini=date_ini, date_end=date_end)
        self.resource = resource
        self.data_index = data_index

    def make_uri(self):
        self.uri = self.generate_uri(resource=self.resource)

    def extract_data(self, data):
        try:
            date = [item['data'] for item in data[self.data_index]]
            temp = [item['temp'] for item in data[self.data_index]]
            extracted = {'date': date, self.data_index: temp}
        except KeyError:
            date = ['2020-06-25 13:00:00']
            temp = [0]
            extracted = {'date': date, self.data_index: temp}
        self.extracted_data = extracted


class DataConsolidado(DataTemperature):
    def extract_data(self, data):
        try:
            key = self.data_index
            extracted = [row.get(key) for row in data.get('consolidado')]
        except Exception:
            data = {'consolidado': [{'tseco': 0, 'data': '2020-01-01 00:00:00'}]}
            extracted = [row.get(key) for row in data.get('consolidado')]
        self.extracted_data = extracted
