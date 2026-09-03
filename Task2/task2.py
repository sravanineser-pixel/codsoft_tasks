import math

# Display the board
def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")


# Check whether a player has won
def check_winner(board, player):
    winning_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for combination in winning_combinations:
        if all(board[i] == player for i in combination):
            return True

    return False


# Check whether the board is full
def is_board_full(board):
    return all(cell != " " for cell in board)


# Minimax algorithm
def minimax(board, depth, is_maximizing):

    # AI wins
    if check_winner(board, "O"):
        return 10 - depth

    # Human wins
    if check_winner(board, "X"):
        return depth - 10

    # Draw
    if is_board_full(board):
        return 0

    # AI's turn
    if is_maximizing:
        best_score = -math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"

                score = minimax(board, depth + 1, False)

                board[i] = " "

                best_score = max(best_score, score)

        return best_score

    # Human's turn
    else:
        best_score = math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"

                score = minimax(board, depth + 1, True)

                board[i] = " "

                best_score = min(best_score, score)

        return best_score


# Find the best move for AI
def find_best_move(board):
    best_score = -math.inf
    best_move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"

            score = minimax(board, 0, False)

            board[i] = " "

            if score > best_score:
                best_score = score
                best_move = i

    return best_move


# Get human player's move
def human_move(board):

    while True:
        try:
            move = int(input("Enter your position (1-9): "))

            if move < 1 or move > 9:
                print("Please enter a number between 1 and 9.")
                continue

            index = move - 1

            if board[index] != " ":
                print("That position is already occupied.")
                continue

            board[index] = "X"
            break

        except ValueError:
            print("Please enter a valid number.")


# Main game
def play_game():

    board = [" "] * 9

    print("\n==============================")
    print("     TIC-TAC-TOE AI")
    print("==============================")
    print("You are X")
    print("AI is O")

    print("\nBoard positions:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")

    while True:

        # Human turn
        human_move(board)
        print_board(board)

        if check_winner(board, "X"):
            print("🎉 Congratulations! You won!")
            break

        if is_board_full(board):
            print("🤝 It's a draw!")
            break

        # AI turn
        print("🤖 AI is thinking...")

        ai_move = find_best_move(board)
        board[ai_move] = "O"

        print_board(board)

        if check_winner(board, "O"):
            print("🤖 AI wins! Better luck next time.")
            break

        if is_board_full(board):
            print("🤝 It's a draw!")
            break


# Start the game
if __name__ == "__main__":
    play_game()
