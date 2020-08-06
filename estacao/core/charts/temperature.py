from bokeh.layouts import layout
from bokeh.embed import components

from .plot import TemperaturePlot
from .graphs import LineGraph, BarGraph


class Temperature():
    def __init__(self):
        self.temperature_plot = TemperaturePlot()
        self.temp_plot = self.temperature_plot.get_plot()

    def plot(self):
        self.make_plots()
        self.make_components()

    def make_components(self):
        plot = layout([self.graph], sizing_mode='stretch_width')
        script, div = components(plot)
        self.components = {'script': script, 'div': div}

    def make_plots(self):
        temp = PlotTemperature()
        temp.generate_graph()
        self.graph = temp.graph

    def make_line(self, x, y, line_color, legend):
        line_settings = dict(x=x, y=y, line_color=line_color,
                             legend=legend, plot=self.temp_plot,
                             source=self.temperature_plot.data_source)

        plot = LineGraph(**line_settings).get_line()
        setattr(self, 'temp_plot', plot)

    def make_vbar(self, x, top, color, label, gutter):
        temperature_plot = TemperaturePlot()
        plot = temperature_plot.get_plot()

        vbar_settings = dict(x=x, top=top, color=color, plot=self.temp_plot,
                             width=0.2, bar_gutter=gutter, label=label,
                             source=self.temperature_plot.data_source)
        plot = BarGraph(**vbar_settings).get_bar()
        setattr(self, 'temp_plot', plot)

    def get_scripts(self):
        return self.components.get('script')

    def get_div(self):
        return self.components.get('div')
