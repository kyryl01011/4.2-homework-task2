from custom_requester.custom_requester import CustomRequester


class BookingApiClient(CustomRequester):
    BOOKING_ENDPOINT = '/booking'

    def create_booking(self, booking_data: dict):
        response = self.send_request('POST', self.BOOKING_ENDPOINT, json=booking_data)
        return response

    def get_booking_by_id(self, booking_id: int, expected_status_code=200):
        response = self.send_request(
            'GET',
            f'{self.BOOKING_ENDPOINT}/{booking_id}',
            expected_status_code=expected_status_code)
        return response

    def get_booking_id_by_full_name(self, first_name: str, last_name: str):
        response = self.send_request('GET', f'{self.BOOKING_ENDPOINT}?firstname={first_name}&lastname={last_name}')
        return response

    def get_booking_id_by_check_dates(self, check_in: str, check_out: str):
        response = self.send_request('GET', f'{self.BOOKING_ENDPOINT}?checkin={check_in}&checkout={check_out}')
        return response

    def update_full_booking_data(self, booking_id: int, booking_data: dict):
        response = self.send_request(
            'PUT',
            f'{self.BOOKING_ENDPOINT}/{booking_id}',
            json=booking_data
        )
        return response

    def update_partial_booking_data(self, booking_id: int, booking_data: dict):
        response = self.send_request(
            'PATCH',
            f'{self.BOOKING_ENDPOINT}/{booking_id}',
            json=booking_data)
        return response

    def delete_booking_by_id(self, booking_id: int):
        response = self.send_request(
            'DELETE',
            f'{self.BOOKING_ENDPOINT}/{booking_id}',
            expected_status_code=201
        )
        return response
