# Put the "Fun" in Functions

## Overview

## Setup

Create a `Lab_5` directory and `cd` into it. Put each question into its own Python file.

## Programs

### `print_area_of_rectangle`

Complete the following program with a function that takes an input length and width, then **prints** the area of the corresponding rectangle.

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

# Write a statement that calls the function with inputs that will print 99 as the output
```


### Willigrams
After Scott invented the Scottometer, Will needed his own unit of measurement so he created the **Willigram**. The actual magnitude of the Willigram is a bit uncertain (the definition has varied over time), but is currently set at 10000 pounds per Willigram.

Write a program that reads a number of pounds from the user and prints the corresponding number of Willigrams. Use a function called `pounds_to_willigrams` to perform the conversion and print the result. Your function should take one input called `pounds`. 

Make sure that your function has an appropriate docstring.

Notice that the `input` statement is in the main part of the program and the input value is passed to the function to get the result. Don't use `input` in the function itself.

```
"""
Convert pounds to Willigrams
"""

### Write your function definition here
#
# The input argument should be named pounds


### Main

# Read a number of pounds
value = int(input('Enter a number of pounds: '))

# Call the function that performs the conversion and prints the result
pounds_to_willigrams(value)
```


### Crickets

Let's return to the cricket protein powder question. Recall that one cricket contains about .3 grams of protein. Complete the program below by writing a function that takes grams of protein as input and **prints** the number of crickets required for that amount.

Tip: Make sure to include a docstring at the start of your function.


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


### Doge II: Return of Doge

<img src="https://i.redd.it/bkhyosuip8g51.jpg" width="300px" />

*The Doge of Venice. You can also read about the complete insanity involved in [selecting a new doge](https://en.wikipedia.org/wiki/Doge_of_Venice#Selection_of_the_doge)*.


Complete the program below by writing a function called `usd_to_doge` that takes a number of USD as input and converts to the equivalent number of DOGE. The function should **print** the result.

Notice how the main section uses an input statement to read a value from the user, then passes that input as a parameter to the function. Don't use `input` in the function itself.

1 dollar is currently worth about 9.17 DOGE.

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

### Card printing

Write a function called `print_card` that takes a number 1 to 13 as input and prints the corresponding playing card name.

- if the input is 1, print `ACE`
- if the input is 2 through 10, print that number
- if the input is 11, print `JACK`, and so forth

```
def print_card(card):

  if card == 1:
    print('Ace')
  elif card == 11:
    print('Jack')
    
  # Add other cases to finish the method
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
