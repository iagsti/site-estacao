from django.test import TestCase
from django.conf import settings
from .mock import mock_uri, temperature_max, mock_api

from estacao.core.charts.chart import Chart
from estacao.core.charts.data import DataTemperature


API_URL = getattr(settings, 'API_URL')


class DataTemperatureTest(TestCase):
    def setUp(self):
        self.obj = DataTemperature(resource='temperatura-max',
                                   data_index='temp_max')

    def test_has_resource_attribute(self):
        self.assertTrue(hasattr(self.obj, 'resource'))

    def test_has_data_index_attribute(self):
        self.assertTrue(hasattr(self.obj, 'data_index'))

    def test_is_instance_from_chart(self):
        """It should be an instance from Chart"""
        self.assertIsInstance(self.obj, Chart)

    def test_make_uri(self):
        """It should return the endpoint uri"""
        expected = mock_uri(resource='temperatura-max')
        self.obj.make_uri()
        self.assertEqual(expected, self.obj.uri)

    def test_extract_data(self):
        data = temperature_max
        expected = dict()
        expected['date'] = [item['data'] for item in data['temp_max']]
        expected['temp_max'] = [item['temp'] for item in data['temp_max']]
        self.obj.extract_data(temperature_max)
        self.assertEqual(expected, self.obj.extracted_data)

    @mock_api
    def test_handle_data(self):
        data = temperature_max
        date = [item['data'] for item in data['temp_max']]
        temp = [item['temp'] for item in data['temp_max']]
        expected = dict(date=date, temp_max=temp)
        self.obj.handle_data()
        self.assertDictEqual(expected, self.obj.extracted_data)

    def test_has_generate_graph_attribute(self):
        """It should have generate_graph attribute"""
        self.assertTrue(self.obj, 'generate_graph')
