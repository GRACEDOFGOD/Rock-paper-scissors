import random

def predict_next_move(history, n=2):
    """
    Predict opponent's next move based on last n moves using n-gram frequency.
    """
    if len(history) < n:
        return random.choice(['R', 'P', 'S'])
    
    seq = ''.join(history[-n:])
    # Implement frequency lookup here (mocked)
    # For now, random:
    return random.choice(['R', 'P', 'S'])

def counter_move(move):
    """Return the move that beats the given move."""
    counters = {'R': 'P', 'P': 'S', 'S': 'R'}
    return counters.get(move, random.choice(['R', 'P', 'S']))

def player(prev_play, opponent_history=[]):
    """Professional standard player with stateful opponent history and prediction."""
    if prev_play:
        opponent_history.append(prev_play)

    predicted = predict_next_move(opponent_history)
    move = counter_move(predicted)

    return move
