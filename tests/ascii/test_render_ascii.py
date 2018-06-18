
import io
from PIL import Image
from app.ascii.renderer import render_ascii_art, render_frame


def test_rendering_ascii_frame(gradient_png, gradient_ascii):
    image = Image.open(io.BytesIO(gradient_png))
    generated_ascii = render_frame(image, image.width, image.height).encode("utf8")
    assert generated_ascii == gradient_ascii


def test_rendering_animated_gif(animated_gif):
    image = Image.open(io.BytesIO(animated_gif))
    generated_ascii = list(render_ascii_art(image, 100, 100))
    assert len(generated_ascii) == 5
