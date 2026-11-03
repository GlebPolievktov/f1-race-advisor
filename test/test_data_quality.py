import pytest
from pathlib import Path
import pandas as pd


def test_race_ids_unique():
    base_dir = Path(__file__).resolve().parent.parent
    proc =  base_dir / "data" / "processed" / "races_2023.csv"

    df = pd.read_csv(proc)

    assert not df.empty,"The DF is empty"

    assert df['race_id'].is_unique, "Race IDs are not unique"
def test_results_drivers_unique():
    base_dir = Path(__file__).resolve().parent.parent
    proc =  base_dir / "data" / "processed" / "results_2023_01.csv"

    df = pd.read_csv(proc)

    assert not df.empty,"The DF is empty"

    assert df['driver_id'].is_unique, "Driver IDs are not unique"

    assert df["race_id"].notna().all()
    assert df["driver_id"].notna().all()


def test_results_match_races():
    base_dir = Path(__file__).resolve().parent.parent

    races_path = (
        base_dir / "data" / "processed" / "races_2023.csv"
    )

    results_path = (
        base_dir / "data" / "processed" / "results_2023_01.csv"
    )

    races_df = pd.read_csv(races_path)
    results_df = pd.read_csv(results_path)


    assert not races_df.empty
    assert not results_df.empty

    race_ids = set(races_df["race_id"])

    result_race_ids = set(results_df["race_id"])

    assert result_race_ids.issubset(race_ids), (
        "Результаты содержат неизвестные race_id"
    )

