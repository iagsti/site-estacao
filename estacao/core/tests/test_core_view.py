from django.test import TestCase
from django.shortcuts import resolve_url as r


class ViewCoreTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('core:home'))

    def test_current_conditions_items(self):
        items = ['Temperatura do Ar', 'UR', 'Temperatura Mínima', 'Temperatura Máxima',
                'Vento', 'Pressão', 'Visibilidade Horizontal', 'Nuvens Baixas', 'Nuvens Médias',
                'Nuvens Altas', 'Fenômenos Diverso']

        for expected in items:
            with self.subTest():
                self.assertContains(self.resp, expected)

    def test_current_conditions_context(self):
        """Context should contain conditions values"""
        conditions = self.resp.context['conditions']
        values = dict(temperatura_ar='22.7ºC', temperatura_orvalho='18.5ºC', ur='77.3%',
                        temperatura_min='17.9 °C às 14:00', temperatura_max='26.0 °C às 15:00',
                        vento='Calmo', pressao='924.8 hPa', visibilidade='4 km a 10 km',
                        nuvens_baixas='Sc/Fc - 6/10', nuvens_medias='----', nuvens_altas='----',
                        diversos='Não Disponível')
    
        self.assertDictEqual(conditions, values)

    def test_current_conditions_temperature_header(self):
        expected = '22.7ºC - 77.3%'
        self.assertContains(self.resp, expected)

    def test_current_conditions_values(self):
        """Template should render current condition values"""
        condition_values = ((2, 22.7), (1, 18.5), (2, 77.3), (1,'17.9 °C às 14:00'), (1,'26.0 °C às 15:00'),
                            (1, 'Calmo'), (1, '924.8 hPa'), (1, 'Sc/Fc - 6/10'), (2, '----'), (1, 'Não Disponível'))

        for count, expected in condition_values:
            with self.subTest():
                self.assertContains(self.resp, expected, count)

        