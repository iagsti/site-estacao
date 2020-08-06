from bokeh.transform import dodge


class LineGraph:
    def __init__(self, **kwargs):
        self.x = kwargs.get('x')
        self.y = kwargs.get('y')
        self.line_color = kwargs.get('line_color')
        self.plot = kwargs.get('plot')
        self.source = kwargs.get('source')
        self.legend = kwargs.get('legend')

    def get_line(self):
        self.set_line()
        return self.plot

    def set_line(self):
        self.plot.line(x=self.x, y=self.y, line_color=self.line_color,
                       legend_label=self.legend, source=self.source)


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
