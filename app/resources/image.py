import base64
import io
import json
from marshmallow import fields, Schema, ValidationError
from PIL import Image


class ImageField(fields.Field):
    def _deserialize(self, value, attr, data):
        try:
            image_bytes = base64.decodebytes(value.encode())
            return Image.open(io.BytesIO(image_bytes))
        except:  # noqa: E722
            raise ValidationError("Image not valid.")


class ImageRequestSchema(Schema):
    image = ImageField(required=True)


class ImageResource:  # pylint: disable=too-few-public-methods
    def on_post(self, req, resp):  # pylint: disable=no-self-use
        schema = ImageRequestSchema(strict=True)
        request = schema.loads(req.bounded_stream.read())

        resp.body = json.dumps(request.data["image"].mode)