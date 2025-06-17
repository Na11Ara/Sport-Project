from api import fetch_recent_games

def test_fetch_recent_games():
    data = fetch_recent_games()
    assert "data" in data
    assert isinstance(data["data"], list)
    assert len(data["data"]) > 0
