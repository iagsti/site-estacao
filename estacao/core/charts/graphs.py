from bokeh.plotting import figure
from bokeh.transform import dodge


class TemperatureGraphs:
    def __init__(self, line_settings=[], legend='', **kwargs):
        self.line_settings = line_settings
        self.legend = legend
        self.params = kwargs

    def get_graph(self):
        self.set_figure()
        self.set_line()
        return self.plot

    def set_figure(self):
        plot = figure(title=self.params.get('title'), x_axis_type='datetime',
                      plot_height=300, tools="pan,wheel_zoom,box_zoom,reset")
        plot.xaxis.axis_label = self.params.get('xlabel')
        plot.yaxis.axis_label = self.params.get('ylabel')
        plot.toolbar.logo = None
        self.plot = plot

    def set_line(self):
        for line in self.line_settings:
            self.plot.line(
                x=line.get('x'),
                y=line.get('y'),
                line_color=line.get('line_color'),
                legend_label=line.get('legend'),
                source=line.get('source')
            )
            self.plot.legend.location = 'top_right'


class BarGraph:
    def __init__(self, **kwargs):
        self.x = kwargs.get('x')
        self.top = kwargs.get('top')
        self.width = kwargs.get('width')
        self.color = kwargs.get('color')
        self.label = kwargs.get('label')
        self.gutter = kwargs.get('bar_gutter')
        self.source = kwargs.get('source')
        self.plot = kwargs.get('plot')

    def get_bar(self):
        self.set_bar()
        return self.plot

    def set_bar(self):
        self.plot.vbar(x=dodge(self.x, self.gutter, range=self.plot.x_range),
                       top=self.top, width=self.width, source=self.source,
                       color=self.color, legend_label=self.label)
