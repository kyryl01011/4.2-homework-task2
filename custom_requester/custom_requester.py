from http import HTTPStatus

from enums.consts import BASE_URL
from requests import Session


class CustomRequester:
    def __init__(self, session: Session):
        self.session = session
        self._base_url = BASE_URL
        self._endpoint = ''

    def get_full_url(self, endpoint):
        return self._base_url + endpoint

    def send_request(self, method, endpoint, json=None, data=None, expected_status_code=200):
        url = self._base_url + endpoint
        response = self.session.request(method, url, json=json, data=data)
        assert response.status_code == expected_status_code, f'Unexpected status code: {response.status_code}, expected: {expected_status_code}'
        return response