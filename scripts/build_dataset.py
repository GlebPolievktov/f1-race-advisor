import pandas as pd
from scripts.fetch_races import fetch_races
from scripts.fetch_results import fetch_results
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
PROC_DIR = BASE_DIR / "data" / "processed"
def build_dataset()->None:
    seasons = [2022,2023]
    all_races = []
    all_results = []
    for year in seasons:
        df_races = fetch_races(year)
        all_races.append(df_races)
        for round in range(1,3+1):
            df_results = fetch_results(year, round)
            all_results.append(df_results)
    df_races = pd.concat(all_races,ignore_index=True)
    df_results = pd.concat(all_results,ignore_index=True)
    df_races.to_csv(
        PROC_DIR / "races_2022_2023.csv",
        index=False
    )

    df_results.to_csv(
        PROC_DIR / "results_2022_2023_first3.csv",
        index=False
    )
    if df_races["race_id"].duplicated().any():
        raise ValueError("Duplicate races found")

    if df_results.duplicated(subset=["race_id", "driver_id"]).any():
        raise ValueError("Duplicate results found")
if __name__ == "__main__":
    build_dataset()