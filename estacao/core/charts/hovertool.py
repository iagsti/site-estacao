from bokeh.models import HoverTool


class ChartHoverTool:
    def __init__(self, **kwargs):
        self.plot = kwargs.get('plot')
        self.tooltips = kwargs.get('tooltips')

    def add_hovertools(self):
        self.get_names()
        self.set_hovertools()

    def get_names(self):
        names = tuple(self.tooltips.keys())
        setattr(self, 'names', names)

    def set_hovertools(self):
        formatter = {'@date': 'datetime'}
        for item in self.names:
            hover = HoverTool(tooltips=self.tooltips.get(item),
                              names=[item], formatters=formatter)

            self.plot.add_tools(hover)

