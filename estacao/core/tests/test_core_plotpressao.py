from django.test import TestCase
from bokeh.plotting import Figure
from bokeh.models import HoverTool
from math import pi

from .mock import mock_api, consolidado
from estacao.core.charts.pressao_plot import PressaoPlot


class PressaoPlotTest(TestCase):
    def setUp(self):
        self.obj = PressaoPlot()

    @mock_api
    def test_load_data(self):
        expected = self.mock_data()
        self.obj.load_data()
        self.assertEqual(expected, self.obj.data)

    @mock_api
    def test_set_data_source(self):
        data = self.mock_data()
        pressao = {'date': data.get('date'),
                   'pressao': data.get('pressao')}
        pressao_hpa = {'date': data.get('date'),
                       'pressao_hpa': data.get('pressao_hpa')}

        self.obj.load_data()
        self.obj.set_data_source()
        self.assertDictEqual(pressao, self.obj.datasource.get('pressao').data)
        self.assertDictEqual(pressao_hpa,
                             self.obj.datasource.get('pressao_hpa').data)

    def test_set_plot_instance(self):
        self.obj.load_data()
        self.obj.set_data_source()
        self.obj.set_plot()

        self.assertIsInstance(self.obj.plot, Figure)

    def test_has_plot_attribute(self):
        self.assertTrue(hasattr(self.obj, 'plot'))

    @mock_api
    def test_plot_parameters(self):
        data = self.mock_data()
        self.obj.plot()
        plot = self.obj.plot
        self.assertEqual(plot.title.text, 'Pressão')
        self.assertEqual(plot.plot_height, 400)
        self.assertEqual(plot.x_range.factors, data.get('date'))

    @mock_api
    def test_plot_labels(self):
        self.obj.plot()
        plot = self.obj.plot

        self.assertEqual(plot.xaxis.axis_label, 'Data')
        self.assertEqual(plot.yaxis.axis_label, 'Pressão Atmosférica(mmHg)')
        self.assertEqual(plot.xaxis.major_label_orientation, pi/3.8)

    def test_has_set_tools(self):
        self.assertTrue(hasattr(self.obj, 'set_tools'))

    @mock_api
    def test_has_hovertool(self):
        self.obj.plot()
        obj = self.obj.plot.select(type=HoverTool)
        self.assertIsInstance(obj[0], HoverTool)

    @mock_api
    def test_set_tools(self):
        self.obj.plot()
        expected_pressao = [
            ('Pressão', '@pressao'),
            ('Data', '@date{%d/%m/%Y %H:%M}')
        ]

        expected_pressao_hpa = [
            ('Pressão hpa', '@pressao_hpa'),
            ('Data', '@date{%d/%m/%Y %H:%M}')
        ]

        hovertools = self.obj.plot.select(type=HoverTool)
        tools = [hover.tooltips for hover in hovertools]

        self.assertIn(expected_pressao, tools)
        self.assertIn(expected_pressao_hpa, tools)

    def mock_data(self):
        data = consolidado
        date = [row.get('data') for row in data.get('consolidado')]
        pressao = [row.get('pressao') for row in data.get('consolidado')]
        pressao_hpa = [
            row.get('pressao_hpa') for row in data.get('consolidado')
        ]

        return {'date': date, 'pressao': pressao, 'pressao_hpa': pressao_hpa}
