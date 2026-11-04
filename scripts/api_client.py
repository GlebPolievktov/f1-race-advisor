import requests

HEADERS = {
    "USER-AGENT": "F1RaceAdvisor/0.1"
}

def fetch_json(url:str,timeout:int=30,params=None)->dict:
    response = requests.get(url,headers=HEADERS,timeout=timeout,params=params)
    print(response.status_code)
    response.raise_for_status()
    return response.json()

'''url = "https://api.jolpi.ca/ergast/f1/2023/races.json"

data = fetch_json(
    url,
    params={"limit": 100}
)
url = "https://api.jolpi.ca/ergast/f1/2023/1/results.json"

data = fetch_json(
    url,
    params={"limit": 100}
)
print(data)'''