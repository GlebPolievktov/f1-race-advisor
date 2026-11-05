import pandas as pd
from pathlib import Path
import json
from api_client import fetch_json
from parsers import parse_results
BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / "data" / "raw"
YEAR = 2023
PROC =  BASE_DIR / "data" / "processed" 
ROUND = 1

url = f"https://api.jolpi.ca/ergast/f1/{YEAR}/{ROUND}/results.json"

data = fetch_json(url,params={"limit": 100})
json_path = RAW_DIR / f"results_{YEAR}_{ROUND}.json"
with open(json_path,"w",encoding="utf-8") as f:
    json.dump(data,f,indent=4)
df_race = parse_results(data)
print(df_race.head())
print(df_race.shape)
df_race.to_csv(
    PROC / f"results_{YEAR}_{ROUND:02d}.csv",
    index=False
)