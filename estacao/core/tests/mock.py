import httpretty
import json
import functools
from django.conf import settings


API_URI = getattr(settings, 'API_URL') + '/2020-01-01/2020-02-01/'


def mock_meteogram_request(uri=API_URI):
    def request_decorator(request):
        @functools.wraps(request)
        @httpretty.activate
        def wrapper(*args, **kwargs):
            body = json.dumps(make_data())
            httpretty.register_uri(httpretty.GET, uri=uri, body=body)
            response = request(*args, **kwargs)
            return response
        return wrapper
    return request_decorator


def make_data():
    data = {
        'temp_min':  [
            {'date': '2020-01-01 00:13:00', 'temp': '12'},
            {'date': '2020-01-01 00:14:00', 'temp': '23'},
            {'date': '2020-01-01 00:15:00', 'temp': '20'},
            {'date': '2020-01-01 00:16:00', 'temp': '19'},
            {'date': '2020-01-01 00:17:00', 'temp': '18'},
        ]
    }
    return data
