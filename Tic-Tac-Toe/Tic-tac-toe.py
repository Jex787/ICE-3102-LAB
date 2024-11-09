import random

# Global variables
board = [[' ' for _ in range(3)] for _ in range(3)]
moves = 0

# Function to initialize the board
def initialize_board():
    global board, moves
    board = [[' ' for _ in range(3)] for _ in range(3)]
    moves = 0

# Function to print the board
def print_board():
    for i in range(3):
        print(f"| {board[i][0]} | {board[i][1]} | {board[i][2]} |")
        if i < 2:
            print("|---|---|---|")
    print("\n")

# Function to check for a winner
def check_winner():
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return True
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return True
    return False

# Function to check for a draw
def check_draw():
    return moves == 9

# Function to make the human move
def human_move():
    global moves
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            row, col = divmod(move, 3)
            if board[row][col] == ' ':
                board[row][col] = 'X'
                moves += 1
                break
            else:
                print("Invalid move! Try again.")
        except (ValueError, IndexError):
            print("Please enter a valid number between 1 and 9.")

# Function to make the CPU move
def cpu_move():
    global moves
    print("Computer's turn!")
    while True:
        move = random.randint(1, 9) - 1
        row, col = divmod(move, 3)
        if board[row][col] == ' ':
            board[row][col] = 'O'
            moves += 1
            print(f"Computer chooses position {move + 1}.")
            break

# Main game loop
def main():
    initialize_board()
    while True:
        print_board()
        human_move()
        if check_winner():
            print_board()
            print("You win!")
            break
        if check_draw():
            print_board()
            print("It's a draw!")
            break

        cpu_move()
        if check_winner():
            print_board()
            print("Computer wins!")
            break
        if check_draw():
            print_board()
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
