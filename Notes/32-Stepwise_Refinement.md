# Stepwise Refinement

Complete the tic-tac-toe activity in the `Actvities` directory. A solution is given below.

```
"""
TIC-TAC-TOE
"""

# Dictionary stores the symbol at each position
#
# Each square has a number 1 to 9
# At the beginning all 9 numbers are mapped to None
board = {}
for i in range(1, 10):
    board[i] = None


def print_player(player):
    print()  # Blank line
    print(f'Player {player}, it\'s your turn.')


def print_board():
    """
    Print the board
    """
    for i in range(1, 10):
        # If the space is open, print its number
        # If occupied, print its symbol
        if board[i] == None:
            print(f' {i} ', end='')
        else:
            print(f' {board[i]} ', end='')

        # Move to the next row
        if i % 3 == 0:
            print()

            # Print horizontal lines after rows 1 and 2
            if i == 3 or i == 6:
                print('-----------------')
        else:
            print(' | ', end='')

    print()


def get_move():
    """
    Read the player's move 1-9

    The move must be in that range and non-occupied
    """

    reading_input = True
    while reading_input:
        try:
            move = int(input('Choose an open square 1-9: '))

            if move < 1 or move > 9:
                print('That is not a valid choice.')
            elif board[move] != None:
                print('Choose an open spot.')
            else:
                reading_input = False

        except ValueError:
            print('Enter a number 1-9.')

    return move


def check_first_row():
    return board[1] != None and (board[1] == board[2] == board[3])


def check_second_row():
    return board[4] != None and (board[4] == board[5] == board[6])


def check_third_row():
    return board[7] != None and (board[7] == board[8] == board[9])


def check_rows():
    """
    Return True if there are three matching symbols in any row
    """
    return check_first_row() or check_second_row() or check_third_row()


def check_first_col():
    return board[1] != None and (board[1] == board[4] == board[7])


def check_second_col():
    return board[2] != None and (board[2] == board[5] == board[8])


def check_third_col():
    return board[3] != None and (board[3] == board[6] == board[9])


def check_cols():
    """
    Return True if there are three matching symbols in any column
    """
    return check_first_col() or check_second_col() or check_third_col()


def check_first_diag():
    return board[1] != None and (board[1] == board[5] == board[9])


def check_second_diag():
    return board[3] != None and (board[3] == board[5] == board[7])


def check_diags():
    """
    Return True if there are three matching symbols in any diagonal
    """
    return check_first_diag() or check_second_diag()


def check_win():
    """
    Return True if there are three matching symbols on the board
    """
    return check_rows() or check_cols() or check_diags()


def main():
    """
    Main tic-tac-toe game
    """

    # Keep track of the current player's symbol
    player = 'X'

    # Turn counter
    turn = 1

    # Main game loop
    while True:

        # 1. Print the current player
        print_player(player)

        # 2. Print the board
        print_board()

        # 3. Get the current player's move
        move = get_move()

        # 4. Update the board
        board[move] = player

        # 5. Check for a winning condition
        if check_win():
            print_board()
            print(f'Player {player} wins!')
            break
        elif turn == 9:
            print_board()
            print('Draw!')
            break

        # 6. If the game didn't end, move to the next turn
        player = 'O' if player == 'X' else 'X'
        turn += 1

if __name__ == '__main__':
    main()
```
