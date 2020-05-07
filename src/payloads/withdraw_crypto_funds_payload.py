from .base_payload import BasePayload


class WithdrawCryptoFundsPayload(BasePayload):
    def __init__(self,
                 address,
                 amount,
                 currency,
                 version='v1',
                 account=None):
        """
        Initializes the WithdrawCryptoFundsPayload class.
        :param str address: the whitelisted crypto currency address where funds will be sent
        :param str amount: the amount of funds to withdraw
        :param str currency: the crypto currency variety to withdraw
        :param str version: the api version to use
        :param str account: (optional) required for Master API keys; the name of the account in the sub-account group
        """
        super().__init__()
        self._address = address
        self._amount = amount
        self._currency = currency
        self._version = version
        self._account = account
        self._append_required_payload_params()
        self._append_optional_payload_params()

    @property
    def request(self):
        return "/{0}/withdraw/{1}".format(self._version, self._currency)
    
    @property
    def address(self):
        return self._address
    
    @property
    def amount(self):
        return self._amount
    
    @property
    def currency(self):
        return self._currency

    @property
    def account(self):
        return self._account

    @property
    def payload(self):
        return self._payload

    @property
    def required_payload_param_keys(self):
        return ['request', 'nonce', 'address', 'amount']

    @property
    def required_payload_param_values(self):
        return [self.request, self.nonce, self.address, self.amount]

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
