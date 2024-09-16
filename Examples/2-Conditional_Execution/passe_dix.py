"""
Passe-dix dice game
"""

from random import randint

# Roll three dice, saving each one to its own variable
die1 = randint(1, 6)
die2 = randint(1, 6)
die3 = randint(1, 6)
print(f'The dice are {die1}, {die2}, and {die3}.')

# Add their sum
total = die1 + die2 + die3
print(f'The total is {total}.')

# Check if the sum is less than, greater than, or equal to 10
if total < 10:
    print('Lose')
elif total > 10:
    print('Win')
else:
    print('Draw')
