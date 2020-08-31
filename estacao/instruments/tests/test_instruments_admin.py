from django.test import TestCase
from django.contrib import admin

from estacao.instruments.admin import InstrumentsAdmin
from estacao.instruments.models import Instruments


class AdminTest(TestCase):
    def setUp(self):
        self.obj = InstrumentsAdmin(Instruments, InstrumentsAdmin)

    def test_instance(self):
        self.assertIsInstance(self.obj, admin.ModelAdmin)

    def test_list_display(self):
        list_itens = ('title', 'photo_image')
        for item in list_itens:
            with self.subTest():
                self.assertIn(item, InstrumentsAdmin.list_display)
