# Rock-paper-scissors
import random

def player(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)

    # Use a random choice strategy as a baseline
    possible_moves = ['R', 'P', 'S']
    
    # If you want, you can track the opponent's history and build smarter strategies here
    if len(opponent_history) > 0:
        # Example strategy: Play a counter to their last move
        last_move = opponent_history[-1]
        if last_move == "R":
            return "P"  # Counter rock with paper
        elif last_move == "P":
            return "S"  # Counter paper with scissors
        elif last_move == "S":
            return "R"  # Counter scissors with rock

    # For the first move, or if no pattern is detected, return a random move
    return random.choice(possible_moves)
