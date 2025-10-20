# Intro to the `while` Loop

## Topics

This note is a short introduction to the mechanics of `while`. We also did Activity 4 on random choices and lists.

- Condition-controlled loops
- Infinite loops
- Ending the loop

## Condition-controlled loops

The `while` loop uses a boolean condition to control whether the loop body executes. When Python encounters a `while` statement, it evaluates the given boolean expression and if the result is `True`, executes the body of the loop. Each iteration checks the loop condition and the loop continues executing as long as it evaluates to `True`.

The `while` loop is preferred for interactive programs that need to interact with a user repeatedly. The example below is a simple echo program. It uses a variable named `looping` as a boolean flag to control the loop execution.
```
"""
Echoing user input
"""

# Flag variable used to control the loop
looping = True

while looping:
    user_input = input('Say something: ')
    print(user_input)
```

## Infinite loops

As written, the example loops forever. The flag variable `looping` is never set to `False`, so the loop can never end.

Recall that you can kill an out-of-control program using CTRL + c. When you write a `while` loop that goes out of control, use the keyboard to stop it manually.

In this case, though, we should add a way for the user to end the loop.
```
"""
Echoing user input
"""

# Flag variable used to control the loop
looping = True

while looping:
    user_input = input('Say something: ')

    if user_input.lower() == 'quit':
        looping = False

    print(user_input)
```

This example illustrates a common pattern:

- Create a variable that controls the state of the loop. Set it to `True` initially.
- The loop checks the variable and executes the body.
- Inside the body, check to see if the stopping condition is satisfied. This may be controlled by user input or something else. When it's time for the loop to end, set the loop flag variable to `False`.


## Ending the loop

Here's a common point of confusion: **Setting `looping = False` does not automatically break out of the loop**.

The loop doesn't end until we finish the body, return back to the top to check the condition again, and *then* discover that it's been set to `False`, which ends the loop and continues with the rest of the program.

If you need to skip out of a loop without executing the rest of the body or checking the condition again, you can use `break`, but it's generally better to write your loops so that they end naturally when the stopping condition is reached, without the complexity of extra `break` jumps.
