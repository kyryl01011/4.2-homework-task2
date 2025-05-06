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
    response = fresh_session.send_request('POST', '/auth', data=BASE_DATA)
    print(response.json())
    token = response.json().get('token', False)
    if token:
        fresh_session.session.headers.update({'Cookie': f'token={token}'})
    else:
        raise ValueError(f'Failed to get auth token - {token}')

    yield fresh_session
    fresh_session.session.close()

@pytest.fixture(scope='session')
def booking_data(auth_session) -> BookingDataModel:
    return BookingData.create_booking_data().model_dump()

    # че-то оно не хочет удалять
    # created_booking_id = auth_session.send_request('GET', f'/booking?firstname={fake_booking_data.firstname}&lastname={fake_booking_data.lastname}').json()[0].get('bookingid', '')
    # created_booking_exists = auth_session.send_request('GET', f'/booking/{created_booking_id}')
    # if created_booking_exists:
    #     auth_session.send_request('DELETE', f'/booking/{created_booking_id}')
    #     second_check = auth_session.send_request('DELETE', f'/booking/{created_booking_id}')
    # assert second_check.status_code == 404, f'Failed on removing created booking with id {created_booking_id}'