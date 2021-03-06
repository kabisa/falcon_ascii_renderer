import base64
import io
import json
from marshmallow import fields, Schema, ValidationError
from PIL import Image
from app.ascii.renderer import get_image_duration, render_ascii_art


class ImageField(fields.Field):
    def _deserialize(self, value, attr, data):
        try:
            image_bytes = base64.decodebytes(value.encode())
            image = Image.open(io.BytesIO(image_bytes))
        except:  # noqa: E722
            raise ValidationError("Image not valid.")

        return image


class ImageRequestSchema(Schema):
    image = ImageField(required=True)
    width = fields.Integer(as_string=False)
    height = fields.Integer(as_string=False)


class ImageResource:  # pylint: disable=too-few-public-methods
    def on_post(self, req, resp):  # pylint: disable=no-self-use
        schema = ImageRequestSchema(strict=True)
        request = schema.loads(req.bounded_stream.read())
        data = request.data
        ascii_art = render_ascii_art(data['image'],
                                     data['width'],
                                     data['height'])
        resp.body = json.dumps(
            {"frames": list(ascii_art), "duration": get_image_duration(data["image"])}
        )
