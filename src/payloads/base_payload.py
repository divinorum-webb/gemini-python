import datetime
import time


class BasePayload:
    def __init__(self):
        self._payload = {"nonce": self.nonce}

    @property
    def nonce(self):
        current_time = datetime.datetime.now()
        return str(int(time.mktime(current_time.timetuple()) * 1000))
