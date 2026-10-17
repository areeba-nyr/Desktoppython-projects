import random

def print_board(board):
    print()
    display = []
    for i in range(9):
        if board[i] == " ":
            display.append(str(i + 1))
        else:
            display.append(board[i])
    for i in range(3):
        row = display[i*3:i*3+3]
        print(" | ".join(row))
        if i < 2:
            print("---------")
    print()

def check_winner(board, player):
    win_combos = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    for combo in win_combos:
        if all(board[i] == player for i in combo):
            return True
    return False

def is_board_full(board):
    return " " not in board

def computer_move(board):
    empty_spots = [i for i in range(9) if board[i] == " "]
    return random.choice(empty_spots)

def player_move(board):
    while True:
        move = input("Enter your move (1-9): ")
        if not move.isdigit():
            print("Please enter a number.")
            continue
        move = int(move) - 1
        if move < 0 or move > 8:
            print("Enter a number between 1 and 9.")
            continue
        if board[move] != " ":
            print("That spot is taken. Try again.")
            continue
        return move

def play_game():
    board = [" "] * 9
    print("Welcome to Tic-Tac-Toe! You are X, computer is O.")
    print_board(board)

    while True:
        move = player_move(board)
        board[move] = "X"
        print_board(board)

        if check_winner(board, "X"):
            print("You win!")
            break
        if is_board_full(board):
            print("It's a draw!")
            break

        move = computer_move(board)
        board[move] = "O"
        print(f"Computer played position {move + 1}")
        print_board(board)

        if check_winner(board, "O"):
            print("Computer wins!")
            break
        if is_board_full(board):
            print("It's a draw!")
            break

play_game()