# F1 Race Advisor

AI-powered Formula 1 race recommendation system.

## Goal
Recommend F1 races based on natural-language
queries and user preferences.

## Stack
Python, Pandas, Scikit-learn, LLM API,
FastAPI, Streamlit, PostgreSQL.

# F1 Race Advisor

LLM-powered Formula 1 race recommendation system.

## Current progress
- F1 race calendar loading
- Race results loading
- JSON and CSV processing
- Data quality tests

## Setup
pip install -r requirements.txt

## Run
python scripts/fetch_races.py
python scripts/fetch_results.py

## Tests
python -m pytest -v

## Next steps
- Reusable API client
- Multi-season data collection
- LLM-based recommendation interface