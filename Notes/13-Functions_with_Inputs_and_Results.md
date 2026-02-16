# Functions That Take Inputs and Return Results

## Topics

- Functions that take input parameters
- Parameters vs. `input`
- Multiple inputs
- Returning results
- Return vs. `print`
- Calling a function from a function

## Input parameters

The program below defines a function name `area_of_circle` with an input named `radius`. It calculates the area of the corresponding circle and **prints** it. The input parameter is specified in the parentheses as part of the function definition.
```
"""
Example of a function with an input parameter
"""

from math import pi

def area_of_circle(radius):
    area = pi * radius ** 2
    print(area)

### Main
area_of_circle(5.0)
```
When Python encounters the final line, it calls `area_of_circle`, which we conceptually think of as jumping up to the function to run its block of associated code. The input argument `5.0` is assigned to the parameter `radius` and then used in the calculation of `area`. The result is to print 78.53.

You can call the function as many times as you want, with different input radius values. Each call assigns the given input to `radius`, then calculates and prints the corresponding area.
```
area_of_circle(50.0)
area_of_circle(500.0)
```

## Parameters vs. `input`
We've previously written programs that used `input` to read values from the terminal. Consider the following:
```
def area_of_circle(radius):
    radius = float(input('Enter the radius: '))
    area = pi * radius ** 2
    print(area)

### Main
area_of_circle(5.0)
```
This version of the program would call `area_of_circle` with an input radius of 5.0, *then immediately call `input` to read a different value of `radius`*. This is unnecessary!

As a general rule: **Functions take inputs through their declared parameters**, not by calling `input` in the body of the function. Don't mix the two!

## Multiple inputs

Declare multiple inputs to a function by separating them with commas.
```
def area_of_rectangle(length, width):
    area = length * width
    print(area)

### Main
area_of_rectangle(11, 7)
```
The first input argument (11, in this case) is assigned to the first parameter (`length`), the second input to the second parameter, and so forth.

## Returning results

The following function simulates the roll of a six-sided die and **returns** it so that it can be used in other parts of the program.
```
"""
Returning results from a function
"""

from random import randint

def roll():
    die = randint(1, 6)
    return die


### Main
die_roll = roll()
print(die_roll)
```
The `return` statement ends the function. The given value (`die`, in thise case) is passed back as the result of the function. In this example, the line
```
die_roll = roll()
```
calls the `roll` function, which generates a random integer using `randint`, then returns that value so it can be assigned to `die_roll`.

**Returning is not the same as printing**!

- `print` outputs a value to the terminal so we can see it
- `return` sends a value back as the result of a function so that it can be used in other parts of the program

 **Use `return` to output the results of a function**. Don't print the results of a function before returning.

The `roll` function can now be a building-block for more complex die rolling functions.
```
def sum_of_two_dice():
    total = roll() + roll()
    return total
```
This can be further simplified to remove the temporary variable:
```
def sum_of_two_dice():
    return roll() + roll()
```
