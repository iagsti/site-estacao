from bokeh.layouts import layout
from bokeh.embed import components

from .plot import PlotTemperature


class Temperature():
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

