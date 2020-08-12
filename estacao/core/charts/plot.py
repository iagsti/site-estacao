from math import pi
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, DatetimeTickFormatter

from .data import DataTemperature, DataConsolidado
from .hovertool import ChartHoverTool

PLOT_TITLE = 'Temperatura'
PLOT_HEIGHT = 400
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

    def load_tseco_data(self):
        date = DataConsolidado('consolidado', 'data')
        date.handle_data()
        tseco = DataConsolidado('consolidado', 'tseco')
        tseco.handle_data()
        tseco_data = {
            'date': date.extracted_data,
            'tseco': tseco.extracted_data
        }
        setattr(self, 'tseco_data', tseco_data)

    def set_data_source(self):
        data = getattr(self, 'data')
        temp_min = ColumnDataSource({
            'date_min': data.get('temp_min').get('date'),
            'temp_min': data.get('temp_min').get('temp_min')
        })

        temp_max = ColumnDataSource({
            'date_max': data.get('temp_max').get('date'),
            'temp_max': data.get('temp_max').get('temp_max'),
        })

        tseco = ColumnDataSource({
            'date_tseco': self.tseco_data.get('date'),
            'tseco': self.tseco_data.get('tseco')
        })

        self.data_sources = {
            'temp_min': temp_min, 'temp_max': temp_max,
            'tseco': tseco
        }

    def set_tools(self):
        tmin = [
            ('Temperatura mínima', '@temp_min'),
            ('Data', '@date_min{%d/%m/%Y %H:%M}')
        ]
        tmax = [
            ('Temperatura máxima', '@temp_max'),
            ('Data', '@date_max{%d/%m/%Y %H:%M}')
        ]
        tseco = [
            ('Temp bulbo seco', '@tseco'),
            ('Data', '@date_tseco{%d/%m/%Y %H:%M}')
        ]
        tooltips = {'tmin': tmin, 'tmax': tmax, 'tseco': tseco}
        chart_tools = ChartHoverTool(plot=getattr(self, 'plot'),
                                     tooltips=tooltips)
        chart_tools.add_hovertools()

    def set_plot(self):
        data = getattr(self, 'data')
        tseco_data = getattr(self, 'tseco_data')

        date_min = data.get('temp_min').get('date')
        date_max = data.get('temp_max').get('date')
        date_tseco = tseco_data.get('date')
        x_range = list(set(date_min + date_max + date_tseco))
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
