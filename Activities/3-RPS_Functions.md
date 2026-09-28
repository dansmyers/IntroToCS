# RPS with Functions

We're going to return to the rock-paper-scissors program, but modify it to use functions. The code below is a solution based on the activity we did last time. We're going to modify it to move some of the work into functions using the instructions below. 

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

# Print the welcome message and list the three moves
print('Welcome to Rock-Paper-Scissors.')
print('1. Rock')
print('2. Paper')
print('3. Scissors')

# Read the user's move
player_move = int(input('Select your move: '))

# If the move is not 1, 2, or 3, print an error and exit
if player_move < 1 or player_move > 3:
    print('You must enter 1, 2 or 3.')
    quit()

# Print a message in response to the user's move
if player_move == ROCK:
    print('Rock. A strong choice.')
elif player_move == PAPER:
    print('Paper. The flexible weapon.')
else:
    print('Scissors. Snicker-snack.')

# Randomly generate the CPU's move using randint
cpu_move = randint(1, 3)

# Print a string representing the CPU's move
if cpu_move == ROCK:
    print('BEEP-BOOP. I CHOOSE ROCK.')
elif cpu_move == PAPER:
    print('BEEP-BOOP. PRINT ON THIS, NERD.')
else:
    print('BEEP-BOOP. SCISSORS. THE ELEGANCE OF METAL.')

# Determine the outcome and print a message
if player_move == cpu_move:
    print('TIE. I\'LL GET YOU NEXT TIME, HUMAN.')

# Cases where player_move == ROCK
elif player_move == ROCK and cpu_move == PAPER:
    print('HUMANS...SO SOFT...SO WEAK.')
elif player_move == ROCK and cpu_move == SCISSORS:
    print('MY FAILURE...DOES NOT COMPUTE.')

# Cases where player_move == PAPER
elif player_move == PAPER and cpu_move == ROCK:
    print('I WILL GET YOU NEXT TIME, MEATBAG.')
elif player_move == PAPER and cpu_move == SCISSORS:
    print('ARTIFICIAL > ORGANIC')

# Cases where player_move == SCISSORS
elif player_move == SCISSORS and cpu_move == ROCK:
    print('YOU GOT CLANKED, HUMAN.')
elif player_move == ROCK and cpu_move == SCISSORS:
    print('FAREWELL, MY MECHANICAL BROTHER.')
```

## Setup

`cd` to your `3-Functions` directory and make a file named `rps_functions.py`.

## Starting code
Use the code below as your starting point. You can see that it follows the same approach as the version above, but calls functions to perform several of the steps. You're going to write the functions using the instructions below.
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

## Functions

### `print_welcome_and_moves`
Add a `def` statement for `print_welcome_and_moves`. The function takes no inputs and prints a short welcome line and then the numered list of moves, like so:
```
Welcome to rock-paper-scissors!
1. Rock
2. Paper
3. Scissors
```

### `read_player_move`
Add a function named `read_player_move` that takes no input parameters. This function does two things:

- Read the player's move using `input`. This is a case where it's okay to use `input` inside a function, because the purpose of this function is to get input from the player.
- Check the input. If the value is bad, print an error message and quit. If the value is good, return it as the result of the function.

```
def read_player_move():
    """
    Read and check the player's move
    """

    # Read the player's move using input - remember to turn it into an int

    # Check the player's move - if it's bad, print an error and quit

    # Else, the move was good, so return it

```

### `get_player_move_message`

Add a function that takes the player's move number (1, 2 or 3) as input and **returns** a message to print about the move. For example,

```
def get_player_move_message(move):
    """
    Return a string describing the player's move
    """
    if move == ROCK:
        return 'When will you humans learn that some problems can\'t be solved by smashing?'

    # Add more cases for the other moves
```

### `get_cpu_move_message`
Repeat with another function called `get_cpu_move_message` that takes the computer's move as input and **returns** a string describing it.

### `get_result`

The last function takes both moves as input and returns the string describing the outcome.

```
def get_result(player_move, cpu_move):
    """
    Return a string for the outcome
    """
    if player_move == ROCK and cpu_move == SCISSORS:
        return 'MY FAILURE...DOES NOT COMPUTE...'

    # Add more cases for the other combinations
    # Think carefully about covering every case!
```
