from django.test import TestCase

from .mock import mock_api, consolidado
from estacao.core.charts.pressao_plot import PressaoPlot


class PressaoPlotTest(TestCase):
    def setUp(self):
        self.obj = PressaoPlot()

    @mock_api
    def test_load_data(self):
        data = consolidado
        date = [row.get('data') for row in data.get('consolidado')]
        pressao = [row.get('pressao') for row in data.get('consolidado')]
        pressao_hpa = [row.get('pressao_hpa') for row in data.get('consolidado')]

        expected = {'date': date, 'pressao': pressao,
                    'pressao_hpa': pressao_hpa}

        self.obj.load_data()
        self.assertEqual(expected, self.obj.data)
