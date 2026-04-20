# Practice with specifications-driven development

## Overview

We practiced using the specs-driven approach to create a tic-tac-toe game. The steps were:

- Ask your model to have a discussion with you about the problem
- Clarify requirements
- Produce a detailed specification document that summarizes what the program should do in natural language
- Ask the model to use the spec to implement the program
- Test the result and make sure that it performs as expected
- If there problems, ask the model to update the spec and re-generate the code

Use that strategy to work on the practice problems below.

## Questions

### Notakto

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/81/Three-board_Notakto.svg/500px-Three-board_Notakto.svg.png" width="300px" />

*Example from Wikipedia*

Like tic-tac-toe but both players make only X's. The first player to complete three in a row (horizontall, vertically, or diagonally) *loses*.

Team up with your neighbor and play a few games.


### Pig

A classic dice game. The object is to be the first person to achieve a score of 100 points.

- On her turn, a player rolls a single six-sided die
- If she rolls a 1, her turn ends immediately and she scores no points for that turn
- If the roll is anything else, it's added to her turn score
- The player can then choose to end her turn and add her current turn score to her total score, or roll again
- Rolling again allows her to accumulate more points, but at the risk of rolling a 1 and ending her turn with a score of 0
- She can continue to roll as many times as she wants until she either chooses to end her turn or rolls a 1

### Blackjack

Implement the blackjack card game. [See here](https://wizardofodds.com/games/blackjack/basics/) for a summary of the rules.

If you're unfamiliar with the game, you can start by just implementing the basic mechanics of dealing cards, hitting and standing. If you've played before, you can think about implementing some of the more advanced features like doubling down, splitting, and insurance.

Think about whether you want to play single hands and keep track of a winning percentage, or implement betting with a player bankroll. Use the planning mode to clarify how the game should work.

### Ship, captain, crew

Another dice game. The player rolls six dice, with the goal of rolling a 6 ("the ship"), a 5 ("the captain"), a 4 ("the crew"), and the highest possible total for the remaining three dice ("the cargo").

- The player rolls six dice
- He can then choose to re-roll some or all of the dice up to three more times
- If multiple players achieve the required 6-5-4 combination, the winner is the player with the highest cargo total. If no player achieves the full 6-5-4, then the winner is the player who comes the closest, where achieving the ship beats any combination that doesn't have a ship, and a ship and captain beat any combination without those two. If multiple players have the same combination, it's a tie.
