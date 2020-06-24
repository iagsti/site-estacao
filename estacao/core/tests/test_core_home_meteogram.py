from django.test import TestCase
from django.shortcuts import resolve_url as r
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
        libraries = [
            'src="https://cdn.bokeh.org/bokeh/release/bokeh-2.1.0.min.js',
            'src="https://cdn.bokeh.org/bokeh/release/bokeh-widgets-2.1.0.min.js',
            'src="https://cdn.bokeh.org/bokeh/release/bokeh-tables-2.1.0.min.js'
        ]
        for expected in libraries:
            with self.subTest():
                self.assertContains(self.resp, expected)
