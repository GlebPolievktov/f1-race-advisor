import pandas as pd

def parse_races(data:dict)->pd.DataFrame:
    races = data['MRData']['RaceTable']['Races']
    total_races = int(data["MRData"]["total"])
    if not total_races:
        raise ValueError("Total races is zero")
    if total_races != len(races):
        raise ValueError(f"It is expected all {total_races} races, but got {len(races)}")

    rec = []
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
    df = pd.DataFrame(rec)
    if len(df.columns) == 0:
        raise ValueError("DataFrame is empty")
    if df["race_id"].duplicated().any():
        raise ValueError("The race_id contains duplicates")
    return df.sort_values(by=["round"]).reset_index(drop=True)
def parse_results(data:dict)->pd.DataFrame:
    races = data["MRData"]["RaceTable"]["Races"]

    if not races:
        raise ValueError("List of races is empty")

    race = races[0]
    results = race["Results"]

    total_races = int(data["MRData"]["total"])
    if not results:
        raise ValueError("List of results is empty")

    if len(results) != total_races:
        raise ValueError(
            f"Expected {total_races} results, "
            f"but got {len(results)}"
        )

    races = races[0]
    year = int(races["season"])
    round_number = int(races["round"])

    race_id = f"{year}_{round_number:02d}"
    records = []
    for res in races["Results"]:
        r = {
            "race_id" : race_id,
            "driver_id" : res["Driver"]["driverId"],
            "name_surname" : res["Driver"]["givenName"] + " " + res["Driver"]['familyName'],
            "constructor_id" : res['Constructor']['constructorId'],
            'grid' : int(res['grid']),
            'position' : int(res['position']),
            'status' : res['status']
            }
        records.append(r)
    df_race = pd.DataFrame(records).sort_values(by=['position']).reset_index(drop=True)
    if df_race.duplicated(subset=["race_id", "driver_id"]).any():
        raise ValueError("The race_id contains duplicates")
    return df_race