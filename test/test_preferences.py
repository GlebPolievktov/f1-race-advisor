
import pytest
from pydantic import ValidationError

from advisor.preferences import RacePreferences


def test_valid_preferences():
    prefs = RacePreferences(
        driver="alonso",
        weather="rain",
        year_from=2015
    )

    assert prefs.driver == "alonso"
    assert prefs.weather == "rain"
    assert prefs.year_from == 2015


def test_default_values():
    prefs = RacePreferences()

    assert prefs.spoiler_free is True
    assert prefs.limit == 3


def test_invalid_weather():
    with pytest.raises(ValidationError):
        RacePreferences(weather="snow")


def test_invalid_year_range():
    with pytest.raises(ValidationError):
        RacePreferences(
            year_from=2023,
            year_to=2010
        )


def test_invalid_limit():
    with pytest.raises(ValidationError):
        RacePreferences(limit=10)
