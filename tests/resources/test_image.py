import base64
import json
import os
import pytest
import falcon
from falcon import testing
from app.app import APP


# pylint: disable=C0103, R0903, W0621, no-self-use

API_URL = '/api/image'


def _base64_encode_file(file_name):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images')
    file = open(f'{path}/{file_name}.png', "rb")
    file_as_bytes = base64.b64encode(file.read())
    return file_as_bytes.decode()


@pytest.fixture
def client():
    return testing.TestClient(APP)


@pytest.fixture
def valid_request():
    return {
        "image": _base64_encode_file('gradient')
    }


class TestValidation:
    def test_accepts_valid_request(self, client, valid_request):
        response = client.simulate_post(API_URL, body=json.dumps(valid_request))

        assert response.status == falcon.HTTP_OK

    def test_rejects_request_without_request_body(self, client):
        response = client.simulate_post(API_URL)

        assert response.status == falcon.HTTP_BAD_REQUEST
        assert response.json == {
            "title": "Invalid JSON"
        }

    def test_rejects_request_without_encoded_image(self, client, valid_request):
        request = valid_request
        del request["image"]
        response = client.simulate_post(API_URL, body=json.dumps(request))

        assert response.status == falcon.HTTP_BAD_REQUEST
        assert response.json == {
            "title": "Validation error",
            "description": {
                "image": [
                    "Missing data for required field."
                ]
            }
        }

    def test_rejects_request_with_invalid_image(self, client, valid_request):
        request = valid_request
        request["image"] = "nonsense"
        response = client.simulate_post(API_URL, body=json.dumps(request))

        assert response.status == falcon.HTTP_BAD_REQUEST
        assert response.json == {
            "title": "Validation error",
            "description": {
                "image": [
                    "Image not valid."
                ]
            }
        }


class TestImage:
    def test_returns_image_mode(self, client, valid_request):
        response = client.simulate_post(API_URL, body=json.dumps(valid_request))

        assert response.json == "RGB"
