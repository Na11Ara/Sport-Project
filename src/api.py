import json
import os

def fetch_recent_games():
    path = os.path.join(os.path.dirname(__file__), '..', 'mock_nba_stats.json')
    full_path = os.path.abspath(path)
    print("👉 Attempting to read from:", full_path)  # Add this line to confirm the file location

    with open(full_path, 'r') as file:
        content = file.read()
        print("📄 File content starts with:", content[:100])  # Show the first part of the file

        data = json.loads(content)
    return data
