import requests

class GlassnodeClient():
    def __init__(self, api_key):
        self.base_url = "https://api.glassnode.com"
        self.api_key = api_key
    
    def get(self, path: str, params: dict = {}):
        url = f"{self.base_url}{path}"
        params["api_key"] = self.api_key
        return requests.get(url, params=params)