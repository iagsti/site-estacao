from django.test import TestCase
from bokeh.plotting.figure import Figure
from .mock import temperature_max, temperature_min, mock_api, consolidado

from estacao.core.charts.plot import TemperaturePlot


def mock_loaded_data():
    data_max = temperature_max
    date_max = [item['data'] for item in data_max['temp_max']]
    temp_max = [item['temp'] for item in data_max['temp_max']]

    data_min = temperature_min
    date_min = [item['data'] for item in data_min['temp_min']]
    temp_min = [item['temp'] for item in data_min['temp_min']]

    date_tseco = [row.get('data') for row in consolidado.get('consolidado')]
    tseco = [row.get('tseco') for row in consolidado.get('consolidado')]

    return {
        'temp_max': {'date': date_max, 'temp_max': temp_max},
        'temp_min': {'date': date_min, 'temp_min': temp_min},
        'tseco': {'date': date_tseco, 'tseco': tseco}
    }


class TemperaturePlotTest(TestCase):
    def setUp(self):
        self.obj = TemperaturePlot()

    @mock_api
    def test_load_temperature_data(self):
        data = mock_loaded_data()
        expected = {
            'temp_max': data.get('temp_max'),
            'temp_min': data.get('temp_min')
        }
        self.obj.load_temperature_data()
        self.assertDictEqual(expected, self.obj.data)

    @mock_api
    def test_set_data_source(self):
        data = mock_loaded_data()
        temp_min = {
            'date_min': data.get('temp_min').get('date'),
            'temp_min': data.get('temp_min').get('temp_min')
        }
        temp_max = {
            'date_max': data.get('temp_max').get('date'),
            'temp_max': data.get('temp_max').get('temp_max'),
        }
        tseco = {
            'date_tseco': data.get('tseco').get('date'),
            'tseco': data.get('tseco').get('tseco')
        }
        self.obj.load_temperature_data()
        self.obj.load_tseco_data()
        self.obj.set_data_source()
        sources = self.obj.data_sources
        self.assertDictEqual(temp_min, sources.get('temp_min').data)
        self.assertDictEqual(temp_max, sources.get('temp_max').data)
        self.assertDictEqual(tseco, sources.get('tseco').data)

    def test_set_tools(self):
        expected = ['tmin', 'tmax', 'tseco']
        self.obj.load_temperature_data()
        self.obj.load_tseco_data()
        self.obj.set_plot()
        self.obj.set_tools()
        response = [hover.names[0] for hover in self.obj.plot.hover]
        self.assertListEqual(expected, response)

    @mock_api
    def test_set_plot(self):
        self.obj.load_temperature_data()
        self.obj.load_tseco_data()
        self.obj.set_plot()
        self.obj.set_tools()
        self.assertIsInstance(self.obj.plot, Figure)

    @mock_api
    def test_get_plot(self):
        plot = self.obj.get_plot()
        self.assertIsInstance(plot, Figure)

    @mock_api
    def test_get_tseco_data(self):
        data = mock_loaded_data()
        expected = data.get('tseco')
        self.obj.load_tseco_data()
        self.assertDictEqual(expected, self.obj.tseco_data)
