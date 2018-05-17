
import io
from PIL import Image
from app.ascii.renderer import render_ascii_art


def test_rendering_ascii(gradient_png, gradient_ascii):
    image = Image.open(io.BytesIO(gradient_png))
    generated_ascii = render_ascii_art(image).encode('utf8')
    assert generated_ascii == gradient_ascii
