#include <stdio.h>
#include <stdlib.h>
#include <time.h>

char board[3][3];
int moves = 0;

// Function to initialize the board
void initializeBoard() {
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
            board[i][j] = ' ';
}

// Function to print the board
void printBoard() {
    for (int i = 0; i < 3; i++) {
        printf("| %c | %c | %c |\n", board[i][0], board[i][1], board[i][2]);
        if (i < 2) printf("|---|---|---|\n");
    }
    printf("\n");
}

// Function to check for a winner
int checkWinner() {
    for (int i = 0; i < 3; i++) {
        if (board[i][0] == board[i][1] && board[i][1] == board[i][2] && board[i][0] != ' ')
            return 1;
        if (board[0][i] == board[1][i] && board[1][i] == board[2][i] && board[0][i] != ' ')
            return 1;
    }
    if (board[0][0] == board[1][1] && board[1][1] == board[2][2] && board[0][0] != ' ')
        return 1;
    if (board[0][2] == board[1][1] && board[1][1] == board[2][0] && board[0][2] != ' ')
        return 1;
    return 0;
}

// Function to check for a draw
int checkDraw() {
    return moves == 9;
}

// Function to make the human move
void humanMove() {
    int move;
    printf("Enter your move (1-9): ");
    scanf("%d", &move);
    int row = (move - 1) / 3;
    int col = (move - 1) % 3;

    if (board[row][col] == ' ') {
        board[row][col] = 'X';
        moves++;
    } else {
        printf("Invalid move! Try again.\n");
        humanMove();
    }
}

// Function to make the CPU move
void cpuMove() {
    int move;
    printf("Computer's turn!\n");
    do {
        move = rand() % 9 + 1;
        int row = (move - 1) / 3;
        int col = (move - 1) % 3;
        if (board[row][col] == ' ') {
            board[row][col] = 'O';
            moves++;
            break;
        }
    } while (1);
    printf("Computer chooses position %d.\n", move);
}

// Main game loop
int main() {
    srand(time(0));
    initializeBoard();
    while (1) {
        printBoard();
        humanMove();
        if (checkWinner()) {
            printBoard();
            printf("You win!\n");
            break;
        }
        if (checkDraw()) {
            printBoard();
            printf("It's a draw!\n");
            break;
        }

        cpuMove();
        if (checkWinner()) {
            printBoard();
            printf("Computer wins!\n");
            break;
        }
        if (checkDraw()) {
            printBoard();
            printf("It's a draw!\n");
            break;
        }
    }
    return 0;
}
