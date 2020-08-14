from faker import Faker
from faker.providers import BaseProvider

fake = Faker('pt_BR')


class ConsolidadoProvider(BaseProvider):
    def consolidado(self):
        return {
            "data": "2020-08-06 00:00", "dir": "C", "evap_piche": 4.45,
            "evap_piche_ar": 13.8, "piche": 4.45, "piche_ar": 13.8,
            "pressao": 704.2, "pressao_hpa": 802.7, "qtda": 0, "qtdb": 0,
            "qtdm": 0, "t10cm": 18.6, "t20cm": 20.7, "t30cm": 20.7,
            "t40cm": 20.5, "t5cm": 16.7, "temp_bar": 17.0, "tipoa": "",
            "tipob": "", "tipom": "", "tmax": 14.0, "tmin": 11.5,
            "tseco": 12.0, "tsfc": 11.9, "tumido": 11.4, "vento": 0.0, "vis": 6
        }


def consolidado_factory(lenght=1):
    data = list()
    fake.add_provider(ConsolidadoProvider)
    for _ in range(lenght):
        data.append(fake.consolidado())
    return data
