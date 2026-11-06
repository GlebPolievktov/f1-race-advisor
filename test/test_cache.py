import json

from scripts.cashe import load_or_fetch_json


def test_cache_hit(tmp_path, monkeypatch):
    cache_file = tmp_path / "results_2023_01.json"

    expected_data = {"MRData": {"total": "20"}}

    cache_file.write_text(
        json.dumps(expected_data),
        encoding="utf-8"
    )

    def fake_fetch(*args, **kwargs):
        raise AssertionError("API should not be called")

    monkeypatch.setattr(
        "scripts.cashe.fetch_json",
        fake_fetch
    )

    data = load_or_fetch_json(
        cache_file,
        "https://example.com/results.json"
    )

    assert data == expected_data


def test_cache_miss(tmp_path, monkeypatch):
    cache_file = tmp_path / "results_2023_01.json"

    expected_data = {"MRData": {"total": "20"}}
    calls = []

    def fake_fetch(url, params=None):
        calls.append((url, params))
        return expected_data

    monkeypatch.setattr(
        "scripts.cashe.fetch_json",
        fake_fetch
    )

    url = "https://example.com/results.json"

    data = load_or_fetch_json(
        cache_file,
        url,
        params={"limit": 100}
    )

    assert data == expected_data
    assert cache_file.exists()

    saved_data = json.loads(
        cache_file.read_text(encoding="utf-8")
    )

    assert saved_data == expected_data
    assert calls == [(url, {"limit": 100})]