from enum import Enum


class BaseRequestAttributes(Enum):
    URL = 'https://restful-booker.herokuapp.com'
    HEADERS = {"Content-Type": "application/json", "Accept": "application/json"}
    ADMIN_CREDS = {"username": "admin", "password": "password123"}
