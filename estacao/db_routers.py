class DadosRouter:
    route_app_tables = {'dados'}
    route_model_name = {'dados'}

    def db_for_read(self, model, **hints):
        if model._meta.db_table in self.route_app_tables:
            return 'dados'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.db_table in self.route_app_tables:
            return 'dados'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        return None

    def allow_migrate(self, db, app_label=None, model_name=None, **hints):
        if model_name in self.route_model_name:
            return db == 'dados'
        return None

