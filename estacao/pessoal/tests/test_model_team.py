from django.test import TestCase
from estacao.pessoal.models import TeamModel


class TeamModelTest(TestCase):
    def setUp(self):
        self.obj = TeamModel.objects.create(name='Dr. Thomas Jeferson', role='Chefe da Seção Técnica de Serviços Meteorológicos',
                                image='https://i.picsum.photos/id/866/300/200.jpg')

    def test_team_model_attributes(self):
        attributes = ['name', 'role', 'image']
        fields = [str(item.name) for item in TeamModel._meta.fields]

        for expected in attributes:
            with self.subTest():
                self.assertIn(expected, fields)

    def test_create(self):
      self.assertTrue(TeamModel.objects.exists())