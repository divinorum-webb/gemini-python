from .base_endpoint import BaseEndpoint
from src.decorators import verify_api_method_exists


class TickerEndpoint(BaseEndpoint):
    def __init__(self, symbol, version='v1', sandbox=False):
        """
        Initializes the TickerEndpoint class.
        :param str symbol: the crypto symbol being queried
        :param str version: the api version to use
        :param bool sandbox: True if using the sandbox api, False otherwise
        """
        super().__init__(version, sandbox)
        self._symbol = symbol

    @property
    def symbol(self):
        return self._symbol

    @property
    def url_component(self):
        url_components = {
            "v1": "pubticker",
            "v2": "ticker"
        }
        return url_components[self.version]

    @verify_api_method_exists('v1')
    def get_endpoint(self):
        if self.sandbox:
            url = self.base_sandbox_url
        else:
            url = self.base_url
        return "{0}/{1}/{2}/{3}".format(url, self.version, self.url_component, self.symbol)
