# Fun

<img src="https://collectionapi.metmuseum.org/api/collection/v1/iiif/9821/33434/restricted" width="400px" />

*Frank Lloyd Wright's "kinder-symphony" windows designed for the Avery Coonley House outside of Chicago. From [The Metropolitan Museum of Art](https://www.metmuseum.org/art/collection/search/9821).*

## Overview

Let's practice writing some functions. All of the problems below will let you write functions that take inputs. General tips:

- Remember that function names use the same style as variable names
  
- Give each function a docstring that describes its purpose and inputs

- Functions take **arguments** that are passed when the function is called. Don't use `input` to read the parameters of a function!

- Put function definitions at the top of the program, above the "main" section that contains the executable statements

For this lab, all of our functions will **print** their results. Soon we'll extend this to functions that **return** results so they can be used by other parts of the program.

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

<img src="https://www.liveabout.com/thmb/VL-U6f9b4pDPuedh1OFORBlM0lo=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/GettyImages-84892625-5c76ff65c9e77c0001d19c74.jpg" width="300px" />

*Buddy Holly and the Crickets*

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

### Even-odd

Write a program with a function that takes an integer `n` as input and prints `Even` if `n` is even and `Odd` if `n` is odd. Use an `if-else` block inside the function that tests `n` and prints the appropriate output.

Use a main section that reads a number using `input` and then calls `even_odd`.

```
### Main
number = int(input('Enter a number: '))
even_odd(number)
```

Tip: Recall that you can use the modulus operator to test for evenness: `n % 2 == 0` is `True` if `n` is even.


### Positive-negative-zero

Repeat the previous problem, but write a function called `positive_or_negative` that takes a number `n` as input and prints either `Postive`, `Negative`, or `Zero`, depending on the value of `n`.


### Max

Write a program with a function named `max` that takes **two** inputs named `a` and `b` and prints the larger value.

Tip: There is a built-in `max` function, but don't use it for this problem. Use an `if`-`else` block that compares the two input arguments.

```
"""
Find the max of two inputs
"""

def max(a, b):
    # Print the larger of a or b


### Main

# Read two inputs
first_num = int(input('Enter the first number: '))
second_num = int(input('Enter the second number: '))

# Call the function to compare them
print('The larger value is:')
max(first_num, second_num)
```


### Card printing

Write a function called `print_card` that takes a number 1 to 13 as input and prints the corresponding playing card name.

- if the input is 1, print `Ace`
- if the input is 2 through 10, print the number as a word.
- if the input is 11, print `Jack`, and likewise for the Queen and King.

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

- Print the two choices, then read the player's number. If the player enters anything other than 1 or 2, print an error and quit immediately.
- Roll the two dice, calculate their sum, and print.
- Deal the card using `randint`, then use `print_card` to output it.
- Determine whether the dice or the card are greater.
- Compare the result against the player's bet and announce the result.


### Triple Max

Modify your `max` function to take **three** inputs named `a`, `b`, and `c` and print the largest value. Again, don't use the built-in `max` function.

Tip: Use an `if`-`else` inside of an `if`-`else`. If `a` is greater than `b`, then you can compare `a` and `c` to identify the largest value. Else, `b` is larger, so you can then compare `b` and `c`.

```
"""
Find the max of two inputs
"""

def max(a, b, c):
    # Print the largest of a, b, or c


### Main

# Read three inputs
first_num = int(input('Enter the first number: '))
second_num = int(input('Enter the second number: '))
third_num = int(input('Enter the third number: '))


# Call the function to compare them
print('The largest value is:')
max(first_num, second_num, third_num)
```
