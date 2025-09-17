# Variables

## Topics

- Assignment statements
- Mental model of variables
- Naming conventions
- Example

## Assignments

A variable is a *label* associated with a piece of data. After performing a variable assignment, we can use the variable's name to interact with its underlying data value. This is useful, because it allows us to write more complex programs by using symbolic names that are more descriptive and easier to understand instead of raw numbers.

Use the `=` operator to perform a variable assignment. The name of the variable is placed on the left and the assigned value on the right.
```
pounds = 39525
```
This action associates the name `pounds` with the value `39525`. After performing the assignment, we can use `pounds` to refer to the number.
```
# Prints the value 39525
print(pounds)
```

The ordering is important! The `=` operator performs *assignment*; it isn't the same as mathematical equality.
```
# This is mathematically equivalent, but not a valid Python statement
39525 = pounds
```
The name is always placed on the left side of `=` and the value on the right.


## Mental model of variables

The assignment operation allocates a little box in the computer's memory. The right-hand value is placed in the box and the left-hand name is set as a label that refers to the box's contents.
```
         -------
pounds: | 39525 |
         -------
```
When Python sees a reference to the name `pounds`, it looks inside the box and retrieves the associated value.

## Naming conventions

**Always use descriptive names**. Variables provide context for understanding the program, so each name should tell something useful about the data it represents. Outside of special cases where the context is clear, do not use single-letter names like `x`, `y`, and `z`.

Variable names can contain lowercase and uppercase letters, digits 0-9, and the `_` character. By convention, however, **names start with a lowercase letter**. Multi-word names use only lowercase letters with words separated by an underscore.
```
pounds_per_kilo = 2.20462
liters_of_blood = 5
number_of_bones = 206
```
This style of naming is called `snake_case` because it makes long, low variable names. The alternative style is `camelCase` where subseqeunt words are capitalized and names appear bumpy.


## Example
The program below (which we wrote together in class) calculates the area of a circle using a `radius` variable. It also demonstrates importing the built-in value of `pi` to obtain the most accurate approximation possible.
```
# Calculate a circle given its radius

# Import the built-in value of pi from the math library
from math import pi

radius = 5.0

area = pi * radius ** 2
print(area)
```

The language will allow it, but notice that there's no reason to enclose the right-side expression in parentheses.
```
# Outer parentheses are unnecessary
area = (pi * radius ** 2)
```
Only use parentheses when they're required to get the correct order-or-operations.
