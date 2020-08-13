from django.test import TestCase
from django.shortcuts import resolve_url as r
from estacao.core.tests.mock import mock_api


class ViewCoreTest(TestCase):
    @mock_api
    def setUp(self):
        self.resp = self.client.get(r('core:home'))

    def test_current_conditions_items(self):
        items = ['Temperatura do Ar', 'UR', 'Temperatura Mínima',
                 'Temperatura Máxima', 'Vento', 'Pressão',
                 'Visibilidade Horizontal', 'Nuvens Baixas', 'Nuvens Médias',
                 'Nuvens Altas', 'Fenômenos Diverso']

        for expected in items:
            with self.subTest():
                self.assertContains(self.resp, expected)

    def test_context_has_weather_data(self):
        """Context should have conditions data"""
        self.assertIn('conditions', self.resp.context)

    def test_context_has_pressao_data(self):
        self.assertIn('pressao', self.resp.context)
