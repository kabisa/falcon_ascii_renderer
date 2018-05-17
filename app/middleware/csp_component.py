class ContentSecurityPolicyComponent:  # pylint: disable=too-few-public-methods
    def process_response(self, req, resp, resource, req_succeeded):  # pylint: disable=no-self-use
        del req, resource, req_succeeded
        resp.set_header("Access-Control-Allow-Origin", "*")
        resp.set_header("Access-Control-Allow-Headers", "Content-Type")
