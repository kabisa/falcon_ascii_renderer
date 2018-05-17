import falcon


def handle_json_decode_error(*_):
    raise falcon.HTTPBadRequest("Invalid JSON")
