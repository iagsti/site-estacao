from django.test import TestCase
from estacao.core.resources import MeteogramTemperature
from unittest.mock import MagicMock
from estacao.core.resources import UriManager
from .mock import make_path, mock_uri, mock_api


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

    def test_instance(self):
        """It should be an instance of UriManager"""
        self.assertIsInstance(self.obj, UriManager)

    def make_data(self, **kwargs):
        data = [
            {'date': '2020-01-01 00:13:00', 'temp': '12'},
            {'date': '2020-01-01 00:14:00', 'temp': '23'},
            {'date': '2020-01-01 00:15:00', 'temp': '20'},
            {'date': '2020-01-02 00:16:00', 'temp': '19'},
            {'date': '2020-01-02 00:17:00', 'temp': '18'},
            {'date': '2020-01-02 00:17:00', 'temp': '18'},
        ]
        return data


class UriManagerTest(TestCase):
    def setUp(self):
        self.obj = UriManager()

    def test_instance(self):
        self.assertTrue(isinstance(self.obj, UriManager))

    def test_has_generate_uri_attribute(self):
        self.assertTrue(hasattr(self.obj, 'generate_uri'))

    def test_has_make_date_range_attribute(self):
        self.assertTrue(hasattr(self.obj, 'make_date_range'))

    def test_make_date_range(self):
        expected = make_path(version='')
        self.obj.make_date_range(step=1)
        self.assertEqual(expected, self.obj.date_range)

    def test_has_generate_path_attribute(self):
        self.assertTrue(hasattr(self.obj, 'generate_path'))

    def test_generate_path(self):
        expected = make_path(resource='temperature_min')
        self.obj.make_date_range()
        self.obj.generate_path(resource='temperature_min')
        self.assertEqual(expected, self.obj.path)

    def test_generate_uri(self):
        expected = mock_uri(resource='temperature_min')
        resp = self.obj.generate_uri(resource='temperature_min')
        self.assertEqual(expected, resp)


class MeteogramTemperatureGetTest(TestCase):
    def setUp(self):
        self.obj = MeteogramTemperature()

    @mock_api
    def test_temperature_min(self):
        expected = self.make_data()
        resp = self.obj.temperature_min()
        self.assertListEqual(expected, resp['temp_min'])

    @mock_api
    def test_temperature_max(self):
        expected = self.make_data()
        resp = self.obj.temperature_max()
        self.assertListEqual(expected, resp['temp_max'])

    def make_data(self, **kwargs):
        data = [
            {'date': '2020-01-01 00:13:00', 'temp': '12'},
            {'date': '2020-01-01 00:14:00', 'temp': '23'},
            {'date': '2020-01-01 00:15:00', 'temp': '20'},
            {'date': '2020-01-02 00:16:00', 'temp': '19'},
            {'date': '2020-01-02 00:17:00', 'temp': '18'},
            {'date': '2020-01-02 00:17:00', 'temp': '12'},
        ]
        return data
