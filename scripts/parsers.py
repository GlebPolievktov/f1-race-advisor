import pandas as pd

def parse_races(data:dict)->pd.DataFrame:
    races = data['MRData']['RaceTable']['Races']
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
    return df.sort_values(by=["round"]).reset_index(drop=True)
def parse_results(data:dict)->pd.DataFrame:
    races = data["MRData"]["RaceTable"]["Races"]

    if not races:
        raise ValueError("List of races is empty")

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
    return df_race