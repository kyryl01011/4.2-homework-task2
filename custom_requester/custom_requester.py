from src.enums.base_request_attributes import BaseRequestAttributes
from requests import Session


class CustomRequester:
    def __init__(self, session: Session):
        self.session = session
        self._base_url = BaseRequestAttributes.URL.value
        self._endpoint = ''

    def get_full_url(self, endpoint):
        return self._base_url + endpoint

    def send_request(self, method, endpoint, json=None, data=None, expected_status_code=200):
        url = self._base_url + endpoint
        response = self.session.request(method, url, json=json, data=data)

        # for debug
        # print(f'-----REQUEST------'
        #       f'\n{response.request.url}'
        #       f'\n{response.request.method}'
        #       f'\n{response.request.body}')
        # print(f'-----RESPONSE------'
        #       f'\n{response.text}')

        assert response.status_code == expected_status_code, \
            (f'Unexpected status code: {response.status_code}, '
             f'Expected: {expected_status_code}')
        return response
