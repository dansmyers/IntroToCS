# Challenge Project: Hipster Restaurant Menu Generator

*farm-to-table lamb crunchwrap $22*  
*eldritch sea scallop fettucine $18*  
*microwaved languostine globules $29*

## Description

<img src="https://travelgrrrls.files.wordpress.com/2019/05/edison-bar2.jpg" width="35%" />

[*LATFH*](https://travelgrrrls.wordpress.com/2019/05/02/hipster-light/)

<br/>

I’ve decided to open a new restaurant and I need your help coming up with the menu. This place is going to be slick and hip, with all kinds of exposed ductwork, bricks, 
and those old-timey lightbulbs, so it needs a hip menu to match. In fact, I think the menu should be **randomly generated**.

Let's play around with a few ways of combining lists with random choices.

`cd` into your `Lists_and_Loops` directory and make a new file named `menu.py`.

## The `choice` function

Start by making three lists of strings named `descriptions`, `ingredients`, and `preparations`. For example,
```
descriptions = ['non-euclidean', 'carbonized', 'impossible']
ingredients = ['aubergine', 'bonemeal', 'cuttlefish', 'durian']
preparation = ['crunchwrap', 'foam', 'confetti']
```
Pick your own choices for each list and put at least five options in each one.

We're going to create menu items by assembling random options from each list. There is a function in the `random` module named `choice` that returns a random selection from a list.
```
# Put this at the top of your program
from random import choice

# Choose random selections from each list
desc = choice(descriptions)
ing = choice(ingredients)
prep = choice(preparations)

# Output
print(f'{desc} {ing} {prep}')
```
Write a loop with `choice` that prints ten different item combinations.

## Random selection

You can also choose a random item from the list by picking a random index. Consider the following:
```
index = randint(0, len(ingredients) - 1)
```
Recall that `randint` generates a random integer value in the range of its given inputs, including both. Therefore, starting at 0 and going up to the last index will choose a random position in the list.

Another function is `randrange`, which returns a random choice from a range of integers specified by `range`. For example,
```
index = randrange(10)
```
Would generate a random value from 0 to 9.

To generate a random index from a list, use
```
index = randrange(len(ingredients))
```
to produce a choice in the range 0 to `len(ingredients) - 1`.

Modify your program to use index-based random selection instead of `choice`. Generate separate random indices for each list.

## Removing options

You might notice that both previous versions can select the same item multiple times. You might prefer to remove options once they've been chosen so that you can't generate duplicates.

Modify your program one more time to use `pop` to remove the randomly chosen index to take its corresponding item out of the list.
```
# Remove the item at the given position from the ingredients list
ingredients.pop(index)
```
Reduce the number of loop iterations to five.

