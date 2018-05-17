import falcon


def handle_validation_error(exception, *_):
    raise falcon.HTTPBadRequest("Validation error", exception.messages)
