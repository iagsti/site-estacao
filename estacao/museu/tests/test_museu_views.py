from django.test import TestCase
from django.shortcuts import resolve_url as r


class MuseuTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('museu:index'))

    def test_status_code(self):
        self.assertTrue(200, self.resp.status_code)

    def test_tempalte(self):
        self.assertTemplateUsed(self.resp, 'museu.html')
        self.assertTemplateUsed(self.resp, 'main.html')
        
