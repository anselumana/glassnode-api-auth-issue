import os
import json
from dotenv import dotenv_values
from library.client import GlassnodeClient

def get_api_key():
    config = dotenv_values()
    api_key = config.get("api_key")
    if not api_key:
        raise Exception("API key not found. Either no .env was found in the root directory or no API_KEY=value was found within it")
    return api_key

def get_endpoints(api_key: str):
    client = GlassnodeClient(api_key)
    res = client.get("/v2/metrics/endpoints")
    endpoints = [{
        "path": endpoint["path"],
        "tier": endpoint["tier"]
    } for endpoint in res.json()]
    return endpoints

def save_data(data):
    path = f".{os.sep}data{os.sep}data.json"
    print(f"saving fetched data to {path}")
    with open(path, "w") as file:
        file.write(json.dumps({
            "data": data
        }, indent=2))