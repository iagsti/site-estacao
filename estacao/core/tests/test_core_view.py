from django.test import TestCase
from django.shortcuts import resolve_url as r
from estacao.core.models import Dados
from datetime import datetime


class ViewCoreTest(TestCase):

    databases = ['dados']

    def setUp(self):
        data = self.make_data()
        Dados.objects.create(**data)
        self.resp = self.client.get(r('core:home'))

    def test_current_conditions_items(self):
        items = ['Temperatura do Ar', 'UR', 'Temperatura Mínima', 'Temperatura Máxima',
                'Vento', 'Pressão', 'Visibilidade Horizontal', 'Nuvens Baixas', 'Nuvens Médias',
                'Nuvens Altas', 'Fenômenos Diverso']

        for expected in items:
            with self.subTest():
                self.assertContains(self.resp, expected)

    def test_current_conditions_temperature_header(self):
        expected = '%sºC - %s%%' % ('25,4', '70,39')
        self.assertContains(self.resp, expected)

    def test_current_conditions_values(self):
        """Template should render current condition values"""
        condition_values = ((2, '25,4'), (1, '19,56'), (2, '70,39'), (1,'18,2ºC'), (1,'20,2'),
                            (1, 'Calmo'), (1, '922'), (1, '10 km a 20 km'), (1, 'Sc/Cu - 5/10'), 
                            (1, 'Ac - 3/10'), (1, 'St - 1/10'), (1, 'Não disponível'))

        for count, expected in condition_values:
            with self.subTest():
                self.assertContains(self.resp, expected, count)

    def make_data(self, **kwargs):
        default_data = {"data" : "1995-02-10 17:00:00", "vis" : 7, "tipob" : "Sc/Cu", "qtdb" : 5,
		        "tipom" : "Ac", "qtdm" : 3, "tipoa" : 'St', "qtda" : 1, "dir" : "C", "vento" : 3,
		        "temp_bar" : 24, "pressao" : 695.5, "tseco" : 25.4, "tumido" : 21, "tsfc" : 28.5,
		        "t5cm" : 27, "t10cm" : 26.5, "t20cm" : 25, "t30cm" : 23.3, "t40cm" : 23.2, "piche" : 4,
		        "evap_piche" : 4, "piche_ar" : 4.5, "evap_piche_ar" : 4.5, "tmax" : 20.2, "tmin" : 18.2
	    }

        data = dict(default_data, **kwargs)
        return data

        