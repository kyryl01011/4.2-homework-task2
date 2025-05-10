import pytest
import requests

from custom_requester.custom_requester import CustomRequester
from data.booking_data import BookingData, BookingDataModel
from enums.consts import BASE_HEADERS, BASE_DATA


@pytest.fixture(scope='session')
def auth_session():
    session = requests.Session()
    session.headers.update(BASE_HEADERS)

    fresh_session = CustomRequester(session)
    response = fresh_session.send_request('POST', '/auth', json=BASE_DATA)
    token = response.json().get('token', False)
    if token:
        fresh_session.session.headers.update({'Cookie': f'token={token}'})
    else:
        raise ValueError(f'Failed to get auth token - {token}')

    yield fresh_session
    fresh_session.session.close()

@pytest.fixture(scope='session')
def booking_data(auth_session):
    created_data = BookingData.create_booking_data()
    yield created_data.model_dump()

    # booking removal teardown
    found_result = auth_session.send_request('GET',f'/booking?firstname={created_data.firstname}&lastname={created_data.lastname}')
    first_match = found_result.json()[0]['bookingid']
    auth_session.send_request('DELETE', f'/booking/{first_match}', expected_status_code=201)
    auth_session.send_request('GET', f'/booking/{first_match}', expected_status_code=404)