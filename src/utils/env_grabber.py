import os

from dotenv import load_dotenv

load_dotenv()

def get_value_from_env(key):
    return os.environ.get(key)

USERNAME=get_value_from_env('TEST_USERNAME')
PASSWORD=get_value_from_env('TEST_PASSWORD')