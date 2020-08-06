from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, HoverTool, DatetimeTickFormatter

from .data import DataTemperature

PLOT_TITLE = 'Temperatura'
PLOT_HEIGHT = 300
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

        }

