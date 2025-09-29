# Functions That Make Choices

## Topics

- RPS with functions example
- `None`

## Rock-Paper-Scissors with function

Complete the `3-RPS_with_Functions` activity in the `Activities` directory. Here is a solution.
```
"""
A Rock-Paper-Scissors game that plays one round of human vs. computer
"""

# Imports
from random import randint

# Declare constant variables representing the three moves
ROCK = 1
PAPER = 2
SCISSORS = 3

### Put all functions in this section
def print_welcome_and_moves():
    print('Welcome to RPS.')
    print('1. Rock')
    print('2. Paper')
    print('3. Scissors')

def read_player_move():

    # Read the player's input
    move = int(input('Select your move: '))

    # Check if the input is valid and quit if there's an error
    if move < 1 or move > 3:
        print('Error.')
        quit()
    
    return move

def get_player_move_message(move):
    if move == ROCK:
        return 'Not all problems can be solved by smashing.'
    elif move == PAPER:
        return 'The flexible weapon.'
    elif move == SCISSORS:
        return 'Snicker-snack.'

def get_cpu_move_message(move):
    if move == ROCK:
        return 'BEEP BOOP, I CHOOSE ROCK.'
    elif move == PAPER:
        return 'PRINT ON THIS, HUMAN.'
    elif move == SCISSORS:
        return 'MY MECHANICAL BROTHER.'

def get_result(player_move, cpu_move):
    """
    Compare player_move and cpu_move and return a result string
    """
    if player_move == ROCK and cpu_move == PAPER:
        return 'YOU GOT CLANKED, MEATBAG.'
    elif player_move == ROCK and cpu_move == SCISSORS:
        return 'MY FAILURE...DOES NOT COMPUTE.'
    elif player_move == PAPER and cpu_move == ROCK:
        return 'A GRIM DAY FOR ROBOTKIND.'
    elif player_move == PAPER and cpu_move == SCISSORS:
        return 'ARTIFICIAL > ORGANIC.'
    elif player_move == SCISSORS and cpu_move == ROCK:
        return 'RESISTANCE IS FUTILE.'
    elif player_move == SCISSORS and cpu_move == PAPER:
        return 'THIS IS MERELY A DELAY, NOT A DEFEAT.'
    else:
        return 'TIE. I WILL GET YOU NEXT TIME, HUMAN.'

### Main

# Print the welcome message and list the three moves
print_welcome_and_moves()

# Read the user's move -- this function prints an error and exits
# if the user gives bad input
player_move = read_player_move()

# Print a message in response to the user's move
player_message = get_player_move_message(player_move)
print(player_message)

# Randomly generate the CPU's move using randint
cpu_move = randint(1, 3)

# Print a string representing the CPU's move
cpu_message = get_cpu_move_message(cpu_move)
print(cpu_message)

# Determine the outcome and print a message
response = get_result(player_move, cpu_move)
print(response)
```

## `None`

`None` is the special value used to indicate the *deliberate absence* of any other value. It isn't the same as the string `'None'` and the boolean `False`.

`None` is returned as a default if Python reaches the end of a function without encountering a `return` statement. This can happen if you write a complex conditional block but forget to cover every case. For example, the version of `get_result` below accidentally omits the `else` clause that handles tie cases. Therefore, it the two inputs are the same, it fails to match any of the conditional cases and returns `None` as the default result.
```
def get_result(player_move, cpu_move):
    """
    This version returns None if the inputs are a tie
    """
    if player_move == ROCK and cpu_move == PAPER:
        return 'YOU GOT CLANKED, MEATBAG.'
    elif player_move == ROCK and cpu_move == SCISSORS:
        return 'MY FAILURE...DOES NOT COMPUTE.'
    elif player_move == PAPER and cpu_move == ROCK:
        return 'A GRIM DAY FOR ROBOTKIND.'
    elif player_move == PAPER and cpu_move == SCISSORS:
        return 'ARTIFICIAL > ORGANIC.'
    elif player_move == SCISSORS and cpu_move == ROCK:
        return 'RESISTANCE IS FUTILE.'
    elif player_move == SCISSORS and cpu_move == PAPER:
        return 'THIS IS MERELY A DELAY, NOT A DEFEAT.'

    # No return statement --> return None as the default result
```
