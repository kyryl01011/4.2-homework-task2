from enum import Enum
from src.utils.env_grabber import USERNAME, PASSWORD

class BaseRequestAttributes(Enum):
    URL = 'https://restful-booker.herokuapp.com'
    HEADERS = {"Content-Type": "application/json", "Accept": "application/json"}
    ADMIN_CREDS = {"username": USERNAME, "password": PASSWORD}
