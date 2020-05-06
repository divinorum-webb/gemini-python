from .base_endpoint import BaseEndpoint
from src.decorators import verify_api_method_exists


class TradeHistoryEndpoint(BaseEndpoint):
    def __init__(self, symbol, version='v1', sandbox=False, timestamp=None, limit_trades=None, include_breaks=None):
        """
        Initializes the CurrentOrderBookEndpoint class.
        :param str symbol: the crypto symbol being queried
        :param str version: the api version to use
        :param bool sandbox: True if using the sandbox api, False by default
        :param int timestamp: (optional) only trades occurring after this timestamp will be returned
        :param int limit_trades: (optional) sets the maximum number of trades to return; defaults to 50
        :param bool include_breaks: (optional) True if displaying broken trades; False otherwise
        """
        super().__init__(version, sandbox)
        self._symbol = symbol
        self._timestamp = timestamp
        self._limit_trades = limit_trades
        self._include_breaks = str(int(include_breaks)) if isinstance(include_breaks, bool) else "0"
        self._parameter_dict = self.parameter_dict

    @property
    def symbol(self):
        return self._symbol

    @property
    def url_param_keys(self):
        return ['timestamp', 'limit_trades', 'include_breaks']

    @property
    def url_param_values(self):
        return [f"timestamp={str(self._timestamp)}" if self._timestamp else None,
                f"limit_trades={str(self._limit_trades)}" if self._limit_trades else None,
                f"include_breaks={self._include_breaks}" if self._include_breaks else None]

    @property
    def parameter_dict(self):
        self._parameter_dict.update(self._get_parameter_dict(self.url_param_keys, self.url_param_values))
        return self._parameter_dict

    @verify_api_method_exists('v1')
    def get_endpoint(self):
        if self.sandbox:
            url = self.base_sandbox_url
        else:
            url = self.base_url
        url = "{0}/{1}/trades/{2}".format(url, self.version, self.symbol)
        return self._append_url_parameters(url)
