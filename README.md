# gemini-python

This library written in Python is intended to provide streamlined control of the Gemini Exchange REST API for trading cryptocurrency.

Build a dict as demonstrated below and pass it as the 'config' argument to the GeminiConnection class to get started.

gemini_config = {
    "api_key": "<YOUR_API_KEY_NAME",
    "api_secret": "<YOUR_API_KEY_SECRET>"
}


conn = GeminiConnection(config=gemini_config)

response = conn.get_symbols()
