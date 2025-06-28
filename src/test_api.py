from typing import List, Dict
import unittest
from api import fetch_recent_games

class TestNBAStats(unittest.TestCase):
    def setUp(self) -> None:
        """Load data once before each test."""
        self.full_data: Dict[str, List[Dict]] = fetch_recent_games()
        self.players: List[Dict] = self.full_data["data"]

    def test_fetch_returns_dict_with_data(self) -> None:
        """Test that fetched data is a dictionary with a 'data' list."""
        self.assertIsInstance(self.full_data, dict)
        self.assertIn("data", self.full_data)
        self.assertIsInstance(self.players, list)

    def test_players_have_stats(self) -> None:
        """Test that each player has the required statistics and identity keys."""
        for player in self.players:
            self.assertIn("pts", player)
            self.assertIn("reb", player)
            self.assertIn("ast", player)
            self.assertIn("player", player)
            self.assertIn("first_name", player["player"])
            self.assertIn("last_name", player["player"])
            self.assertIn("team", player["player"])
    def test_get_top_scorer(self):
        from main import get_top_scorer
        top = get_top_scorer(self.players)
        self.assertIn("pts", top)
        self.assertGreaterEqual(top["pts"], max(player["pts"] for player in self.players))



if __name__ == "__main__":
    unittest.main()
