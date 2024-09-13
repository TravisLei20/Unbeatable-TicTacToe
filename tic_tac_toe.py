import numpy as np

# Constants
MINIMAX_X_SQUARE = 2
MINIMAX_O_SQUARE = 1
MINIMAX_EMPTY_SQUARE = 0

MINIMAX_X_WINNING_SCORE = 10
MINIMAX_O_WINNING_SCORE = -10
MINIMAX_DRAW_SCORE = 0
MINIMAX_NOT_ENDGAME = -1

# Board size
MINIMAX_BOARD_ROWS = 3
MINIMAX_BOARD_COLUMNS = 3

# Initialize the board to all empty squares.
def minimax_initBoard():
    return np.full((MINIMAX_BOARD_ROWS, MINIMAX_BOARD_COLUMNS), MINIMAX_EMPTY_SQUARE)

# Determine if the game is over by looking at the score.
def minimax_isGameOver(score):
    return score != MINIMAX_NOT_ENDGAME

# Returns the score of the board, based upon the player turn and the board.
def minimax_computeBoardScore(board, player_is_x):
    # Check all the cases to see if X wins
    if (np.all(board[0, :] == MINIMAX_X_SQUARE) or
        np.all(board[1, :] == MINIMAX_X_SQUARE) or
        np.all(board[2, :] == MINIMAX_X_SQUARE) or
        np.all(board[:, 0] == MINIMAX_X_SQUARE) or
        np.all(board[:, 1] == MINIMAX_X_SQUARE) or
        np.all(board[:, 2] == MINIMAX_X_SQUARE) or
        np.all(np.diag(board) == MINIMAX_X_SQUARE) or
        np.all(np.diag(np.fliplr(board)) == MINIMAX_X_SQUARE)):
        return MINIMAX_X_WINNING_SCORE

    # Check all the cases to see if O wins
    if (np.all(board[0, :] == MINIMAX_O_SQUARE) or
        np.all(board[1, :] == MINIMAX_O_SQUARE) or
        np.all(board[2, :] == MINIMAX_O_SQUARE) or
        np.all(board[:, 0] == MINIMAX_O_SQUARE) or
        np.all(board[:, 1] == MINIMAX_O_SQUARE) or
        np.all(board[:, 2] == MINIMAX_O_SQUARE) or
        np.all(np.diag(board) == MINIMAX_O_SQUARE) or
        np.all(np.diag(np.fliplr(board)) == MINIMAX_O_SQUARE)):
        return MINIMAX_O_WINNING_SCORE

    # Check if there are any empty spaces left
    if np.any(board == MINIMAX_EMPTY_SQUARE):
        return MINIMAX_NOT_ENDGAME

    # If no one won and there are no more spaces left, the game ends in a draw
    return MINIMAX_DRAW_SCORE

# Minimax algorithm to calculate the best move
def minimax(board, current_player_is_x):
    scores = []
    moves = []

    # Check if the game is finished
    score = minimax_computeBoardScore(board, current_player_is_x)
    if minimax_isGameOver(score):
        return score

    for row in range(MINIMAX_BOARD_ROWS):
        for col in range(MINIMAX_BOARD_COLUMNS):
            if board[row, col] == MINIMAX_EMPTY_SQUARE:
                board[row, col] = MINIMAX_X_SQUARE if current_player_is_x else MINIMAX_O_SQUARE
                scores.append(minimax(board, not current_player_is_x))
                moves.append((row, col))
                board[row, col] = MINIMAX_EMPTY_SQUARE

    if current_player_is_x:
        max_score_index = np.argmax(scores)
        choice = moves[max_score_index]
        return scores[max_score_index]
    else:
        min_score_index = np.argmin(scores)
        choice = moves[min_score_index]
        return scores[min_score_index]

# Compute the next move using the minimax algorithm
def minimax_computeNextMove(board, current_player_is_x):
    scores = []
    moves = []

    for row in range(MINIMAX_BOARD_ROWS):
        for col in range(MINIMAX_BOARD_COLUMNS):
            if board[row, col] == MINIMAX_EMPTY_SQUARE:
                board[row, col] = MINIMAX_X_SQUARE if current_player_is_x else MINIMAX_O_SQUARE
                scores.append(minimax(board, not current_player_is_x))
                moves.append((row, col))
                board[row, col] = MINIMAX_EMPTY_SQUARE

    if current_player_is_x:
        max_score_index = np.argmax(scores)
        return moves[max_score_index]
    else:
        min_score_index = np.argmin(scores)
        return moves[min_score_index]

# Print the board
def print_board(board):
    for row in board:
        print(" ".join(['X' if cell == MINIMAX_X_SQUARE else 'O' if cell == MINIMAX_O_SQUARE else '.' for cell in row]))
    print()

# Main game loop
def main():
    board = minimax_initBoard()
    current_player_is_x = True

    while True:
        print_board(board)
        if current_player_is_x:
            row, col = minimax_computeNextMove(board, current_player_is_x)
            board[row, col] = MINIMAX_X_SQUARE
        else:
            row = int(input("Enter row (0, 1, 2): "))
            col = int(input("Enter column (0, 1, 2): "))
            if board[row, col] == MINIMAX_EMPTY_SQUARE:
                board[row, col] = MINIMAX_O_SQUARE
            else:
                print("Invalid move. Try again.")
                continue

        score = minimax_computeBoardScore(board, current_player_is_x)
        if minimax_isGameOver(score):
            print_board(board)
            if score == MINIMAX_X_WINNING_SCORE:
                print("X wins!")
            elif score == MINIMAX_O_WINNING_SCORE:
                print("O wins!")
            else:
                print("It's a draw!")
            break

        current_player_is_x = not current_player_is_x

if __name__ == "__main__":
    main()
  