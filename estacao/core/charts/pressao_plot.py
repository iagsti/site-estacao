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
