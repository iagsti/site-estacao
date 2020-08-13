from bokeh.models import HoverTool


class ChartHoverTool:
    def __init__(self, **kwargs):
        self.plot = kwargs.get('plot')
        self.tooltips = kwargs.get('tooltips')
        self.formatters = kwargs.get('formatters')

    def add_hovertools(self):
        self.get_names()
        self.set_hovertools()

    def get_names(self):
        names = tuple(self.tooltips.keys())
        setattr(self, 'names', names)

    def set_hovertools(self):
        for item in self.names:
            formatter = self.get_formatter_for_column(item)
            hover = HoverTool(tooltips=self.tooltips.get(item),
                              names=[item], formatters=formatter)

            self.plot.add_tools(hover)

    def get_formatter_for_column(self, column_name):
        return self.formatters.get(column_name)
