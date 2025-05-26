from custom_requester.custom_requester import CustomRequester


class BookingApiClient(CustomRequester):

    def create_booking(self, endpoint: str, booking_data: dict):
        response = self.send_request('POST', self.get_full_url(endpoint), json=booking_data)
        if response.status_code not in (200, 201):
            response.raise_for_status()
        return response

    def get_booking_by_id(self, endpoint: str, booking_id: str):
        response = self.send_request('GET', self.get_full_url(endpoint))
        if response.status_code not in (200, 201):
            response.raise_for_status()
        return response

    def get_booking_by_full_name(self, endpoint: str):
        response = self.send_request('GET', self.get_full_url(endpoint))
        if response.status_code not in (200, 201):
            response.raise_for_status()
        return response

    def get_booking_by_check_dates(self, endpoint: str):
        response = self.send_request('GET', self.get_full_url(endpoint))
        if response.status_code not in (200, 201):
            response.raise_for_status()
        return response

    def update_full_booking_data(self, endpoint: str, booking_data: dict):
        response = self.send_request('PUT', self.get_full_url(endpoint), json=booking_data)
        if response.status_code not in (200, 201):
            response.raise_for_status()
        return response

    def update_partial_booking_data(self, endpoint: str, booking_data: dict):
        response = self.send_request('PATCH', self.get_full_url(endpoint), json=booking_data)
        if response.status_code not in (200, 201):
            response.raise_for_status()
        return response

    def delete_booking_by_id(self, endpoint: str):
        response = self.send_request('DELETE', endpoint)
        if response.status_code not in (200, 201):
            response.raise_for_status()
        return response
