class BaseEndpoint:
    def __init__(self, version, sandbox=False):
        self._version = version
        self._sandbox = sandbox
        self._parameter_dict = {}

    def _params_exist(self):
        if self.parameter_dict:
            return list(self.parameter_dict.keys())
        else:
            return []

    def _params_text(self):
        if self.parameter_dict:
            return list(self.parameter_dict.values())
        else:
            return []

    def _append_url_parameters(self, url):
        text_to_append = "?" if any(self._params_exist()) else ""
        for i, text in enumerate(self._params_text()):
            if self._params_exist()[i]:
                text_to_append += text if text_to_append.endswith('?') else ('&' + text)
        return "{0}{1}".format(url, text_to_append)

    @staticmethod
    def _get_parameter_dict(param_keys, param_values):
        params_dict = {}
        for i, key in enumerate(param_keys):
            if param_values[i] or param_values[i] is False:
                params_dict.update({key: param_values[i]})
        return params_dict

    @property
    def version(self):
        return self._version

    @property
    def sandbox(self):
        return self._sandbox

    @property
    def parameter_dict(self):
        return self._parameter_dict

    @property
    def base_url(self):
        return "https://api.gemini.com"

    @property
    def base_sandbox_url(self):
        return "https://api.sandbox.gemini.com"
