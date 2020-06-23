import json
import httpretty
from django.test import TestCase
from estacao.core.charts.temperature import Temperature
from estacao.core.resources import MeteogramTemperature

API_URI = 'http://api.estacao.iag.usp.br/v0/2020-01-01/2020-02-01/'


class TemperatureTest(TestCase):
    def setUp(self):
        self.temp = Temperature()
        self.resource = MeteogramTemperature()

    def test_instance(self):
        self.assertIsInstance(self.temp, Temperature)

    def test_has_load_data_attribute(self):
        """It should have load_data attribute"""
        self.assertTrue(hasattr(self.temp, 'load_data'))

    def test_load_data(self):
        """It should get temperature data"""
        self.set_mock(self.temp.plot)
        self.assertDictEqual(self.temp.temperature_data, self.make_data())

    def test_has_plot_attribute(self):
        """It should have plot attribute"""
        self.assertTrue(hasattr(self.temp, 'plot'))

    def test_has_extract_temperature(self):
        self.assertTrue(hasattr(self.temp, 'extract_data'))

    def test_extract_data(self):
        data = self.make_data()
        expected = dict()
        expected['date'] = [item['date'] for item in data['temp_min']]
        expected['temp_min'] = [item['temp'] for item in data['temp_min']]
        self.temp.extract_data(self.make_data())
        self.assertDictEqual(expected, self.temp.extracted_data)

    def test_generate_components(self):
        self.set_mock(self.temp.plot)
        self.temp.generate_components()
        for expected in ['script', 'div']:
            message = '{} not found'.format(expected)
            with self.subTest():
                self.assertTrue(hasattr(self.temp, expected), msg=message)

    def test_plot(self):
        self.set_mock(self.temp.plot)
        self.assertIn('text/javascript', self.temp.script)
        self.assertIn('class', self.temp.div)

    def test_get_script(self):
        self.set_mock(self.temp.plot)
        self.assertIn('text/javascript', self.temp.get_script())

    def test_get_div(self):
        self.set_mock(self.temp.plot)
        self.assertIn('class', self.temp.get_div())

    def test_generate_uri(self):
        expected = API_URI
        self.temp.generate_uri('2020-01-01', '2020-02-01')
        self.assertEqual(expected, self.temp.uri)

    @httpretty.httprettified
    def set_mock(self, function):
        uri = API_URI
        body = json.dumps(self.make_data())
        httpretty.register_uri(httpretty.GET, uri=uri, body=body)
        data = function(date_ini='2020-01-01', date_end='2020-02-01')
        return data

    def make_data(self):
        data = {
            'temp_min':  [
                {'date': '2020-01-01 00:13:00', 'temp': '12'},
                {'date': '2020-01-01 00:14:00', 'temp': '23'},
                {'date': '2020-01-01 00:15:00', 'temp': '20'},
                {'date': '2020-01-01 00:16:00', 'temp': '19'},
                {'date': '2020-01-01 00:17:00', 'temp': '18'},
            ]
        }
        return data
