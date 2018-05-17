import json
import falcon
from falcon import testing
import pytest
from app.app import APP


# pylint: disable=C0103, W0621, unused-argument

API_URL = '/api/image'


@pytest.fixture
def exception():
    return Exception("Something terrible has happended")


@pytest.fixture
def exception_raising_schema(mocker, exception):
    mocker.patch("app.resources.image.ImageRequestSchema", side_effect=exception)


@pytest.fixture
def logger_mock(mocker):
    return mocker.patch("app.errorhandlers.base_exception.LOGGER.error")


def test_returns_json_for_internal_server_error(exception_raising_schema):
    response = testing.TestClient(APP).simulate_post(API_URL, body=json.dumps({}))

    assert response.status == falcon.HTTP_INTERNAL_SERVER_ERROR
    assert response.json == {
        "title": "Internal server error"
    }


def test_logs_cause_of_internal_server_error(exception_raising_schema, logger_mock, exception):
    testing.TestClient(APP).simulate_post(API_URL, body=json.dumps({}))

    logger_mock.assert_called_once_with('Internal server error: %s', exception)
