from django.test import TestCase
from django.db import models

from ..models import Boletin
from ..managers import BoletinQuerySet


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


class BoletimManagerTest(TestCase):
    def setUp(self):
        Boletin.objects.create(
            title='2020', category='climatologico', file='boletim.pdf')
        Boletin.objects.create(
            title='Trimestral', category='trimestral', file='boletim.pdf')
        Boletin.objects.create(
            title='mensal', category='mensal', file='boletim.pdf')
        Boletin.objects.create(
            title='tecnico', category='tecnico', file='boletim.pdf')

    def test_manager_climatologico(self):
        resp = Boletin.objects.climatologico().first()
        self.assertEqual(resp.category, 'climatologico')

    def test_manager_trimestral(self):
        resp = Boletin.objects.trimestral().first()
        self.assertEqual(resp.category, 'trimestral')

    def test_manager_mensal(self):
        resp = Boletin.objects.mensal().first()
        self.assertEqual(resp.category, 'mensal')

    def test_manager_tecnico(self):
        resp = Boletin.objects.tecnico().first()
        self.assertEqual(resp.category, 'tecnico')
