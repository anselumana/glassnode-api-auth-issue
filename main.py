import time
from lib.utils import get_api_key, get_endpoints, save_data
from lib.client import GlassnodeClient

if __name__ == "__main__":
    sleep_between_requests = 2.1
    api_key = get_api_key()
    client = GlassnodeClient(api_key)
    data = []
    exploited_endpoints = 0
    # get all glassnode T3 endpoints
    endpoints = [endpoint for endpoint in get_endpoints(api_key) if endpoint["tier"] == 3]
    count = 1
    print(f"starting data fetch (est. time: {len(endpoints) * sleep_between_requests} seconds)")
    for endpoint in endpoints:
        print(f"processing endpoint {count}/{len(endpoints)} ({round(count/len(endpoints)*100, 2)}%)", end="\r")
        path = endpoint["path"]
        tier = endpoint["tier"]
        # make HTTP request
        res = client.get(path, {"a": "BTC"})
        if res.status_code == 200:
            data.append({
                "path": path,
                "data": res.json()
            })
            exploited_endpoints += 1
        # this prevents exceeding the 30 req/min limit of the free tier
        time.sleep(sleep_between_requests)
        count += 1
    # save results to file
    print(f"\nexploited {exploited_endpoints}/{len(endpoints)} T3 endpoints")
    save_data(data)