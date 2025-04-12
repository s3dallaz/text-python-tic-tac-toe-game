def display_board(board):
    print("------------------")
    print(f"| {board[0]} | {board[1]} | {board[2]} |")
    print("------------------")
    print(f"| {board[3]} | {board[4]} | {board[5]} |")
    print("------------------")
    print(f"| {board[6]} | {board[7]} | {board[8]} |")
    print("------------------")

def get_player_move(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): "))
            if 1 <= move <= 9 and board[move - 1] == " ":
                return move - 1
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")
        except EOFError:
            print("Game interrupted. Exiting.")
            return None

def check_win(board):
    win_patterns = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6],
    ]

    for pattern in win_patterns:
        if board[pattern[0]] == board[pattern[1]] == board[pattern[2]] != " ":
            return board[pattern[0]]
    return None

def check_draw(board):
    return " " not in board

def play_game():
    board = [" "] * 9
    player = "X"
    game_over = False

    print("Welcome to Tic-Tac-Toe!")
    display_board(board)

    while not game_over:
        move = get_player_move(board, player)
        if move is None:
            print("Exiting the game.")
            return

        board[move] = player
        display_board(board)

        winner = check_win(board)
        if winner:
            print(f"Player {winner} wins!")
            game_over = True
        elif check_draw(board):
            print("It's a draw!")
            game_over = True
        else:
            player = "O" if player == "X" else "X"

if __name__ == "__main__":
    play_game()
