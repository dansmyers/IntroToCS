# `if`, `elif`, and `else`

## Topics

- Making mutually exclusive choices with `if`-`else`
- Multi-way choices with `elif`
- Input validation
- `randint`

## Mutually exclusive choices

Choosing one of two mutually exclusive options is a common situation. The example below demonstrates using the `if`-`else` structure to test if a number is odd or even.
```
# Read a number
x = int(input('Enter an integer: '))

# Test if x is even or odd
if x % 2 == 0:
    print('Even')
else:
    print('Odd')
```

`if`-`else` works the way you would expect based on English grammar.

- Evaluate the boolean condition
- If it's `True`, execute the code in the `if` block and skip over the `else` block
- If it's `False`, skip the `if` block and execute the `else` block instead

In both cases, we continue executing the rest of the program after evaluating the branch.

A common mistake is trying to attach the false condition to the `else` block.
```
# Error: else never takes a condition!
if x % 2 == 0:
    print('Even')
else x % 2 == 1:
    print('Odd')
```

## `elif`

The `elif` (short for "else-if") statement is used to add more than two options to a conditional block. The example below checks if a number is positive, negative, or zero.
```
# Read a number
x = int(input('Enter an integer: '))

# Test if x is positive, negative, or zero
if x > 0:
    print('Positive')
elif x < 0:
    print('Negative')
else:
    print('Zero')
```

The block is evaluated as follows:

- Start at the top `if` statement and evalute its condition. If the answer is `True`, execute the `if` code, skip everything else, then continue with the rest of the program.

- If the first condition is `False`, continue to the next condition for the `elif` clause and evaluate it. If *that* condition is `True`, execute the code for the `elif` block, and skip the rest of the statement

- If every condition evaluates to `False`, execute the code in the `else` block as as default.

A conditional statement may contain an arbitrary number of `elif` clauses, with one condition for each one. Look at Lab 3 for examples of conditionals with more than 3 options.

It would also be acceptable to write the example this way, using an `elif` statement with conditionals for each case.
```
if x > 0:
    print('Positive')
elif x < 0:
    print('Negative')
elif x == 0:
    print('Zero')
```
This is a common point of confusion: **A conditional block doesn't have to include an `else` clause!**

## Input validation

Here's an example that reads input and checks if it's non-negative. If the user enters a bad value, print an error message and exit using the built-in `quit` function.

```
"""
Input validation example
"""

POUNDS_PER_KILO = 2.20462

# Read input
pounds = float(input('Enter a number of pounds: '))

# Check and quit if input is negative
if pounds < 0:
    print('You must enter a non-negative value.')
    quit()

# Convert
kilos = pounds / POUNDS_PER_KILO

# Output
print(f'That is {kilos: .2f} kilograms.')
```

Notice that there is no `else`. If the input is good (that is, not negative) then the program skips the `if` block, doesn't quit, and continues with the rest of the program.

## Generating random values

Python includes a built-in `random` module that contains functions for generating random numbers. A useful function is `randint`, which takes two integers as input and generates a random value from that range, including both endpoints. For example, the line
```
r = randint(1, 6)
```
will assign `r` an integer from the range 1 to 6, including both, chosen at random. All options have equal probability. You can think of this line a simulating the roll of a standard six-sided die.

The example below uses `randint` to simulate flipping a coin.
```
"""
Simulated coin flip
"""

# Import randint
from random import randint

# Generate a random flip: 0 --> heads, 1 --> tails
flip = random(0, 1)

# Output 'Heads' or 'Tails' based on flip
if flip == 0:
    print ('Heads')
else:
    print('Tails')
```

Every time you run this program, Python generates a random value that is either 0 or 1, then uses it to output `'Heads'` or `'Tails'`. If you run the program, you'll observe that it's possible to get the same value multiple times in a row. Remember: the result of `randint` is **random**, so it's not guaranteed to be different from the previous result. If the range is small, it's very possible to get long runs of repeated values.


