from pathlib import Path
import json
import pandas as pd
from scripts.parsers import parse_races
from scripts.cashe import load_or_fetch_json
YEAR = 2023
BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / "data" / "raw"
PROC =  BASE_DIR / "data" / "processed" 
url = f"https://api.jolpi.ca/ergast/f1/{YEAR}/races.json"


json_path = RAW_DIR / f"races_{YEAR}.json"
data = load_or_fetch_json(
    json_path,
    url,
    params={"limit": 100},
    validate=parse_races
)

df = parse_races(data)
df.to_csv(PROC / f"races_{YEAR}.csv",index=False)