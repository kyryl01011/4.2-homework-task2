import pytest
from pydantic import BaseModel, ValidationError
from requests import Response
from typing import Type


def validate_response(
        response: Response,
        model: Type[BaseModel],
        expected_status: int = 200,
        expected_data: dict | None = None
) -> BaseModel:
    """
    Universal API response validator
    - Validates status code
    - Validates Model Schema
    - Comparison with expected result (optional)

    :param expected_status: expected status code of response
    :param response: response of request
    :param model: Data model to compare
    :param expected_data: Optional
    :return: Pydantic object of response data
    """
    if response.status_code != expected_status:
        pytest.fail(f'Expected status: {expected_status}, got {response.status_code}')

    try:
        response_data: dict = response.json()
    except Exception as e:
        pytest.fail(f'JSON parsing error: {e}'
                    f'\nResponse: {response.text}')

    if isinstance(response_data, list):
        models_list = []
        for el in response_data:
            parsed_data = parse_dict_to_model(model, el)
            models_list.append(parsed_data)
            if expected_data:
                compare_curr_data_and_expected(model, parsed_data, expected_data)
        return models_list

    parsed_data = parse_dict_to_model(model, response_data)
    if expected_data:
        compare_curr_data_and_expected(model, parsed_data, expected_data)

    return parsed_data


def parse_dict_to_model(model, el):
    try:
        parsed_data = model(**el)
    except ValidationError as e:
        pytest.fail(f'JSON Validation error:\n{e}')
    return parsed_data


def compare_curr_data_and_expected(model, parsed_data, expected_data):
    expected_model = model(**expected_data)
    if expected_model.model_dump(exclude_unset=True) != parsed_data.model_dump(exclude_unset=True):
        pytest.fail(f'Received data model not equals to expected:'
                    f'\nGot: {parsed_data.model_dump(exclude_unset=True)}'
                    f'\nExpected: {expected_model.model_dump(exclude_unset=True)}')
