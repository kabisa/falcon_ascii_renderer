import logging
import falcon


LOGGER = logging.getLogger(__name__)
logging.basicConfig(
    format='[%(asctime)s] [%(process)d] [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %I:%M:%S %z'
)


def handle_base_exception(exception, *_):
    LOGGER.error("Internal server error: %s", exception)
    raise falcon.HTTPInternalServerError("Internal server error")
