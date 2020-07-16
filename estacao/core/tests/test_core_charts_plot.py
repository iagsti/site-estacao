from django.test import TestCase
from estacao.core.charts.plot import PlotTemperature
from .mock import temperature_max, temperature_min, mock_api, to_datetime


class PlotTemperatureTest(TestCase):
    def setUp(self):
        self.obj = PlotTemperature()

    def test_has_load_temperature(self):
        self.assertTrue(hasattr(self.obj, 'load_temperature'))

    @mock_api
    def test_load_temperature_data(self):
        """It should set data attribute"""
        data_max = temperature_max
        date_max = [item['data'] for item in data_max['temp_max']]
        date_max = to_datetime(date_max)
        temp_max = [item['temp'] for item in data_max['temp_max']]

        data_min = temperature_min
        date_min = [item['data'] for item in data_min['temp_min']]
        date_min = to_datetime(date_min)
        temp_min = [item['temp'] for item in data_min['temp_min']]

        expected = {
            'temp_max': {'date': date_max, 'temp_max': temp_max},
            'temp_min': {'date': date_min, 'temp_min': temp_min}
        }
        self.maxDiff = None
        self.obj.load_temperature('temperatura-max', 'temp_max')
        self.obj.load_temperature('temperatura-min', 'temp_min')
        self.assertDictEqual(expected, self.obj.data)

    @mock_api
    def test_make_data_source(self):
        data_max = temperature_max
        date = [item['data'] for item in data_max['temp_max']]
        date = to_datetime(date)
        temp = [item['temp'] for item in data_max['temp_max']]
        expected = {'date': date, 'temp': temp}
        self.obj.load_temperature('temperatura-max', 'temp_max')
        self.obj.make_data_source('temp_max')
        self.assertEqual(expected, self.obj.data_source.data)
