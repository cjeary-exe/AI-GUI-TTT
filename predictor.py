from joblib import load
import functions as fn

# Load the trained model

model = load("tic_tac_toe_model.joblib")

# Predict

test_board = [
    'X', 'O', 'X',
    'O', 'X', '0',
    '0', 'O', '0'
]

numeric_test = [1 if c == 'X' else -1 if c == 'O' else 0 for c in test_board]

predicted_probs = model.predict_proba([numeric_test])[0]
best_move = predicted_probs.argmax()
print("Predicted best move:", best_move)