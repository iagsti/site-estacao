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


def temperature_factory(lenght):
    data = list()
    fake.add_provider(TemperatureProvider)
    for item in range(lenght):
        data.append(fake.temperature())
    return data
