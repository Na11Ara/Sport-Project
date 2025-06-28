from typing import Dict
import json
import os

def fetch_recent_games() -> Dict:
    """
    Reads and returns recent NBA game statistics from a mock JSON file.

    Returns:
        dict: A dictionary containing a 'data' key with a list of player stats.
    """
    path = os.path.join(os.path.dirname(__file__), '..', 'mock_nba_stats.json')
    full_path = os.path.abspath(path)
    print("👉 Attempting to read from:", full_path)

    with open(full_path, 'r') as file:
        content = file.read()
        print("📄 File content starts with:", content[:100])

        data = json.loads(content)
    return data
