from .base_payload import BasePayload


class PastTradesPayload(BasePayload):
    def __init__(self,
                 symbol,
                 version='v1',
                 account=None):
        """
        Initializes the GenericPayload class.
        :param str symbol: the currency symbol for the new order
        :param str version: the api version to use
        :param str account: (optional) required for Master API keys; the name of the account in the sub-account group
        """
        super().__init__()
        self._symbol = symbol
        self._version = version
        self._account = account
        self._append_required_payload_params()
        self._append_optional_payload_params()

    @property
    def request(self):
        return "/{0}/mytrades".format(self._version)

    @property
    def symbol(self):
        return self._symbol

    @property
    def account(self):
        return self._account

    @property
    def payload(self):
        return self._payload

    @property
    def required_payload_param_keys(self):
        return ['request', 'nonce', 'symbol']

    @property
    def required_payload_param_values(self):
        return [self.request, self.nonce, self.symbol]

    @property
    def optional_payload_param_keys(self):
        return ['account']

    @property
    def optional_payload_param_values(self):
        return [self.account]

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
