# Decisions

## Overview

This lab will allow you to practice writing programs that use `if` statements to implement branching.


## Setup

Create a new `Lab_3` directory and then `cd` into it.
```
mkdir Lab_3
```
```
cd Lab_3
```

Put each program into its own `.py` file. You can choose the names for each file.

## Problems

### Even-odd

Recall that Python supports a special operator, `%`, which is called the **modulus operator**. The mod operator calculates the remainder after division. For example,
```
11 % 3  is  2

13 % 4  is  1

8 % 2  is  0 (because 8 is evenly divisible by 2)

17 % 6  is  5
```
The mod operator can be used to check for divisibility. For example, suppose you want to test if an input value `n` is even. A number is even if it's evenly divisible by 2, so
```
if n % 2 == 0:
    # n is even
else:
    # n is odd
```
Write a program that reads an integer from the terminal and prints `Even` if the number is even or `Odd` if it's odd.

### Input validation

How many liters are in a gallon? No one knows.

But it turns out it's 3.78541. Write a program that reads in a non-negative number of liters and converts it to the equivalent number of gallons:

- Use a constant to define the conversion factor
- Use an `if` statement to check that the input is non-negative
- If the input is negative, print an error message and call `quit()` to end the program
- Use a f-string for formatted printing
```
print(f'{liters} liters is equal to {gallons: .2f} gallons.')
```


### Guessing game

Write a number guessing game. This version will have one **pre-set** number that the user is trying to guess. When the program runs, prompt the user to enter a guess.

- If the guess is correct, print `Correct!`
- If the guess is too high, print `Too high...`
- If the guess is too low, print `Too low...`

The user can run the program multiple times and adjust the guess each time. Later, we'll see how to do a program like this with a loop.

```
"""
Guessing a pre-set number
"""

# The target number
TARGET = 777


# Prompt the user for a guess in the range 1 to 1000


# Use an if-elif-else statement to compare the user's input against TARGET
# There are three options: correct, too high, or too low

```

### `fortune`

There's a classic UNIX program called `fortune` that prints random messages when you run it. Let's use it as an example for installing new packages in Linux.

First, you need to update the package install, which is called `apt-get`. Run the following command **in your terminal** (not in a Python script):
```
sudo apt-get update
```
You can then install `fortune`. Enter `Y` when you're asked if you want to continue.
```
sudo apt-get install fortune
```
The program is installed into a special directory called `/usr/games`. You can run it in the terminal by typing
```
/usr/games/fortune
```
You can think of this command as telling the shell to run the program named `fortune` that's located in `/usr/games`. Run the program a few times to see a different random output each time.

#### `sudo`

Here's a side point: What is `sudo` doing in the install command? 

Linux systems have the notion of privilege levels and access control. The top level account on any system is the **superuser** or **root** account, which has the ability to make any change to anything. Regular user accounts always run with privileges below that of root. A major goal of a malicious hacker is to perform *privilege escalation* by starting with a regular account and then using exploits to gain root access.

`sudo` stands for `substitute user do`. It allows you to run individual commands with superuser-level privileges without actually logging in as the root account.

`apt-get` is a standard command for managing packages and installing programs on many Linux distros. It has to be run as root to make
system changes, so it's prefixed by `sudo`.

<img src="https://imgs.xkcd.com/comics/sandwich.png" width="300px" />


### `cowsay`

```
 ___________________________________
/ After all, all he did was string  \
| together a lot of old, well-known |
| quotations.                       |
|                                   |
\ -- H. L. Mencken, on Shakespeare  /
 -----------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
```

Here's another program to install:
```
sudo apt-get install cowsay
```
Run the program in your terminal:
```
/usr/games/cowsay "Hello, world!"
```
Linux allows you to "pipe" programs together, so that the output of one becomes the input to another. Try the following command and run it multiple times:
```
/usr/games/fortune | /usr/games/cowsay
```

### Fortuna has spun me down

<img src="https://assets.nintendo.com/image/upload/c_fill,w_1200/q_auto:best/f_auto/dpr_2.0/ncom/software/switch/70010000010066/529133f9f52ff1874e16c0dbe0ef5ce377d6114cad7ac2e876ff6ac28040b508" width="400px" />

Let's write our own version of `fortune`, which will generate a **random number** and use it to pick a saying as output.

Python has a `random` package that includes functions for generating random numbers. One is `randint`, which generates a random integer within a given range. For example, to generate a random number drawn from 1 to 6 (including both), use
```
r = randint(1, 6)
```
Every time you run the program, `randint` will execute and generate a new random value drawn from the integers 1 to 6 that is assigned to the variable `r`. Note that you might get the same value multiple times in a row, which is more likely if the range is small.

Here's a starting program that generates a random number and uses it to choose a random message.

- Fill in your own print statements for the three messages.
- Run the program multiple times and verify that it works. Note that you might get the same result multiple times in a row.
- Modify the program to use **seven** messages

```
"""
Output random messages
"""

# Import the random function
from random import randint

# Generate a random number from the given range
#
# The value assigned to r is randomly generated every time the program runs
r = randint(1, 3)

# Use the random r value to choose a message
if r == 1:
  # Print the first option
elif r == 2:
  # Print the second option
else:
  # Print the third option
```

### 2d6

Write a program that simulates the roll of two six-sided dice, adds their sum, and prints the two dice and the sum.

Tip: You have to make two calls to `randint`. You can't make one roll and then multiply it by 2. Try using f-strings for the printing.

```
"""
Roll two six-sided dice
"""

# Import randint

# Roll two dice using two variables

# Add their sum

# Print the two dice and then the sum

```

### Shoe sizing

You'd think that shoe sizes would be based on the size of the foot in units of patriotic American inches. And you'd be right...sort of.

Standard U.S. shoe sizing is actually based on units of **barleycorns**, where each barleycorn is one-third of an inch. This standard comes from ye medieval dayes, when, in about the year 1300, the English Parliament passed the *Composition of Yards and Perches*, which defined an inch as equal to three grains of dry barley laid end-to-end.

(A **perch** is a unit equal to five and a half yards, sixteen and a half feet.)

American shoe sizes are determined as follows:

- Measure the length of the foot in inches
- Multiply by 3 to obtain the length in barleycorns
- Subtract a constant, which is 22 barleycorns for men's sizes and 21 for women's

This actually gets even more complicated 

Write a program that can read a foot length in inches and calculate the corresponding show size. For this problem, don't worry about rounding up to the nearest half size; just print the exact size after doing the conversion.

This problem illustrates a new technique: using a numbered menu to select from among a fixed set of options. Use the following code as a starting point. Fill in the statements associated with each comment.
```
"""
Calculate shoe size given foot length in inches
"""

# Define offset constants
OFFSET_MEN = 22
OFFSET_WOMEN = 21


# Read the foot length in inches


# Verify that the length is non-negative


# Print a menu of choices
print('Convert to:')
print('1. Men's size')
print('2. Women's size')


# Read the user's choice as an int


# Choose the offset value based on the user's choice
if choice == 1:
    constant = OFFSET_MEN
else:
    constant = OFFSET_WOMEN

# Calculate the shoe size using constant

# Print the resulting size to two decimal places

```



