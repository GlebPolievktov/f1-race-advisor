from pathlib import Path
import json
import pandas as pd
from api_client import fetch_json
YEAR = 2023
BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / "data" / "raw"
PROC =  BASE_DIR / "data" / "processed" 
url = f"https://api.jolpi.ca/ergast/f1/{YEAR}/races.json"


data = fetch_json(url,params={"limit": 100})
json_path = RAW_DIR / f"races_{YEAR}.json"

with open(json_path,"w",encoding="utf-8") as f:
    json.dump(data,f,indent=4)
rec = []
races = data["MRData"]["RaceTable"]["Races"]
for race in races:
    year = int(race["season"])
    round_number = int(race["round"])
    race_id = f"{year}_{round_number:02d}"

    race_record = {
        "race_id" : race_id,
        "year": year,
        "round": round_number,
        "race_name": race["raceName"],
        "circuit_id": race["Circuit"]["circuitId"],
        "circuit": race["Circuit"]["circuitName"],
        "date": race["date"]
    }
    rec.append(race_record)
df = pd.DataFrame(rec).sort_values(by=["round"]).reset_index(drop=True)
print(df.head())
df.to_csv(PROC / f"races_{YEAR}.csv",index=False)