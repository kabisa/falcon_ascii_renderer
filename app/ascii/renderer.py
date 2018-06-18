from PIL import Image

ASCII_CHARS = "MNHQ$OC?7>!:-;. "
NUM_ASCII_CHARS = len(ASCII_CHARS)


def render_frame(frame, width, height):
    scaled_image = frame.resize((width, height), Image.BILINEAR)
    pixels = scaled_image.load()

    string = ""
    for row in range(height):
        for col in range(width):
            pixel = pixels[col, row]  # RGB
            rgb = pixel[:3]
            avg_rgb = sum(rgb) / 3.0
            string += ASCII_CHARS[int(avg_rgb / 256.0 * NUM_ASCII_CHARS)]

        string += "\n"
    return string


def render_ascii_art(image, width, height):
    while True:
        try:
            yield render_frame(image.convert("RGB"), width, height)
            image.seek(image.tell() + 1)
        except EOFError:
            break


def get_image_duration(image):
    return image.info.get("duration", 1000)

