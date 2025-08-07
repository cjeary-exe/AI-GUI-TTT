import functions as fn
import numpy as np
from joblib import dump

from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split

# Create the board, 0 = Empty slot

board = [
    '0', '0', '0',
    '0', '0', '0',
    '0', '0', '0',
]

possible_boards = []
fn.generate_all_boards(board, 'X', possible_boards)

# Create empty tables for training

X = [] # The boards to accompany y
y = [] # The best moves to accompany X

# Go through each possible board

for board in possible_boards:

    # If the game is over, skip this board

    if fn.is_game_over(board):
        continue

    # Get the current player

    current_player = fn.whos_turn(board)

    # Loop through every cell in the current board

    best_score = -float('inf') if current_player == 'X' else float('inf')
    best_moves = []

    for cell in fn.get_empty_cells(board):

        # Create a copy of the board

        copy = board.copy()

        # Make the move

        copy[cell] = current_player

        # Use the minimax function to generate a score for this move

        score = fn.minimax(copy)

        # Check who is the current player

        if current_player == 'X':
            if score > best_score:
                best_score = score
                best_moves = [cell]
            elif score == best_score:
                best_moves.append(cell)
        else:
            if score < best_score:
                best_score = score
                best_moves = [cell]
            elif score == best_score:
                best_moves.append(cell)

    # Skip if best move was "None"

    import random
    if best_moves:
        best_move = random.choice(best_moves)
        numeric_board = [1 if c == 'X' else -1 if c == 'O' else 0 for c in board]
        X.append(numeric_board)
        y.append(best_move)

# Convert X and y to numpy arrays

X = np.array(X)
y = np.array(y)

# Split into training/testing

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Create model

model = MLPClassifier(hidden_layer_sizes=(64, 64), max_iter=500)

# Train the model

model.fit(X_train, y_train)

# Dump the model to be used in predictor.py

dump(model, "tic_tac_toe_model.joblib")