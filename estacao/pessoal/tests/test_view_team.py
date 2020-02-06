from django.test import TestCase
from django.shortcuts import resolve_url as r
from django.utils.translation import gettext as _
from estacao.pessoal.models import TeamModel


class TeamViewGetTest(TestCase):
    def setUp(self):
        data = self.make_team()
        TeamModel.objects.create(**data[0])
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
        team = self.TeamDict(context)
        expected = self.make_team()
        self.assertListEqual(expected, team)

    def test_team_name(self):
        """Tempate should render team name"""
        self.assertTeam('name')

    def assertTeam(self, attr):
        context = self.resp.context['team']
        team = self.TeamDict(context)
        for expected in team:
            with self.subTest():
                self.assertContains(self.resp, expected[attr])

    def test_pessoal_link(self):
        expected = 'href="%s"' % r('pessoal:pessoal_index')
        self.assertContains(self.resp, expected)

    def test_home_link(self):
        expected = 'href="%s"' % r('core:home')
        self.assertContains(self.resp, expected)
    
    def TeamDict(self, qs):
        team = [{'name': e.name, 'role': e.role, 'image': e.image} for e in qs]
        return team


    def make_team(self, **kwargs):
        pessoal_default = dict(name='Dr. Thomas Jeferson', role='Chefe da Seção Técnica de Serviços Meteorológicos',
                                image='https://i.picsum.photos/id/866/300/200.jpg')
        
        pessoal = dict(pessoal_default, **kwargs)
        return [pessoal]
