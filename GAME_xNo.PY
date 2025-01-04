# Tic Tac Toe Game in Python
def print_board(board):
    
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_draw(board):
    return all(cell != " " for row in board for cell in row)

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0

    print("Welcome to Tic Tac Toe! Player X and Player O take turns.")
    print_board(board)

    while True:
        print(f"Player {players[current_player]}'s turn.")
        try:
            row = int(input("Enter row (0, 1, 2): "))
            col = int(input("Enter column (0, 1, 2): "))

            if row not in range(3) or col not in range(3):
                print("Invalid input. Please enter values between 0 and 2.")
                continue

            if board[row][col] != " ":
                print("Cell already taken. Choose another.")
                continue

            board[row][col] = players[current_player]
            print_board(board)

            if check_winner(board, players[current_player]):
                print(f"Player {players[current_player]} wins!")
                break

            if is_draw(board):
                print("It's a draw!")
                break

            current_player = 1 - current_player
        except ValueError:
            print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    play_game()
