import json
import requests
import logging
from requests import Response

logger = logging.getLogger("ABCloud API")


class BaseClass:
    def __init__(self, app):
        self.app = app

    @staticmethod
    def request(method: str, url: str, **kwargs) -> Response:
        """
        Request method
        method: method for the new Request object: GET, OPTIONS, HEAD, POST, PUT, PATCH, or DELETE. # noqa
        url – URL for the new Request object.
        **kwargs:
            params – (optional) Dictionary, list of tuples or bytes to send in the query string for the Request. # noqa
            json – (optional) A JSON serializable Python object to send in the body of the Request. # noqa
            headers – (optional) Dictionary of HTTP Headers to send with the Request.
        """
        return requests.request(method, url, **kwargs)

    def to_dict(self) -> dict:
        """
        Convert nested object to dict
        :return: dict
        """
        return json.loads(json.dumps(self, default=lambda o: o.__dict__))