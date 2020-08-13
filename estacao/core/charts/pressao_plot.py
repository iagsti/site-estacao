from bokeh.models import ColumnDataSource

from .data import DataConsolidado

class PressaoPlot:
    def __init__(self):
        self.data = {'date': [], 'pressao': [], 'pressao_hpa': []}

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
