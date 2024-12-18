# The Compleat Gamester

<img src="https://upload.wikimedia.org/wikipedia/commons/f/fe/Scenes_of_life_in_the_Dutch_factory_at_Deshima_building_detail.jpg" width="500px" />

*Gaming scene from a Dutch factory in the Edo period. From Wikipedia.*

## Overview

This lab will let you practice writing more games of chance using functions that return results. All of these programs are moderately long and will required combining all of the techniques we've seen so far in the course.

The title of this lab comes from an early English book on gaming, *The Compleat Gamester*, published in 1674 and attributed to Charles Cotton.

Mr. Cotton was a big fan of compleatness: He also contributed to a book called *The Compleat Angler* ("Being a difcourfe of FISH and FISHING not unworthy of the perufal of moft Anglers.")

## Setup

Create a `Lab_6` directory in your workspace and `cd` into it.
```
mkdir Lab_6
```
```
cd Lab_6
```
The questions will tell you how to create and name your Python scripts.


## Mob Programming

<img src="https://upload.wikimedia.org/wikipedia/commons/c/c8/Forrester-Kangaroo-mob.jpg?20060125000755" width="300px" />

[Mob programming](https://www.agilealliance.org/glossary/mob-programming/) is a programming strategy where the entire team works together, as a group, at one computer.

Form a team of **three**. You will all work together, at the same time, on the same problem. One person will be the "driver" who actually types code onto the computer. Change drivers for each problem, so everyone gets a chance to type.

At the end of the lab, download and e-mail the finished solutions to all of the team members.


##  Hi-Lo

### Description

Let's start with a simple card game. We'll write the basic game without using functions, then add some more features in the next question.

- The computer generates one randomized playing card and shows it to the player.
- The player guesses whether the next card will be **higher** in rank or **lower** in rank.
- The computer generates a second card, shows it to the player, and announces whether the guess was correct.

Use `randint(1, 13)` to generate a random card. For this first version, **print the number of the card**.

Put your program in a file named `hi_lo.py`.

```
"""
Hi-Lo card game
"""

from random import randint


### Main

# Generate the first card
first_card = randint(1, 13)

# Print the first card
print(f'The first card is: {first_card}')

# Print the menu of choices for the user
# 1. Higher
# 2. Lower

# Read the user's input

# Generate and print the second card

# Print a winning or losing message based on the user's choice and result

```

Quick question: Is generating a card using `randint(1, 13)` the same as simulating drawing from a deck of 52 cards?

### Card printing

Now improve the program by writing a `card_name` function that takes a number 1 to 13 as input and **returns** the corresponding playing card name as a string.

- if the input is 1, return `'Ace'`
- if the input is 2, return `'Two'` and likewise for the other number cards
- if the input is 11, return `'Jack'`, and so forth for the Queen and King.

```
def card_name(card):
    """
    Fill in this docstring
    """

    if card == 1:
        return 'Ace'
    elif card == 2:
        return 'Two'
    
    # Add other cases to finish the method
```

Add this function to your `hi_lo.py` program and then modify the main section to print the name of the card instead of its number.
```
print(f'The first card is: {card_name(first_card)}')
```


### Dice vs. card

Here's a variation of the Hi-lo game that I learned from the [Wizard of Odds](https://wizardofodds.com/games/easy-over-under/), my go-to source for gambling knowledges.

The player bets if the sum of two dice will be greater than or less than the value of a single card. The card is scored 1-13, as in the previous problems. Here's an example output:
```
Welcome to dice vs. card.
1. The dice will be higher
2. The card will be higher
Select your bet: 1
The dice are 5 and 4. The sum is 9.
The card is: Jack
The card is higher.
You lose.
```

Put your code in a file named `dice_vs_card.py`. Use an approach similar to our previous chance games:

- Print the two choices, then read the player's number. If the player enters anything other than 1 or 2, print an error and quit immediately.
- Roll the two dice, calculate their sum, and print.
- Deal the card using `randint`, then use `card_name` to output it.
- Compare the two results against the player's bet and announce the result.

## Two-Card Blackjack

[*I like to live dangerously*.](https://www.youtube.com/watch?v=s_uAjPV7qec)

### Description

Let's write a variation of the classic blackjack game.

The goal of this version will be to get as close as possible to **11** without going over. The player starts with a single card and can choose to **draw one (and only one) more card**.

Here's a more detailed description of the game:

1. Deal one card to the player and print it
2. Deal one card to the dealer and print it
3. If the card is an Ace, the player wins immediately
4. If the dealer's card is an Ace and the player's card is not, the dealer wins immediately
5. The player may choose to Hit or Stand
6. If the player hits, he takes one more card
7. If the combined total of the player's two cards is greater than 11, he busts and loses immediately
8. If the dealer's card is less than 7, he hits and takes one more card
9. If the dealer's total is greater than 11, he busts and the player wins immediately
10. If neither busted, compare the totals of the two hands; the highest score wins

Here is example output:
```
Welcome to two-card blackjack.
Your first card is: Six.
The dealer's card is: Three.
1. Hit
2. Stand
Do you want to hit or stand? 1
Your second card is: Four.
Your total is 10.
The dealer draws: Five.
The dealer's total is 8.
Your 10 beats the dealer's 8.
You win!
```

### Starting code

Make a new file called `blackjack.py`. Paste in the following starter code. It includes space for three functions that you'll write in a moment.

This code is long, but don't be intimidated! Look at the structure given by the comments and compare it to the example output above.

```
"""
BLACKJACK
"""

from random import randint


### Define a function called deal that returns a randomly generated card, 1 to 13


### Define a function called card_name that returns the name of a card


### Define a function called value that returns the blackjack value of a card



### Main

# Print the welcome message

# Deal the player's first card and print its name
first_card = deal()
print(f'Your first card is {card_name(first_card)}')

# Deal one card to the dealer and print its name

# If the first card is an Ace, the player wins immediately

# Print the choices to hit or stand
print('1. Hit')
print('2. Stand')

# Read the player's choice
choice = int(input('Do you want to hit or stand? '))

# If the player chose to hit, deal one more card
if choice == 1:
    second_card = deal()
else:
    second_card = 0

# Calculate and print the total of the player's hand
player_total = value(first_card) + value(second_card)
print(f'Your total is {player_total}')

# If the total is greater than 11, the player busts and loses immediately

# If the value of the dealer's card is less than 7, give the dealer a second card
# Else, the dealer's second card is 0

# Calculate and print the dealer's total

# If they dealer's total is greater than 11, it busts and loses immediately

# Neither player has busted, compare their scores and announce the winner

```

### The `deal` function
Write the first function, `deal`, which returns the result of calling `randint(1, 13)`.


### The `card_name` function

Copy your `card_name` function from the Hi-Lo program.


### The `value` function

This function takes a card number 1 to 13 as input and returns its blackjack value:

- Number cards 2-10 count for their face value
- Jack, Queen, and King count for **10**
- Aces, in this version, count for **1**
- If the card anything else, return a value of 0

```
def value(card):
    """
    Complete this docstring
    """

    if card == 1:  # Ace
        return 1

    # Add more cases to complete the method

    elif card == 13:  # King
        return 10
    else:
        return 0
```

Tip: You don't need to write individual cases for all the numbers 2 through 10. Think about how you can write one `elif` statement that works for any input in that range.

### Finish the game

After adding the three functions, finish coding the main section. You have a few lines to add in the player section, which you can then use as a model to complete the dealer section.

Build incrementally! Add a few lines at a time, then test to make sure your code works before you add more.

Once you've finished, experiment with playing several hands. Make sure that your code works for every case.


## Red Dog

<img src="https://cms-tc.pbskids.org/global/_generic600Wide/905x510_Clifford_Mezzanine_V2.jpg" width="300px" />

*PBS Kids*

### Description

Another old card game existing in many variants. Deal two cards, then the player bets if a third card will be between the two or not.

- Deal two cards and announce their values
- Calcuate and annouce the spread, which is the difference between the cards
- If the two cards are equal, the game ends immediately
- The player enters an amount they wish to bet (minimum $1)
- Deal the third card
- If the third card is between the first two (inclusive of both), the player's bet wins
- If the card is outside the first two cards, the bet loses

Note that the player **wins** if the third card **equals** either of the first two.


Here's example output:
```
Welcome to Red Dog.
The cards are Jack and Seven.
The spread is 4.
Enter your bet: 50
You bet $50.
The third card is Eight.
You win $100.
```

#### Payouts

The player can bet any amount as long as it's at least 1. To keep the betting interesting, the payout depends on the spread between the first two cards:

- If the spread is 1, the player wins 5 times the bet
- If the spread is 2, the player wins 4 times the bet
- If the spread is 3, the players wins 2 times the bet
- If the spread is 4 or more, the player wins the bet amount

#### Card values

In our game, cards are scored 1 to 13, with Ace low and King high.

### Starter code

Make a file named `red_dog.py`. Start by sketching out the solution in comment form, using the rules and output above as a guide.

### Implement!

Work on filling in your program one step at a time. Again, think about developing incrementally and **test as you go**.

You will need `randint` to generate the cards and the `card_name` method for printing. You can add other functions if you find them helpful.


#### Tip: Card Ordering

It's helpful to order the cards so that the first card is the lower-valued one. After generating the first two cards, compare and swap them if necessary:
```
# Swap the cards if necessary so that first_card is lower
if first_card > second_card:
    temp = first_card
    first_card = second_card
    second_card = temp
```
You can then calculate the spread:
```
spread = second_card - first_card
```
And test if the third card is in between:
```
if third_card >= first_card and third_card <= second_card:
    # The bet wins
```
