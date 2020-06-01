from django.test import TestCase
from estacao.core.resources import MeteogramTemperature
from unittest.mock import MagicMock


class ResourcesMeteogramTemperatureTest(TestCase):
    def setUp(self):
        self.obj = MeteogramTemperature()
        self.original_attribute = self.obj.temperature_min
        self.obj.temperature_min = MagicMock(return_value=self.make_data())

    def tearDown(self):
        super().tearDown()
        self.obj.temperature_min = self.original_attribute

    def test_has_temperature_min(self):
        """ It should has temperature_min attribute"""
        self.assertTrue(hasattr(self.obj, 'temperature_min'))

    def test_temperature_min_data(self):
        """It should return temperature data"""
        data = self.obj.temperature_min()
        self.assertListEqual(data, self.make_data())

    def test_has_temperature_max(self):
        """It should return temperature data"""
        self.assertTrue(hasattr(self.obj, 'temperature_max'))

    def make_data(self, **kwargs):
        data = [
            {'date': '2020-01-01 00:13:00', 'temp': '12'},
            {'date': '2020-01-01 00:14:00', 'temp': '23'},
            {'date': '2020-01-01 00:15:00', 'temp': '20'},
            {'date': '2020-01-01 00:16:00', 'temp': '19'},
            {'date': '2020-01-01 00:17:00', 'temp': '18'},
        ]
        return data


