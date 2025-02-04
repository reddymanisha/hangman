import os

# Function to display the Tic-Tac-Toe board
def display_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen for better UI
    print("\n")
    print("  {} | {} | {} ".format(board[0], board[1], board[2]))
    print(" ---|---|---")
    print("  {} | {} | {} ".format(board[3], board[4], board[5]))
    print(" ---|---|---")
    print("  {} | {} | {} ".format(board[6], board[7], board[8]))
    print("\n")

# Function to check for a winner
def check_winner(board, player):
    win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
                        (0, 4, 8), (2, 4, 6)]            # Diagonals
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

# Main function to play Tic-Tac-Toe
def play_tic_tac_toe():
    board = [' '] * 9  # Empty board
    current_player = 'X'  # Player X starts
    moves = 0 # Track the number of moves

    while moves < 9: # The game runs for a maximum of 9 moves
        display_board(board) # shows the current board
        try:
            move = int(input(f"Player {current_player}, enter a position (1-9): ")) - 1
            if move < 0 or move >= 9 or board[move] != ' ':
                print("Invalid move! Try again.")
                continue

            board[move] = current_player # place the player's symbol
            moves += 1 

            if check_winner(board, current_player):
                display_board(board) # show final board
                print(f"🎉 Player {current_player} wins! 🎉")
                return

            # Switch players
            current_player = 'O' if current_player == 'X' else 'X'

        except ValueError:
            print("Invalid input! Please enter a number between 1-9.")

    display_board(board)
    print("It's a tie! 🤝")

# Run the game
if __name__ == "__main__":
    play_tic_tac_toe()
