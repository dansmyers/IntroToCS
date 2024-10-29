# Jeu Monégasque

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Monaco_Monte_Carlo_1.jpg/2560px-Monaco_Monte_Carlo_1.jpg" width="400px" />

*Monte Carlo is a district of the small European principality of Monaco. It's the home of a famous casino and entertainment complex that has been in operation since the 1800s.*


## Setup


## Written lab

Complete the written lab document posted on Canvas. Do this first before working on the problems below.


## Problems

### Passe-Dix

Recall the passe-dix dice game: the gambler wins if the sum of three six-sided dice is greater than ten.

What is the probability of winning at passe-dix? We can estimate this using the Monte Carlo technique. Use a loop to play a large number of games of passe-dix.Count the number that win, then report the winning percentage.
```
"""
Simulating passe-dix
"""

from random import randint

num_wins = 0

for trial in range(10000):
    # Get the sum of three six-sided dice

    # Count a win if the sum is greater than ten

# Calculate and print the winning percentage
```
Complete the program. Put your solution into a file named `passe_dix.py`.

### Simulation with a method

Repeat the previous problem, but put the code to simulate one round of the game into a method that returns `True` or `False`.
```
def sim_passe_dix():
    """
    Simulate one round of the game and return True if a win occurs, False otherwise
    """

    # Complete this method


### Main
num_wins = 0

# Loop that calls the simulation method and counts the number of trials that win
for trial in range(10000):
    if sum_passe_dix():
        num_wins += 1

# Calculate and print the fraction of wins
```


### The Newton-Pepys Problem


<img src="https://cdn.aarp.net/content/dam/aarp/food/healthy-eating/2016/2016-05/1140-peeps-nation.imgcache.rev3aa6a5a0b7d521bbef63f0e833d97a8f.web.900.513.jpg" width="300px" />

<br/>

Samuel Pepys (pronounced "Peeps") was a 17th Century British naval administrator, best known for the detailed diary he kept describing his life in the 1660's. In 1693 he corresponded with Isaac Newton regarding a wager:

>Which of the following three propositions has the greatest chance of success?
>
>- Six fair dice are tossed independently and at least one six appears.
>- Twelve fair dice are tossed independently and at least two sixes appear.
>- Eighteen fair dice are tossed independently and at least three sixes appear.

What is the answer to Pepys' question? Write a simulation program to find the answer.

Tips:

Try writing three different simulate methods, one that simulates the first proposition of tossing 6 dice, a second for the case of tossing 12 dice, and a third for tossing 18 dice. Perform 1000 trials of each simulation and observe the one that achieves the greatest number of successes.

Notice that the problem is phrased as **at least** not **exactly**.

Python's lists have a built-in method called `count` that can check the number of occurrences of an item in the list. For example, the `sim_prop_one` method can be implemented as follows:
```
def sim_prop_one():
    """
    Simulate the roll of 6 dice and return True if at least one 6 occurs
    """

    # Generate a list of six random die rolls using a list comprehension
    rolls = [randint(1, 6) for i in range(6)]

    # Count the number of sixes that resulted
    num_6 = rolls.count(6)

    # If at least 1 six occurs, proposition one has succeeded
    return num_6 >= 1
```
Call `sim_prop_one` in a loop and keep count of the number of calls that return `True`. Then write similar methods for the other two propositions.

Check the [Wikipedia page](https://en.wikipedia.org/wiki/Newton%E2%80%93Pepys_problem) for the solution and calculations for each case. The first proposition is the most likely to occur.

### Craps

The most popular dice game in American casinos, craps allows players to make an extensive array of bets. The most common is called the "pass" bet, and it works as follows:

- A player (the "shooter") rolls two six-sided dice.

- If their sum is 7 or 11, the bet immediately wins. If the sum is 2 ("snake eyes"), 3, or 12 ("boxcars" or "midnight"), the bet immediately loses.

- If the sum is any other number, that number becomes the **point** and the bet enters a second phase.

- During the second phase, the shooter continues rolling the dice with the goal of rolling the point value again before rolling a 7. If the point comes up first, the bet wins; if a 7 comes up first, the bet loses. The shooter will re-roll as many times as required until either the point or 7 comes up.

Write a simulation program to estimate the probability of winning the pass bet in craps.

Tips:

- Use a `simulate` method and a main loop, like in the previous problems. The simulate method should complete one round of craps and return `True` or `False` to indicate whether the pass bet won or lost on that round.

- Within the `simulate` method, roll two dice and check their sum. If the result is 7, 11, 2, 3, or 12, you can return the result immediately. If the result is anything else, use a `while` loop to implement the second phase of the bet.
```
def sim_craps():
    """
    Simulate one round of craps
    """

    # Roll two dice and add their sum

    # If the sum is 7 or 11 return True immediately

    # elif the sum is 2, 3 or 12 return False immediately

    # else, enter the third phase
    else:
        point = total  # the first sum becomes the point value

        # Loop until a result is achieved
        while True:

            # Roll two dice and add their sum

            # If the roll equals the point, return True

            # If the roll equals 7, return False

            # Any other outcome just continues the loop to try again
```

- Run 10000 trials. The answer should be about 49%.
