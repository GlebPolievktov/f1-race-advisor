# F1 Race Advisor

AI-powered Formula 1 race recommendation system.

## Goal

Build a conversational recommendation system that understands requests such as:

> "Recommend an exciting rainy F1 race featuring Fernando Alonso, without spoilers."

The system will combine structured Formula 1 data, recommendation algorithms, and an LLM to provide personalized race suggestions.

### Currently Used

- Python
- requests
- pandas
- pytest
- Jolpica F1 API

## Current progress
- F1 race calendar loading
- Race results loading
- JSON and CSV processing
- Collecting data over several seasons
- Completeness and duplicate checks
- JSON Cashing
- Test data integrity and caching with pytest.

## Setup
pip install -r requirements.txt

## Project Structure

```text
f1_race_advisor/
├── scripts/
│   ├── api_client.py
│   ├── cache.py
│   ├── parsers.py
│   ├── fetch_races.py
│   ├── fetch_results.py
│   └── build_dataset.py
├── data/
│   ├── raw/
│   └── processed/
├── test/
│   ├── test_cache.py
│   └── test_dataset.py
├── requirements.txt
└── README.md
```

## Installation

Clone the repository and navigate to the project directory.

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

## Run

Run commands from the project root.
```bash
python -m scripts.fetch_races

python -m scripts.fetch_results

python -m scripts.build_dataset
```

## Testing

Run all tests:

```bash
python -m pytest -v
```

## Next steps
- Reusable API client
- Multi-season data collection
- LLM-based recommendation interface