import pandas as pd
from pathlib import Path
import json
from scripts.api_client import fetch_json
from scripts.parsers import parse_results
BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / "data" / "raw"
YEAR = 2023
PROC =  BASE_DIR / "data" / "processed" 
ROUND = 1


def fetch_results(year:int, round:int)->pd.DataFrame:
    url = f"https://api.jolpi.ca/ergast/f1/{year}/{round}/results.json"
    json_path = RAW_DIR / f"results_{year}_{round}.json"
    if json_path.exists():
        with open(json_path,"r",encoding="utf-8") as f:
            data = json.load(f) 
        print("Using cached JSON")
    else:
        data = fetch_json(url,params={"limit": 100})
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        print("Downloaded JSON from API")

    df_race = parse_results(data)
    PROC.mkdir(parents=True, exist_ok=True)
    df_race.to_csv(
        PROC / f"results_{year}_{round:02d}.csv",
        index=False
    )
    return df_race

if __name__ == "__main__":
    fetch_results(2023, 1)