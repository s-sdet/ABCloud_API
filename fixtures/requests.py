import requests
from environment import ENV_OBJECT


class MyRequests():
    @staticmethod
    def post(url: str, data: dict = None, headers: dict = None, verify: bool = None):
        return MyRequests._send(url, data, headers, 'POST', verify)

    @staticmethod
    def get(url: str, data: dict = None, headers: dict = None, verify: bool = None):
        return MyRequests._send(url, data, headers, 'GET', verify)

    @staticmethod
    def put(url: str, data: dict = None, headers: dict = None, verify: bool = None):
        return MyRequests._send(url, data, headers, 'PUT', verify)

    @staticmethod
    def delete(url: str, data: dict = None, headers: dict = None, verify: bool = None):
        return MyRequests._send(url, data, headers, 'DELETE', verify)

    @staticmethod
    def _send(url: str, data: dict, headers: dict, method: str, verify: bool):

        url = f"{ENV_OBJECT.get_base_url()}{url}"

        if headers is None:
            headers = {}
        if data is None:
            data = {}
        if verify is None:
            verify = False

        if method == 'GET':
            response = requests.get(url, params=data, headers=headers, verify=verify)
        elif method == 'POST':
            response = requests.post(url, data=data, headers=headers, verify=verify)
        elif method == 'PUT':
            response = requests.put(url, data=data, headers=headers, verify=verify)
        elif method == 'DELETE':
            response = requests.delete(url, data=data, headers=headers, verify=verify)
        else:
            raise Exception(f"Bad HTTP method '{method}' was received")

        return response
