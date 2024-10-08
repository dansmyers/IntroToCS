# Hurricane Make-Up

[Me every time I have to record a video for class](https://www.youtube.com/watch?v=Sv3A95yEDR4).

## Overview

This is the make-up practice assignment for the week of 10/7. Each section below has a link to a video followed by a short practice problem, then a few more substantial problems. Work through the document, completing each section in order. At the end, you'll submit your programs to an assignment on Canvas so that I have a record that everyone completed the make-up work.

This lab has a target deadline of Tuesday, 10/15. I realize that we don't know how things will be after the storm, so I understand that we may need to make adjustments.


## AI Usage

This is practice of fundamental content. If we were in-person, we'd do it in together in class, but we aren't. I'm asking you to do these questions **without using any AI**. 

That's on the honor system, but be aware that you'll need to understand how lists and loops work for the midterm. It's to your advantage to work through these questions in a way that actually helps you learn the material.

Remember that you can always reach out to me if you have questions.


## Setup

Make a `Hurricane` directory and `cd` into it.
```
mkdir Hurricane
```
```
cd Hurricane
```

## Intro to Lists


### Video
[Watch and follow along with this video](https://www.youtube.com/watch?v=Gb4MUBxtmHI). Remember that you can pause or rewind if you need to.

### Mixtape

Verify that you're in your `Hurricane` directory, then create a file named `mixtape.py`. Put the following starting code in your file:

```
"""
Make a mixtape with lists - inspired by a Codecademy's taylor.swift project
"""

def tape():
    print(".------------------------.   ")
    print("|     YACHT ROCK MIX     |   ")
    print("|     __  ______  __     |   ")
    print("|    /  \\|\\.....|/  \\    |")
    print("|    \\__/|/_____|\\__/    | ")
    print("|    ________________    |   ")
    print("|___/_._o________o_._\\___|  ")

    print()
    

### Main

# Totally gratuitous ASCII art
tape()

# Create an empty list to hold the songs
songs = []
```

Change the name of the mix to be whatever you want. Then use `append` to fill the `songs` list with entries. For example (sticking with the yacht rock theme):
```
songs.append('Sailing by Christopher Cross')
songs.append('Peg by Steely Dan')
songs.append('Africa by Toto')
```
Add at least five songs to your list. Print your list using
```
print(songs)
```
Run your program to verify that it prints the correct list of values in the order you appended them.

### Don't stop, make it pop
Use `pop` to remove the second and fourth items in your list, then add a print statement to output the list and verify that the items were correctly removed.

Then use `insert` to put new songs at the second position and fourth position and print the list again to verify that the operation succeeded.


## The `for` Loop

### Video

[Start with this video](https://www.youtube.com/watch?v=_Ebkl6l8pVs), which shows the basics of how to use the `for` loop to iterate through a list and print each item.

### Practice loop

Add a loop to the end of your `mixtape.py` file to print the items in `songs` one at a time. Use a loop like the one in the video. Remember that you can choose any loop variable name you want.


## More Looping Examples

### Video

[Watch this third video](https://www.youtube.com/watch?v=1OKThD6IPK0), which reviews the main ideas from the first two, then works through some more advanced looping examples.

I recorded this one during the *last* hurricane, so it uses a different coding platform and I have a different haircut. It makes some references to the class schedule and coming back on Monday - those are from a previous semester so ignore them.

### Minimum of a list

Modify the maximum example given in the video to find the *minimum* value in a list. Put your solution in a file named `minimum.py`.

```
"""
Practice problem finding the minimum of a list
"""

# Example data
data = [2, 3, 1, 7, 5, 9]

# Write your code to find the minimum value of the data list

# Print the minimum

```

## Looping Over a Range of Numbers

### Video

[This is the last video](https://www.youtube.com/watch?v=sp1HgQTpzzQ), which is also from a previous semester. It covers the `range` function, which is used to loop over a range of numbers.

### Beep

Write a program named `beep.py` that loops through the numbers 1 to 25 and prints each number, but prints `BEEP` for numbers divisible by 4.


## Main Problems

### Project Euler #1

[Project Euler](https://projecteuler.net/problem=1) is a site with a large number of mathematical-themed programming problems. Here's problem #1:

>If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6, and 9. The sum of these multiples is 23.
>
>Find the sum of all the multiples of 3 or 5 below 1000.

Use the `for` loop with `range` to solve this problem. Put your solution in a file named `euler.py`.



### Primes

Write a function called `is_prime` that takes an integer `n` as input and returns `True` if the number is prime and `False` otherwise.

The easiest way to test if `n` is prime is to loop over the numbers from 2 to `sqrt(n)`. Here's a ***pseudocode*** example:

```
def is_prime(n):
    root = int(n ** .5)

    for i in range(2, root + 1):
        if i divides n:
            n is not prime, return False

    loop finished without returning False, so return True
```

If you complete the loop and never return `False`, then `n` is prime and you can return `True` at the end of the function. Make sure that your code works correctly for 2.

Note: `int(n ** .5)` calculates the square root of n and then truncates it to an integer. `range` won't accept a decimal value as a parameter.

Put the following code in a file named `primes.py`, then complete the function:

```
"""
Testing if a number is prime
"""

def is_prime(n):
    # Complete this function using the instructions above


### Main

# Test cases
for i in range(2, 20):
    print(i, is_prime(i))
```

### Day of the year

Write a function called `day_of_the_year` that takes a `month` and `day` as input and returns the associated day of the year. Let the month be a number from 1 (representing January) to 12 (representing December). For example,
```
day_of_the_year(1, 1) = 1     # January 1
day_of_the_year(2, 1) = 32    # February 1 is the 32nd day of the year
day_of_the_year(3, 1) = 60    # March 1 is the 60th day of the year
```
You can ignore Leap Years and assume that February has 28 days.

Tip: Make a list with the number of days in each month.
```
days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
```
Given the input `month`, add up all the days from the *previous* months. For example, if `month = 4` (representing April) you would add up the first 3 entries in the list to get the total days in January, February, and March. You can then add the value of `day` to get the day of the year.

Think about how to implement that operation using `range`. Here is some test code; put it in a file named `days.py`.
```
"""
Calculating the day of the year
"""

def day_of_the_year(month, day):
    """
    Complete this docstring
    """

    days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Add up the days from all months before the given month

    # Add in the given day

    # Return the result


### Main
print(day_of_the_year(1, 1))
print(day_of_the_year(1, 31))
print(day_of_the_year(2, 1))
print(day_of_the_year(2, 28))
print(day_of_the_year(3, 1))
print(day_of_the_year(3, 31))
print(day_of_the_year(4, 1))
print(day_of_the_year(10, 31))
print(day_of_the_year(12, 31))
```


### Conway's Doomsday Algorithm

<img src="https://upload.wikimedia.org/wikipedia/commons/f/f2/Game_of_life_animated_glider.gif" width="150px" />

*The famous glider pattern of Conway's Game of Life*


John Conway was a mathematics professors at Cambridge. He had a long academic research career but is best known for his contributions to recreational mathematics, including the [Life cellular automaton](https://youtu.be/C2vgICfQawE?t=70). He died of COVID-19 on April 11, 2020.


Conway's **Doomsday algorithm** is a technique for computing the day of the week of any given date. It relies on the fact that certain easy-to-remember dates in each year are all guaranteed to fall on the same day of the week, which Conway calls the "Doomsday" for that year. 

The most important dates that fall on the Doomsday are 4/4, 6/6, 8/8, 10/10, 12/12, and the last day of February.  January 3 also falls on the Doomsday in non-leap years. Thursday is the Doomsday for 2024.

Here's the procedure:

- Given the chosen date, choose one of the days that is guaranteed to fall on the Doomsday. For example, if the given date is 4/14, you could choose 4/4.
- Calculate the number of days separating the chosen date from the Doomsday.
- The distance in days modulo 7 gives the number of days of the week separating the final answer from the Doomsday.

In the example, 4/14 is ten days from 4/4, one of the dates guaranteed to fall on the Doomsday.  Therefore the day of the week of 4/14 is three days from the Doomsday. The Doomsday for 2024 is Thursday, so 4/14 falls three days after Thursday, which is a Sunday.

Write a function called `doomsday` that takes a `month` and `day` as input and returns the associated day of the week. Use the code below and put it in a file named `doomsday.py`.

- Copy the `day_of_the_year` function from the previous problem to convert `month` and `day` into an integer; then do the same thing with one of the days known to be on the Doomsday.

- You might want to create a list containing the days of the week starting with Thursday. Use the difference computed in the previous step as an index into the list to get the correct day.
```
days = ['Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday']
```

```
"""
DOOMSDAY
"""

def day_of_the_year(month, day):
    # Copy the function from the previous problem


def doomsday(month, day):
    """
    Implement the Doomsday algorithm
    """

    # Calculate the day of the year for the given month and day

    # Calculate day of the year for a known Doomsday

    # Find the difference mod 7

    # Use the difference to determine and return the correct day



### Main
print(doomsday(4, 1))   # Monday
print(doomsday(4, 2))   # Tuesday
print(doomsday(4, 3))   # Wednesday
print(doomsday(4, 4))   # Thursday
print(doomsday(4, 5))   # Friday
print(doomsday(4, 6))   # Saturday
print(doomsday(4, 7))   # Sunday
print(doomsday(4, 8))   # Monday
print(doomsday(4, 9))   # Tuesday
print(doomsday(4, 10))   # Wednesday
```

## Submission

Upload all of your `.py` files to the assignment on Canvas.
