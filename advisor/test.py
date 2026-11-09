from pydantic import BaseModel
from preferences import RacePreferences

prefs = RacePreferences(
    driver="alonso",
    weather="wet",
    year_from=2010,
    year_to=2020
)

print(prefs.model_dump())

