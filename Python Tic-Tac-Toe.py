import random

def display_board(board):
    """
    Prints the Tic-Tac-Toe board in a user-friendly format.
    """
    print("+---+---+---+")
    print(f"| {board[0] or ' '} | {board[1] or ' '} | {board[2] or ' '} |")
    print("+---+---+---+")
    print(f"| {board[3] or ' '} | {board[4] or ' '} | {board[5] or ' '} |")
    print("+---+---+---+")
    print(f"| {board[6] or ' '} | {board[7] or ' '} | {board[8] or ' '} |")
    print("+---+---+---+")



def get_player_move(board, player):
    """
    Gets the player's move (1-9) and validates it.
    """
    while True:
        try:
            move = int(input(f"Okay, {player}, it's your turn. Where do you want to go? (1-9): "))
            if 1 <= move <= 9 and board[move - 1] == " ":
                return move - 1
            else:
                print("Hmm, that spot's not free. Try again.")
        except ValueError:
            print("Oops, that's not a number! Please enter a number between 1 and 9.")
        except EOFError:
            print("Game interrupted. Exiting.")
            return None

def check_win(board):
    """
    Checks if there is a winner.
    """
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
    """
    Checks if the game is a draw.
    """
    return " " not in board

def play_game():
    """
    Main function to play the Tic-Tac-Toe game.
    """
    board = [" "] * 9
    player = "X"
    game_over = False

    print("Welcome to Tic-Tac-Toe! Let's have some fun!")
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
            print(f"Great job! Player {winner} takes the win!")
            game_over = True
        elif check_draw(board):
            print("Looks like it's a tie! Good game, everyone.")
            game_over = True
        else:
            # Switch player
            player = "O" if player == "X" else "X"
            # Add a little encouragement
            print(f"Alright, {player}, your turn!")

    Play_again()

def Play_again():
    """
    Asks the player if they want to play again.  Handles input validation.
    """
    while True:
        print("Want to play again?")
        print("1. Play again!")
        print("2. Exit game!")
        pick = input("Please pick a number (1 or 2): ")
        if pick == '1':
            play_game()  # Restart the game
            break # Exit the loop, play_game() will start the new game.
        elif pick == '2':
            print("Thanks for playing!")
            break  # Exit the loop, ending the program
        else:
            print(f"You entered a wrong input: {pick}. Please enter 1 or 2.")
            # No break here, loop back to ask again
if __name__ == "__main__":
    play_game()
