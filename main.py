# main.py

from RPS_game import play, quincy, abbey, kris, mrugesh
from RPS import player
from test_module import test_win_rate

# Number of games per match
GAMES = 1000

# Match each opponent
print("Playing against Quincy...")
play(player, quincy, GAMES)

print("\nPlaying against Abbey...")
play(player, abbey, GAMES)

print("\nPlaying against Kris...")
play(player, kris, GAMES)

print("\nPlaying against Mrugesh...")
play(player, mrugesh, GAMES)

# Run tests
print("\nRunning performance test...")
test_win_rate(player)
