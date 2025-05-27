from src.api.booking_client import BookingApiClient
from src.data_models.booking_data import BookingDataModel, BookingDataResponse
from src.utils.data_validator import validate_response


class BookingScenarios:
    def __init__(self, booking_api_client: BookingApiClient):
        self.booking_api_client = booking_api_client

    def create_booking(self, booking_data: BookingDataModel):
        response = self.booking_api_client.create_booking(booking_data.model_dump())
        response_model = validate_response(response, BookingDataResponse)

        verify_response = self.booking_api_client.get_booking_by_id(response_model.bookingid)
        verify_response_model = validate_response(
            verify_response,
            BookingDataModel,
            expected_data=booking_data.model_dump()
        )

        # TODO assert to validate if creation response equals to sent data

        assert response_model.booking.model_dump(exclude_unset=True) == verify_response_model.model_dump(exclude_unset=True), \
            (f'Generated data not equals to data received from GET request by ID: '
             f'generated - {response_model.booking.model_dump(exclude_unset=True)}, '
             f'got - {verify_response_model.model_dump(exclude_unset=True)}')
        return response_model
