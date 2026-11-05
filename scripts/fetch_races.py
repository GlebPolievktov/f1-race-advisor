from pathlib import Path
import json
import pandas as pd
from api_client import fetch_json
from parsers import parse_races
YEAR = 2023
BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / "data" / "raw"
PROC =  BASE_DIR / "data" / "processed" 
url = f"https://api.jolpi.ca/ergast/f1/{YEAR}/races.json"


data = fetch_json(url,params={"limit": 100})
json_path = RAW_DIR / f"races_{YEAR}.json"

with open(json_path,"w",encoding="utf-8") as f:
    json.dump(data,f,indent=4)
df = parse_races(data)
df.to_csv(PROC / f"races_{YEAR}.csv",index=False)