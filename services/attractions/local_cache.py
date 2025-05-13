from pathlib import Path
import json

CACHE_PATH = Path(__file__).parent / "attractions_cache.json"

def load_cached_attractions(city: str) -> list:
    if not CACHE_PATH.exists():
        return []
    with open(CACHE_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
        return data.get(city.lower(), [])

def save_cached_attractions(city: str, attractions: list):
    data = {}
    if CACHE_PATH.exists():
        with open(CACHE_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
    data[city.lower()] = attractions
    with open(CACHE_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
