# Tic-Tac-Toe feat. Stepwise Refinement

## Overview

**Stepwise refinement** is a programming strategy that empahsizes breaking a complex problem down into discrete substeps, then implementing a function to perform each substep. Those functions might themselves consist of multiple steps, which can be broken down and implemented as their own functions. This process continues until you reach a level of complexity that can be implemented as a simple block of code with no major substeps.

This activity will lead you through writing a tic-tac-toe game using the refinement appproach. It will also show off using a dictionary to manage the state of the game.

## Starter Code

`cd` to your `Dictionaries` directory. Create a new file named `tic_tac_toe.py` and put the following code inside it:
```
"""
TIC-TAC-TOE
"""

# TODO: Declare the board


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

        # 2. Print the board

        # 3. Get the current player's move

        # 4. Update the board

        # 5. Check for a winning condition

        # 6. If the game didn't end, move to the next turn

if __name__ == '__main__':
    main()
```
The top-level game-playing function is called `main`. It contains some lines to initialize the player symbol, which we'll use to keep track of whose turn it is, and then steps inside the main game loop. The following sections will write functions to implement each of the game steps.

## Declare the Board
The top of the file has a place to declare the board data structure. Here's the strategy:

- Let each board position be a number 1 to 9.
```
  1  |  2  |  3 
-----------------
  4  |  5  |  6 
-----------------
  7  |  8  |  9
```

- `board` will be a dictionary that maps each number 1 to 9 to the symbol at that position, or `None` if no symbol has been assigned yet.


Put the following code at the top of the file, in the place marked by the `TODO` comment.
```
# Dictionary stores the symbol at each position
#
# Each square has a number 1 to 9
# At the beginning all 9 numbers are mapped to None
board = {}
for i in range(1, 10):
    board[i] = None
```

## Print the Player
The stepwise refinement strategy says that we should break the top-level problem into substeps, then write functions to implement each substep. The main game loop in `main` contains comments specifiying the substeps.

The first step is to print the current player. Add a call to a function called `print_player` that takes the current player as input:
```
# 1. Print the current player
print_player(player)
```
The define the new function above `main`:
```
def print_player(player):
    print()  # Blank line
    print(f'Player {player}, it\'s your turn.')
```

## Print the Board
We'll now repeat with the board. Add a function call to `print_board` in the main game loop.
```
# 2. Print the board
print_board()
```
This function loops through the entries 1 to 9 in the dictionary and prints the 3x3 grid. If a position has a symbol mapped, it prints the symbol (X or O), but if the mapping is `None` it prints the number instead, so the user can select that position as a move.
```
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

            # Add code here to print horizontal lines between the rows
        else:
            print(' | ', end='')

    print()
```
At this point, run the program and verify that it prints the opening message and the grid. Use `CTRL + c` to end the loop.

## Get the Player's Move
Add another function call for step 3:
```
# 3. Get the current player's move
move = get_move()
```
This function will prompt the user to select a square 1 through 9, checking that the player enters a valid number and that the square is not already taken.
```
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
```
Take a look at this function. It reuses some of our techniques from the previous input-getting example. Note the use of `try`-`except` to deal with the case where the user enters something non-numeric.

The lines
```
elif board[move] != None:
    print('Choose an open spot.')
```
Check that the user's chosen board space is currently unoccupied.

Once you have that function in place, you can complete step 4 with a single line:
```
# 4. Update the board
board[move] = player
```
This line assigns the current player's symbol (`X` or `O`) to the numbered position chosen by the player.

## Check the Winning Condition
The last step is to check the outcome. If the current player just completed a row of three symbols in any row, column, or diagonal, then they've just won. the other option is that the player took the last space, but didn't win, which means the game is a draw. We'll move the win-checking code into a function that you'll implement in just a minute.
```
# 5. Check for a winning condition
if check_win():
    print_board()
    print(f'Player {player} wins!')
    break
elif turn == 9:
    print_board()
    print('Draw!')
    break
```
Step 6 is only a couple of lines that switch the current player symbol and increment the turn counter.
```
# 6. If the game didn't end, move to the next turn
player = 'O' if player  == 'X' else 'X'
turn += 1
```
Notice how you can toggle the player symbol in one line.

### `check_win`
Let's think about the `check_win` function. It needs to return `True` if there are three of the same symbol in any row, column, or diagonal.

This is a perfect setup for the stepwise refinemnt approach: break the overall task of checking for a win into three subtasks that check each of the three groups:
```
def check_win():
    """
    Return True if there are three matching symbols on the board
    """
    return check_rows() or check_cols() or check_diags()
```

What about checking the rows? This itself be decomposed into checking the first row, the second, and the third:
```
def check_rows():
    """
    Return True if there are three matching symbols in any row
    """
    return check_first_row() or check_second_row() or check_third_row()
```
Each row-checking method is a single comparison:
```
def check_first_row():
    return board[1] != None and (board[1] == board[2] == board[3])
```
The function returns `True` if the three positions in the first row have the same value and aren't `None`.

**Finish the rest of the row-checking functions. Then implement `check_cols` and `check_diags` using the same strategy.** All of the functions will look similar, but you'll choose the correct positions for each test that you need.

## Play

Once you have the game finished, play and test it. Think about the cases you would need to check to verify that your program is working correctly.



