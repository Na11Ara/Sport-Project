from api import fetch_recent_games

def calculate_average_points(stats):
    total_points = sum(player["pts"] for player in stats["data"])
    return total_points / len(stats["data"])

def main():
    stats = fetch_recent_games()  

    for player in stats["data"]:
        name = f"{player['player']['first_name']} {player['player']['last_name']}"
        team = player["player"]["team"]
        print(f"{name} ({team}) - PTS: {player['pts']}, REB: {player['reb']}, AST: {player['ast']}")

    avg_pts = calculate_average_points(stats)  
    print(f"\n📊 Average Points per Player: {avg_pts:.2f}")

if __name__ == "__main__":
    main()

def print_player_stats(stats: list[dict]) -> None:
    print(f"{'Player':<20} {'Team':<25} {'PTS':<5} {'REB':<5} {'AST':<5}")
    print("-" * 60)
    for player in stats:
        name = f"{player['player']['first_name']} {player['player']['last_name']}"
        team = player['player']['team']
        pts = player['pts']
        reb = player['reb']
        ast = player['ast']
        print(f"{name:<20} {team:<25} {pts:<5} {reb:<5} {ast:<5}")



