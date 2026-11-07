from pathlib import Path
import json
import pandas as pd
from scripts.parsers import parse_races
from scripts.cashe import load_or_fetch_json
YEAR = 2023
BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / "data" / "raw"
PROC =  BASE_DIR / "data" / "processed" 
#url = f"https://api.jolpi.ca/ergast/f1/{YEAR}/races.json"

def fetch_races(year: int) -> pd.DataFrame:
    url = f"https://api.jolpi.ca/ergast/f1/{year}/races.json"
    json_path = RAW_DIR / f"races_{year}.json"
    data = load_or_fetch_json(json_path,url,params={"limit": 100},validate=parse_races)
    df = parse_races(data)
    PROC.mkdir(parents=True, exist_ok=True)
    df.to_csv(PROC / f"races_{year}.csv",index=False)
    return df


if __name__ == "__main__":
    fetch_races(2023)