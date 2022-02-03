# Games and Functions

## Overview

This lab will let you practice one more text-based game project: rock-paper-scissors, which will tie together everything that we've done in the class up to this point.

The second part of the lab will let you practice writing your own functions and help you get familiar with Python's function syntax.

## Rock-Paper-Scissors

### Overview
This section will lead you guide you through the implementation of an RPS game. This program will tie together pretty much everything that we've done so far in the class:

- Printing
- Variables
- User input
- Relational operators
- Conditional execution
- Randomness
- Logical operations

This version of the game will play one round of human vs. computer. A little later, we can talk about how to modify the program to play something like best two-out-of-three.

Here's an example play session.

```
Welcome to Rock, Paper, Scissors.
1. Rock
2. Paper
3. Scissors
Select your move:
1
Rock. A strong choice.
BEEP BOOP I CHOOSE SCISSORS.
ROCK CRUSHES SCISSORS!
MY FAILURE...DOES NOT COMPUTE...
```

### Setup

```
cd CMS_120

mkdir Lab_4

cd Lab_4

touch rps.py

open rps.py
```

### Starting Code

Use the code below as a starting point. Each of the sections below will ask you to add a new part to the skeleton program.

```
"""
A Rock-Paper-Scissors game that plays one round of human vs. computer

CMS 120
"""

# Imports
from random import randint
import sys

# Declare constant variables representing the three moves

# Print the welcome message and list the three moves

# Read the user's move

# If the move is not 1, 2, or 3, exit the program

# Randomly generate the CPU's move using randint

# Print a string representing the CPU's move

# Determine the outcome and print a message

```

### Step 1: Declare Constants
We have to decide how to represent the player's and computer's moves. There are many different ways to do this. We could, for example, 
have the player type in a string for the chosen move, like "Rock". This approach could work, but we'd have to deal with the complexity 
of raw text input.

A more structured approach is to assign each move a number. Now, we can read the user's move by prompting him or her to type 1, 2, or 3 and generate the computer's move by picking a random value 1, 2, or 3.

Add three lines mapping the three moves to the numbers 1, 2, and 3:

```
ROCK = 1
PAPER = 2
SCISSORS = 3
```

Now you can use the name ROCK in your program instead of always remembering "1 stands for rock."

### Aside: Constants

Recall that variables named with ALL CAPS are considered to be **constants**: the value of a constant variable **should not change** after its first assignment.

The use of ALL CAPS names to indicate constants is a **convention** of Python programming, not a rule. Other languages, like Java, have ways to declare constants that literally cannot change: the Java compiler will generate an error if you attempt to modify a constant variable.


### Step 2: Print the Welcome Message and List the Three Moves
Add four print statements that print the opening text for the game.

```
Welcome to Rock, Paper, Scissors.
1. Rock
2. Paper
3. Scissors
```


### Step 3: Read the Player's Move
Prompt the player to select one of the moves and read the response using `input`.

```
player_move = int(input('Select your move: '))
```


### Step 4: Check for Valid Input
The only legal moves are 1, 2 or 3. Add some code to check if the user enters a value outside that range, and if so exit the program.

```
if player_move < 1 or player_move > 3:
    print('That is not a valid move.')
    sys.exit()
```


### Step 5: Print the Player's Move
Add an `if-elif-else` block that tests the player's input and prints the associated move.

```
if player_move == ROCK:
    print('Rock. A strong choice.')
```

Add two more cases for PAPER and SCISSORS.

### Step 6: Randomly Generate the CPU's Move
Write a line that uses `randint` to generate a 1, 2, or 3 and save it into a variable named `cpu_move`.

```
cpu_move = randint(1, 3)
```

### Step 7: Print the CPU's Move
Add another `if-elif-else` block to print a message for each possible computer move.

```
if cpu_move == ROCK:
    print('BEEP BOOP I CHOOSE ROCK.')
```

Add two more cases for PAPER and SCISSORS.

### Step 8: Determine the Outcome
This is the most complex part. You need to write a set of conditional statements that will compare the player and CPU moves and print the appropriate outcome message.

One case is easy: if the moves are the same, it's a draw.

```
if player_move == cpu_move:
    print('DRAW. I WILL GET YOU NEXT TIME HUMAN.')
```

Now add more statements to test for the other possible combinations. For example,

```
if player_move == ROCK and cpu_move == PAPER:
  print('PAPER COVERS ROCK.')
  print('HUMANS...SO SOFT...SO WEAK.')
```

## You Can't Spell "Function" Without "Fun"

### `print_area_of_circle`

Complete the program below by writing a function that takes the radius of a circle as input and **prints** the corresponding area.

```
"""
Write a function that prints the area of a circle
"""

from math import pi

def print_area_of_circle(radius):
    """
    Complete this function docstring
    """
    
    # Calculate the area of the circle with the input radius
    
    # Print the area
    

### Main
#
# Remember: execution of the program starts HERE

print_area_of_circle(1)

print_area_of_circle(10)

print_area_of_circle(100)

# Add one more statement to print the area of a circle with radius 1000

# How about printing the area of a circle with radius 1 million?
```

### `print_area_of_rectangle`

Complete the following program with a function that takes an input length and width, then prints the area of the corresponding rectangle. This example shows how to write a
function that takes multiple parameters.

```
"""
Write a function that prints the area of a rectangle
"""

def print_area_of_rectangle(length, width):
    """
    Complete this function docstring
    """
    
    # Calculate the area of the rectangle
    
    # Print the result
    

### Main

print_area_of_rectangle(10, 5)

print_area_of_rectangle(3, 11)

# Add a statement to print the area of a rectangle with length 7 and width 17

# Write a statement that calls the function and prints 99
```

### Willigrams

After Scott invented the Scottometer, Will needed his own unit of measurement so he created the **Willigram**. The actual magnitude of the Willigram is a bit uncertain (the
definition has varied over time), but is currently set at 10000 pounds per Willigram (no, this does not make any sense; just go with it).

Write a program that reads a number of pounds from the user and prints the corresponding number of Willigrams. Use a function called `pounds_to_willigrams` to perform the conversion and print the result. Your function should take one input called `pounds`. Make sure that your function has an appropriate docstring.

```
"""
Convert pounds to Willigrams
"""

### Write your function definition here


### Main

# Read a number of pounds
value = int(input('Enter a number of pounds: '))

# Call the function that performs the conversion and prints the result
pounds_to_willigrams(value)
```

### Fake Internet Meme Money

<img src="https://external-preview.redd.it/3_iVT6i7dReTdMXS-bNiIS0U9p2QTsfq6BUDC57b8tc.jpg?auto=webp&s=5943d7cf04be56a4de8cf045667e41631c02a90e" width="35%" />

Dogecoins, the favored cryptocurrency of shiba inus everywhere, currently trades for about .071987 USD per DOGE.

Write a program that reads a number of dollars as input, then uses a function to calculate and print the corresponding amount of DOGE. Your function should be called
`usd_to_doge` and take one input parameter called `usd`.

Tip: think carefully about how to do the conversion and whether you need to multiply or divide.

```
"""
USD to DOGE converter
"""

### Write your function definition here


### Main

# Read a number of dollars
value = float(input('Enter a number of dollars: '))

# Call a function that converts to DOGE and prints the result
usd_to_doge(value)
```

### Cricket Protein Powder

<img src="https://cdn.shopify.com/s/files/1/0904/3248/products/chocolate_front_1408x1408.jpg?v=1566244530" width="35%" />

As a deep thinker and observer of modern society, I truly believe that entomophagy is the wave of the future. Crickets are a naturally renewable (albeit noisy) resource and
contain proportionally more protein than chicken or beef.

Through a totally unscientific research process, I have learned that the average cricket weighs .50 grams and consists of about 60% protein, for an average of .30 grams of protein per cricket.

Write a program to read in a number of grams of protein as input, then use a function to calculate and print the corresponding number of crickets needed to produce that 
amount of protein. Your function should be called `grams_of_protein_to_crickets` and take one input parameter named `grams`.

How many crickets are required to make 1 kilogram of protein?

```
"""
Convert grams of protein into crickets
"""

### Write your function definition here


### Main

# Read input number of grams of protein
value = float(input('Enter a number of grams of protein: '))

# Call the function to perform the conversion and print the result
grams_of_protein_to_crickets(value)
```

### 
