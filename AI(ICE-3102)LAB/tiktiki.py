import random

# Initialize the Tic Tac Toe board
board = [" " for _ in range(9)]


def print_board():
    """Prints the Tic Tac Toe board."""
    for row in [board[i * 3 : (i + 1) * 3] for i in range(3)]:
        print("| " + " | ".join(row) + " |")


def check_win(board, player):
    """Checks if a player has won."""
    win_conditions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],  # rows
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],  # columns
        [0, 4, 8],
        [2, 4, 6],  # diagonals
    ]
    return any(
        all(board[cell] == player for cell in condition) for condition in win_conditions
    )


def check_draw(board):
    """Checks if the game is a draw."""
    return " " not in board


def player_move():
    """Takes player's move."""
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if board[move] == " ":
                board[move] = "X"
                break
            else:
                print("Cell already occupied. Choose another one.")
        except (IndexError, ValueError):
            print("Invalid input. Please enter a number between 1 and 9.")


def get_computer_move(difficulty_level):
    """Gets computer's move based on the difficulty level."""
    # 1. Random move (early game)
    if difficulty_level == "easy":
        return random.choice([i for i, cell in enumerate(board) if cell == " "])

    # 2. Block player winning moves (mid game)
    if difficulty_level == "medium":
        # Check if player can win on next move, block it
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                if check_win(board, "X"):
                    board[i] = "O"  # Block the winning move
                    return i
                board[i] = " "  # Undo move

        # Otherwise, pick a random move
        return random.choice([i for i, cell in enumerate(board) if cell == " "])

    # 3. Prioritize winning moves or blocking moves (late game)
    if difficulty_level == "hard":
        # Check if computer can win
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                if check_win(board, "O"):
                    return i
                board[i] = " "  # Undo move

        # Block player if they can win
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                if check_win(board, "X"):
                    board[i] = "O"
                    return i
                board[i] = " "  # Undo move

        # Otherwise, pick center if available, else random
        if board[4] == " ":
            return 4
        return random.choice([i for i, cell in enumerate(board) if cell == " "])


def computer_move(turn_count):
    """Computer's move based on the number of turns (increasing difficulty)."""
    if turn_count < 3:
        difficulty_level = "easy"
    elif turn_count < 6:
        difficulty_level = "medium"
    else:
        difficulty_level = "hard"

    move = get_computer_move(difficulty_level)
    board[move] = "O"
    print(f"Computer chooses position {move + 1}.")


def tic_tac_toe():
    """Main game loop for Tic Tac Toe."""
    turn_count = 0
    while True:
        print_board()
        player_move()
        turn_count += 1

        # Check if player won
        if check_win(board, "X"):
            print_board()
            print("Congratulations! You won the game!")
            break
        elif check_draw(board):
            print_board()
            print("It's a draw!")
            break

        # Computer's move
        computer_move(turn_count)
        turn_count += 1

        # Check if computer won
        if check_win(board, "O"):
            print_board()
            print("Computer won the game!")
            break
        elif check_draw(board):
            print_board()
            print("It's a draw!")
            break


# Start the game
tic_tac_toe()
