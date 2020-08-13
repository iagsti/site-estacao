from bokeh.models import ColumnDataSource, DatetimeTickFormatter, HoverTool
from bokeh.plotting import figure
from math import pi

from .data import DataConsolidado
from .hovertool import ChartHoverTool

PLOT_HEIGHT = 400
TICK_FORMAT = ['%d/%m/%Y %H:%M:%S']


class PressaoPlot:
    def __init__(self):
        self.data = {'date': [], 'pressao': [], 'pressao_hpa': []}

    def plot(self):
        self.load_data()
        self.set_data_source()
        self.set_plot()
        self.set_tools()

    def load_data(self):
        date = DataConsolidado('consolidado', 'data')
        date.handle_data()
        pressao = DataConsolidado('consolidado', 'pressao')
        pressao.handle_data()
        pressao_hpa = DataConsolidado('consolidado', 'pressao_hpa')
        pressao_hpa.handle_data()

        data = {'date': date.extracted_data, 'pressao': pressao.extracted_data,
                'pressao_hpa': pressao_hpa.extracted_data}

        setattr(self, 'data', data)

    def set_data_source(self):
        data = getattr(self, 'data')
        pressao = {'date': data.get('date'), 'pressao': data.get('pressao')}
        pressao_hpa = {'date': data.get('date'),
                       'pressao_hpa': data.get('pressao_hpa')}

        source_pressao = ColumnDataSource(data=pressao)
        source_pressao_hpa = ColumnDataSource(data=pressao_hpa)
        datasource = {'pressao': source_pressao,
                      'pressao_hpa': source_pressao_hpa}

        setattr(self, 'datasource', datasource)

    def set_plot(self):
        data = getattr(self, 'data')
        x_range = data.get('date')

        plot = figure(x_range=x_range,
                      title='Pressão', plot_height=PLOT_HEIGHT)

        plot.xaxis.axis_label = 'Data'
        plot.yaxis.axis_label = 'Pressão Atmosférica(mmHg)'
        plot.xaxis.major_label_orientation = pi/3.8

        plot.toolbar.logo = None

        tick_format = dict(hours=TICK_FORMAT,
                           days=TICK_FORMAT,
                           months=TICK_FORMAT,
                           years=TICK_FORMAT)

        plot.xaxis.formatter = DatetimeTickFormatter(**tick_format)

        setattr(self, 'plot', plot)

    def set_tools(self):
        formatter = {
            'pressao': {'@date_min': 'datetime'},
            'pressao_hpa': {'@date_max': 'datetime'},
        }
        pressao = [
            ('Pressão', '@pressao'),
            ('Data', '@date{%d/%m/%Y %H:%M}')
        ]
        pressao_hpa = [
            ('Pressão hpa', '@pressao_hpa'),
            ('Data', '@date{%d/%m/%Y %H:%M}')
        ]
        tooltips = {'pressao': pressao, 'pressao_hpa': pressao_hpa}

        chart_tools = ChartHoverTool(plot=getattr(self, 'plot'),
                                     tooltips=tooltips,
                                     formatters=formatter)
        chart_tools.add_hovertools()
