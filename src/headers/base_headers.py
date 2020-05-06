import base64
import hmac
import hashlib
import json


class BaseHeaders:
    def __init__(self,
                 api_key,
                 api_secret,
                 payload,
                 content_length='0',
                 content_type='text/plain',
                 cache_control='no-cache'):
        self._api_key = api_key
        self._api_secret = api_secret.encode()
        self._payload = payload
        self._content_length = content_length
        self._content_type = content_type
        self._cache_control = cache_control

    @property
    def b64(self):
        encoded_payload = json.dumps(self._payload).encode()
        return base64.b64encode(encoded_payload)

    @property
    def signature(self):
        return hmac.new(self._api_secret, self.b64, hashlib.sha384).hexdigest()

    @property
    def headers(self):
        return {
            "Content-Length": self._content_length,
            "Content-Type": self._content_type,
            "X-GEMINI-APIKEY": self._api_key,
            "X-GEMINI-PAYLOAD": self.b64,
            "X-GEMINI-SIGNATURE": self.signature,
            "Cache-Control": self._cache_control
        }

    def get_headers(self):
        return self.headers
