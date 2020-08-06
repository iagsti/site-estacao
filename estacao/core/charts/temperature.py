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

    def get_scripts(self):
        return self.components.get('script')

    def get_div(self):
        return self.components.get('div')
