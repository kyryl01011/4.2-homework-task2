from pydantic import BaseModel
from src.utils.data_generator import DataGenerator


class BookingIDsModel(BaseModel):
    bookingid: int


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
            firstname=DataGenerator.generate_first_name(),
            lastname=DataGenerator.generate_last_name(),
            totalprice=DataGenerator.generate_random_int(100, 10000),
            depositpaid=True,
            bookingdates=BookingDatesModel(
                checkin=DataGenerator.generate_random_checkin_date(),
                checkout=DataGenerator.generate_random_checkout_date()
            ),
            additionalneeds=DataGenerator.generate_first_name()
        )
