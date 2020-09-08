from django.test import TestCase
from django.contrib import admin

from estacao.boletins.admin import BoletinAdmin
from estacao.boletins.models import Boletin


class AdminTest(TestCase):
    def setUp(self):
        self.obj = BoletinAdmin(Boletin, BoletinAdmin)

    def test_instance(self):
        self.assertIsInstance(self.obj, admin.ModelAdmin)

    def test_list_display(self):
        list_itens = ('title', 'category', 'file')
        for item in list_itens:
            with self.subTest():
                self.assertIn(item, BoletinAdmin.list_display)
