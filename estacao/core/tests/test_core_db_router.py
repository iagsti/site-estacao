from django.test import TestCase
from estacao.db_routers import DadosRouter
from estacao.core.models import Dados


class DBRouterCoreTest(TestCase):
    def setUp(self):
        self.obj = DadosRouter()

    def test_route_app_tables(self):
        expected = {'dados'}
        self.assertEqual(expected, DadosRouter.route_app_tables)
        
    def test_db_for_read(self):
        expected = 'dados'
        db_for_read = self.obj.db_for_read(Dados)
        self.assertEqual(expected, db_for_read)

    def test_db_for_write(self):
        expected = 'dados'
        db_for_write = self.obj.db_for_read(Dados)
        self.assertEqual(expected, db_for_write)

    def test_allow_relation(self):
        expected = None
        allow_relation = self.obj.allow_relation(Dados, Dados)
        self.assertEqual(expected, allow_relation)

    def test_allow_migrate(self):
        expected = 'dados'
        allow_migrate = self.obj.allow_migrate(db='dados', app_label='core', model_name='dados')
        self.assertTrue(allow_migrate)
