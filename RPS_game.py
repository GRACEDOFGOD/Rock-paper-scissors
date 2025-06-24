# RPS_game.py

import random

def play(player1, player2, num_games=1000, verbose=False):
    p1_score = 0
    p2_score = 0
    tie = 0
    prev_play1 = ""
    prev_play2 = ""
    player1_history = []
    player2_history = []

    for i in range(num_games):
        move1 = player1(prev_play2, player1_history.copy())
        move2 = player2(prev_play1, player2_history.copy())

        if move1 == move2:
            tie += 1
        elif beats(move1, move2):
            p1_score += 1
        else:
            p2_score += 1

        if verbose:
            print(f"Game {i+1}: P1 ({move1}) vs P2 ({move2})")

        prev_play1 = move1
        prev_play2 = move2
        player1_history.append(move1)
        player2_history.append(move2)

    print(f"Results after {num_games} games:")
    print(f"Player 1 won {p1_score} times")
    print(f"Player 2 won {p2_score} times")
    print(f"Tie: {tie} times")
    return {"player1": p1_score, "player2": p2_score, "tie": tie}

def beats(one, two):
    return (one == "R" and two == "S") or (one == "S" and two == "P") or (one == "P" and two == "R")

# Prebuilt opponents

def quincy(prev_play, opponent_history=[]):
    return "P"

def abbey(prev_play, opponent_history=[]):
    if not prev_play:
        opponent_history.clear()
    if prev_play:
        opponent_history.append(prev_play)

    last_ten = opponent_history[-10:]
    if last_ten.count("R") > last_ten.count("S") and last_ten.count("R") > last_ten.count("P"):
        return "P"
    elif last_ten.count("P") > last_ten.count("R") and last_ten.count("P") > last_ten.count("S"):
        return "S"
    elif last_ten.count("S") > last_ten.count("P") and last_ten.count("S") > last_ten.count("R"):
        return "R"
    else:
        return "R"

def kris(prev_play, opponent_history=[]):
    if not prev_play:
        opponent_history.clear()
    if prev_play:
        opponent_history.append(prev_play)

    if len(opponent_history) > 0:
        last = opponent_history[-1]
        if last == "R":
            return "P"
        elif last == "P":
            return "S"
        else:
            return "R"
    else:
        return "R"

def mrugesh(prev_play, opponent_history=[]):
    if not prev_play:
        opponent_history.clear()
    if prev_play:
        opponent_history.append(prev_play)

    if len(opponent_history) < 2:
        return "R"
    else:
        pattern = "".join(opponent_history[-2:])
        if pattern in ["RR", "RP", "RS"]:
            return "P"
        elif pattern in ["PP", "PR", "PS"]:
            return "S"
        else:
            return "R"
