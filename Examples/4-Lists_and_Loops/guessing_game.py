"""
Number guessing game with a while loop

This version lets the user loop until they guess the number, then
reports the number of guesses that they needed
"""

from random import randint

target = randint(1, 1000)
guesses = 0

looping = True
while looping:
    guess = int(input('Guess my number: '))
    guesses += 1

    if guess == target:
        print(f'That\'s it! You needed {guesses} guesses.')
        looping = False
    elif guess < target:
        print('Too low')
    elif guess > target:
        print('Too high')
