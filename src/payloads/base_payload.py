import time


class BasePayload:
    def __init__(self):
        self._payload = {"nonce": self.nonce}

    @property
    def nonce(self):
        current_time = time.time()
        return str(int(current_time * 1000000))

    @staticmethod
    def _get_parameters_dict(param_keys, param_values):
        params_dict = {}
        for i, key in enumerate(param_keys):
            if param_values[i] or param_values[i] is False:
                params_dict.update({key: param_values[i]})
        return params_dict
