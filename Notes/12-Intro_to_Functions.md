# Intro to Functions

## Topics

- Built-in functions
- Mental model
- Functions that print messages

## Built-in functions

We've seen several examples of built-in Python functions, including:

- `print`
- `input`
- The type conversion functions `int`, `float`, and `str`
- `sqrt`
- `randint` and `random`

A function is *a name associated with a block of code*. Functions are useful because they allow us to **hide complexity** in our programs. We've used complex built-in functions like `randint` without worrying about how they're implemented, because their complex operations are hidden behind a simple interface. Functions are also useful for organizing and designing programs, because they give us a way to break our program up into smaller units that may be easier to reason about.

Functions can take inputs and return outputs. For example,

- `sqrt` takes an input number and returns its square root
- `randint` takes two input integers and returns a random integer in their range
- `print` takes an input, which is the value to print, but doesn't return any output
- `random` takes no inputs and returns a random value sampled from [0, 1)

## Mental model

Look at the `green_eggs_and_ham.py` program in the `Examples/3-Function` directory. Here's an excerpt:
```
"""
Would you?
CMS 120
"""

def print_refrain():
    print()  # Blank line
    print('I do not like them, Sam-I-Am.')
    print('I do not like Green Eggs and Ham!')
    print()  # Blank line
    
    
### Main
print('Would you like them in a house?')
print('Would you like them with a mouse?')

print_refrain()

print('Would you like them in Japan?')
print('With Godzilla and Rodan?')

print_refrain()
```

The `def` statement defines a function. On encountering a `def`, Python notes that the name, which is `print_refrain` in this case, is associated with block of code statements in the function's body. In this case, there are four print statements in the body of `print_refrain`. Observe that the body is indented with respect to the `def` statement, like other code blocks we've seen.

The line
```
print_refrain()
```
calls the function. Mentally, think about a function call as *jumping up* to the function to execute its code, then *jumping back down* to the calling location to continue with the rest of the program.

The comment `### Main` is a little note that I like to use to separate the section of the program that contains function definitions from the "main" part with the executable statements. It isn't required, but you'll see me use it in most of our programs for a while.

A common error is to omit the parentheses:
```
# Error: doesn't call the function
print_refrain
```
This won't crash your program, but it won't call the function. If you have a function that you think should run but doesn't, always start by making sure that you're correctly invoking it by using a pair of parentheses.

## Functions that print messages
The following program defines two functions that each print an output message, then calls each one in the main part of the program. Experiment with modifying the functions and adding your own to print different messages.
```
"""
Print hello and goodbye messages
"""

def say_hello():
    print('Hello, World!')

def say_goodbye():
    print('Have a pleasant day.')

### Main
say_hello()
say_goodbye()
```

A function definition has five components:

1. The `def` keyword
2. The name of the function. Functions use the same conventions as variable names: start with a lowercase letter, separate words with `_`
3. A pair of parentheses. These will be used to specify any input parameters that the function takes, but they're required even if the function doesn't take any inputs.
4. A colon, to indicate we're opening a new indented block.
5. The indented body of the function.


