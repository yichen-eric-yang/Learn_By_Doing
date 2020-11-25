import requests
import sys


class request_body:
    def __init__(self, url: str, headers: str, payload: str = None):
        self.url = url
        self.headers = headers
        self.payload = payload

    def post(self) -> str:
        return requests.post(url=self.url, headers=self.headers, json=self.payload)

    def get(self) -> str:
        return requests.get(url=self.url, headers=self.headers)

