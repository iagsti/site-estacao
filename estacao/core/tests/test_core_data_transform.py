from django.test import TestCase
from estacao.core.data_transform import DataTransform


class TransformDataTest(TestCase):
    def setUp(self):
        self.obj = DataTransform()

    def test_ep(self):
        expected = 32.504082187607324
        ep = self.obj.ep(temp=25.4)
        self.assertEqual(expected, ep)

    def test_pressao(self):
        expected = 922.4859092327467
        pressao = self.obj.pressao(pressao=695.5, temp_bar=20.1)
        self.assertEqual(expected, pressao)

    def test_rh(self):
        expected = 70.39200814354001
        rh = self.obj.rh(25.4, 21, 695.5)
        self.assertEqual(expected, rh)

    def test_td(self):
        expected = 19.84863450752878
        td = self.obj.td(24.5, 21, 695.5)
        self.assertEqual(expected, td)

    def test_visibility(self):
        expected = '200 a 500 m'
        visibility = self.obj.visibility(2)
        self.assertEqual(expected, visibility)

    def test_windchill(self):
        expected = 26.372809014693235
        wd = self.obj.windchill(24.5, 3)
        self.assertEqual(expected, wd)


