from pydantic import BaseModel
from src.utils.data_generator import GenerateData


class BookingDatesModel(BaseModel):
    checkin: str
    checkout: str


class BookingDataModel(BaseModel):
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    bookingdates: BookingDatesModel
    additionalneeds: str


class BookingDataResponse(BaseModel):
    bookingid: int
    booking: BookingDataModel


class BookingData:

    @staticmethod
    def create_booking_data() -> BookingDataModel:
        return BookingDataModel(
            firstname=GenerateData.generate_first_name(),
            lastname=GenerateData.generate_last_name(),
            totalprice=GenerateData.generate_random_int(100, 10000),
            depositpaid=True,
            bookingdates=BookingDatesModel(
                checkin=GenerateData.generate_random_checkin_date(),
                checkout=GenerateData.generate_random_checkout_date()
            ),
            additionalneeds=GenerateData.generate_first_name()
        )
