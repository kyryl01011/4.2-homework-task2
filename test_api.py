from conftest import scenarios
from src.data_models.booking_data import BookingDataResponse, BookingDataModel, BookingData


class TestBooking:

    def test_get_all_bookings_ids(self, auth_session):
        endpoint = '/booking'
        response = auth_session.send_request('GET', endpoint)
        assert type(response.json()) == list and 'bookingid' in response.json()[
            0], f'Unexpected type of response data: {type(response.json())}, expected list'
        return response

    def test_general(self, scenarios, booking_data):
        created_booking_model = scenarios.create_booking(booking_data)
        scenarios.get_booking_by_id(created_booking_model.bookingid)
        scenarios.delete_booking_by_id(created_booking_model.bookingid)

    def test_successful_booking_creation(self, scenarios, booking_data):
        scenarios.create_booking(booking_data)

    def test_search_id_by_full_name(self, scenarios, booking_data):
        created_booking_response_model = scenarios.create_booking(booking_data)
        scenarios.get_booking_id_by_full_name(
            created_booking_response_model.booking.firstname,
            created_booking_response_model.booking.lastname)

    def test_search_id_by_check_dates(self, scenarios, booking_data):
        created_booking_response_model = scenarios.create_booking(booking_data)
        scenarios.get_booking_id_by_check_dates(
            created_booking_response_model.booking.bookingdates.checkin,
            created_booking_response_model.booking.bookingdates.checkout)

    def test_search_booking_data_by_id(self, scenarios, booking_data):
        created_booking_model = scenarios.create_booking(booking_data)
        scenarios.get_booking_by_id(created_booking_model.bookingid)

    # TODO

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
