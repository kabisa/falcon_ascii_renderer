import json
import pytest
import falcon
from falcon import testing
from app.app import APP


# pylint: disable=C0103, R0903, W0621, no-self-use

API_URL = '/api/image'


@pytest.fixture
def client():
    return testing.TestClient(APP)


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

    def test_rejects_request_with_non_rgb_based_image(self, client, request_with_bad_mode):
        request = request_with_bad_mode
        response = client.simulate_post(API_URL, body=json.dumps(request))

        assert response.status == falcon.HTTP_BAD_REQUEST
        assert response.json == {
            "title": "Validation error",
            "description": {
                "image": [
                    "Only RGB and RGBA images are supported."
                ]
            }
        }


class TestImage:
    def test_returns_ascii(self, client, valid_request, gradient_ascii):
        response = client.simulate_post(API_URL, body=json.dumps(valid_request))
        assert response.json.encode('utf8') == gradient_ascii
