# Character Encodings

## Reading

Read [this article](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/) by Joel Spolsky for background on character encodings, ASCII, and Unicode.

## ROT13 cipher

Complete the `Encryption.md` activity. It demonstrates using the `ord` and `chr` functions to map between a character and its underlying numeric code, then uses them to implement the ROT13 cipher. A solution is given below.

```
"""
Implement the ROT13 cipher using character encodings
"""

import sys

def rot13_letter(letter):
    """
    Performs ROT13 encoding for a single capital letter
    """

    # Map the letter to its position in the alphabet
    position = ord(letter) - ord('A')

    # Rotate, wrapping around the alphabet if necessary
    rotated_position = (position + 13) % 26

    # Return the rotated position to a character - map into the space of letters
    rotated_letter = chr(rotated_position + ord('A'))

    return rotated_letter

def rot13(message):
    """
    Perform ROT13 encoding of a message of all uppercase letters
    """
    
    output = ""
    for letter in message:
        output += rot13_letter(letter)

    return output

### Main

# All of the command line argument are collected into a list called sys.argv
#
# The name of the program is always the first item in sys.argv
#
# So the message will be the second item in sys.argv
message = sys.argv[1]
encrypted = rot13(message)
print(encrypted)
```
