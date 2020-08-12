from django.test import TestCase
from bokeh.plotting import Figure

from estacao.core.charts.hovertool import ChartHoverTool


class ChartHoverToolTest(TestCase):
    def setUp(self):
        tooltips = {'tmin': [], 'tmax': [], 'tseco': []}
        formatters = {'tmin': {}, 'tmax': {}, 'tseco': {}}
        self.plot = Figure()
        self.obj = ChartHoverTool(plot=self.plot, tooltips=tooltips,
                                  formatters=formatters)

    def test_has_plot_attribute(self):
        self.assertTrue(hasattr(self.obj, 'plot'))

    def test_plot_attribute_instance(self):
        self.assertIsInstance(self.obj.plot, Figure)

    def test_has_tooltips_attribute(self):
        self.assertTrue(hasattr(self.obj, 'tooltips'))

    def test_get_names(self):
        expected = ('tmin', 'tmax', 'tseco')
        self.obj.get_names()
        self.assertTupleEqual(expected, self.obj.names)

    def test_set_hovertools(self):
        expected = ('tmin', 'tmax', 'tseco')
        self.obj.get_names()
        self.obj.set_hovertools()
        for hover in self.plot.hover:
            with self.subTest():
                self.assertIn(hover.names[0], expected)

    def test_add_hovertools(self):
        expected = ['tmin', 'tmax', 'tseco']
        self.obj.add_hovertools()
        hovertools_names = [hover.names[0] for hover in self.plot.hover]
        self.assertListEqual(expected, hovertools_names)
