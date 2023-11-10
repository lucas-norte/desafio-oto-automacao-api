import httpx

class LoginEndpoint:
    def __init__(self):
        self.path_endpoint = 'https://reqres.in/api/login'
        body = {}

    def send_request(self, _data):
        _header = {"Content-Type": "application/json"}

        with httpx.Client() as client:
            return client.post(self.path_endpoint, data=_data, headers=_header)
