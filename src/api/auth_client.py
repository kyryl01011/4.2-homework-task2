from custom_requester.custom_requester import CustomRequester
from src.enums.base_request_attributes import BaseRequestAttributes


class AuthApiClient(CustomRequester):

    def auth_current_session(self):
        response = self.send_request('POST', '/auth', json=BaseRequestAttributes.ADMIN_CREDS.value)
        token = response.json().get('token')
        if token:
            self.session.headers.update({'Cookie': f'token={token}'})
        else:
            raise ValueError(f'Failed to get auth token - {token}')
