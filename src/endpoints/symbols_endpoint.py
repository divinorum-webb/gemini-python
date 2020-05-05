from .base_endpoint import BaseEndpoint
from src.decorators import verify_api_method_exists


class SymbolsEndpoint(BaseEndpoint):
    def __init__(self, version='v1', sandbox=False):
        super().__init__(version, sandbox)

    @verify_api_method_exists('v1')
    def get_endpoint(self):
        if self.sandbox:
            url = self.base_sandbox_url
        else:
            url = self.base_url
        return "{0}/{1}/symbols".format(url, self.version)
