# Dice Games

## Passe-Dix

Passe-dix (French for "pass ten") is an ancient dice game. According to some early gambling books, it was allegedly the game played by Roman soldiers to divide the clothes of Jesus at the Crucifixion. The rules are simple: roll three dice and add their sum. The player wins if the sum is strictly greater than 10, loses if the sum is strictly less than 10, and draws ("pushes" in gambling terms) if the sum equals 10.

Write a program that implements passe-dix. Here is example output:

```
The dice are 2, 5, and 1.
The sum is 8.
You lose.
```

Your program should use `randint` three times to generate the three die rolls. Assign each roll to its own variable. Calculate the sum, then use an `if`-`elif`-`else` block to test for the three conditions.


## Cho-Han



Cho-han is a traditional Japanese dice game. The rules are simple:

- The player bets if the sum of two six-sided dice will be odd or even.
- If the player's guess is correct, he wins. If not, he loses.

The game appears in Japanese movies set in historical periods, where it's played by Yakuza gangsters and wandering samurai.

Write a program for cho-han. Your program should prompt the user to choose an even or odd bet, then simulate the roll of two dice and announce if the player was correct. Here's example output:

```
Welcome to Cho-Han.
1. Even
2. Odd
Select a bet: 1
The dice are 1 and 5.
The sum is 6.
You win.
```

Check the user's input to make sure that it's either 1 or 2:
```
Welcome to Cho-Han.
1. Even
2. Odd
Select a bet: -1
You must enter 1 or 2.
```
Use `quit()` to end the program immediately if the user gives you bad input.

The code below shows the general flow of the program. Use it to help you get started. Fill in the code associated with each comment.
```
"""
CHO-HAN
"""

# Import the randint method


# Print the welcome message and the two bets


# Read the number 1 or 2 from the user


# Check if the user's input is 1 or 2; if not, print an error and quit


# Roll two six-sided dice and add their sum


# Use a conditional block to print the output
#
# There are two ways to win:
#     If the player entered 1 and the sum is even
#     If the player entered 2 and the sum is odd
# Every other outcome is a loss
#
# Think about how to turn that into an if-elif-else block

```

## Sic Bo

Sic bo ("precious dice") is a dice game of Chinese origin, now available in many American casinos that cater to Asian gamers. The game is similar to craps: Players roll three dice and bet on the outcome. There are a wide variety of possible bets, but the two most common wagers in sic bo are "big" and "little".

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

Both bets lose if the result is a triple, so you can check for that condition first. To test for a triple, you need the logical `and` of three comparisons
```
if die1 == die2 and die2 == die3 and die1 == die3:
    print('Triple! You have lost.')
```
There are two winning cases:

- The player enter 1 and the result is in the big range
- The player entered 2 and the result is in the little range

Think about how to write conditions for those. Every other outcome is a loss.

