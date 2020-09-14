from django.test import TestCase
from django.shortcuts import resolve_url as r

from ..models import Boletin


class BoletinsGetTest(TestCase):
    def setUp(self):
        Boletin.objects.create(title='Boletim climatológico',
                               category='climatologico', file='boletim.pdf')
        Boletin.objects.create(title='Boletim trimestral',
                               category='trimestral', file='boletim.pdf')
        Boletin.objects.create(title='Boletim mensal',
                               category='mensal', file='boletim.pdf')
        Boletin.objects.create(title='Boletim técnico',
                               category='tecnico', file='boletim.pdf')

        self.resp = self.client.get(r('boletins:index'))

    def test_status_code(self):
        self.assertTrue(200, self.resp.status_code)

    def test_template_rendering(self):
        self.assertTemplateUsed(self.resp, 'boletins.html')
        self.assertTemplateUsed(self.resp, 'main.html')

    def test_context_has_climatologico(self):
        self.assertContextHasMember('climatologico')

    def test_context_has_trimestral(self):
        self.assertContextHasMember('trimestral')

    def test_context_has_mensal(self):
        self.assertContextHasMember('mensal')

    def test_context_has_tecnico(self):
        self.assertContextHasMember('tecnico')

    def test_template_contains_boletin_data(self):
        content = ('Boletim climatológico', 'Boletim trimestral',
                   'Boletim mensal', 'Boletim técnico')

        for item in content:
            with self.subTest():
                self.assertContains(self.resp, item)

    def assertContextHasMember(self, member):
        context = self.resp.context
        self.assertIn(member, context)
