# Types, Input, and Formatted Printing

## Topics

- Four basic data types
- The `input` statement
- Converting strings to numbers
- Formatted printing using f-strings

## Data types

Every data value in a Python program has a *type*. There are four basic Python data types:

1. `int` is the type of the positive and negative whole numbers, including 0. Examples: `5`, `0`, `-1001`

2. `str` is the string type. Anything enclosed in single or double quotes is a string. Examples: `'hello'`, `"5"`, `'True'`

3. `float` is the type of decimal numbers. The name refers to the internal *floating point* data format used to represent non-integer values in computers. Any number with a decimal point is a `float`. Examples: `1.01`, `3.14`, `5.0`

4. `bool` is the *Boolean* data type, used to represent logical true and false values. There are two special Boolean values, `True` and `False`, and these are the only values that have the `bool` type. Notice that `True` and `False` don't have quotes and aren't the same as the strings `'True'` and `'False'`.

Values that are mathematically equivalent may correspond to different types. For example, `5` and `5.0` are mathematically equal to each other, but have different types: one is an `int` and the other is a `float`.

## `input`

Use the built-in `input` command to read user input from the terminal. It takes a string that it prints as a prompt, then waits for the user to respond. The value the user types is assigned to the given variable.
```
# Read a number of feet from the user
user_input = input('Enter a number of feet: ')
```

**The result returned by `input` is always a *string***. If you want to use it as a number in an expression, you need to convert it to `int` or `float` using one of the built-in conversion functions.
```
# Read a number of feet from the user
user_input = input('Enter a number of feet: ')

# Convert the string input to a float
feet = float(user_input)
```

For now, I recommend using this two-step process when reading input:

- Prompt the user to enter a value, which is saved as a variable named `user_input` or similar
- Convert `user_input` to a number using `float` or `int`, whichever is most appropriate for the problem. Use a descriptive variable name for the result of the conversion, which you then use in the rest of the program.

## Formatted printing

It's convenient to mix output text with variable values. An easy way to do this is with a formatted string, which Python calls an *f-string*.
```
print(f'The area of the circle is {area}.') 
```
Python prints the literal text string, as given, but treats text in curly braces as the name of a variable. When Python sees `{area}` in the output, it will take the value of the `area` variable and insert it into that location in the output string.

You can supply additional formatting information to specify the number of decimal places. To print to two decimal places use
```
print(f'The area of the circle is {area:.2f}.') 
```
The specifier `.2f` tells Python to format the output value to two decimal places. Use `.3f` for three decimal places, `.4f` for four, etc.

## Example
The example below reads a number of feet and converts to miles using all of the techniques we've discussed so far. Use it as a model when completing the questions in Lab 2.

```
# Convert feet to miles
#
# 1 mile = 5280 feet

# Read input
user_input = input('Enter a number of feet: ')

# Convert to a number
feet = float(user_input)

# Perform conversion
miles = feet / 5280

# Print to two decimal places
print(f'That is {miles:.2f} miles.')
```
