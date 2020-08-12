from bokeh.models import ColumnDataSource


class DataSource:
    def __init__(self, data, date_key, data_key):
        self.data = data
        self.date_key = date_key
        self.data_key = data_key

    def get_datasource(self):
        self.make_datasource()
        return self.datasource

    def make_datasource(self):
        self.data.handle_data()
        datasource = ColumnDataSource(self.data.extracted_data)
        setattr(self, 'datasource', datasource)
