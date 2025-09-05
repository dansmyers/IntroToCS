# Variable Practice

This class was a review of the techniques we've used during week 2.

- variables
- `input`
- formatted printing
- constants
- docstrings

## Assignments are not equations

Take a look at the following code fragment. It assigns values to `length` and `width`, calculates and prints `area`, then changes the values of `length` and `width`. What will be printed by the second statement?

```
# Assign length and width
length = 10
width = 7

# Calculate and print area
area = length * width
print(f'The area is {area:.2f}.')

# Change
length = 100
width = 70

# Does this print 70 or 7000?
print(f'The area is {area:.2f}.')
```

If you run the program, you'll see that the second statement prints **70**. Changing the values of `length` and `width` **does not** automatically update the value of `area`.

Remember that `=` is an assignment operation: it's not the same as mathematical equality! Therefore, a line like
```
area = length * width
```
performs a one-time assignment to the value of `area`. It **does not** define an equation that automatically updates the value of `area` if `length` or `width` change. 

If you want to change the value of a variable, you can only do that by making an explicit assignment to it.

## Constants

Programs often contain fixed values that do not change, like special math constants or conversion factors. It's conventional to indicate that a variable is a constant by naming it in `ALL_CAPS`. That style indicates to any future readers that the variable should not be arbitrarily modified.

Here's another version of the Smoots converter program that combines all of the features we've talked about so far:

- Triple-double quoted docstring at the top of the program
- Constant definition for the conversion factor
- Read a value using `input` and convert it to a number using `float`
- Calculate and store the result in a variable
- Print to three decimal places

```
"""
Read a number of feet and convert to Smoots
"""

# Constant conversion factor
FEET_PER_SMOOT = 5.5833

# Read input, single-line style
feet = float(input('Enter a number of feet: '))

# Calculation
smoots = feet / FEET_PER_SMOOT

# Print to three decimal places
print(f'That is {smoots:.3f} smoots.')
```
