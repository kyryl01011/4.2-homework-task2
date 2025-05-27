from custom_requester.custom_requester import CustomRequester


class BookingApiClient(CustomRequester):
    BOOKING_ENDPOINT = '/booking'

    def create_booking(self, booking_data: dict):
        response = self.send_request('POST', self.BOOKING_ENDPOINT, json=booking_data)
        return response

    def get_booking_by_id(self, booking_id: int):
        response = self.send_request('GET', f'{self.BOOKING_ENDPOINT}/{booking_id}')
        return response

    def get_booking_by_full_name(self, first_name: str, last_name: str):
        response = self.send_request('GET', self.get_full_url(self.BOOKING_ENDPOINT))
        return response

    def get_booking_by_check_dates(self, check_dates: dict):
        response = self.send_request('GET', self.get_full_url(self.BOOKING_ENDPOINT))
        return response

    def update_full_booking_data(self, booking_id: str, booking_data: dict):
        response = self.send_request('PUT', self.get_full_url(self.BOOKING_ENDPOINT + booking_id), json=booking_data)
        return response

    def update_partial_booking_data(self, booking_id: str, booking_data: dict):
        response = self.send_request('PATCH', self.get_full_url(self.BOOKING_ENDPOINT + booking_id), json=booking_data)
        return response

    def delete_booking_by_id(self, booking_id: str):
        response = self.send_request('DELETE', self.get_full_url(self.BOOKING_ENDPOINT + booking_id))
        return response
