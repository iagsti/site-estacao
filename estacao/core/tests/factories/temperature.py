from faker import Faker
from faker.providers import BaseProvider, date_time


fake = Faker('pt_BR')


class TemperatureProvider(BaseProvider):
    def temperature(self):
        fake.add_provider(date_time)
        return dict(
            data=str(fake.date_time()),
            temp=fake.random_int(max=40)
        )

    def weather(self):
        elements = ('Ac/As-10/10', 'Am/As-20/20')
        return dict(data=str(fake.date_time()),
                    temperatura_ar=fake.random_int(max=40),
                    temperatura_ponto_orvalho=fake.random_int(max=20),
                    umidade_relativa=fake.random_int(max=100),
                    temperatura_min=fake.random_int(max=30),
                    temperatura_max=fake.random_int(max=40),
                    vento=fake.random_int(max=200),
                    pressao=fake.random_int(max=300),
                    visibilidade_min=fake.random_int(max=100),
                    visibilidade_max=fake.random_int(max=100),
                    nuvens_baixas=fake.random_element(elements=elements),
                    nuvens_medias=fake.random_element(elements=elements),
                    nuvens_altas=fake.random_element(elements=elements))


def temperature_factory(lenght):
    data = list()
    fake.add_provider(TemperatureProvider)
    for item in range(lenght):
        data.append(fake.temperature())
    return data


def weather_factory():
    fake.add_provider(TemperatureProvider)
    return fake.weather()
