from json.decoder import JSONDecodeError
import falcon
from marshmallow import ValidationError
from app.resources.image import ImageResource
from app.errorhandlers.base_exception import handle_base_exception
from app.errorhandlers.http_error import handle_http_error
from app.errorhandlers.json_decode_error import handle_json_decode_error
from app.errorhandlers.validation_error import handle_validation_error
from app.middleware.csp_component import ContentSecurityPolicyComponent


APP = falcon.API(middleware=ContentSecurityPolicyComponent())

APP.add_route('/api/image', ImageResource())

APP.add_error_handler(BaseException, handle_base_exception)
APP.add_error_handler(falcon.HTTPError, handle_http_error)
APP.add_error_handler(JSONDecodeError, handle_json_decode_error)
APP.add_error_handler(ValidationError, handle_validation_error)
