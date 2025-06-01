class TestBooking:

    def test_general(self, scenarios, booking_data):
        test_data = booking_data()
        scenarios.create_and_delete_booking(test_data)

    def test_successful_booking_creation(self, scenarios, booking_data):
        test_data = booking_data()
        scenarios.create_booking(test_data)

    def test_search_id_by_full_name(self, scenarios, booking_data):
        test_data = booking_data()
        created_booking_response_model = scenarios.create_booking(test_data)
        scenarios.get_booking_id_by_full_name(
            created_booking_response_model.booking.firstname,
            created_booking_response_model.booking.lastname)

    def test_search_id_by_check_dates(self, scenarios, booking_data):
        test_data = booking_data()
        created_booking_response_model = scenarios.create_booking(test_data)
        scenarios.get_booking_id_by_check_dates(
            created_booking_response_model.booking.bookingdates.checkin,
            created_booking_response_model.booking.bookingdates.checkout)

    def test_search_booking_data_by_id(self, scenarios, booking_data):
        test_data = booking_data()
        created_booking_model = scenarios.create_booking(test_data)
        scenarios.get_booking_by_id(created_booking_model.bookingid)

    def test_full_booking_update(self, scenarios, booking_data):
        initial_booking_data_model = booking_data()
        new_booking_data_model = booking_data()
        scenarios.full_booking_update(initial_booking_data_model, new_booking_data_model)

    def test_partial_booking_update(self, scenarios, booking_data):
        initial_booking_data_model = booking_data()
        new_booking_data_model = booking_data()
        scenarios.partial_booking_update(initial_booking_data_model, new_booking_data_model)
