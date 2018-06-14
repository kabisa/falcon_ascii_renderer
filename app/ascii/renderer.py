
ASCII_CHARS = "MNHQ$OC?7>!:-;. "
NUM_ASCII_CHARS = len(ASCII_CHARS)


def render_frame(frame):
    pixels = frame.load()
    width, height = frame.width, frame.height

    string = ""
    for row in range(height):
        for col in range(width):
            pixel = pixels[col, row]  # RGB
            rgb = pixel[:3]
            avg_rgb = sum(rgb) / 3.0
            string += ASCII_CHARS[int(avg_rgb / 256.0 * NUM_ASCII_CHARS)]

        string += "\n"
    return string


def render_ascii_art(image):
    while True:
        try:
            yield render_frame(image.convert("RGB"))
            image.seek(image.tell() + 1)
        except EOFError:
            break
