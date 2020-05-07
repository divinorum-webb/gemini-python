from .base_payload import BasePayload


class InternalTransfersPayload(BasePayload):
    def __init__(self,
                 source_account,
                 target_account,
                 amount,
                 currency,
                 version='v1',
                 account=None):
        """
        Initializes the InternalTransfersPayload class.
        :param str source_account: the nickname of the account you are transferring from
        :param str target_account: the nickname of the account you are transferring to
        :param str amount: the amount of funds to transfer
        :param str currency: the crypto currency variety being transferred
        :param str version: the api version to use
        :param str account: (optional) required for Master API keys; the name of the account in the sub-account group
        """
        super().__init__()
        self._source_account = source_account
        self._target_account = target_account
        self._amount = amount
        self._currency = currency
        self._version = version
        self._account = account
        self._append_required_payload_params()
        self._append_optional_payload_params()

    @property
    def request(self):
        return "/{0}/account/transfer/{1}".format(self._version, self._currency)

    @property
    def source_account(self):
        return self._source_account

    @property
    def target_account(self):
        return self._target_account

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
        return ['request', 'nonce', 'sourceAccount', 'targetAccount', 'amount']

    @property
    def required_payload_param_values(self):
        return [self.request, self.nonce, self.source_account, self.target_account, self.amount]

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
