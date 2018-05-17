import base64
import pytest


@pytest.fixture
def gradient_ascii():
    with open('tests/resources/images/gradient.txt', 'rb') as file:
        return file.read()


@pytest.fixture
def gradient_png():
    with open('tests/resources/images/gradient.png', 'rb') as file:
        return file.read()


@pytest.fixture
def bird_jpg():
    with open('tests/resources/images/bird.jpg', 'rb') as file:
        return file.read()


@pytest.fixture
def valid_request(gradient_png):  # pylint:disable=W0621
    file_as_bytes = base64.b64encode(gradient_png)
    return {
        "image": file_as_bytes.decode()
    }


@pytest.fixture
def request_with_bad_mode(bird_jpg):  # pylint:disable=W0621
    file_as_bytes = base64.b64encode(bird_jpg)
    return {
        "image": file_as_bytes.decode()
    }
