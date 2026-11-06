
import json
from pathlib import Path

from scripts.api_client import fetch_json


def load_or_fetch_json(path, url, params=None, validate=None):
    path = Path(path)

    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        print("Using cached JSON")

    else:
        data = fetch_json(url, params=params)

        if validate is not None:
            validate(data)

        path.parent.mkdir(parents=True, exist_ok=True)

        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

        print("Downloaded JSON from API")

        return data

    if validate is not None:
        validate(data)

    return data
