from django.test import TestCase
from django.utils.translation import gettext as _
from django.shortcuts import resolve_url as r
from .mock import mock_api, weather


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
        content = (
          (2, _('Estação Meteorológica')),
          (1, _('Seção Técnica de Serviços Meteorológicos')),
          (1, _('Instituto de Astronomia, Geofísica e Ciências Atmosféricas'))
        )

        for count, expected in content:
            with self.subTest():
                self.assertContains(self.resp, expected, count)

    def test_weather_data(self):
        """Template should render weather data"""
        for expected in weather.get('current').values():
            with self.subTest():
                self.assertContains(self.resp, expected)


class HomeGetMeteorologicDataTest(TestCase):
    @mock_api
    def setUp(self):
        self.resp = self.client.get(r('core:home'))

    def test_render_conditions_data(self):
        """Conditions data should be rendered"""
        expected = weather
        conditions = self.resp.context['conditions']
        self.assertDictEqual(expected, conditions)
