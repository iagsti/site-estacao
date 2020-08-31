from django.test import TestCase
from django.db import models

from estacao.instruments.models import Instruments


class InstrumentsModelTest(TestCase):
    def setUp(self):
        self.obj = Instruments()

    def test_is_instance_of_Models(self):
        self.assertIsInstance(self.obj, models.Model)

    def test_has_attributes(self):
        attributes = ('title', 'text', 'image')
        for expected in attributes:
            message = '{} not found'.format(expected)
            with self.subTest():
                self.assertTrue(hasattr(self.obj, expected), msg=message)

    def test_attributes_type(self):
        attribute_instances = (('title', models.CharField),
                               ('text', models.CharField),
                               ('image', models.FileField))
        for attribute in attribute_instances:
            with self.subTest():
                attr_name, instance = attribute
                field = getattr(Instruments, attr_name).field
                self.assertIsInstance(field, instance)

    def test_upload_image_destination(self):
        """upload_to image attribute should be equal instruments"""
        self.assertEqual(Instruments.image.field.upload_to, 'instruments')

    def test_create(self):
        """It should create an instrument on database"""
        instrument = dict(title='Nebulosidade', text='Visibilidade horizontal',
                          image='https://picsum.photos/200/300')
        Instruments.objects.create(**instrument)
        self.assertTrue(Instruments.objects.exists())
