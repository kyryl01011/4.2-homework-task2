import pytest
import requests

from src.api.auth_client import AuthApiClient
from src.api.booking_client import BookingApiClient
from src.scenarios.scenarios import BookingScenarios
from src.data_models.booking_data import BookingData, BookingDataModel
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
def booking_data(auth_session, scenarios):
    created_data_collection: list[BookingDataModel] = []

    def _create_booking_data():
        created_data = BookingData.create_booking_data()
        created_data_collection.append(created_data)
        return created_data

    yield _create_booking_data

    for data_model in created_data_collection:
        try:
            booking_id = scenarios.get_booking_id_by_full_name(data_model.firstname, data_model.lastname)
            scenarios.delete_booking_by_id(booking_id)
        # Ignore modified or not created bookings
        except UnboundLocalError as e:
            continue
