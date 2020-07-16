from .graphs import TemperatureGraphs
from .data import DataTemperature
from bokeh.models import ColumnDataSource


class PlotTemperature():
    def __init__(self):
        self.data = dict()
        self.settings = list()

    def generate_graph(self):
        self.load_temperature('temperatura-max', 'temp_max')
        self.load_temperature('temperatura-min', 'temp_min')
        self.make_data_source('temp_max')
        self.set_line('red', 'temperatura máxima')
        self.make_data_source('temp_min')
        self.set_line('blue', 'temperatura mínima')
        graph = TemperatureGraphs(line_settings=self.settings,
                                  legend='Temperatura', title='Temperatura',
                                  xlabel='data', ylabel='Temperatura')
        self.graph = graph.get_graph()

    def load_temperature(self, resource, data_index):
        data = DataTemperature(resource=resource, data_index=data_index)
        data.handle_data()
        self.data.update({data_index: data.extracted_data})

    def make_data_source(self, data_index):
        temp_data = self.data.get(data_index)
        data = {
            'date': temp_data.get('date'),
            'temp': temp_data.get(data_index)
        }
        self.data_source = ColumnDataSource(data=data)

    def set_line(self, line_color, legend):
        line_settings = {'x': 'date', 'y': 'temp', 'line_color': line_color,
                         'legend': legend,
                         'source': self.data_source}
        self.settings.append(line_settings)
