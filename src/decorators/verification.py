import warnings
from functools import wraps

from src.exceptions import InvalidRestApiVersion


def verify_api_method_exists(version_introduced, ):
    """
    Verifies that the connection's REST API version is equal to or greater than the version the method was introduced.

    :param str version_introduced: the REST API version when the method was introduced
    :return: decorated function
    """
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            input_api_version = self.version
            if input_api_version < version_introduced:
                raise InvalidRestApiVersion(func,
                                            api_version_used=input_api_version,
                                            api_version_required=version_introduced)
            return func(self, *args, **kwargs)
        return wrapper
    return decorator
