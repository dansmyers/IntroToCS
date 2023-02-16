# Creative Writing

## Warm-Up: Perfectly Rational Pirates

<img src="https://upload.wikimedia.org/wikipedia/en/0/09/Pirates_who_dont_do_anything_poster.jpg" width="30%" />

A group of pirates has discovered a buried treasure of 100 gold
pieces and they need to divide it. Such matters are, of course,
governed by the Pirates' Code, which has strict rules:

1. The first pirate will propose a division of the gold pieces.
    
2. All of the pirates vote on accepting or rejecting the 
proposed distribution.
    
3. If the vote succeeds, the treasure is divided and the process
   ends. Ties are broken ***in favor*** of the proposer.
       
4. If the vote fails, the proposer is thrown overboard and the
   next pirate makes a proposal. The proposal order is 
   alphabetical.
       
5. This process continues until the treasure is divided.
    
Pirates want to survive, but are also very greedy and want as much
gold as possible. Pirates are also bloodthirsty, so a pirate would prefer to vote to
throw a proposer overboard if it doesn't make any difference in the
amount of gold he receives.

All pirates are ***perfectly rational*** in matters of treasure.

Pirates honor the Code absolutely, which also forbids reprisals.
Being pirates, they do not care about their reputations: the only
things they care about are survival, gold, and throwing each other overboard.

### Two Pirates
Suppose there are two pirates, D and E.

D can propose to take all 100 coins for himself. Ties are broken in
favor of the proposer, so E is forced to accept this distribution.

### More Pirates

What if there are three pirates: C, D, and E? What should C propose?

- Think about D's goals. If C's proposal fails, D will then become the proposer and can take all 100 gold pieces, by the two pirates argument above. Therefore, D has no incentive to accept any offer of C's. It's more rational (and fun) to throw C overboard and then take all 100 pieces.

- What about E's situation? If C's proposal fails, then D can take all 100 pieces for himself, so E should rationally support C. But how much gold is necessary to buy E's support?

How about four pirates: B, C, D, and E? What does B propose?

What about five pirates: A, B, C, D, E? What does A propose?

### More Pirates than Coins

Suppose there are only three gold coins, but **seven** pirates. Make an argument that the first pirate (the one making the first proposal) can survive, but only if he doesn't take any gold for himself.

What if there are three coins but **nine** pirates? Make an argument that the first pirate is guaranteed to die in this situation.

What about **ten** pirates? Can the first pirate survive? Tip: think carefully about the rational incentives for the second pirate. What happens to him if the first pirate dies?


## Choose Your Own Adventure


<img src="https://upload.wikimedia.org/wikipedia/en/f/f0/Cave_of_time.jpg" width="25%" />


If you had been a kid in the 80's, your elementary school library would have been stuffed with *Choose Your Own Adventure* books, for the downtime you had when you weren't playing [*Oregon Trail*](https://en.wikipedia.org/wiki/The_Oregon_Trail_(1985_video_game)) on your school's Apple II computers.

Each book was the story of "you", the nameless protagonist, making your way through some type of fantastic adventure story. After reading for a few pages, you'd be offered a choice. For example,

- *If you choose to explore the mysterious Cave of Time, turn to page 41*.
- *If you would rather go back to your house and make a sandwich, go to page 17*.

Each choice would lead to a different path of the story and eventually you would reach an ending page, which might good, bad, or curiously ambiguous.

We're going to use Python to write our own text-based Choose Your Own Adventure story. A key idea of this program will be **using functions to organize a complex program**. 
Each "page" of the story will be its own function. Within each function, print a little descriptive text, then prompt the user to make a choice. 
Each choice corresponds to another function call, which runs the code for the next page.

## Interactive Fiction

<img src="https://upload.wikimedia.org/wikipedia/en/a/ac/Zork_I_box_art.jpg" width="35%" />

*The Zork series published by Infocom was an influential early computer game. It is pitch black. You are likely to be eaten by a grue.*

The CYOA books are part of the larger gaming lineage of **interactive fiction**. Some of the earliest PC games were structured as interactive stories, where the player types commands to move around the world, gather items, and solve puzzles. These early text-based IF games later evolved into graphical adventure games.

IF is kind of a weird genre. It's both totally unpopular and extremely popular at the same time. There are still writers creating interesting parser-based IF in the 
style of the early text adventure games: Modern IF in this style is often experimental or socially-conscious. Basically none of that crosses over to the commerical gaming market. On the other hand, there is huge genre of visual novel games, dating sims, and other text-and-image games that have achieved widespread popularity, even if they often get tagged as "casual" or "romance" games.

While I'm certainly **not** a connossieur of the form, many of these games are gloriously weird.

<img src="https://cdn.akamai.steamstatic.com/steam/apps/251990/ss_267dc852c216b2bf58d48c58f3ea31d6896e19e4.1920x1080.jpg?t=1568494485" width="60%" />

*Long Live the Queen*, a dark and gritty stats-based princess simulator where you have to train skills that will allow you to survive until your coronation.

<img src="https://hips.hearstapps.com/digitalspyuk.cdnds.net/14/25/gaming-hatoful-boyfriend-screenshot-2_1.jpg" width="60%" />

*Hatoful Boyfriend*, the dating sim game where the guys you're trying to date just happen to be pigeons.

<img src="https://i.pcmag.com/imagery/articles/03vQmmuNtMgqoVDDHYMhunN-1.1569489919.fit_lim.png" width="60%" />

*I Love You, Colonel Sanders*, the KFC-themed dating simulator. Colonel *senpai*, notice me!

## *Adventure*

*Adventure* is the trope codifier for old-school text-based adventure games. The first version was written in the 1970's by a programmer named Will Crowther and based on his experiences exploring the Mammoth Cave system in Kentucky. Many locations in the game correspond to real locations in Mammoth Cave.

Spend a few minutes playing around with an online version here:

[https://quuxplusone.github.io/Advent/]


## Example

### Setup

Create a new file named `cyoa.py` in the `Lab_5` repl.it workspace.

### Some Starter Code

Copy the following code in your `cyoa.py` file, then run it a couple of times to see how it works. Once you have played through a few paths, trace the execution of the source code and verify that you understand how it works.

```
"""
A Choose Your Own Adventure Story, featuring functions

CMS 120
"""

def read_choice():
    """
    Read and return an integer value
    """
    return int(input('Make a choice: '))
    

def go_to_house():
    
    print()
    print('Congratulations! You made back to your house!')
    print('If only there was some way to get inside...')
    print()
    
    # Add some more choices
    # Each choice corresponds to a function that represents the next page in the story
   
   
def read_leaflet():

    print()
    print('The leaflet turns out to be a coupon for a nearby all-you-can-eat buffet.')
    print('Your stomach rumbles...')
    print('But you need to head back to your house before you do anything else.')
    print()
    
    # Go directly to the next page without offering a choice
    go_to_house()

    
def open_mailbox():
    
    print()
    print('Opening the mailbox reveals a small leaflet.')
    print()
    
    print('1. Read the leaflet.')
    print('2. Change your mind and go to the house.')
    
    choice = read_choice()
    
    if choice == 1:
        read_leaflet()
    else:
        go_to_house()
        

def start():
    
    print()
    print('You are standing in an open field west of a white house with a boarded front door.')
    print('There is a small mailbox here.')
    print()
    
    print('1. Go to the house.')
    print('2. Open the mailbox.')
    
    choice = read_choice()
    
    if choice == 1:
        go_to_house()
    else:
        open_mailbox()
        
        
def print_instructions():
    
    print('Welcome to my Choose Your Own Adventure story!')
    print()
    
    print('Every page in this book is implemented as a function.')
    print('On each page, you\'ll make a choice, which calls the next function.')
    print('Let\'s begin!')
        
        
### Main
print_instructions()
start()
```

### Structure of the Program

The `main` part calls two functions: `print_instructions`, which just prints an intro message and then returns, and `start`, which is
the first page of the story.

The `start` function prints a little description of the scene and then prompts the user to choose option 1 or 2, reading the choice
with the `input` function.

Each choice corresponds to another function: `go_to_house` or `open_mailbox`. If the user makes choice 2, for example, the program calls the `open_mailbox` function, which represents another page in the story with another set of choices.

Here's a key idea: within `start`, we're using functions to **describe what should happen next**. Each function represents one self-contained page with calls to the functions representing other pages. Thus, the code is nicely compartmentalized. In particular, **we could change the code for one page without having to rewrite any other page**.

## Your Mission

Once you're comfortable with the basic example story, take control and write your own. You can use the starter code as a model and either keep the same opening scenario and choices or write something completely different.
Here's the basic plan:

- Use the `start` function as a model for all of your functions.

- Each function prints some text of the story, then prints some choices. You can do 1, 2, 3, or more choices, depending on how you want
the story to develop.

- Read the number for the user's choice with the `read_choice()` function. You can assume the user will always put in a valid number.

- For each choice, call a function that decribes what you want to happen next.

- Then go write those methods to create the next pages of the story.

## More Questions

## Chuck-a-Luck

An old-time carnival game.

The player bets on a number 1 through 6 and then rolls three dice.

- If the number comes up one time the player wins $1.
- If it comes up two times the player wins $2.
- If it comes up three times the player wins $3.

Here is some starter code. Fill in the methods.

```
"""
Chuck-a-Luck

CMS 195, Spring 2020
"""

from random import randint

def read_int():
    """
    Read and return an integer from the terminal
    """
    
    # Write code to read a value with input(), then convert it to an int and return it
    
  
def die_roll():
    """
    Generate and return a six-sided die roll
    """
    
    # Fill in the body of the method


def print_instructions():
    """
    Instructions for the chuck-a-luck game
    """
    
    # Print instruction messages for the user
    # This method doesn't return anything
    
    
### Main
    
print_instructions()

# Read the user's bet
bet = read_int()

# Generate three dice -- add two more lines for die2 and die3
die1 = die_roll()
    
# Count up the number of dice that match the user's bet
# Tip: create a count variable and test each die with an if statement

# Print the outcome based on the value of the count variable

```


## One-Armed Bandit

<img src="https://upload.wikimedia.org/wikipedia/commons/b/bf/Antique_one-armed_bandit%2C_Ventnor%2C_Isle_of_Wight%2C_UK.jpg" width="30%" />

Write a slot machine program.

- Generate three random numbers in the range 0 to 9.
- Print the three numbers.
- If all three numbers are the same, print `Jackpot!`.
- If two of the three are the same, print `Winner!`.

Design your own functions for this program. Look at the chuck-a-luck game as a template. You don't need to prompt the user for any input.
