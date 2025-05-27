import pytest
import requests

from src.api.auth_client import AuthApiClient
from src.api.booking_client import BookingApiClient
from src.api.scenarios import BookingScenarios
from src.data_models.booking_data import BookingData
from src.enums.base_request_attributes import BaseRequestAttributes


@pytest.fixture(scope='session')
def auth_session():
    session = requests.Session()
    session.headers.update(BaseRequestAttributes.HEADERS.value)

    authed_session = AuthApiClient(session)
    authed_session.auth_current_session()

    yield authed_session

    authed_session.session.close()


@pytest.fixture(scope='session')
def booking_api_client(auth_session):
    client = BookingApiClient(auth_session.session)
    return client

@pytest.fixture(scope='session')
def scenarios(booking_api_client):
    scens = BookingScenarios(booking_api_client)
    return scens


@pytest.fixture(scope='session')
def booking_data(auth_session):
    created_data = BookingData.create_booking_data()
    yield created_data

    # booking removal teardown
    # found_result = auth_session.send_request('GET',
    #                                          f'/booking?firstname={created_data.firstname}&lastname={created_data.lastname}')
    # first_match = found_result.json()[0]['bookingid']
    # auth_session.send_request('DELETE', f'/booking/{first_match}', expected_status_code=201)
    # auth_session.send_request('GET', f'/booking/{first_match}', expected_status_code=404)
