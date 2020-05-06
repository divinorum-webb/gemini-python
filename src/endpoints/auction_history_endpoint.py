from .base_endpoint import BaseEndpoint
from src.decorators import verify_api_method_exists


class AuctionHistoryEndpoint(BaseEndpoint):
    def __init__(self,
                 symbol,
                 version='v1',
                 sandbox=False,
                 since=None,
                 limit_auction_results=None,
                 include_indicative=True):
        """
        Initializes the CurrentOrderBookEndpoint class.
        :param str symbol: the crypto symbol being queried
        :param str version: the api version to use
        :param bool sandbox: True if using the sandbox api, False by default
        :param since: (optional) if specified, only events occurring after this timestamp will be included
        :param limit_auction_results: (optional) sets the maximum number of auction events to return; default is 50
        :param include_indicative: (optional) True by default, includes publication of indicative prices and quantities
        """
        super().__init__(version, sandbox)
        self._symbol = symbol
        self._since = since
        self._limit_auction_results = limit_auction_results
        self._include_indicative = include_indicative
        self._parameter_dict = self.parameter_dict

    @property
    def symbol(self):
        return self._symbol

    @property
    def parameter_dict(self):
        if self._since:
            self._parameter_dict['since'] = 'since=' + str(self._since)
        if self._limit_auction_results:
            self._parameter_dict['limit_auction_results'] = 'limit_auction_results=' + str(self._limit_auction_results)
        if isinstance(self._include_indicative, bool):
            self._parameter_dict['include_indicative'] = 'include_indicative=' + str(int(self._include_indicative))
        return self._parameter_dict

    @verify_api_method_exists('v1')
    def get_endpoint(self):
        if self.sandbox:
            url = self.base_sandbox_url
        else:
            url = self.base_url
        url = "{0}/{1}/auction/{2}/history".format(url, self.version, self.symbol)
        return self._append_url_parameters(url)
