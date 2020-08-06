from django.test import TestCase
from bokeh.plotting.figure import Figure
from .mock import temperature_max, temperature_min, mock_api

from estacao.core.charts.plot import TemperaturePlot


def mock_loaded_data():
    data_max = temperature_max
    date_max = [item['data'] for item in data_max['temp_max']]
    temp_max = [item['temp'] for item in data_max['temp_max']]

    data_min = temperature_min
    date_min = [item['data'] for item in data_min['temp_min']]
    temp_min = [item['temp'] for item in data_min['temp_min']]

    return {
        'temp_max': {'date': date_max, 'temp_max': temp_max},
        'temp_min': {'date': date_min, 'temp_min': temp_min}
    }


class TemperaturePlotTest(TestCase):
    def setUp(self):
        self.obj = TemperaturePlot()

    @mock_api
    def test_load_temperature_data(self):
        expected = mock_loaded_data()
        self.obj.load_temperature_data()
        self.assertDictEqual(expected, self.obj.data)

    @mock_api
    def test_set_data_source(self):
        data = mock_loaded_data()
        expected = {
            'date_min': data.get('temp_min').get('date'),
            'temp_min': data.get('temp_min').get('temp_min'),
            'date_max': data.get('temp_max').get('date'),
            'temp_max': data.get('temp_max').get('temp_max')
        }
        self.obj.load_temperature_data()
        self.obj.set_data_source()
        self.assertDictEqual(expected, self.obj.data_source.data)

    def test_set_tools(self):
        self.obj.set_tools()
        expected = [
            ('Temperatura mínima', '@temp_min'),
            ('Temperatura máxima', '@temp_max'),
            ('Data', '@date_max{%d/%m/%Y %H:%M}'),
        ]
        self.assertListEqual(expected, self.obj.tools.tooltips)

    @mock_api
    def test_set_plot(self):
        self.obj.load_temperature_data()
        self.obj.set_tools()
        self.obj.set_plot()
        self.assertIsInstance(self.obj.plot, Figure)

    def test_get_plot(self):
        plot = self.obj.get_plot()
        self.assertIsInstance(plot, Figure)
