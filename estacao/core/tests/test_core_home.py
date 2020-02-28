from django.test import TestCase
from django.utils.translation import gettext as _
from django.shortcuts import resolve_url as r
from estacao.core.models import Dados


class HomeGetTest(TestCase):

    databases = ['dados']

    def setUp(self):
        data = self.make_data()
        Dados.objects.create(**data)
        self.resp = self.client.get(r('core:home'))

    def test_status_code(self):
        """Status code should be 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """It must render home.html template"""
        self.assertTemplateUsed(self.resp, 'home.html')

    def test_main_template(self):
        """It must render main.html template"""
        self.assertTemplateUsed(self.resp, 'main.html')

    def test_html_title(self):
        """Html title must be Estação Meteorológica"""
        self.assertContains(self.resp, _('Estação Meteorológica'))

    def test_html_tags(self):
        """It must contain a set of html tags"""
        content = ((1, '<nav'),(1, '<header'))

        for count, expected in content:
            with self.subTest():
                self.assertContains(self.resp, expected, count)

    def test_menu_content(self):
        """Template should render a list of menu itens"""
        menu_itens = ['Home', _('Contato e Localização'), _('Pessoal')]
        
        for item in menu_itens:
            with self.subTest():
                self.assertContains(self.resp, item)

    def test_page_title(self):
        """Template should render page title"""
        content = ((2, _('Estação Meteorológica')), (1, _('Seção Técnica de Serviços Meteorológicos')),
                    (1, _('Instituto de Astronomia, Geofísica e Ciências Atmosféricas')))

        for count, expected in content:
            with self.subTest():
                self.assertContains(self.resp, expected, count)

    def test_content(self):
        """Template should render content"""
        content = [_('Condições Atuais'), _('Meteograma'), _('Boletins e Relatórios'),
                    _('Museu de Meteorologia'), _('Instrumentos'), _('Solicitação de Dados'),
                    _('Explorando a Meteorologia'), _('Cursos')]

        for expected in content:
            with self.subTest():
                self.assertContains(self.resp, expected)

    def make_data(self, **kwargs):
        default_data = {"data" : "1995-02-10 17:00:00", "vis" : 7, "tipob" : "Sc/Cu",
		                "qtdb" : 5, "tipom" : "Ac", "qtdm" : 3, "tipoa" : 'Ac',
		                "qtda" : 0, "dir" : "WNW", "vento" : 3, "temp_bar" : 24,
		                "pressao" : 695.5, "tseco" : 25.4, "tumido" : 21, "tsfc" : 28.5,
		                "t5cm" : 27, "t10cm" : 26.5, "t20cm" : 25, "t30cm" : 23.3,
		                "t40cm" : 23.2, "piche" : 4, "evap_piche" : 4, "piche_ar" : 4.5,
		                "evap_piche_ar" : 4.5, "tmax" : 18, "tmin" : 0}

        data = dict(default_data, **kwargs)
        return data
    