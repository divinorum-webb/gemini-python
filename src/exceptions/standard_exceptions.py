class InvalidParameterException(Exception):
    """
    Raised when an invalid set of parameters are passed to a class or instance method
    """
    def __init__(self, class_name, parameters):
        error_message = """
        \n{} received an invalid combination of parameters.
         Evaluate the parameters below and correct accordingly:\n{}
         """.format(class_name, parameters)
        super().__init__(error_message)


class InvalidRestApiVersion(Exception):
    """
    Exception for flagging API method calls to endpoints that do not exist for the (older) version being used.
    """
    def __init__(self, func, api_version_used, api_version_required):
        """
        Generates an error message citing the api_version_used and api_version_required.
        :param str api_version_used: the REST API being used by the active connection
        :param str api_version_required: the minimum REST API version required
        """
        error_message = """
        The REST API endpoint referenced in function '{0}' requires a minimum API version of {1}.
        The API version you are using is {2}, which pre-dates the endpoint referenced.
        Please visit Gemini's REST API reference to identify the versions required to use each endpoint.
        """.format(func.__name__, api_version_required, api_version_used)
        super().__init__(error_message)
