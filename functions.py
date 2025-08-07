def who_won(board):
    winning_combos = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for combo in winning_combos:
        values = [board[i] for i in combo]
        if values == ['X', 'X', 'X']:
            return 'X'
        elif values == ['O', 'O', 'O']:
            return 'O'
    return None

def is_full(board):
    return '0' not in board

def generate_all_boards(board, player, all_boards):
    # If terminal state, add the board and return

    all_boards.append(board.copy())

    if who_won(board) is not None or is_full(board):
        return

    # Otherwise try every empty cell
    for i in range(9):
        if board[i] == '0':
            new_board = board.copy()
            new_board[i] = player
            next_player = 'O' if player == 'X' else 'X'
            generate_all_boards(new_board, next_player, all_boards)

def whos_turn(board):
    x_count = board.count('X')
    o_count = board.count('O')
    return 'X' if x_count == o_count else 'O'

def get_empty_cells(board):
    empty_cells = []
    for i in range(9):
        if board[i] == '0':
            empty_cells.append(i)

    return empty_cells

def is_game_over(board):
    if who_won(board) is not None:
        return who_won(board)
    if is_full(board):
        return "Draw"
    else:
        return None

def get_winner(board):
    win_patterns = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    for a,b,c in win_patterns:
        if board[a] == board[b] == board[c] and board[a] != '0':
            return board[a]
    if '0' not in board:
        return 'Draw'
    return None

def score(board):
    if who_won(board) == 'X':
        return +1
    elif who_won(board) == 'O':
        return -1
    else:
        return 0

def print_board(board):
    symbols = {'X': 'X', 'O': 'O', '0': '.'}
    for i in range(0, 9, 3):
        print(' '.join(symbols[c] for c in board[i:i+3]))

def minimax(board):
    if is_game_over(board):
        return score(board)
    turn = whos_turn(board)
    empties = get_empty_cells(board)

    if turn == 'X':
        best_score = -float('inf')
        for empty_cell in empties:
            copy = board.copy()
            copy[empty_cell] = turn
            s = minimax(copy)
            best_score = max(best_score, s)

    else:
        best_score = float('inf')
        for empty_cell in empties:
            copy = board.copy()
            copy[empty_cell] = turn
            s = minimax(copy)
            best_score = min(best_score, s)

    return best_score
