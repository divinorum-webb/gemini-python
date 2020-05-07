from .base_endpoint import BaseEndpoint
from src.decorators import verify_api_method_exists


class TransfersEndpoint(BaseEndpoint):
    def __init__(self, version='v1', sandbox=False, timestamp=None, limit_transfers=None):
        """
        Initializes the TransfersEndpoint class.
        :param str version: the api version to use
        :param bool sandbox: True if using the sandbox api, False by default
        :param int timestamp: (optional) only trades occurring after this timestamp will be returned
        :param int limit_transfers: (optional) sets the maximum number of transfers to return; defaults to 50
        """
        super().__init__(version, sandbox)
        self._timestamp = timestamp
        self._limit_transfers = limit_transfers
        self._parameter_dict = self.parameter_dict

    @property
    def url_param_keys(self):
        return ['timestamp', 'limit_transfers']

    @property
    def url_param_values(self):
        return [f"timestamp={str(self._timestamp)}" if self._timestamp else None,
                f"limit_transfers={str(self._limit_transfers)}" if self._limit_transfers else None]

    @property
    def parameter_dict(self):
        self._parameter_dict.update(self._get_parameter_dict(self.url_param_keys, self.url_param_values))
        return self._parameter_dict

    @verify_api_method_exists('v1')
    def get_endpoint(self):
        if self.sandbox:
            url = self.base_sandbox_url
        else:
            url = self.base_url
        url = "{0}/{1}/transfers".format(url, self.version)
        return self._append_url_parameters(url)
