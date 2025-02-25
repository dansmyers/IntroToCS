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


## Dice Baccarat

<img src="https://assets.bwbx.io/images/users/iqjWHBFdfxIU/iyOGRok9ziCM/v1/1000x-1.jpg" width="50%" />

### Overview

> “The two cards slithered towards him across the green sea. Like an octopus under a rock, Le Chiffre watched him from the other side of the table. Bond reached out a steady right hand and drew the cards towards him. Would it be the lift of the heart which a nine brings, or an eight brings? He fanned the two cards under the curtain of his hand. The muscles of his jaw rippled as he clenched his teeth. His whole body stiffened in a reflex of self-defence. He had two queens, two red queens. They looked roguishly back at him from the shadows. They were the worst. They were nothing. Zero. Baccarat. ‘A card,’ said Bond fighting to keep hopelessness out of his voice. He felt Le Chiffre’s eyes boring into his brain.”
>
> Ian Fleming - *Casino Royale*

*Casino Royale* is the first James Bond novel, published in 1953. In it, Bond travels to a French casino with the goal of challenging and bankrupting Le Chiffre ("The Number"), 
an agent of the Soviets. Bond's game of choice, which occurs repeatedly throughout the early Ian Fleming novels, is **baccarat**.

In real-world casinos, baccarat carries an image of exclusion and luxury. It's traditionally played in special roped off areas with very 
high bets, although many casinos now offer "Mini-Bac", which uses the same rules as the high-end game, but at smaller tables on the main casino floor and with more 
reasonable bets.

This game is a [dice-based variant](https://wizardofodds.com/games/3-dice-baccarat/) of the real baccarat card game.

### Rules

The round begins with the gambler placing bets. The fundamental bet in baccarat is to choose which of two hands will win: the "Player" hand or the "Banker" hand. The names are traditional



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
