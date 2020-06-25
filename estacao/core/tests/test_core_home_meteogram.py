from django.test import TestCase
from django.shortcuts import resolve_url as r
from importlib.metadata import version
from .mock import mock_api


class HomeMeteogramTest(TestCase):
    @mock_api
    def setUp(self):
        self.resp = self.client.get(r('core:home'))

    def test_home_has_bockeh_scripts(self):
        self.assertContains(self.resp, 'BokehJS')

    def test_home_has_bokeh_div(self):
        self.assertContains(self.resp, '<div class="bk-root"')

    def test_has_bokeh_library(self):
        bokeh_version = version('bokeh')
        libraries = [
            'src="https://cdn.bokeh.org/bokeh/release/bokeh-{}.min.js'.format(bokeh_version),
            'src="https://cdn.bokeh.org/bokeh/release/bokeh-widgets-{}.min.js'.format(bokeh_version),
            'src="https://cdn.bokeh.org/bokeh/release/bokeh-tables-{}.min.js'.format(bokeh_version)
        ]
        for expected in libraries:
            with self.subTest():
                self.assertContains(self.resp, expected)
