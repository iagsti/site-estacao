from django.test import TestCase
from bokeh.plotting import Figure

from .mock import mock_api
from estacao.core.charts.temperature import Temperature


class TemperatureCoreTest(TestCase):
    def setUp(self):
        self.obj = Temperature()

    def test_has_make_plots_attributes(self):
        """It should have a make_plots attribute"""
        self.assertTrue(hasattr(self.obj, 'make_plots'))

    def test_make_plots(self):
        """It should make temp_min and temp_max plots"""
        self.obj.make_plots()
        self.assertIsInstance(self.obj.temp_plot, Figure)

    @mock_api
    def test_make_components(self):
        """It should make a components dict"""
        self.obj.make_plots()
        self.obj.make_components()
        components = ('script', 'div')
        for expected in components:
            with self.subTest():
                self.assertIn(expected, self.obj.components.keys())

    @mock_api
    def test_plot(self):
        self.obj.plot()
        components = ('script', 'div')
        for expected in components:
            with self.subTest():
                self.assertIn(expected, self.obj.components.keys())

    @mock_api
    def test_get_scripts(self):
        """It should return the component scrips"""
        self.obj.plot()
        self.assertIn('BokehJS', self.obj.get_scripts())

    def test_get_div(self):
        """It should return the component div"""
        self.obj.plot()
        self.assertIn('<div class="bk-root"', self.obj.get_div())

    def test_make_line_graph(self):
        self.obj.make_line(x='date_min', y='temp_min',
                           line_color='blue', legend='Tem min')
        self.assertIsInstance(self.obj.temp_plot, Figure)

    def test_make_vbar_graph(self):
        self.obj.make_vbar(x='date_min', top='temp_max',
                           color='red', label='Tem max', gutter=-0.15)
        self.assertIsInstance(self.obj.temp_plot, Figure)
