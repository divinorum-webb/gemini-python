from .base_payload import BasePayload


class OrderPayload(BasePayload):
    def __init__(self,
                 endpoint_text,
                 order_id,
                 version='v1',
                 account=None):
        """
        Initializes the CancelOrderPayload class.
        :param str endpoint_text: the tail end of the endpoint url to append to the base url
        :param str order_id: the order's unique identifier
        :param str version: the api version to use
        :param str account: (optional) required for Master API keys; the name of the account in the sub-account group
        """
        super().__init__()
        self._endpoint_text = endpoint_text
        self._order_id = order_id
        self._version = version
        self._account = account
        self._append_required_payload_params()
        self._append_optional_payload_params()

    @property
    def request(self):
        return "/{0}/{1}".format(self._version, self._endpoint_text)

    @property
    def order_id(self):
        return self._order_id

    @property
    def account(self):
        return self._account

    @property
    def payload(self):
        return self._payload

    @property
    def required_payload_param_keys(self):
        return ['request', 'nonce', 'order_id']

    @property
    def required_payload_param_values(self):
        return [self.request, self.nonce, self.order_id]

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
