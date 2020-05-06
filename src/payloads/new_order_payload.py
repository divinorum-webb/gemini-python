import json
from .base_payload import BasePayload


class NewOrderPayload(BasePayload):
    def __init__(self,
                 symbol,
                 amount,
                 price,
                 side,
                 version='v1',
                 order_type='exchange limit',
                 client_order_id=None,
                 min_amount=None,
                 options=None,
                 stop_price=None,
                 account=None):
        """
        Initializes the NewOrderPayload class.
        :param str symbol: the currency symbol for the new order
        :param str amount: the quoted decimal amount to purchase
        :param str price: the quoted decimal amount to spend per unit
        :param str side: 'buy' or 'sell'
        :param str version: the api version to use
        :param str order_type: the order type; 'exchange stop limit' for stop-limit orders, 'exchange limit' otherwise
        :param str client_order_id: (recommended) a unique order id defined by the user
        :param str min_amount: (optional) minimum decimal amount to purchase, for block trades only
        :param list options: (optional) a list containing at most one supported order execution option
        :param str stop_price: (optional) the price to trigger a stop-limit order; only available for stop-limit orders
        :param str account: (optional) required for Master API keys; the name of the account in the sub-account group
        """
        super().__init__()
        self._client_order_id = client_order_id
        self._symbol = symbol
        self._amount = amount
        self._price = price
        self._side = side
        self._version = version
        self._order_type = order_type
        self._min_amount = min_amount
        self._options = options
        self._stop_price = stop_price
        self._account = account
        self._append_required_payload_params()
        self._append_optional_payload_params()

    @property
    def request(self):
        return "/{0}/order/new".format(self._version)

    @property
    def client_order_id(self):
        return self._client_order_id

    @property
    def symbol(self):
        return self._symbol

    @property
    def amount(self):
        return self._amount

    @property
    def min_amount(self):
        return self._min_amount

    @property
    def price(self):
        return self._price

    @property
    def side(self):
        if self._side not in ['buy', 'sell']:
            raise ValueError(f"Invalid 'side': {self._side}). The 'side' argument must be either 'buy' or 'sell'.")
        return self._side

    @property
    def order_type(self):
        if self._stop_price and not self._order_type == 'exchange stop limit':
            raise ValueError("A 'stop_price' has been set, so 'order_type' must be set to 'exchange stop limit'.")
        return self._order_type

    @property
    def options(self):
        return self._options

    @property
    def stop_price(self):
        if self._stop_price:
            if self._side == 'buy':
                if self._stop_price >= self._price:
                    raise ValueError("The 'stop_price' must be lower than the 'price' for buy orders.")
            if self._side == 'sell':
                if self._stop_price <= self._price:
                    raise ValueError("The 'stop_price' must be higher than the 'price' for sell orders.")
            return self._stop_price

    @property
    def account(self):
        return self._account

    @property
    def valid_order_execution_options(self):
        return [
            'make-or-cancel',
            'immediate-or-cancel',
            'fill-or-kill',
            'auction-only',
            'indication-of-interest'
        ]

    @property
    def payload(self):
        return self._payload

    @property
    def required_payload_param_keys(self):
        return ['request', 'nonce', 'symbol', 'amount', 'price', 'side', 'type']

    @property
    def required_payload_param_values(self):
        return [self.request, self.nonce, self.symbol, self.amount, self.price, self.side, self.order_type]

    @property
    def optional_payload_param_keys(self):
        return ['client_order_id', 'min_amount', 'options', 'stop_price', 'account']

    @property
    def optional_payload_param_values(self):
        return [self.client_order_id, self.min_amount, self.options, self.stop_price, self.account]

    def _append_required_payload_params(self):
        if any(self.required_payload_param_values):
            self._payload.update(self._get_parameters_dict(self.required_payload_param_keys,
                                                           self.required_payload_param_values))

    def _append_optional_payload_params(self):
        if any(self.optional_payload_param_values):
            self._payload.update(self._get_parameters_dict(self.optional_payload_param_keys,
                                                           self.optional_payload_param_values))

    def get_payload(self):
        return self.payload
