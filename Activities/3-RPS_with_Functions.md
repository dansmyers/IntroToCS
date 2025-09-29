# RPS with Functions

We're going to return to the rock-paper-scissors program, but modify it to use functions. The code below is a solution based on the activity we did last time. We're going to modify
it 

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
