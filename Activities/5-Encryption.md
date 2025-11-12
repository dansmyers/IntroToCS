# Encryption

This activity will allow you to practice writing a Caesar-style cipher using the concept of character encodings. You're going to implement the **ROT13** cipher, which uses a 13-position rotation through the alphabet. Along the way, we'll practice using the `ord` and `chr` functions to interact with the underlying numeric codes of text characters.

## Character encodings with `ord` and `chr`

Here's an interesting fact about characters in Python: **Every character is really a number**. That is, every character has an underlying numeric code, and we can treat operations on characters as being equivalent to operations on their underlying numeric codes.

You can use the `ord` function to get the numeric code of a character. For example,
```
ord('A')
```
evaluates to 65, because capital A is mapped to numeric code 65 in the ASCII character encoding system.

The `chr` function converts a numeric code into its corresponding character. For example, `chr(65)` will evaluate to `'A'`.

Type `python3` in your terminal to run the interactive Python prompt. Then answer the following questions:

- What is the character code of capital `Z`?
- What is the character code of lowercase `a`?
- What character has code 48?
- What is the code of a single space?
- What is the code of `\n`?

Press `CTRL + d` to leave the Python shell when you're done. 

## ROT13

### Rotating letters
The **ROT13** cipher is a Caesar-style rotational cipher that rotates *13 positions* in the alphabet. This choice allows the same operation to be used for both encryption and decryption: rotating forward 13 positions and then forward another 13 positions recovers the original message. It has frequently been used as a way to obscure jokes and spoilers on messageboards and in e-mail.

Make a file called `rot13.py` in your `5-Dictionaries` directory.

Let's implement the ROT13 cipher. Start by writing a function called `rot13_letter` that takes a *single capital letter* `A`-`Z` as input and returns its ROT13 encoded equivalent.
```
def rot13_letter(letter):
    """
    Perform 13-position rotation on the given capital letter 'A'-'Z'
    """

    # Use ord to turn the letter into its numeric code
    #
    # Subtract ord('A') to get the letter's position in the alphabet


    # Add 13, wrapping around the alphabet if necessary

    # Use ord to turn rotated code into a letter

    # Return the rotated letter


### Main
print(rot13_letter('A'))
print(rot13_letter('B'))
print(rot13_letter('C'))

print(rot13_letter('X'))
print(rot13_letter('Y'))
print(rot13_letter('Z'))
```

Tip:

Let the input parameter be named `letter`. You can convert it to its position in the alphabet using:
```
position = ord(letter) - ord('A')
```
This change maps `A` to 0, `B` to 1 and so forth. You can then add 13 to `position` to perform the rotation. Think about how to wrap around the alphabet if necessary.

After you've calculated the `rotated_position`, you can shift back using:
```
rotated_letter = chr(rotated_position + ord('A'))
```

### Rotating an entire message

Now add a `rot13` function that takes a string `message` as input and returns its ROT13 encoded counterpart. You can assume that `message` contains only capital letters `A` to `Z`. Use a loop over the characters of `message` and use `rot13_letter` to rotate each one.

Write some test code to verify that you can use your function to both encrypt and decrypt messages.


## Command-line arguments

Let's add one more piece: reading arguments from the command line. We've already used this several times when working with the standard terminal commands. For example,
```
ls -l
```
prints the files in the directory using the "long" format that gives more information.

Python program can also take arguments from the command line. We're going to update the `rot13 program so that you can call it with a word you want to encrypt given when you run the program:
```
python3 rot13.py HELLO
```

### `sys` and `argv`

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
The `sys.argv` list collects all of the words typed on the command line after `python3`. Each word becomes an entry in the list. The name of the program - `print_args.py` in this case - is the first item in the list, followed by any other words typed after the program name.

### 

Modify `rot13.py` to take the input string from the command line as an argument, then print the rotated string. For example, if you type
```
python3 rot13.py HELLO
```
Your program should print out the rotated version of `"HELLO"`.

Tip: `sys.argv` is a list. The first element of the list is the program name. What is the index of the word after the program name?
