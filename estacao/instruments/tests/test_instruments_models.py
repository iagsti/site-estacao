from django.test import TestCase
from django.db import models

from estacao.instruments.models import Instruments


class InstrumentsModelTest(TestCase):
    def setUp(self):
        self.obj = Instruments()

    def test_is_instance_of_Models(self):
        self.assertIsInstance(self.obj, models.Model)
