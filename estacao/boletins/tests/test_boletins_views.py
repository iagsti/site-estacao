from django.test import TestCase
from django.shortcuts import resolve_url as r


class BoletinsGetTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('boletins:index'))

    def test_status_code(self):
        self.assertTrue(200, self.resp.status_code)

    def test_template_rendering(self):
        self.assertTemplateUsed(self.resp, 'boletins.html')
        self.assertTemplateUsed(self.resp, 'main.html')

    def test_context_has_boletins(self):
        context = self.resp.context
        self.assertIn('boletins', context)
