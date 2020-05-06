from .base_endpoint import BaseEndpoint
from src.decorators import verify_api_method_exists


class GenericEndpoint(BaseEndpoint):
    def __init__(self, endpoint_text, version='v1', sandbox=False):
        """
        Initializes the GenericEndpoint class.
        :param str endpoint_text: the tail end of the endpoint url to append to the base url
        :param str version: the api version to use
        :param bool sandbox: True if using the sandbox api, False otherwise
        """
        super().__init__(version, sandbox)
        self._endpoint_text = endpoint_text

    @verify_api_method_exists('v1')
    def get_endpoint(self):
        if self.sandbox:
            url = self.base_sandbox_url
        else:
            url = self.base_url
        return "{0}/{1}/{2}".format(url, self.version, self._endpoint_text)
