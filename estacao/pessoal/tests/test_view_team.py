from django.test import TestCase
from django.shortcuts import resolve_url as r
from django.utils.translation import gettext as _


class TeamViewGetTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('pessoal:pessoal_index'))

    def test_status_code(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'pessoal_index.html')

    def test_main_template(self):
        self.assertTemplateUsed(self.resp, 'main.html')

    def test_page_title(self):
        expected = _('Pessoal') + '</p'
        self.assertContains(self.resp, expected)

    def test_context(self):
        """Context should have pessoal data"""
        context = self.resp.context['team']
        expected = self.make_team()
        self.assertListEqual(expected, context)

    def test_team_name(self):
        """Tempate should render team name"""
        self.assertTeam('name')

    def assertTeam(self, attr):
        team = self.resp.context['team']
        for expected in team:
            with self.subTest():
                self.assertContains(self.resp, expected[attr])
    
    def make_team(self, **kwargs):
        pessoal_default = dict(name='Dr. Thomas Jeferson', role='Chefe da Seção Técnica de Serviços Meteorológicos',
                                image='https://i.picsum.photos/id/866/300/200.jpg')
        
        pessoal = dict(pessoal_default, **kwargs)
        return [pessoal]
