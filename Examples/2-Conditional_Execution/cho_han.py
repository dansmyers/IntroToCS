"""
Cho-Han: roll two dice and bet whether the sum is even or odd
"""

from random import seed, randint
import sys

# Set the random number generator's seed
# DON'T MODIFY THIS LINE
seed(0)

print('Welcome to Cho-Han.')
print('1. Even')
print('2. Odd')

bet = int(input('Select a bet: '))

if not (bet == 1 or bet == 2):
    print('You must enter 1 or 2.')
    sys.exit()

die1 = randint(1, 6)
die2 = randint(1, 6)

roll = die1 + die2

print('The dice are %d and %d.' % (die1, die2))
print('The sum is %d.' % roll)

if roll % 2 == 0 and bet == 1:
    print('You win.')
elif roll % 2 == 1 and bet == 2:
    print('You win.')
else:
    print('You lose.')
