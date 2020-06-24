import json
from django.test import TestCase
from django.utils.translation import gettext as _
from django.shortcuts import resolve_url as r
from .mock import mock_api


class HomeGetTest(TestCase):
    @mock_api
    def setUp(self):
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
        content = ((1, '<nav'), (1, '<header'))

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


class HomeGetMeteorologicDataTest(TestCase):
    @mock_api
    def setUp(self):
        self.resp = self.client.get(r('core:home'))

    def test_render_conditions_data(self):
        """Conditions data should be rendered"""
        conditions_data = ((3, '>20'), (2, '>10'), (1, '>80'), (1, 'calmo'),
                           (1, '>129'), (1, '>4'), (1, 'Ac/As-10/10'),
                           (2, 'Am/As-20/20'), (1, '10/04/2020 - 13:20'))

        for count, expected in conditions_data:
            with self.subTest():
                self.assertContains(self.resp, expected, count)

    def make_request_body(self):
        data = {
                "data": "10/04/2020 - 13:20",
                "temperatura_ar": "20",
                "temperatura_orvalho": "10",
                "ur": "80",
                "temperatura_min": "10",
                "temperatura_max": "20",
                "vento": "calmo",
                "pressao": "129",
                "visibilidade_min": "4",
                "visibilidade_max": "10",
                "nuvens_baixas": "Ac/As-10/10",
                "nuvens_medias": "Am/As-20/20",
                "nuvens_altas": "Am/As-20/20"
            }
        return json.dumps(data)
