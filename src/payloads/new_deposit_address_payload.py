from .base_payload import BasePayload


class NewDepositAddressPayload(BasePayload):
    def __init__(self,
                 network,
                 label=None,
                 legacy=None,
                 version='v1',
                 account=None):
        """
        Initializes the NewDepositAddressPayload class.
        :param str network: the crypto currency network
        :param str label: (optional) a label for the deposit address
        :param bool legacy: (optional) False by default; True if generating a legacy P2SH-P2PKH litecoin address
        :param str version: the api version to use
        :param str account: (optional) required for Master API keys; the name of the account in the sub-account group
        """
        super().__init__()
        self._network = network
        self._label = label
        self._legacy = legacy
        self._version = version
        self._account = account
        self._append_required_payload_params()
        self._append_optional_payload_params()

    @property
    def network(self):
        if self._network not in self.valid_networks:
            raise ValueError(f"The provided network ('{self._network}') is not a valid network: {self.valid_networks}")
        return self._network

    @property
    def valid_networks(self):
        return [
            'bitcoin',
            'ethereum',
            'bitcoincash',
            'litecoin',
            'zcash'
        ]

    @property
    def request(self):
        return "/{0}/deposit/{1}/newAddress".format(self._version, self._network)

    @property
    def label(self):
        return self._label

    @property
    def legacy(self):
        return self._legacy

    @property
    def account(self):
        return self._account

    @property
    def payload(self):
        return self._payload

    @property
    def required_payload_param_keys(self):
        return ['request', 'nonce']

    @property
    def required_payload_param_values(self):
        return [self.request, self.nonce]

    @property
    def optional_payload_param_keys(self):
        return ['account', 'label', 'legacy']

    @property
    def optional_payload_param_values(self):
        return [self.account, self.label, self.legacy]

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
