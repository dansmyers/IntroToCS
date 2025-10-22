# `while` Loop Examples and Files

## Topics

- Counting with `while`
- Babylonian square root algorithm
- Opening and iterating through files

## Counting

The `for` loop with `range` is the preferred way to iterate through a sequence of numbers, bu sometimes you need to do so with a `while` loop. The loop below counts from 0 to 13 and prints each number.
```
i = 0
while i <= 13:
    print(i)

    # Remember: you need to manually increment the loop counter
    i += 1
```
The important line is
```
i += 1
```
to increment the counter. If you forget this line your loop will remain stuck at 0 until you kill it with CTRL + c.


## Babylonian square root algorithm

The Babylonian algorithm is an ancient technique for iteratively calculating square roots.

Suppose we want to find the square root of a number `x`. The Babylonian method starts with a `guess` value that we think approximates the real square root. The guess might be initially bad, but that's okay.

The method iteratively calculates an improved square root using
```
guess = .5 * (guess + x / guess)
```
Intuitively, is `guess` is too small, then `x / guess` will be larger than the real root, and the average of the two will be a better approximation. Likewise if `guess` is larger than the real root. This formula can be derived using Newton's method from Calculus to find the roots of the square function.

```
"""
Babylonian square roots
"""

# Find the root of x
x = 100

# Initial guess
 guess = 1

# Iteratively calculate improved roots
looping = True
while looping:
    print(guess)
    old_guess = guess

    # Update rule
    guess = .5 * (guess + x / guess)

    # Stop when the change in the solution is small - indicates convergence
    if abs(guess - old_guess) < .0001:
        looping = False
```
The end of the loop checks the change in the value of `guess`. If the change is small, then the method is converging and its reasonable to stop. This style of stopping condition is common in numerical algorithms, where you don't know the exact target result.

## Files

The code below opens a file named `words.txt`, iterates through its lines, and prints each one.
```
"""
Opening and looping through a file
"""

# Open the file in read mode
f = open('words.txt', 'r')

for line in f:
    # Strip extra white space and new lines
    line = line.strip()

    print(line)

f.close()
```
The `open` command takes two arguments: the name of the file as a string and a "mode" that specifies how you want to interact with the file. Here, `'r'` indicates read mode. The string `'w'` would be used for writing to a file (more on that later).

If you misspell the name of the file, or give an incorrect path, your program will throw a `FileNotFoundError`.

The `strip` method removes extra whitespace padding from the line, including any terminating `\n` characters. This is important if you're writing code that intends to iterate through the characters on a line, since you usually don't want to include the terminating newline in the string's length or its character sequence.

An alternate way of writing the same block is to use the `with` statement. The `with` block automates cleaning up and closing the file when its associated block finishes, so it's preferred in Python.
```
with open('words.txt', 'r') as f:
    for line in f:
        line = line.strip()
        print(line)
```
