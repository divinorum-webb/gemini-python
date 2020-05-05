class BaseEndpoint:
    def __init__(self, version, sandbox=False):
        self._version = version
        self._sandbox = sandbox

    @property
    def version(self):
        return self._version

    @property
    def sandbox(self):
        return self._sandbox

    @property
    def base_url(self):
        return "https://api.gemini.com"

    @property
    def base_sandbox_url(self):
        return "https://api.sandbox.gemini.com"
