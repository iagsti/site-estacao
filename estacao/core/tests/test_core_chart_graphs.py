from django.test import TestCase
from bokeh.plotting.figure import Figure
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource

from estacao.core.charts.graphs import LineGraph, BarGraph


class LineGraphTest(TestCase):
    def setUp(self):
        source = ColumnDataSource({'x': [], 'y': []})
        line_settings = dict(x='x', y='y', line_color='red', name='tmin',
                             legend='Temp min', plot=figure(), source=source)
        self.obj = LineGraph(**line_settings)

    def test_has_set_line_attribute(self):
        """It should have a set_line attribute"""
        self.assertTrue(hasattr(self.obj, 'set_line'))

    def test_contructor_attributes(self):
        attrs = ('x', 'y', 'line_color', 'legend', 'plot', 'source')
        for item in attrs:
            message = '{} not found'.format(item)
            with self.subTest():
                self.assertTrue(hasattr(self.obj, item), msg=message)

    def test_get_line(self):
        self.obj.set_line()
        resp = self.obj.get_line()
        self.assertIsInstance(resp, Figure)

    def test_glyph_name(self):
        plot = self.obj.get_line()
        glyph = plot.select(name='tmin')
        self.assertEqual('tmin', glyph.name)


class BarGraphTest(TestCase):
    def setUp(self):
        source = ColumnDataSource({'x': [], 'top': []})
        bar_settings = dict(x='x', top='y', color='red', width=10,
                            gutter=-0.15, label='Temp min',
                            plot=figure(), source=source)
        self.obj = BarGraph(**bar_settings)

    def test_constructor_attributes(self):
        attributes = ('x', 'top', 'width', 'color',
                      'label', 'source', 'plot', 'gutter')
        for expected in attributes:
            message = '{} not found'.format(expected)
            with self.subTest():
                self.assertTrue(hasattr(self.obj, expected), msg=message)

    def test_get_bar(self):
        self.obj.set_bar()
        resp = self.obj.get_bar()
        self.assertIsInstance(resp, Figure)
