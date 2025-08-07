import functions as fn
from joblib import load
import numpy as np

# Load trained model
model = load("tic_tac_toe_model.joblib")

# Initial empty board
board = ['0'] * 9

# Choose who is X and who is O
human_player = input("Do you want to be X or O? ").upper()
ai_player = 'O' if human_player == 'X' else 'X'

print(f"You are {human_player}, AI is {ai_player}\n")

def get_human_move(board):
    valid = fn.get_empty_cells(board)
    while True:
        try:
            move = int(input(f"Enter your move (0-8): "))
            if move in valid:
                return move
            else:
                print("Invalid move, try again")
        except ValueError:
            print("Enter a number between 0 and 8.")

def get_ai_move(board):
    numeric_board = [1 if c == 'X' else -1 if c == 'O' else 0 for c in board]
    probs = model.predict_proba([numeric_board])[0]

    # Mask invalid moves
    for i in range(9):
        if board[i] != '0':
            probs[i] = -1

    return np.argmax(probs)

# Main
while not fn.is_game_over(board):
    fn.print_board(board)
    print()

    current_player = fn.whos_turn(board)

    if current_player == human_player:
        move = get_human_move(board)
    else:
        print("AI is thinking...")
        move = get_ai_move(board)

    board[move] = current_player

fn.print_board(board)
winner = fn.who_won(board)
if winner:
    print(f"{winner} wins!")
else:
    print("It's a draw!")