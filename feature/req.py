from typing import Generator
import requests
from requests.models import Response


class request_body:
    def __init__(self, url: str, headers: str, payload: str = None):
        self.url = url
        self.headers = headers
        self.payload = payload

    def post(self) -> Response:
        return requests.post(url=self.url, headers=self.headers, json=self.payload)

    def get(self) -> Response:
        return requests.get(url=self.url, headers=self.headers)

