from data.booking_data import BookingDataResponse, BookingDataModel, BookingData
from utils.data_generator import GenerateData


class TestBooking:

    def test_get_all_bookings_ids(self, auth_session):
        endpoint = '/booking'
        response = auth_session.send_request('GET', endpoint)
        assert type(response.json()) == list and 'bookingid' in response.json()[0].keys()
        return response

    def test_successful_booking_creation(self, auth_session, booking_data) -> BookingDataResponse:
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
        return created_booking

    def test_search_id_by_full_name(self, auth_session, booking_data):
        found_result = auth_session.send_request('GET', f'/booking?firstname={booking_data.get('firstname')}&lastname={booking_data.get('lastname')}')
        first_match = found_result.json()[0]
        print(first_match)
        assert found_result.status_code == 200
        assert found_result.json()[0]
        return found_result

    def test_search_id_by_check_dates(self, auth_session, booking_data):
        print('FOUND RESULT: ')
        found_result = auth_session.send_request('GET', f'/booking?checkin={booking_data['bookingdates']['checkin']})&checkout={booking_data['bookingdates']['checkout']}')
        assert found_result.status_code == 200
        assert found_result.json()[0]

    def test_search_booking_data_by_id(self, auth_session, booking_id) -> BookingDataModel:
        return BookingDataModel.model_validate_json(auth_session.send_request('GET', f'/booking/{booking_id}').text)

    def test_full_booking_update(self, auth_session, booking_data):
        new_booking = self.test_successful_booking_creation(auth_session, booking_data)
        booking_id = new_booking.bookingid
        new_booking_data = BookingData.create_booking_data()
        put_response = BookingDataModel.model_validate_json(auth_session.send_request('PUT', f'/booking/{booking_id}', new_booking_data.model_dump()).text)
        assert put_response == new_booking_data, f'New booking data {put_response} not equal to generated new booking data {new_booking_data}'
        assert put_response != booking_data, f'Booking data did not update'

    def test_partial_booking_update(self, auth_session, booking_data: BookingDataModel):
        created_booking_data = self.test_successful_booking_creation(auth_session, booking_data)
        booking_data_dict = created_booking_data.model_dump()['booking']
        booking_id = created_booking_data.bookingid
        new_booking_data = BookingData.create_booking_data()
        new_booking_data_dict = new_booking_data.model_dump()
        for key, value in new_booking_data_dict.items():
            print(new_booking_data_dict[key])
            patch_response = auth_session.send_request('PATCH', f'/booking/{booking_id}', {key: value})
            print(patch_response.text)
            assert patch_response.status_code == 200
            assert patch_response.json()[key] != booking_data_dict[key], f'Field {key} did not change: expected new "{value}, got {patch_response.json()[key]}", old one "{booking_data_dict[key]}"'
