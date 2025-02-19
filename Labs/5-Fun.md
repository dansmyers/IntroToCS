# Fun

<img src="https://collectionapi.metmuseum.org/api/collection/v1/iiif/9821/33434/restricted" width="400px" />

*Frank Lloyd Wright's "kinder-symphony" windows designed for the Avery Coonley House outside of Chicago. From [The Metropolitan Museum of Art](https://www.metmuseum.org/art/collection/search/9821).*

## Overview

Let's practice writing some functions. All of the problems below will let you write functions that take inputs. General tips:

- Remember that function names use the same style as variable names
  
- Give each function a docstring that describes its purpose and inputs

- Functions take **arguments** that are passed when the function is called. Don't use `input` to read the parameters of a function!

- Put function definitions at the top of the program, above the "main" section that contains the executable statements

## Setup

Create a `Lab_5` directory and `cd` into it. Put each question into its own Python file.

## Programs

### Positive-negative-zero

Write a function called `positive_or_negative` that takes a number `n` as input and **prints** either `Postive`, `Negative`, or `Zero`, depending on the value of `n`.

```
"""
Print if a number is positive, negative, or zero
"""

def positive_or_negative(n):
    """
    Fill in this docstring
    """

### Main

positive_or_negative(10)
positive_or_negative(-7)
positive_or_negative(0)
```

### Return of pounds to kilograms
Write a function called `pounds_to_kilograms` that takes a number of pounds as input and **returns** the corresponding number of kilos. There are about 2.20462 pounds in a kilogram.
```
"""
Pounds to kilograms
"""

def pounds_to_kilograms(pounds):
    """
    Fill in this docstring
    """

    # Calculate the number of kilos

    # Return that value - don't print anything!

### Main
num_pounds = 10000
num_kilos = pounds_to_kilos(num_pounds)
print(f'{num_pounds} pounds is about {num_kilos} kgs.')
```

### BTC

Write a program with a function named `btc_to_usd` that takes a number of bitcoins as input and **returns** the corresponding number of patriotic American fiat dollars. There are currently approximately $94167.20 per bitcoin.

- Your function can take one input named `btc`
- Use one `return` statement at the end of the function
- Don't use `input` or `print` inside the function
- Use the main section to read input, call the function, and print the result

Use the previous program as your model.

### Parsecs

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Stellarparallax_parsec1.svg/1024px-Stellarparallax_parsec1.svg.png" width="300px" />

*Explanatory image from [Wikipedia](https://en.wikipedia.org/wiki/Parsec)*

<br/>

A **parsec** is a unit used to measure large astronomical distances.

The name is short for *distance corresponding to a parallax of one second*. "Parallax" refers to the apparent motion of stars as seen from the Earth. As the Earth rotates around the Sun, the angle at which an observer views a star will change over the course of the year. This results in nearer stars appearing to make small orbits relative to the more distant background stars.

The parsec is defined to be the distance at which the angle determined by the apparent orbit is one arcsecond (1/3600 of a degree). This turns out to be 3.26 light years, or 19.2 trillion miles.

Write a program with a function called `parsecs_to_miles` that takes a number of parsecs as input and **returns** the corresponding number of miles. As before, use a main section that reads an input number of parsecs, calls the function, then prints the answer.

Tip: You can represent 19.2 trillion in scientific notation using `19.2e12`. That's short for 19.2 * 10<sup>12</sup>.

### Max

Write a program with a function named `max` that takes **two** inputs named `a` and `b` and **returns** their maximum.

Tip: There is a built-in `max` function, but don't use it for this problem. Use an `if`-`else` block that compares the two input arguments. You can put a return statement in each branch.

```
"""
Find the max of two inputs
"""

def max(a, b):
    # Return the maximum of a or b


### Main

# Read two inputs
first_num = int(input('Enter the first number: '))
second_num = int(input('Enter the second number: '))

# Call the function to compare them
maximum = max(first_num, second_num)
print(f'The larger value is: {maximum}')
```


### Triple Max

Modify your `max` function to take **three** inputs named `a`, `b`, and `c` and return the largest value. Again, don't use the built-in `max` function.

Tip: Use an `if`-`else` with a second `if`-`else` inside each branch.

- If `a` is greater than `b`, then you can compare `a` and `c` to identify the largest value
- Else, `b` is larger, so you can then compare `b` and `c`

```
"""
Find the max of three inputs
"""

def max(a, b, c):
    # Print the largest of a, b, or c


### Main

# Read three inputs
first_num = int(input('Enter the first number: '))
second_num = int(input('Enter the second number: '))
third_num = int(input('Enter the third number: '))


# Call the function to compare them
maximum = max(first_num, second_num, third_num)
print(f'The largest value is {maximum}.')
```

## Dice Rolling

### d20

Write a program with a function called `d6` that **returns** the roll of a twenty-sided die.
```
"""
Die rolling program
"""

from random import randint

def d20():
    """
    Return the roll of a twenty sided die
    """


### Main
die1 = d20()
die2 = d20()
print(die1, die2)
```


### Ability check

Write a function called `check_roll` that uses `d20` to perform a Dungeons n' Dragons style ability check. The function takes two inputs called `modifier` and `difficulty`. The modifier input may be positive or negative.

- Roll `d20` and add `modifier`
- Compare the result to `difficulty`
- If the result is *greater than or equal to* `difficulty`, the player passes the check. Return `True`.
- Otherwise, return False. The player has failed the ability check.

For example, a call to `check_roll(3, 12)` would roll a twenty-sided die, add 3, then check if the sum is at least 12.


## Card Games


### Card printing

Write a function called `print_card` that takes a number 1 to 13 as input and prints the corresponding playing card name.

- if the input is 1, print `Ace`
- if the input is 2 through 10, print the number as a word.
- if the input is 11, print `Jack`, and likewise for the Queen and King.

The function is going to look like this:
```
def print_card(card):
    """
    Fill in this docstring
    """

    if card == 1:
        print('Ace')
    elif card == 2:
        print('Two')
    
    # Add other cases to finish the method

    elif card == 13:
        print('King')
```

Here's a test program:
```
"""
Print cards
"""

from random import randint

# Put your function here


### Main

# Deal some random cards and print them
c1 = randint(1, 13)
print_card(c1)

c2 = randint(1, 13)
print_card(c2)
```

### Hi-Lo

A simple card game.

- The computer generates one randomized playing card and shows it to the player.
- The player guesses whether the next card will be **higher** in rank or **lower** in rank.
- The computer generates a second card, shows it to the player, and announces whether the guess was correct.

Use `randint(1, 13)` to generate a random card and `print_card` from the previous problem to print card names.

```
"""
Hi-Lo card game
"""

from random import randint

### Put your print_card function here


### Main

# Generate the first card
first_card = randint(1, 13)

# Print the first card
print('The first card is: ')
print_card(first_card)

# Print the menu of choices for the user
# 1. Higher
# 2. Lower

# Read the user's input

# Generate and print the second card

# Print a winning or losing message based on the user's choice and result

```

Another question: Is generating a card using `randint(1, 13)` the same as simulating drawing from a deck of 52 cards?


### Dice vs. Card

Here's a variation of the Hi-lo game that I learned from the [Wizard of Odds](https://wizardofodds.com/games/easy-over-under/), my go-to source for gambling knowledges.

The player bets if the sum of two dice will be greater than or less than the value of a single card. The card is scored 1-13, as in the previous problems. Here's an example output:
```
Welcome to dice vs. card.
1. The dice will be higher
2. The card will be higher
Select your bet: 1
The dice are 5 and 4. The sum is 9.
The card is:
Jack
The card is higher.
You lose.
```
Use an approach similar to our previous chance games:

- Print the two bets, then read the player's number. If the player enters anything other than 1 or 2, print an error and quit immediately.
- Roll the two dice, calculate their sum, and print.
- Deal the card using `randint`, then use `print_card` to output it.
- Determine whether the dice or the card are greater.
- Compare the result against the player's bet and announce the result.



