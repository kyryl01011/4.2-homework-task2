from src.data_models.booking_data import BookingDataResponse, BookingDataModel, BookingData


class TestBooking:

    def test_get_all_bookings_ids(self, auth_session):
        endpoint = '/booking'
        response = auth_session.send_request('GET', endpoint)
        assert type(response.json()) == list and 'bookingid' in response.json()[
            0], f'Unexpected type of response data: {type(response.json())}, expected list'
        return response

    def test_successful_booking_creation(self, scenarios, booking_data) -> BookingDataResponse:
        result_model = scenarios.create_booking(booking_data)
        return result_model

    def test_search_id_by_full_name(self, auth_session, booking_data):
        booking_data = self.test_successful_booking_creation(auth_session, booking_data).model_dump()['booking']
        found_result = auth_session.send_request('GET', f'/booking?firstname={booking_data.get('firstname')}&lastname={booking_data.get('lastname')}')
        first_match = found_result.json()[0]['bookingid']
        assert found_result.status_code == 200
        assert found_result.json()[0]
        return first_match

    def test_search_id_by_check_dates(self, auth_session, booking_data):
        booking_dates = self.test_successful_booking_creation(auth_session, booking_data).model_dump()['booking'][
            'bookingdates']
        found_result = auth_session.send_request('GET',
                                                 f'/booking?checkin={booking_dates['checkin']}&checkout={booking_dates['checkout']}')
        assert found_result.json()[0], f'Could not find booking by booking dates: {booking_dates}'
        return found_result

    def test_search_booking_data_by_id(self, auth_session, booking_data) -> BookingDataModel:
        booking_id = self.test_successful_booking_creation(auth_session, booking_data).bookingid
        response = auth_session.send_request('GET', f'/booking/{booking_id}')
        received_booking_data = BookingDataModel.model_validate_json(response.text)
        assert received_booking_data == BookingDataModel.model_validate(
            booking_data), f'Received data {received_booking_data} not equal initial data {BookingDataModel.model_validate(booking_data)}'
        return received_booking_data

    def test_full_booking_update(self, auth_session, booking_data):
        new_booking = self.test_successful_booking_creation(auth_session, booking_data)
        booking_id = new_booking.bookingid
        new_booking_data = BookingData.create_booking_data()
        put_response = BookingDataModel.model_validate_json(
            auth_session.send_request('PUT', f'/booking/{booking_id}', new_booking_data.model_dump()).text)
        assert put_response == new_booking_data, f'New booking data {put_response} not equal to generated new booking data {new_booking_data}'
        assert put_response != booking_data, f'Booking data did not update'

    def test_partial_booking_update(self, auth_session, booking_data: BookingDataModel):
        created_booking_data = self.test_successful_booking_creation(auth_session, booking_data)
        booking_data_dict = created_booking_data.model_dump()['booking']
        booking_id = created_booking_data.bookingid
        new_booking_data = BookingData.create_booking_data()
        new_booking_data_dict = new_booking_data.model_dump()
        if created_booking_data.booking.depositpaid:
            new_booking_data_dict['depositpaid'] = False
        else:
            new_booking_data_dict['depositpaid'] = True
        for key, value in new_booking_data_dict.items():
            patch_response = auth_session.send_request('PATCH', f'/booking/{booking_id}', {key: value})
            assert patch_response.json()[key] != booking_data_dict[
                key], f'Field {key} did not change: expected new "{value}, got {patch_response.json()[key]}", old one "{booking_data_dict[key]}"'
