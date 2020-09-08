from django.test import TestCase
from django.db import models

from ..models import Boletin


class BoletinYearlyTest(TestCase):
    def setUp(self):
        self.obj = Boletin()

    def test_instance(self):
        """It should be an instance of Model"""
        self.assertIsInstance(self.obj, models.Model)

    def test_has_attributes(self):
        attributes = ('title', 'category', 'file')

        for item in attributes:
            with self.subTest():
                message = '{} not found'.format(item)
                self.assertTrue(hasattr(self.obj, item), msg=message)

    def test_attributes_type(self):
        attributes = (
            ('title', models.CharField),
            ('category', models.CharField),
            ('file', models.FileField)
        )

        for item, instance in attributes:
            with self.subTest():
                self.assertIsInstance(getattr(Boletin, item).field, instance)

    def test_category_choices(self):
        category = Boletin.category.field.choices
        expected = (
            ('climatologico', 'Boletim climatológico'),
            ('trimestral', 'Boletim trimestral'),
            ('mensal', 'Boletim mensal'),
            ('tecnico', 'Relatório técnico')
        )
        self.assertTupleEqual(expected, category)

    def test_file_uploa_to_attribute(self):
        upload_to = Boletin.file.field.upload_to
        self.assertEqual(upload_to, 'boletins')
