from .base_endpoint import BaseEndpoint
from src.decorators import verify_api_method_exists


class CurrentOrderBookEndpoint(BaseEndpoint):
    def __init__(self, symbol, version='v1', sandbox=False, limit_bids=None, limit_asks=None):
        """
        Initializes the CurrentOrderBookEndpoint class.
        :param str symbol: the crypto symbol being queried
        :param str version: the api version to use
        :param bool sandbox: True if using the sandbox api, False by default
        :param int limit_bids: (optional) limits the number of bid price (offers to buy) levels returned
        :param int limit_asks: (optional) limits the number of ask price (offers to sell) levels returned
        """
        super().__init__(version, sandbox)
        self._symbol = symbol
        self._limit_bids = limit_bids
        self._limit_asks = limit_asks
        self._parameter_dict = self.parameter_dict

    @property
    def symbol(self):
        return self._symbol

    @property
    def parameter_dict(self):
        if self._limit_bids:
            self._parameter_dict['limit_bids'] = 'limit_bids=' + str(self._limit_bids)
        if self._limit_asks:
            self._parameter_dict['limit_asks'] = 'limit_asks=' + str(self._limit_asks)
        return self._parameter_dict

    @verify_api_method_exists('v1')
    def get_endpoint(self):
        if self.sandbox:
            url = self.base_sandbox_url
        else:
            url = self.base_url
        url = "{0}/{1}/book/{2}".format(url, self.version, self.symbol)
        return self._append_url_parameters(url)
