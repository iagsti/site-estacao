from django.test import TestCase
from bokeh.plotting import Figure

from estacao.core.charts.pressao import Pressao
from estacao.core.charts.pressao_plot import PressaoPlot


class PressaoTest(TestCase):
    def setUp(self):
        self.obj = Pressao()

    def test_has_pressao_plot_attribute(self):
        self.assertTrue(hasattr(self.obj, 'pressao_plot'))

    def test_pressao_plot_instance(self):
        self.assertIsInstance(self.obj.pressao_plot, PressaoPlot)

    def test_has_plot_attribute(self):
        self.assertTrue(hasattr(self.obj, 'plot'))

    def test_plot_instance(self):
        self.assertIsInstance(self.obj.plot, Figure)

    def test_plot_has_pressao_glyph(self):
        self.obj.make_plots()
        pressao_glyph = self.obj.plot.select(name='pressao')[0]
        self.assertEqual(pressao_glyph.name, 'pressao')

    def test_plot_has_pressao_hpa_glyph(self):
        self.obj.make_plots()
        pressao_hpa_glyph = self.obj.plot.select(name='pressao_hpa')[0]
        self.assertEqual(pressao_hpa_glyph.name, 'pressao_hpa')
