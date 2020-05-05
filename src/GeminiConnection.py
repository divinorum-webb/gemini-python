import requests

from .headers import BaseHeaders
from .payloads import BasePayload
from .endpoints import SymbolsEndpoint, TickerEndpoint, CandlesEndpoint


class GeminiConnection:
    def __init__(self, config):
        self._api_key = config['api_key']
        self._api_secret = config['api_secret']
        self.active_endpoint = None
        self.active_headers = None
        self.active_payload = None

    # define public api methods

    def get_symbols(self, version='v1', sandbox=False) -> requests.models.Response:
        """
        Get a list of all available crypto symbols on the Gemini Exchange.
        :param str version: the api version to use
        :param bool sandbox: True if using the sandbox api, False by default
        :return: HTTP response
        """
        self.active_endpoint = SymbolsEndpoint(version=version, sandbox=sandbox).get_endpoint()
        response = requests.get(self.active_endpoint)
        return response

    def get_ticker(self, symbol, version='v1', sandbox=False) -> requests.models.Response:
        """
        Get information about recent trading activity for the specified symbol.
        :param str symbol: the crypto symbol being queried
        :param str version: the api version to use
        :param bool sandbox: True if using the sandbox api, False by default
        :return: HTTP response
        """
        self.active_endpoint = TickerEndpoint(symbol=symbol, version=version, sandbox=sandbox).get_endpoint()
        response = requests.get(self.active_endpoint)
        return response

    def get_candles(self, symbol, time_frame, version='v2', sandbox=False):
        """
        Get time-intervaled data for the specified symbol.
        :param str symbol: the crypto symbol being queried
        :param str time_frame: the time range for each candle
        :param str version: the api version to use
        :param bool sandbox: True if using the sandbox api, False by default
        :return: HTTP response
        """
        self.active_endpoint = CandlesEndpoint(symbol=symbol,
                                               time_frame=time_frame,
                                               version=version,
                                               sandbox=sandbox).get_endpoint()
        response = requests.get(self.active_endpoint)
        return response

    def get_current_order_book(self):
        pass

    def get_trade_history(self):
        pass

    def get_current_action(self):
        pass

    def get_auction_history(self):
        pass

    def get_price_feed(self):
        pass

    # define order placement api methods

    def new_order(self):
        pass

    def cancel_order(self):
        pass

    def cancel_all_session_orders(self):
        pass

    def cancel_all_active_orders(self):
        pass

    # define order status api methods

    def order_status(self):
        pass

    def get_active_orders(self):
        pass

    def get_past_trades(self):
        pass

    # define fee and volume api methods

    def get_notional_volume(self):
        pass

    def get_trade_volume(self):
        pass

    # define gemini clearing api methods

    def new_clearing_order(self):
        pass

    def new_broker_order(self):
        pass

    def clearing_order_status(self):
        pass

    def cancel_clearing_order(self):
        pass

    def confirm_clearing_order(self):
        pass

    # define fund management api methods

    def get_available_balances(self):
        pass

    def get_notional_balances(self):
        pass

    def transfers(self):
        pass

    def get_deposit_addresses(self):
        pass

    def new_deposit_addresses(self):
        pass

    def withdraw_crypto_funds_to_whitelisted_address(self):
        pass

    def internal_transfers(self):
        pass

    # define account administration api methods

    def create_account(self):
        pass

    def get_accounts_in_master_group(self):
        pass

    # define gemini dollar api methods

    def withdraw_usd_as_gusd(self):
        pass

    # define session api methods

    def heartbeat(self):
        pass
