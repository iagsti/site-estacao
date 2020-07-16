import requests
import numpy as np
import abc
from requests.auth import HTTPBasicAuth
from django.conf import settings
from estacao.core.resources import UriManager


API_URL = getattr(settings, 'API_URL')
REQUEST_TIMEOUT = getattr(settings, 'API_REQUEST_TIMEOUT')


class Chart(UriManager, abc.ABC):
    def __init__(self, date_ini=None, date_end=None):
        self.date_ini = date_ini
        self.date_end = date_end
        if not date_ini or not date_end:
            today = np.datetime64('today')
            datetime_delta = np.timedelta64(1, 'D')
            yesterday = today - datetime_delta
            self.date_ini = str(yesterday)
            self.date_end = str(today)

    def handle_data(self):
        self.make_uri()
        self.load_data()
        self.extract_data(self.temperature_data)
        self.to_datetime()

    @abc.abstractmethod
    def make_uri(self):
        pass

    def load_data(self):
        try:
            user = getattr(settings, 'API_USER')
            paswd = getattr(settings, 'API_PASWD')
            auth = HTTPBasicAuth(username=user, password=paswd)
            response = requests.get(self.uri, auth=auth,
                                    timeout=REQUEST_TIMEOUT).json()
        except Exception:
            response = {'tem_min': [{'data': '2020-06-25 13:00:00', 'temp': '0'}]}
        self.temperature_data = response

    @abc.abstractmethod
    def extract_data(self, data):
        pass

    def to_datetime(self):
        date_list = self.extracted_data.get('date')
        datetime_list = []
        for date in date_list:
            date_time = np.datetime64(date)
            datetime_list.append(date_time)
        self.extracted_data['date'] = datetime_list
