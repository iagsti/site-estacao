from django.test import TestCase
from estacao.core.models import Dados


class DadosModelsCoreTest(TestCase):

    databases = ['dados']

    def setUp(self):
        data = self.make_data()
        self.obj = Dados(**data)

    def test_dados_instance(self):
        self.assertIsInstance(self.obj, Dados)

    def test_dados_attr(self):
        attrs = ['data', 'vis', 'tipob', 'qtdb', 'tipom', 'qtdm',
                    'tipoa', 'qtda', 'dir', 'vento', 'temp_bar',
                    'pressao', 'tseco', 'tumido', 'tsfc', 't5cm',
                    't10cm', 't20cm', 't30cm', 't40cm', 'piche', 
                    'evap_piche', 'piche_ar', 'evap_piche_ar', 'tmax',
                    'tmin']
        
        for expected in attrs:
            with self.subTest():
                self.assertTrue(hasattr(Dados, expected))

    def test_create_dados(self):
        self.obj.save()
        self.assertEqual(Dados.objects.count(), 1)

    def test_table_name(self):
        table = Dados._meta.db_table
        self.assertEqual(table, 'dados')

    def test_not_managed(self):
        """Dados should not be managed"""
        self.assertFalse(Dados._meta.managed)

    def make_data(self, **kwargs):
        default_data = {"data" : "1995-02-10 17:00:00", "vis" : 7, "tipob" : "Sc/Cu",
		                "qtdb" : 5, "tipom" : "Ac", "qtdm" : 3, "tipoa" : 'Ac',
		                "qtda" : 0, "dir" : "WNW", "vento" : 3, "temp_bar" : 24,
		                "pressao" : 695.5, "tseco" : 25.4, "tumido" : 21, "tsfc" : 28.5,
		                "t5cm" : 27, "t10cm" : 26.5, "t20cm" : 25, "t30cm" : 23.3,
		                "t40cm" : 23.2, "piche" : 4, "evap_piche" : 4, "piche_ar" : 4.5,
		                "evap_piche_ar" : 4.5, "tmax" : 0, "tmin" : 0}

        data = dict(default_data, **kwargs)
        return data