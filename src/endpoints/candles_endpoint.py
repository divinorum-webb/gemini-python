from .base_endpoint import BaseEndpoint
from src.decorators import verify_api_method_exists


class CandlesEndpoint(BaseEndpoint):
    def __init__(self, symbol, time_frame, version='v2', sandbox=False):
        """
        Initializes the CandlesEndpoint class.
        :param str symbol: the crypto symbol being queried
        :param str time_frame:
        :param str version: the api version to use
        :param bool sandbox: True if using the sandbox api, False by default
        """
        super().__init__(version, sandbox)
        self._symbol = symbol
        self._time_frame = time_frame

    @property
    def symbol(self):
        self._validate_symbol()
        return self._symbol

    @property
    def valid_symbols(self):
        return ['btcusd', 'ethbtc', 'ethusd', 'zecusd', 'zecbtc', 'zeceth', 'zecbch', 'zecltc', 'bchusd', 'bchbtc',
                'bcheth', 'ltcusd', 'ltcbtc', 'ltceth', 'ltcbch', 'batusd', 'daiusd', 'linkusd', 'oxtbtc', 'bateth',
                'daieth', 'linketh', 'oxteth']

    @property
    def time_frame(self):
        self._validate_time_frame()
        return self._time_frame

    @property
    def valid_time_frames(self):
        return [
            '1m',
            '5m',
            '15m',
            '30m',
            '1hr',
            '6hr',
            '1day'
        ]

    def _validate_symbol(self):
        if self._symbol not in self.valid_symbols:
            raise ValueError(f"An invalid symbol was passed to {self.__class__.__name__}: '{self._symbol}'")

    def _validate_time_frame(self):
        if self._time_frame not in self.valid_time_frames:
            raise ValueError(f"An invalid time frame was passed to {self.__class__.__name__}: '{self._time_frame}'")

    @verify_api_method_exists('v2')
    def get_endpoint(self):
        if self.sandbox:
            url = self.base_sandbox_url
        else:
            url = self.base_url
        return "{0}/{1}/candles/{2}/{3}".format(url, self.version, self.symbol, self.time_frame)
