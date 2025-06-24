import unittest
from api import fetch_recent_games

class TestNBAStats(unittest.TestCase):
    def setUp(self):
        self.full_data = fetch_recent_games()
        self.players = self.full_data["data"]  # Now we extract the list

    def test_fetch_returns_dict_with_data(self):
        self.assertIsInstance(self.full_data, dict)
        self.assertIn("data", self.full_data)
        self.assertIsInstance(self.players, list)

    def test_players_have_stats(self):
        for player in self.players:
            self.assertIn("pts", player)
            self.assertIn("reb", player)
            self.assertIn("ast", player)
            self.assertIn("player", player)
            self.assertIn("first_name", player["player"])
            self.assertIn("last_name", player["player"])
            self.assertIn("team", player["player"])

if __name__ == "__main__":
    unittest.main()


