from django.test import TestCase
from django.db import models

from ..models import Boletin


class BoletinYearlyTest(TestCase):
    def setUp(self):
        self.obj = Boletin()

    def test_instance(self):
        """It should be an instance of Model"""
        self.assertIsInstance(self.obj, models.Model)
