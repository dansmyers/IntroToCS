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


