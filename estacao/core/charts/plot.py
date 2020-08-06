from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, HoverTool, DatetimeTickFormatter

from .data import DataTemperature

PLOT_TITLE = 'Temperatura'
PLOT_HEIGHT = 300
X_AXIS_LABEL = 'Data'
Y_AXIS_LABEL = 'Temperatura'
TICK_FORMAT = ['%d/%m/%Y %H:%M:%S']


class TemperaturePlot():
    def get_plot(self):
        self.load_temperature_data()
        self.set_data_source()
        self.set_tools()
        self.set_plot()
        return self.plot

    def load_temperature_data(self):
        t_min = DataTemperature('temperatura-min', 'temp_min')
        t_max = DataTemperature('temperatura-max', 'temp_max')
        t_min.handle_data()
        t_max.handle_data()
        self.data = {
            'temp_min': t_min.extracted_data,
            'temp_max': t_max.extracted_data
        }

    def set_data_source(self):
        data = getattr(self, 'data')
        source = {
            'date_min': data.get('temp_min').get('date'),
            'temp_min': data.get('temp_min').get('temp_min'),
            'date_max': data.get('temp_max').get('date'),
            'temp_max': data.get('temp_max').get('temp_max')
        }
        self.data_source = ColumnDataSource(data=source)

    def set_tools(self):
        t = [
            ('Temperatura mínima', '@temp_min'),
            ('Temperatura máxima', '@temp_max'),
            ('Data', '@date_max{%d/%m/%Y %H:%M}'),
        ]
        formatters = {'@date_max': 'datetime'}
        tools = HoverTool(tooltips=t, formatters=formatters)
        setattr(self, 'tools', tools)

    def set_plot(self):
        data = getattr(self, 'data')

        date_min = data.get('temp_min').get('date')
        date_max = data.get('temp_max').get('date')
        x_range = list(set(date_min + date_max))
        x_range.sort()
        title = PLOT_TITLE
        height = PLOT_HEIGHT

        plot = figure(x_range=x_range, title=title, plot_height=height)

        plot.xaxis.axis_label = X_AXIS_LABEL
        plot.yaxis.axis_label = Y_AXIS_LABEL
        plot.toolbar.logo = None
        tick_format = dict(hours=TICK_FORMAT,
                           days=TICK_FORMAT,
                           months=TICK_FORMAT,
                           years=TICK_FORMAT)

        plot.xaxis.formatter = DatetimeTickFormatter(**tick_format)
        plot.add_tools(getattr(self, 'tools'))
        setattr(self, 'plot', plot)
