# Making Random Choices

## Topics

- `randint`
- `random`
- Making choices with unequal probabilities
- Example

## `randint`

`randint` takes two inputs and returns an integer from the given range, including both. For example, `randint(1, 6)` generates a value from the range 1 to 6, including both. Therefore, the result is one of the values 1, 2, 3, 4, 5 or 6, as in the roll of a six-sided die. All values have an equal probability of being chosen.
```
# Sum of two six-sided dice 
die1 = randint(1, 6)
die2 = randint(1, 6)
total = die1 + die2
printf('The dice are {die1} and {die2}. The sum is {total}.'
```
Check Lab 3 for more examples of using `randint` to generate random choices with equal probabilities.


## `random`

The `random` function takes no inputs and returns a random float value in the range [0.0, 1.0) - 0.0 is included in the possible outputs, but 1.0 is not.

`random` is useful when you want to make choices with unequal probabilities. The program below implements a Magic Eight Ball program with probabilities of 40%, 30%, 20% and 10% for the four answers.

The conditional block selects which region of the number line the random `r` falls into. If the first option has 40% probability, then it corresponds to the range of values from 0.0 to .40. The second option corresponds to the next 30% of the distribution, from .40 to .70, and so forth.
```
                                              Opt. 4
                                                | 
      Option 1          Option 2      Opt. 3    v
|-------------------|--------------|---------|-----|
0.0                .40            .70       .90    1.0 
```

```
"""
Magic Eight Ball with four unequal random choices
"""

# Import random at the top of the program
from random import random

# Intro
print('Welcome to the magic eight ball')
question = input('Enter your question: ')

# Generate random number
r = random()

# Select the outcome based on the response distribution
if r <= .40:
    print('My sources say no.')
elif r <= .70:
    print('It is decidedly so.')
elif r <= .90:
    print('Without a doubt.')
else:
    print('Reply hazy.')
```

## Example: roulette
The American roulette wheel has 38 pockets, of which 18 are colored red, 18 are black, and two (0 and 00) are colored green. The program below prompts the user to bet on red or black, then uses `random` to simulate the color of the spin.

Notice that the program doesn't simulate *the specific pocket* the ball lands in, only the distribution of colors.

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

# Generate the random spin in [0, 1)
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
