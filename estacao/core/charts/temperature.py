

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
class Temperature():



