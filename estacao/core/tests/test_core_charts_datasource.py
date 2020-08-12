from django.test import TestCase
from bokeh.models import ColumnDataSource

from estacao.core.charts.data import DataTemperature
from estacao.core.charts.datasource import DataSource
from .mock import mock_api


class DataSourceTest(TestCase):
    @mock_api
    def setUp(self):
        self.data_temperature = DataTemperature('temperatura-min', 'tem_min')
        self.obj = DataSource(self.data_temperature, 'date', 'temp_min')

    def test_has_initialization_attributes(self):
        attrs = ('data', 'date_key', 'data_key')
        for expected in attrs:
            with self.subTest():
                self.assertTrue(hasattr(self.obj, expected))

    def test_has_make_datasource_attribute(self):
        self.assertTrue(hasattr(self.obj, 'make_datasource'))

    def test_has_datasource_attribute(self):
        self.obj.make_datasource()
        self.assertTrue(hasattr(self.obj, 'datasource'))

    def test_datasource_instance(self):
        self.obj.make_datasource()
        self.assertIsInstance(self.obj.datasource, ColumnDataSource)

    @mock_api
    def test_datasource_response(self):
        self.data_temperature.handle_data()
        expected = self.data_temperature.extracted_data
        self.obj.make_datasource()
        self.assertDictEqual(expected, self.obj.datasource.data)
