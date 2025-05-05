from data.booking_data import BookingDataResponse, BookingDataModel


class TestBooking:

    def test_get_all_bookings_ids(self, auth_session):
        endpoint = '/booking'
        response = auth_session.send_request('GET', endpoint)
        assert type(response.json()) == list and 'bookingid' in response.json()[0].keys()
        return response

    def test_booking_creation(self, auth_session, booking_data):
        endpoint = '/booking'
        generated_booking_data = BookingDataModel.model_validate(booking_data)
        response = auth_session.send_request('POST', endpoint, data=booking_data)
        created_booking = BookingDataResponse.model_validate_json(response.text)
        assert response.status_code == 200
        # assert generated_booking_data.firstname == created_booking.booking.firstname
        # assert generated_booking_data.lastname == created_booking.booking.lastname
        # assert generated_booking_data.totalprice == created_booking.booking.totalprice
        # assert generated_booking_data.depositpaid == created_booking.booking.depositpaid
        # assert generated_booking_data.bookingdates.checkin == created_booking.booking.bookingdates.checkin
        # assert generated_booking_data.bookingdates.checkout == created_booking.booking.bookingdates.checkout
        # assert generated_booking_data.additionalneeds == created_booking.booking.additionalneeds
        assert generated_booking_data == created_booking.booking

    def test_search_by_full_name(self, auth_session, booking_data):
        found_result = auth_session.send_request('GET', f'/booking?firstname={booking_data.get('firstname')}&lastname={booking_data.get('lastname')}')
        assert found_result.status_code == 200
        assert found_result.json()[0]

    def test_search_by_check_dates(self, auth_session, booking_data):
        found_result = auth_session.send_request('GET', f'/booking?checkin={booking_data.get('bookingdates').get('checkin')}&checkout={booking_data.get('bookingdates').get('checkout')}')
        print(f'generated checkout: {booking_data.get('bookingdates').get('checkout')}')
        print(found_result.json())
        assert found_result.status_code == 200
        assert found_result.json()[0]

    def test_full_booking_update(self, auth_session, booking_data):
        response = auth_session.send_request('GET', f'/booking?firstname={booking_data.get('firstname')}&lastname={booking_data.get('lastname')}')
        booking_id = BookingDataResponse.model_validate_json(response.text).bookingid

        auth_session.send_request('PUT', f'/booking/{booking_id}', )