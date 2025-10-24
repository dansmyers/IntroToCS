# Validating Input

## Topics

- The subtraction game
- Forcing the user to give valid input
- `try`-`except` and exception handling

## The subtraction game

Our example for this class is the Subtraction Game, which exists in a lot of variants. Our basic version is as follows:

- There is a pile of 21 stones
- Players alternate turns removing 1, 2 or 3 stones
- The player who takes the last stone is the ***winner*** in our version. A standard variation is to make the player who takes the last stone the loser.

The basic game is below. It uses a `while` loop to play each round. Since we don't know in advance how many rounds will be required, `while` is appropriate. Rather than make two nearly-identical blocks of code for player 1 and then player 2, we'll write the loop to play one round and use a variable to keep track of the current player.

A good strategy for larger programs is to **develop incrementally**. Focus on making the basic game work first, with the assumption that the user will submit valid input, then iterate and gradually add more features.

```
"""
The Subtraction Game

Starts with a pile of 21 stones
On each turn a player can remove 1, 2, or 3 stones from the pile
The player that takes the last stone WINS
"""

# Keep track of the number of stones
stones = 21

# Use a variable to keep track of the current player's turn
current_player = 1

# Use a while loop to play until the number of stones is zero
playing_game = True
while playing_game:

    # Print the current player
    print(f'It is player {current_player}\'s turn.')

    # Print the number of stones
    print(f'There are {stones} stones remaining.')

    # Prompt the user to remove 1, 2, or 3 stones
    removed_stones = int(input('Enter 1, 2, or 3 to remove: '))
  
    # Reduce the number of stones in the pile
    stones -= removed_stones

    # Check if the winning condition has been met
    if stones == 0:
        print(f'Player {current_player} wins!')
        playing_game = False

    # else, switch to the other player for the next turn
    else:
        current_player = (current_player % 2) + 1
```

## Forcing valid input
Suppose we want to force the user to always input 1, 2 or 3. The block below uses a `while` loop that checks the user's given value and repeats until the enters 1, 2 or 3. It also requires that the user can't remove more than the remaining number of stones if there are only 1 or 2 left.
```
# Prompt the user to remove 1, 2, or 3 stones
getting_input = True
while getting_input:
    removed_stones = int(input('Enter 1, 2, or 3 to remove: '))

    if removed_stones < 1 or removed_stones > 3:
        print('You must enter 1, 2, or 3.')
    elif removed_stones > stones:
        print('That is too many stones!')
    else:
        getting_input = False
```
This is similar to our prevoius loop problems. It uses a flag variable (`getting_input`) to control how long the loop executes.

## Exception handling
The version above will still fail if the user enters a non-numeric string, like `"two"`. Recall that the `int` function throws a `ValueError` if the input string is non-numeric.

Python uses the `try` and `except` keywords to handle exceptions.

- Code given in a `try` block is executed as written. If no errors occur, the block executes and ends normally.
- If an exception is thrown, Python jumps down to the `except` block and executes the code it contains to handle the exception.

The version below uses this approach. If a `ValueError` occurs in the `try` block, then the program jumps down to `except` to print an error message, then continues with another iteration of the input-gettting loop.
```
# Prompt the user to remove 1, 2, or 3 stones
getting_input = True
while getting_input:

    # try to execute the block of code in the try statement
    # If no error occurs, the block executes as written
    try:
        removed_stones = int(input('Enter 1, 2, or 3 to remove: '))

        if removed_stones < 1 or removed_stones > 3:
            print('You must enter 1, 2, or 3.')
        elif removed_stones > stones:
            print('That is too many stones!')
        else:
            getting_input = False

    # If an exception happens in the try block, jump down to the except
    # block and run its code to handle the exception
    #
    # except can specify what type of error it handles
    except ValueError:
        print('You must enter a numeric value.')
```


Observe that the `except` statement specifies that it only triggers on a `ValueError`. This isn't required, but it's often useful to specify exactly what kind of exceptions will trigger a given block. In this case, we want to handle `ValueError` without crashing the program, but other kinds of errors like `KeyboadInterrupt` are still anomalous conditions and should still terminate the program.
```
# General exception: catches ALL exceptions, which may not be what we want
except:
    print('You must enter a numeric value.')
```
```
# This exception only catches ValueErrors
except ValueError:
    print('You must enter a numeric value.')
```
It's possible to have multiple `except` statements for different kinds of exceptions that might be thrown during the `try` block's code.
