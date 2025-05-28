from requests import Response

from src.api.booking_client import BookingApiClient
from src.data_models.booking_data import BookingDataModel, BookingDataResponse, BookingIDsModel
from src.utils.data_validator import validate_response
from typing import Type


class BookingScenarios:
    def __init__(self, booking_api_client: BookingApiClient):
        self.booking_api_client = booking_api_client

    def create_booking(self, booking_data: BookingDataModel) -> Type[BookingDataResponse]:
        response = self.booking_api_client.create_booking(booking_data.model_dump())
        response_model = validate_response(response, BookingDataResponse)

        verify_response_model = self.get_booking_by_id(response_model.bookingid, booking_data.model_dump())

        assert response_model.booking.model_dump(exclude_unset=True) == booking_data.model_dump(exclude_unset=True), \
            (f'Sent data not equals to received data: '
             f'\nSent: {booking_data.model_dump(exclude_unset=True)}'
             f'\nReceived: {response_model.booking.model_dump(exclude_unset=True)}')

        assert response_model.booking.model_dump(exclude_unset=True) == verify_response_model.model_dump(
            exclude_unset=True), \
            (f'Generated data not equals to data received from GET request by ID: '
             f'\nGenerated - {response_model.booking.model_dump(exclude_unset=True)}, '
             f'\nGot - {verify_response_model.model_dump(exclude_unset=True)}')
        return response_model

    def get_booking_by_id(
            self,
            booking_id,
            expected_data: dict | None = None,
            expected_status_code=200
    ) -> Type[BookingDataResponse]:
        response = self.booking_api_client.get_booking_by_id(booking_id, expected_status_code=expected_status_code)
        if expected_status_code in (200, 201):
            response_model = validate_response(
                response,
                BookingDataModel,
                expected_data=expected_data
            )
            return response_model
        return response

    def delete_booking_by_id(self, booking_id: int):
        delete_response = self.booking_api_client.delete_booking_by_id(booking_id)

        deleted_booking_response: Response = self.get_booking_by_id(booking_id, expected_status_code=404)

        assert deleted_booking_response.text == 'Not Found', \
            (f'Unexpected response body: '
             f'\nExpected: Not Found'
             f'\nGot: {deleted_booking_response.text}')

    def get_booking_id_by_full_name(self, first_name: str, last_name: str):
        booking_response = self.booking_api_client.get_booking_id_by_full_name(first_name, last_name)
        booking_id = booking_response.json()[0].get('bookingid')

        if booking_id:
            booking_data_model = self.get_booking_by_id(booking_id)

        assert booking_id, f'Booking ID was not found!'
        assert first_name == booking_data_model.firstname, \
            (
                f'Initial firs'
            )
        assert last_name == booking_data_model.lastname