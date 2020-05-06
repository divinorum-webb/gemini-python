import requests

from .headers import BaseHeaders
from .payloads import NewOrderPayload, CancelOrderPayload
from .endpoints import TickerEndpoint, CandlesEndpoint, CurrentOrderBookEndpoint, TradeHistoryEndpoint, \
    CurrentAuctionEndpoint, AuctionHistoryEndpoint, GenericEndpoint


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
        self.active_endpoint = GenericEndpoint('symbols', version=version, sandbox=sandbox).get_endpoint()
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

    def get_candles(self, symbol, time_frame, version='v2', sandbox=False) -> requests.models.Response:
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

    def get_current_order_book(self,
                               symbol,
                               version='v1',
                               sandbox=False,
                               limit_bids=None,
                               limit_asks=None) -> requests.models.Response:
        """
        Get the current order book as two arrays (bids / asks).
        :param str symbol: the crypto symbol being queried
        :param str version: the api version to use
        :param bool sandbox: True if using the sandbox api, False by default
        :param int limit_bids: (optional) limits the number of bid price (offers to buy) levels returned
        :param int limit_asks: (optional) limits the number of ask price (offers to sell) levels returned
        :return: HTTP response
        """
        self.active_endpoint = CurrentOrderBookEndpoint(symbol,
                                                        version=version,
                                                        sandbox=sandbox,
                                                        limit_bids=limit_bids,
                                                        limit_asks=limit_asks).get_endpoint()
        response = requests.get(self.active_endpoint)
        return response

    def get_trade_history(self,
                          symbol,
                          version='v1',
                          sandbox=False,
                          timestamp=None,
                          limit_trades=None,
                          include_breaks=False) -> requests.models.Response:
        """
        Get the trades that have executed since the specified timestamp. Timestamps are in milliseconds.
        :param str symbol: the crypto symbol being queried
        :param str version: the api version to use
        :param bool sandbox: True if using the sandbox api, False by default
        :param int timestamp: (optional) only trades occurring after this timestamp will be returned
        :param int limit_trades: (optional) sets the maximum number of trades to return; defaults to 50
        :param bool include_breaks: (optional) True if displaying broken trades; False otherwise
        :return: HTTP response
        """
        self.active_endpoint = TradeHistoryEndpoint(symbol=symbol,
                                                    version=version,
                                                    sandbox=sandbox,
                                                    timestamp=timestamp,
                                                    limit_trades=limit_trades,
                                                    include_breaks=include_breaks).get_endpoint()
        response = requests.get(self.active_endpoint)
        return response

    def get_current_action(self, symbol, version='v1', sandbox=False) -> requests.models.Response:
        """
        Get current auction details.
        :param str symbol: the crypto symbol being queried
        :param str version: the api version to use
        :param bool sandbox: True if using the sandbox api, False by default
        :return: HTTP response
        """
        self.active_endpoint = CurrentAuctionEndpoint(symbol=symbol, version=version, sandbox=sandbox).get_endpoint()
        response = requests.get(self.active_endpoint)
        return response

    def get_auction_history(self,
                            symbol,
                            version='v1',
                            sandbox=False,
                            since=None,
                            limit_auction_results=None,
                            include_indicative=True) -> requests.models.Response:
        """
        Get historical auction events, optionally including publications of indicative prices, after the 'since' time.
        :param str symbol: the crypto symbol being queried
        :param str version: the api version to use
        :param bool sandbox: True if using the sandbox api, False by default
        :param since: (optional) if specified, only events occurring after this timestamp will be included
        :param limit_auction_results: (optional) sets the maximum number of auction events to return; default is 50
        :param include_indicative: (optional) True by default, includes publication of indicative prices and quantities
        :return: HTTP response
        """
        self.active_endpoint = AuctionHistoryEndpoint(symbol=symbol,
                                                      version=version,
                                                      sandbox=sandbox,
                                                      since=since,
                                                      limit_auction_results=limit_auction_results,
                                                      include_indicative=include_indicative).get_endpoint()
        response = requests.get(self.active_endpoint)
        return response

    def get_price_feed(self, version='v1', sandbox='False') -> requests.models.Response:
        """
        Get price feed details, comparing prices for currency pairs.
        :param str version: the api version to use
        :param bool sandbox: True if using the sandbox api, False by default
        :return: HTTP response
        """
        self.active_endpoint = GenericEndpoint('pricefeed', version=version, sandbox=sandbox).get_endpoint()
        response = requests.get(self.active_endpoint)
        return response

    # define order placement api methods

    def new_order(self,
                  symbol,
                  amount,
                  price,
                  side,
                  version='v1',
                  sandbox='False',
                  client_order_id=None,
                  order_type='exchange limit',
                  options=None,
                  min_amount=None,
                  stop_price=None,
                  account=None) -> requests.models.Response:
        """
        Places new orders on Gemini Exchange.
        :param str symbol: the currency symbol for the new order
        :param str amount: the quoted decimal amount to purchase
        :param str price: the quoted decimal amount to spend per unit
        :param str side: 'buy' or 'sell'
        :param str version: the api version to use
        :param bool sandbox: True if using the sandbox api, False by default
        :param str client_order_id: (recommended) a unique order id defined by the user
        :param str order_type: the order type; 'exchange stop limit' for stop-limit orders, 'exchange limit' otherwise
        :param list options: (optional) a list containing at most one supported order execution option
        :param str min_amount: (optional) minimum decimal amount to purchase, for block trades only
        :param str stop_price: (optional) the price to trigger a stop-limit order; only available for stop-limit orders
        :param str account: (optional) required for Master API keys; the name of the account in the sub-account group
        :return: HTTP response
        """
        self.active_payload = NewOrderPayload(client_order_id=client_order_id,
                                              symbol=symbol,
                                              amount=amount,
                                              price=price,
                                              side=side,
                                              version=version,
                                              order_type=order_type,
                                              min_amount=min_amount,
                                              options=options,
                                              stop_price=stop_price,
                                              account=account).get_payload()
        self.active_headers = BaseHeaders(self._api_key, self._api_secret, self.active_payload).get_headers()
        self.active_endpoint = GenericEndpoint('order/new', version=version, sandbox=sandbox).get_endpoint()
        response = requests.post(url=self.active_endpoint, headers=self.active_headers)
        return response

    def cancel_order(self,
                     order_id,
                     account=None,
                     version='v1',
                     sandbox=False) -> requests.models.Response:
        """
        Cancels the order whose 'order_id' is specified.
        :param str order_id: the order's unique identifier
        :param str account: (optional) required for Master API keys; the name of the account in the sub-account group
        :param str version: the api version to use
        :param bool sandbox: True if using the sandbox api, False by default
        :return: HTTP response
        """
        self.active_payload = CancelOrderPayload(order_id=order_id, version=version, account=account).get_payload()
        self.active_headers = BaseHeaders(self._api_key, self._api_secret, self.active_payload).get_headers()
        self.active_endpoint = GenericEndpoint('order/cancel', version=version, sandbox=sandbox).get_endpoint()
        response = requests.post(url=self.active_endpoint, headers=self.active_headers)
        return response

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
