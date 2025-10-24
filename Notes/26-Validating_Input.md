# Validating Input

## Topics

- The subtraction game
- Forcing the user to give valid input
- `try`-`except` and exception handling

## The subtraction game

Our example for this class is the Subtraction Game, which exists in a lot of variants. Our basic version is as follows:

- There is a pile of 21 stones
- Players alternate turns removing 1, 2 or 3 stones
- The player who takes the last stone is the ***winner*** in our version. A standard variation is to make the player who takes the last stone the loser.

The basic game is below. It uses a `while` loop to play each round. Since we don't know in advance how many rounds will be required, `while` is appropriate. Rather than make two nearly-identical blocks of code 
