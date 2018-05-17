import logging
import traceback
import falcon


LOGGER = logging.getLogger(__name__)
logging.basicConfig(
    format='[%(asctime)s] [%(process)d] [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %I:%M:%S %z'
)


def handle_base_exception(exception, *_):
    stack_trace = traceback.format_exception(None, exception, exception.__traceback__)
    LOGGER.error("Internal server error: %s", exception)
    for line in stack_trace:
        LOGGER.error(line.rstrip('\n'))
    raise falcon.HTTPInternalServerError("Internal server error")
