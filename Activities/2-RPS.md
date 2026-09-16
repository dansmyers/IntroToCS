# Rock-Paper-Scissors

<img src="https://content.instructables.com/FIU/AIWE/I7Q0TCUT/FIUAIWEI7Q0TCUT.jpg?auto=webp&fit=bounds&frame=1" width="350px" />

*Rock, Paper, Scissors, Lizard, Spock - from [Instructables](https://www.instructables.com/How-to-Play-Rock-Paper-Scissors-Lizard-Spock/)*



## Overview
This activity will lead you guide you through the implementation of an RPS game. This program will tie together pretty much everything that we've done so far in the class:

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
Select your move: 1
Rock. A strong choice.
BEEP BOOP I CHOOSE SCISSORS.
ROCK CRUSHES SCISSORS!
MY FAILURE...DOES NOT COMPUTE...
```

## Setup

`cd` into your `2-Conditionals` directory and create a file named `rps.py`:
```
touch rps.py
```

## Starting code

Use the code below as a starting point. Each of the sections below will ask you to add a new part to the skeleton program.

```
"""
A Rock-Paper-Scissors game that plays one round of human vs. computer
"""

# Imports
from random import randint

# Declare constant variables representing the three moves


# Print the welcome message and list the three moves


# Read the user's move


# If the move is not 1, 2, or 3, print an error and exit


# Print a message in response to the user's move


# Randomly generate the CPU's move using randint


# Print a string representing the CPU's move


# Determine the outcome and print a message

```

## Step 1: Declare constants
We have to decide how to represent the player's and computer's moves. There are many different ways to do this. We could, for example, 
have the player type in a string for the chosen move, like "Rock". This approach could work, but we'd have to deal with the complexity 
of raw text input and capitalization.

A more structured approach is to assign each move a number. Now, we can read the user's move by prompting him or her to type 1, 2, or 3 and generate the computer's move by picking a random value 1, 2, or 3.

Add three lines mapping the three moves to the numbers 1, 2, and 3:

```
ROCK = 1
PAPER = 2
SCISSORS = 3
```

Now you can use the name ROCK in your program instead of always remembering that 1 stands for rock.

### Aside: Constants

Recall that variables named with ALL_CAPS are considered to be **constants**: the value of a constant variable **should not change** after its first assignment.

The use of ALL CAPS names to indicate constants is a **convention** of Python programming, not a rule. Other languages, like Java, have ways to declare constants that literally cannot change: the Java compiler will generate an error if you attempt to modify a constant variable.


## Step 2: Print the welcome message and list the three moves
Add four print statements that print the opening text for the game.

```
Welcome to Rock, Paper, Scissors.
1. Rock
2. Paper
3. Scissors
```


## Step 3: Read the player's move
Prompt the player to select one of the moves and read the numeric response using `input` and `int`. Assign it to a variable named `player_move`.


## Step 4: Check for Valid Input
The only legal moves are 1, 2 or 3. Add some code to check if the user enters a value outside that range, and if so exit the program.

Tip: Use the `or` operator to test for a value outside the range of 1 to 3. If the player's input is assigned to a variable named `player_move`, you could use
```
if player_move < 1 or player_move > 3:
    # Add code to print an error message and then quit
```


## Step 5: Print the player's move
Add an `if-elif-else` block that tests the player's input and prints a little text response.
```
if player_move == ROCK:
    print('Rock. A strong choice.')

# Add two more cases for PAPER and SCISSORS
```
Notice how the example code tests against the constant `ROCK` rather than the literal number `1`. This makes it easier to understand what the program is checking.

## Step 6: Randomly generate the CPU's move
Write a line that uses `randint` to generate a 1, 2, or 3 and save it into a variable named `cpu_move`.


## Step 7: Print the CPU's move
Add another `if-elif-else` block to print a message for each possible computer move.
```
if cpu_move == ROCK:
    print('BEEP BOOP I CHOOSE ROCK.')
```
Add two more cases for PAPER and SCISSORS.

## Step 8: Determine the Outcome
This is the most complex part. You need to write a set of conditional statements that will compare the player and CPU moves and print the appropriate outcome message.

One case is easy: if the moves are the same, it's a draw.
```
if player_move == cpu_move:
    print('DRAW. I WILL GET YOU NEXT TIME HUMAN.')
```
Add more statements to test for the other possible combinations. For example,
```
elif player_move == ROCK and cpu_move == PAPER:
  print('PAPER COVERS ROCK.')
  print('HUMANS...SO SOFT...SO WEAK.')
```
Continue until you've covered all combinations of `player_move` and `cpu_move`.


## Sic Bo

When you've finished rock-paper-scissors, here's another dice game.

Sic bo ("precious dice") is a dice game of Chinese origin, now available in many American casinos that cater to Asian gamers. The game is similar to craps: players roll three dice and bet on the outcome. There are a variety of possible bets, but the two most common wagers in sic bo are "big" and "little".

- The big bet wins if the sum of the three dice is 11 to 17 (including both), but not three-of-a-kind
- The little bet wins if the sum of the three dice is 4 to 10 (including both), but not three-of-a-kind

Write a program for sic bo using the big and little bets. For example,
```
Welcome to Sic Bo.
1. Big
2. Little
Choose a bet: 2
The three dice are 3, 5, and 1.
The sum is 9.
You win.
```
Use the code for cho-han as a guide, but adapt it to roll three dice and use the winning and losing conditions for sic bo.

Tip:

Both bets lose if the result is a triple, so you can check for that condition first. Use logical `and`:
```
if die1 == die2 and die2 == die3:
    print('Triple! You have lost.')
```
There are two winning cases:

- The player entered 1 and the result is in the big range
- The player entered 2 and the result is in the little range

Think about how to write conditions for those cases. Every other outcome is a loss.
