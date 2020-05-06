from .base_endpoint import BaseEndpoint
from src.decorators import verify_api_method_exists


class PriceFeedEndpoint(BaseEndpoint):
    def __init__(self, version='v1', sandbox=False):
        """
        Initializes the PriceFeedEndpoint class.
        :param str version: the api version to use
        :param bool sandbox: True if using the sandbox api, False otherwise
        """
        super().__init__(version, sandbox)

    @verify_api_method_exists('v1')
    def get_endpoint(self):
        if self.sandbox:
            url = self.base_sandbox_url
        else:
            url = self.base_url
        return "{0}/{1}/pricefeed".format(url, self.version)
