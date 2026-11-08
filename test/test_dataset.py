import pandas as pd
from scripts.build_dataset import build_dataset

def test_races_unique():
    build_dataset()
    races = pd.read_csv("data/processed/races_2022_2023.csv")
    assert not races["race_id"].duplicated().any()
def test_results_unique():
    build_dataset()
    results = pd.read_csv("data/processed/results_2022_2023_first3.csv")
    assert not results.duplicated(subset=["race_id", "driver_id"]).any()
def test_results_have_valid_races():
    build_dataset()
    races = pd.read_csv("data/processed/races_2022_2023.csv")
    results = pd.read_csv("data/processed/results_2022_2023_first3.csv")
    valid_race_ids = set(races["race_id"])
    assert results["race_id"].isin(valid_race_ids).all()
def test_six_races_loaded():
    build_dataset()
    results = pd.read_csv(
        "data/processed/results_2022_2023_first3.csv"
    )
    assert results['race_id'].nunique() == 6