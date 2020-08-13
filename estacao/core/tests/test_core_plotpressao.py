from django.test import TestCase

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

    def mock_data(self):
        data = consolidado
        date = [row.get('data') for row in data.get('consolidado')]
        pressao = [row.get('pressao') for row in data.get('consolidado')]
        pressao_hpa = [
            row.get('pressao_hpa') for row in data.get('consolidado')
        ]

        return {'date': date, 'pressao': pressao, 'pressao_hpa': pressao_hpa}
