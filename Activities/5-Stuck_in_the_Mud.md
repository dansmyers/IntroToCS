# Stuck in the Mud

## Overview

Stuck in the Mud is a dice game for two or more players. Each player does one round according to the following rules:

- Start with a score of 0.

- Roll five six-sided dice.

- If the player rolled any number of 2s or 5s, the score for the roll is **zero**. Otherwise, add the sum of the dice to the player's score.

- If the player rolled any 2s or 5, those dice become "stuck" and are removed from the rolling pool.

- Repeat the process of rolling the remaining dice, determining the score, and then removing stuck dice until there are no more dice remaining.

- Return the player's final accumulated score.

## Design choices

The major detail of this program is keeping track of the dice pool and removing stuck dice that roll a two or five.

Consider: is it necessary to actually keep track of the individual dice?

No! It's enough to keep track of the *number* of active dice that you need to roll on each round. Making a die "stuck" just reduces this count so you roll fewer dice on the next round.

## Version 1: Basic Game

The code below is a starter version of the basic loop for one player. Put it in a file called `stuck.py`. Run it and play a few rounds.

The code uses a few list features:

- A list comprehension to generate the die rolls. Take a look at that line and make sure you understand how the statement is being interpreted.
- The `count` method to find the number of twos and fives in the list
- The `sum` function to add up the sum of the dice

```
"""
Stuck in the Mud
"""

from random import randint

score = 0
num_dice = 5

# Loop as long as there are dice remaining
while num_dice > 0:
    # Roll the dice - this uses the list comprehension technique
    dice = [randint(1, 6) for i in range(num_dice)]
    print(dice)

    # Count the number of twos and fives
    num_twos_or_fives = dice.count(2) + dice.count(5)

    # If there were twos or fives, reduce the number of dice
    if num_twos_or_fives > 0:
        num_dice -= num_twos_or_fives

    # If not, add the sum to the current score
    else:
        score += sum(dice)

    print(f'Score = {score}')

    # Prompt the user for input before rolling again
    input('Press ENTER to continue.')

print(f'Final score = {score}')
```

## Version 2: Function

Using the code above as a starting point, write a second version that has a `play_round` function. Your function should play one round of the game, as in the version above, and **return** the final score.

```
"""
Stuck in the Mud
"""

from random import randint

def play_round():
    """
    Play one round of the game and return the final score
    """

    # TODO: complete this function


### Main
player_score = play_round()
print(f'Player score = {player_score}')
```

## Version 3: Two players
Modify the version above to allow two players to play the game. Key idea: the code to play one round is now in a function, so you don't have to repeat it; just call the function to implement each player's turn.

Keep track of the two scores and announce the winner.

## Version 4: More players

If you have time, think about a version that works for any number of players.

- At the start, prompt the user to enter the number of players >= 1

- Use a loop to call `play_round` for each player.

- As you go, keep track of the maximum score and the current winning player.

- At the end, announce the top score and the winner.
