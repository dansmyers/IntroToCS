"""
CHO-HAN
"""

# Import the randint method
from random import randint

# Print the welcome message and the two bets
print('Welcome to cho-han.')
print('1. Even')
print('2. Odd')

# Read the number 1 or 2 from the user
choice = int(input('Enter 1 or 2: '))

# Check if the user's input is 1 or 2; if not, print an error and quit
if choice < 1 or choice > 2:
    print('That is not a valid choice.')
    quit()


# Roll two six-sided dice and add their sum
die1 = randint(1, 6)
die2 = randint(1, 6)
print(f'The dice are {die1} and {die2}.')

total = die1 + die2
print(f'The total is {total}.')

# Use a conditional block to print the output
#
# There are two ways to win:
#     If the player entered 1 and the sum is even
#     If the player entered 2 and the sum is odd
# Every other outcome is a loss
#
# Think about how to turn that into an if-elif-else block
if choice == 1 and total % 2 == 0:
    print('Win')
elif choice == 2 and total % 2 != 0:
    print('Win')
else:
    print('Lose')
