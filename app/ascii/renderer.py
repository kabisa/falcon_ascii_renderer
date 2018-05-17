
ASCII_CHARS = "MNHQ$OC?7>!:-;. "
NUM_ASCII_CHARS = len(ASCII_CHARS)


def render_ascii_art(image):
    pixels = image.load()
    width, height = image.width, image.height

    string = ""
    for row in range(height):
        for col in range(width):
            pixel = pixels[col, row]  # RGB
            avg_pixel = sum(pixel) / 3.0
            string += ASCII_CHARS[int(avg_pixel / 256.0 * NUM_ASCII_CHARS)]

        string += "\n"
    return string
