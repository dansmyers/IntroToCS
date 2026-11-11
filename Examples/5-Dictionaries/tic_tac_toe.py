"""
Tic-tac-toe using stepwise refinement and a dictionary to
represent the board
"""


def print_board(board):
    """
    Print the 3x3 grid
    If a spot is unoccupied, print its number position 1-9
    If a spot is occupied, print its symbol 'X' or 'O'
    """

    for i in range(1, 10):
        if board[i] == None:
            print(i, end='\t')  # Print number for unoccupied spaces
        else:
            print(board[i], end='\t')  # Print symbol for occupied spaces

        # Every third output, go to the next line
        if i % 3 == 0:
            print()

def get_move(board):
    """
    Return the player's choice of open square 1-9
    """

    getting_input = True
    while getting_input:
        move = int(input('Choose an open square 1-9: '))

        # Check if the response is valid
        if move < 1 or move > 9:
            print('That is not a valid move.')
        elif board[move] != None:
            print('That square is occupied.')
        else:
            return move

def check_row_1(board):
    return board[1] != None and board[1] == board[2] == board[3]
def check_row_2(board):
    return board[4] != None and board[4] == board[5] == board[6]
def check_row_3(board):
    return board[7] != None and board[7] == board[8] == board[9]
def check_rows(board):
    return check_row_1(board) or check_row_2(board) or check_row_3(board)

def check_col_1(board):
    return board[1] != None and board[1] == board[4] == board[7]
def check_col_2(board):
    return board[2] != None and board[2] == board[5] == board[8]
def check_col_3(board):
    return board[3] != None and board[3] == board[6] == board[9]
def check_cols(board):
    return check_col_1(board) or check_col_2(board) or check_col_3(board)

def check_main_diag(board):
    return board[1] != None and board[1] == board[5] == board[9]
def check_off_diag(board):
    return board[3] != None and board[3] == board[5] == board[7]
def check_diags(board):
    return check_main_diag(board) or check_off_diag(board)

def check_win(board):
    """
    Return True if any row, column, or diagonal contains three matching
    non-None entries
    """
    return check_rows(board) or check_cols(board) or check_diags(board)


def play_tic_tac_toe():
    """
    Main game function
    """

    # Setup the board
    board = {}

    # Initialize the nine square to None (meaning unoccupied)
    for i in range(1, 10):
        board[i] = None

    # Declare variables for the player and other information
    player = 'X'
    num_moves = 0

    # Main game loop
    playing = True
    while playing:

        # 1. Print the current player
        print(player)

        # 2. Print the board
        print_board(board)

        # 3. Get the current player's move
        move = get_move(board)

        # 4. Update the board
        board[move] = player
        num_moves += 1

        # 5. Check win/draw/switch conditions
        if check_win(board):
            print('You just won!')
            playing = False
        elif num_moves == 9:
            print('It is a draw.')
            playing = False
        else:
            player = 'O' if player == 'X' else 'X'


### Main
play_tic_tac_toe()
