# Precision

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Morning_Mist_in_Taj_Mahal%2C_no._5%2C_Hiroshi_yoshida.jpg/1920px-Morning_Mist_in_Taj_Mahal%2C_no._5%2C_Hiroshi_yoshida.jpg" width="400px" />

*Morning Mist in Taj Mahal, no. 5*, Hiroyoshi Yoshida (1932)

## Overview

This lab will allow you to practice working with binary numbers. We'll also investigate the idea of *precision* in computer calculations.

The second part will allow you work with character encodings and implement a variation on the Caesar cipher called **ROT13**.

## Setup

Make `Lab_11` and `cd` into it.


## Written Lab

Complete the lab in the written document posted to Canvas. It will allow you to practice working with binary numbers and experiment the precision of computer calculations.


## Both Sides

Here's an interesting fact about characters in Python: **Every character is really a number**. That is, every character has an underlying numeric code, and we can treat operations on characters as being equivalent to operations on their underlying numeric codes.

You can use the `ord` function to get the numeric code of a character. For example,
```
ord('A')
```
evaluates to 65, because (for reasons that we'll explain in class), capital A is mapped to numeric code 65.

The `chr` function converts a numeric code into its corresponding character. For example, `chr(65)` will evaluate to `'A'`.

Type `python3` in your terminal to run the interactive Python prompt. Then answer the following questions:

- What is the character code of capital `Z`?
- What is the character code of lowercase `a`?
- What character has code 48?
- What is the code of a single space?
- What is the code of `\n`?

Put your answers in a text file named `chars.txt`.

Press `CTRL + d` to leave the Python shell when you're done. 

## ROT13

### Rotating letters
The **ROT13** cipher is a Caesar-style rotational cipher that rotates *13 positions* in the alphabet. This choice allows the same operation to be used for both encryption and decryption: rotating forward 13 positions and then forward another 13 positions recovers the original message. It has frequently been used as a way to obscure jokes and spoilers on messageboards and in e-mail.

Let's implement the ROT13 cipher. Start by writing a function called `rot13_letter` that takes a *single capital letter* `A`-`Z` as input and returns its ROT13 encoded equivalent.

Tip:

Let the input parameter be named `letter`. You can convert it to its position in the alphabet using:
```
position = ord(letter) - ord('A')
```
This change maps `A` to 0, `B` to 1 and so forth.

Perform the 13-position rotation, then shift back using
```
rotated_letter = chr(rotated_position + ord('A'))
```
Think about how to perform the rotation. You'll need to deal with wrapping around the alphabet.

### Rotating an entire message

Now add a `rot13` function that takes a string `message` as input and returns its ROT13 encoded counterpart. You can assume that `message` contains only capital letters `A` to `Z`. Use a loop with `rot13_letter`.

Write some test code to verify that you can use your function to both encrypt and decrypt messages.


### `__name__`

Let's add one more feature using something that you may have seen in AI-generated code.

Python maintains a special internal variable called `__name__` (two underscores on each side) that keeps track of how the current script was entered. If the program was executed from the terminal command line, then the value of `__name__` is `"__main__"`. This leads to a standard formulation for what we've been calling the "Main" section of the program:
```
# Main

if __name__ == '__main__':
    # Main code goes in this block
```
The statement checks if the program was run from the command line using `python3` and, if so, executes the main body of code inside the `if` block.

Why would you do this? Sometimes you want to load a script as a library rather than running it from the command line. If so, then you don't need to run the main part of the script. This setup allows you to verify that the script is actually being run as the main entry point of the program. If you `import` a script, then `__name__` will be the name of the script that did the `import` statement.

One common setup is to put test code inside the main block. Then, running the script from the command line executes its internal test code; if the script is imported from somewhere else, then there's no need to run the tests.

Modify your program to add an `if` block like the one above. Inside it, prompt the user to enter a string (in all caps, no spaces), call `rot13` on it, then print out the result.

### Command-line arguments

Let's add one more piece: reading arguments from the command line. We've already used this several times when working with the standard terminal commands. For example,
```
ls -l
```
prints the files in the directory using the "long" format that gives more information.

Items typed on the command line after the program name are available through the `sys` module.
```
import sys
```

`sys` is initialized with a list called `argv` that contains the command line arguments. The program below uses a loop to print the arguments. Put in a file named `print_args.py`.
```
"""
Print command line arguments using sys.argv
"""
import sys

if __name__ == '__main__':
    for arg in sys.argv:
        print(arg)
```

If you run the program with the input
```
python3 print_args.py one two three
```
you'll see the following output:
```
print_args.py
one
two
three
```
By convention, the program name is always the first item in the `argv` list.

Modify `rot13.py` to take the input string from the command line as an argument, then print the rotated string. For example, if you type
```
python3 rot13.py HELLO
```
Your program should print out the rotated version of `"HELLO"`.

Tip: `sys.argv` is a list. The first element of the list is the program name. What is the index of the word after the program name?
