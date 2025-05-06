from conftest import auth_session
from test_api import TestBooking


def test_update_created_booking():
    TestBooking.test_successful_booking_creation()