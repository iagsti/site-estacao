from django.test import TestCase
from estacao.core.managers import ConditionsManager


class CoreManagersTest(TestCase):
    def setUp(self):
        self.manager = ConditionsManager()

    def test_manager_instance(self):
        """It should be a ConditionManager instance"""
        self.assertIsInstance(self.manager, ConditionsManager)

    def test_max_temperature_attr(self):
        """Manager should have max_temperature attr"""
        self.assertTrue(hasattr(self.manager, 'max_temperature'))

    def test_min_temperature_attr(self):
        """Manager should have min_temperature attr"""
        self.assertTrue(hasattr(self.manager, 'min_temperature'))

    def test_td_attr(self):
        """Manage should have td attr"""
        self.assertTrue(hasattr(self.manager, 'td'))

    def test_p_hpa(self):
        """Manage should have p_hpa attr"""
        self.assertTrue(hasattr(self.manager, 'p_hpa'))

    def test_visibility(self):
        """Manage should have visibility attr"""
        self.assertTrue(hasattr(self.manager, 'visibility'))

    def test_ur_attr(self):
        """manager should have ur attr"""
        self.assertTrue(hasattr(self.manager, 'relative_humidity'))

    def test_nuvens_baixas(self):
        """Manage should have nuvens_baixas attr"""
        self.assertTrue(hasattr(self.manager, 'nuvens_baixas'))

    def test_nuvens_medias(self):
        """Manage should have nuvens_medias attr"""
        self.assertTrue(hasattr(self.manager, 'nuvens_medias'))

    def test_nuvens_altas(self):
        """Manage should have nuvens_altas attr"""
        self.assertTrue(hasattr(self.manager, 'nuvens_altas'))
    


    
