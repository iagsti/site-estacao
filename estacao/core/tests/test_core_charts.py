from django.test import TestCase
from estacao.core.charts.temperature import Temperature
from estacao.core.resources import MeteogramTemperature, UriManager
from estacao.core.tests.mock import mock_api, mock_uri

API_URI = mock_uri('temperature_min')


class TemperatureTest(TestCase):
    def setUp(self):
        self.temp = Temperature()
        self.resource = MeteogramTemperature()

    def test_instance(self):
        self.assertIsInstance(self.temp, Temperature)

    def test_has_load_data_attribute(self):
        """It should have load_data attribute"""
        self.assertTrue(hasattr(self.temp, 'load_data'))

    @mock_api
    def test_load_data(self):
        """It should get temperature data"""
        self.temp.plot()
        self.assertDictEqual(self.temp.temperature_data, self.make_data())

    def test_exception_on_load_data(self):
        expected = {'tem_min': [{'data': '2020-06-25 13:00:00', 'temp': '0'}]}
        self.temp.plot()
        self.assertDictEqual(expected, self.temp.temperature_data)

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

    def test_extract_data_with_empty_data(self):
        expected = self.make_default_data()
        self.temp.extract_data({})
        self.assertDictEqual(expected, self.temp.extracted_data)

    @mock_api
    def test_generate_components(self):
        self.temp.plot()
        self.temp.generate_components()
        for expected in ['script', 'div']:
            message = '{} not found'.format(expected)
            with self.subTest():
                self.assertTrue(hasattr(self.temp, expected), msg=message)

    @mock_api
    def test_plot(self):
        self.temp.plot()
        self.assertIn('text/javascript', self.temp.script)
        self.assertIn('class', self.temp.div)

    @mock_api
    def test_get_script(self):
        self.temp.plot()
        self.assertIn('text/javascript', self.temp.get_script())

    @mock_api
    def test_get_div(self):
        self.temp.plot()
        self.assertIn('class', self.temp.get_div())

    def test_make_uri(self):
        expected = API_URI
        self.temp.make_uri()
        self.assertEqual(expected, self.temp.uri)

    def test_instance_of_uri_manager(self):
        self.assertIsInstance(self.temp, UriManager)

    def make_data(self):
        data = {
            'temp_min':  [
                {'date': '2020-01-01 00:13:00', 'temp': '12'},
                {'date': '2020-01-01 00:14:00', 'temp': '23'},
                {'date': '2020-01-01 00:15:00', 'temp': '20'},
                {'date': '2020-01-02 00:16:00', 'temp': '19'},
                {'date': '2020-01-02 00:17:00', 'temp': '18'},
                {'date': '2020-01-02 00:17:00', 'temp': '12'},
            ]
        }
        return data

    def make_default_data(self):
        return {'date': ['2020-06-25 13:00:00'], 'temp_min': ['0']}