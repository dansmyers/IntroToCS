"""
Simulating a deck of 52 playing cards

Each card has a number 0 to 51

The suit and rank functions map a card's number to its associated
suit (clubs, diamonds, etc.) and rank (ace, two, three, etc.)
"""

from random import shuffle

def suit(card):
    """
    Convert a card id to its given suit
    """

    # List of all suits
    SUITS = ['CLUBS', 'DIAMONDS', 'HEARTS', 'SPADES']

    # Dividing by 13 gives 0 if the card is a club, 1 for diamonds, etc.
    suit = card // 13

    return SUITS[suit]


def rank(card):
    """
    Given a card's number, return its associated rank
    """

    RANKS = ['ACE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT',
             'NINE', 'TEN', 'JACK', 'QUEEN', 'KING']

    index = card % 13
    return RANKS[index]


### Main

# Create a list of numbers 0 to 51
deck = list(range(52))

# Simulate the probability of dealing a blackjack on a fresh deck
blackjacks = 0
for trial in range(1000):
    shuffle(deck)

    first = deck[0]
    second = deck[0]
  
    if rank(first) == 'ACE' and rank(second) in ['TEN', 'JACK', 'QUEEN', 'KING']:
        blackjacks += 1

    if rank(second) == 'ACE' and rank(first) in ['TEN', 'JACK', 'QUEEN', 'KING']:
        blackjacks += 1

print(blackjacks / 1000)
