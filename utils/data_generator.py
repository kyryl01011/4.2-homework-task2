from faker import Faker

fake = Faker()

class GenerateData:

    @staticmethod
    def generate_first_name():
        return fake.first_name()

    @staticmethod
    def generate_last_name():
        return fake.last_name()

    @staticmethod
    def generate_random_int(start, end):
        return fake.random_int(start, end)

    @staticmethod
    def generate_random_data():
        return f'{fake.year()}-0{fake.random_int(0,9)}-0{fake.random_int(0, 9)}'

