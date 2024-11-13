# Nim

## Overview

Nim is a classic mathematical strategy game. It is the more complex version of the Thai 21 subtraction game we looked at in a previous activity.

There are 1 or more piles of stones. On each turn, the player selects one non-empty pile and removes any number of stones from it. The player who is forced to take the last stone is *the loser*.

Let's practice using the stepwise refinement approach to write Nim. Create a file named `nim.py` to hold your program.

## General strategy and starter code

Use a list to represent the piles of stones. We'll use three piles for development, and then modify the program to allow the player to choose the desired number of piles.

Use the code below as your starting point. Work through the numbered steps, implementing the required functions. Use `tic_tac_toe.py` from the last activity as a reference to help you.

```
"""
NIM
"""

# Declare the list of stone piles
stones = [21, 21, 21]
total_stones = 63


### Add additional functions above main


def play_nim():
    """
    Main game loop
    """

    # Variable for the current player
    player = 1

    while True:

        # 1. Print the current player


        # 2. Prompt the current player to select a pile
        #
        # Implement the choose_pile method, which needs to force the
        # player to choose a valid non-empty pile
        pile = choose_pile()


        # 3. Prompt the player to select a number of stones to remove from the pile
        #
        # Again, the function should verify that the choice is valid
        removed = get_removed_stones(pile)


        # 4. Update the number of stones in the chosen pile and the total_stones counter


        # 5. Check for the losing condition, which is total_stones == 0


        # 6. If the game did not end, switch to the other player

        
if __name__ == '__main__':
    play_nim()
```


## Improvements
Once you have the basic game working, modify it to allow the user to choose the number of piles and the starting number of stones. You could do something like the following:
```
num_piles = get_number_of_piles()
num_stones = get_number_of_stones()

stones = [num_stones for i in range(num_piles)]
total_stones = num_stones * num_piles
```


## Advanced RPS

Here's another variation on one of our previous programs. Write a rock-paper-scissors program that allows the human to play multiple rounds against the computer. Play until either the human or computer has two wins and declare the overall winner.

Tip: Think about a main game function that runs a loop. Within that loop, call a second function to play a single round of rock-paper-scissors and return the result of the match, like -1 for a computer win, 0 for a draw, or 1 for a human win. Keep track of the number of computer and human wins and stop when one or the other reaches two. Draws don't affect the count and just continue to the next round.

