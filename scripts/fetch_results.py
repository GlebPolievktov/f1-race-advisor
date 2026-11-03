import pandas as pd
from pathlib import Path
import requests
import json
BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / "data" / "raw"
YEAR = 2023
PROC =  BASE_DIR / "data" / "processed" 
ROUND = 1

url = f"https://api.jolpi.ca/ergast/f1/{YEAR}/{ROUND}/results.json"
timeout = 30

headers = {
    "User-Agent" : "F1RaceAdvisor/0.1 "
}

response = requests.get(url,headers=headers,timeout=timeout,params={"limit": 100})
response.raise_for_status()
print(response.status_code)
data = response.json()
json_path = RAW_DIR / f"results_{YEAR}_{ROUND}.json"
with open(json_path,"w",encoding="utf-8") as f:
    json.dump(data,f,indent=4)
races = data["MRData"]["RaceTable"]["Races"][0]
print("Гонка:", races["raceName"])
print("Количество пилотов:", len(races["Results"]))
print("Первый пилот:", races["Results"][0]["Driver"]["familyName"])
race_id = f"{YEAR}_{ROUND:02d}"
records = []
for res in races["Results"]:
    r = {
        "race_id": race_id,
        "driver_id" : res["Driver"]["driverId"],
        "name_surname" : res["Driver"]["givenName"] + " " + res["Driver"]['familyName'],
        "constructor_id" : res['Constructor']['constructorId'],
        'grid' : int(res['grid']),
        'position' : int(res['position']),
        'status' : res['status']
        }
    records.append(r)
df_race = pd.DataFrame(records).sort_values(by=['position']).reset_index(drop=True)
print(df_race.head())
print(df_race.shape)
df_race.to_csv(
    PROC / f"results_{YEAR}_{ROUND:02d}.csv",
    index=False
)