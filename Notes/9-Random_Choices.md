# Making Random Choices

## Topics

- `randint`
- `random`
- Example




## Example: roulette
The American roulette wheel has 38 pockets, of which 18 are colored red, 18 are black, and two (0 and 00) are colored green. The program below prompts the user to bet on red or black, then uses `random` to simulate the color of the spin.

```
"""
Simulate the red/black bet in roulette

Ask the user to pick red or black
Simulate the outcome of landing on red or black or green
Print whether the bet wins or loses

Probability of red = 18/38
Likewise for black
Probability of green = 2/38
"""

from random import random

print('Welcome to roulette.')
print('1. Red')
print('2. Black')
choice = int(input('Select your bet: '))

# Generate the random spin
spin = random()

# Select the color based on the spin result
if spin < 18 / 38:
    color = 'Red'
elif spin < 36 / 38:
    color = 'Black'
else:
    color = 'Green'

# Print the result
print(f'The wheel landed on {color}.')

# Determine win or loss
if choice == 1 and color == 'Red':
    print('Win.')
elif choice == 2 and color == 'Black':
    print('Win.')
else:
    print('Loss.')
```
