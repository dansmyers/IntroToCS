# The Heart of the Cards

## Overview

## Setup


## Enumerated Types

Start by making a file named `card.py`.

To begin, we're going to define special classes that represent the four playing card suits (clubs, diamonds, hearts, and spades) and the 13 card ranks (Ace through King). We previously managed this by mapping each suit and rank to an integer, but now we're going to introduce a more robust object-oriented technique: **enumerated types**.

An enumerated type (often shortened to *enum*) is a data type that can take on only a limited, fixed set of values. For example, we might define an enum to represent the four cardinal directions north, south, east, and west. A variable with that type can then only take one of those four specific values. Here we're going to create a enumerated types to represent the four playing card suits and the thirteen ranks. 

Put the following code in `card.py`:
```
"""
A single playing card with a suit and rank
"""

from enum import Enum

class Suit(Enum):
    CLUBS = 1
    DIAMONDS = 2
    HEARTS = 3
    SPADES = 4
```
Capital-E `Enum` is Python's built-in module for representing enumerated types. The class declaration for `Suit` specifies that it is a type of `Enum` and then declares the enumerated values.

Each value has a name (`CLUBS`, `DIAMONDS`, and so forth) and a value (1, 2, 3, or 4). The values are used to give an ordering to the types, so that we can compare them. Here, `CLUBS` has the lowest value, followed by `DIAMONDS`, then `HEARTS`, with `SPADES` as the highest-valued suit. This type of ordering is used in games like Bridge. The values don't have to be consecutive integers, although that's the most common case.

Now add a second class declaration to create a `Rank` enum and give it types for `ACE`, `TWO`, `THREE`, and so forth up to `JACK`, `QUEEN`, and `KING`.
```
class Rank(Enum):
    ACE = 1
    TWO = 2

    # Finish the rest of the declarations
```

## The `Card` Class

Now make a `Card` class with `__init__` and `__str__` methods:
```
class Card:
    """
    A single playing card with a suit and rank
    """

    def __init__(self, new_suit, new_rank):
        # Fill in the body of the constructor that assigns the internal suit and rank fields


    def __str__(self):
        return f'{self.rank.name} of {self.suit.name}' 

```
The `__str__` method returns a string representation of the object's data. Notice how it uses the `name` field of the enumerated type to get printable name of the rank and suit variables.

You can then add a main block to the end of the script that creates and prints some example cards:
```
if __name__ == '__main__':
    ace_of_spades = Card(Suit.SPADES, Rank.ACE)
    print(ace_of_spades)
```
Add additional statements to create and print the Queen of Hearts, Jack of Diamonds, and Two of Clubs.


## Comparisons

Add the following code to your testing block and see what happens when you run it:
```
ace_of_spades_2 = Card(Suit.SPADES, Rank.ACE)
print(ace_of_spades_2 == ace_of_spades)
```

Consider: the two cards have equal suits and ranks, but a comparison using `==` returns `False`. Prompt your favorite chat to give you an explanation of this behavior.

### Reference equality vs. value equality

As my friend Claude explained, the default object comparison behavior checks if the two objects **are the same object in memory**; that is, if they are stored at the same underlying memory address. This is called **reference equality**.

Even though the two aces of spades have the same suit and rank values, they are *different objects* created with two calls to the constructor, so they're stored at different locations in memory and, hence, unequal by the standard comparison.

In most cases, we want to compare objects using **value equality** by testing if they have equivalent data.

### The `__eq__` method

You can add a custom equality checking method called `__eq__` to a class to test for value equality. As the name implies, this is an internal method that *overrides* the default `==` behavior. When Python sees two objects of the same class compared using `==`, it will call the `__eq__` method behind the scenes and use the boolean it returns as the result of the comparison.
```
def __eq__(self, other):
    """
    Test if this card has the same suit and rank as the other card
    """
    return self.suit == other.suit and self.rank == other.rank
```
Add the new method to your class and re-run to verify that you're now comparing cards using value equality.

### The `__lt__` method
Add another method called `__lt__` that implements the less-than comparison. You can use the suit and rank values to test for ordering:

- If the suits are different, return `True` if `self.suit.value < other.suit.value`
- If the suits are equal, return `True` if `self.rank.value < other.rank.value`

# Deck

Make a new file called `deck.py`. This file will have a class representing a deck of 52 playing cards.
```
"""
Deck of cards
"""

# This line imports the class definitions from card.py
from card import Card, Suit, Rank

class Deck:
    def __init__(self):
        # Complete this method below

    def __str__(self):
        # Complete this method below


if __name__ == '__main__':
    d = Deck()
    print(d)
```

### The `__init__` method

The deck will use a list to store 52 `Card` objects having all suit-rank combinations. This turns out to be easy to initialize:
```
def __init__(self):
    self.cards = []

    for suit in Suit:
        for rank in Rank:
            self.cards.append(Card(suit, rank))
```
The loops iterate through all combinations of suit and rank, construct a `Card` object with the combination, then append it to the list of cards. This can also be done in list comprehension style:
```
self.cards = [Card(suit, rank) for suit in Suit for rank in Rank]
```

### The `__str__` method
The to-string method needs to return a string representation of the cards in the deck. This is partly done, since the `Card` class has its own `__str__` method, so we can convert any `Card` into its own string.

Here's an approach:

- Construct a list containing the *names* of every `Card` in the deck
- Convert that list to a string

```
# Construct a list containing the name of every card
card_name_list = [str(card) for card in self.cards]

# Convert that list to a printable string
return str(card_name_list)
```
Both actions use the `str` method. We previously used that to covert numbers in their string forms. When applied to an object, it invokes the built-in `__str__` method to get a string representation.

After you've implemented both methods, run the basic program and verify that it prints the complete list of cards. Observe that they're in the ordering determined by the enumerated type declarations.

### Shuffle

Suppose we want a method that will shuffle the deck. For example, in the main section, we could do something like:
```
d = Deck()
d.shuffle()  # Call the shuffle method using dot notation
print(d)
```
Think of the call to `shuffle` as a message given to `d`: "Hey, `Deck d`, please shuffle yourself."

Shuffling could be hard, if we weren't lazy geniuses. Recall that there's a built-in `shuffle` method in the `random` module.
```
from random import shuffle
```
You can then make a method that shuffles the cards in one line:
```
def shuffle(self):
    shuffle(self.cards)
```
Notice that `shuffle` doesn't return or print anything. It rearranges the order of the internal `cards` list.

Run the script again and verify that you're now printing a shuffled array of cards.

### Deal

Finally, add a method called `deal` that **removes and returns** the first card in the deck. For example:
```
d = Deck()
d.shuffle()
print(d)

first_card = d.deal()
second_card = d.deal()
print(first_card, second_card)  # The first two cards of the printed deck

print(d)  # Prints deck with first two cards removed
```
Use a chat tool to help you write the `deal` method.


## Game





