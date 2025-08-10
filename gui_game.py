import tkinter as tk
from tkinter import messagebox
from joblib import load
import functions as fn

# Load model

model = load("tic_tac_toe_model.joblib")

# Game state

board = ['0'] * 9
player_symbol = 'X'
ai_symbol = 'O'
buttons = []

def reset_game():
    global board
    board = ['0'] * 9
    for btn in buttons:
        btn.config(text="", state=tk.NORMAL)

def on_click(i):
    global board

    if board[i] != '0':
        return

    board[i] = player_symbol
    buttons[i].config(text=player_symbol, state=tk.DISABLED)

    if fn.is_game_over(board):
        end_game()
        return

    ai_move()

def ai_move():
    global board

    numeric_board = [1 if c == player_symbol else -1 if c == ai_symbol else 0 for c in board]
    predicted_move = model.predict([numeric_board])[0]

    if board[predicted_move] == '0':
        board[predicted_move] = ai_symbol
        buttons[predicted_move].config(text=ai_symbol, state=tk.DISABLED)

    if fn.is_game_over(board):
        end_game()

def end_game():
    winner = fn.get_winner(board)
    if winner:
        messagebox.showinfo("Congratulations!", f"{winner} wins!")
    else:
        messagebox.showinfo("Congratulations!", f"It's a draw!")
    for btn in buttons:
        btn.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Tic Tac Toe AI")

frame = tk.Frame(root)
frame.pack()

for i in range(9):
    btn = tk.Button(frame, text="", font=('Arial', 32), width=3, height=1,
                    command=lambda i=i: on_click(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

reset_button = tk.Button(root, text="Redo", command=reset_game)
reset_button.pack(pady=10)

reset_game()
root.mainloop()