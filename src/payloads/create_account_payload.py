from .base_payload import BasePayload


class CreateAccountPayload(BasePayload):
    def __init__(self,
                 name,
                 account_type,
                 version='v1'):
        """
        Initializes the CreateAccountPayload class.
        :param str name: the unique (account-wide) name for the new account
        :param str account_type: (optional) dictates the account type created; either 'exchange' or 'custody'
        :param str version: the api version to use
        """
        super().__init__()
        self._name = name
        self._account_type = account_type
        self._version = version
        self._append_required_payload_params()
        self._append_optional_payload_params()

    @property
    def request(self):
        return "/{0}/account/create".format(self._version)

    @property
    def name(self):
        return self._name

    @property
    def account_type(self):
        if self._account_type not in self.valid_account_types:
            raise ValueError(f"The account type '{self._account_type}' is not a valid type: {self.valid_account_types}")
        return self._account_type

    @property
    def valid_account_types(self):
        return ['exchange', 'custody']

    @property
    def payload(self):
        return self._payload

    @property
    def required_payload_param_keys(self):
        return ['request', 'nonce', 'name', 'type']

    @property
    def required_payload_param_values(self):
        return [self.request, self.nonce, self.name, self.account_type]

    @property
    def optional_payload_param_keys(self):
        return []

    @property
    def optional_payload_param_values(self):
        return []

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
