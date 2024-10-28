# Assignment 6: Jeu Monégasque

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Monaco_Monte_Carlo_1.jpg/2560px-Monaco_Monte_Carlo_1.jpg" width="50%" />

*Monte Carlo is a district of the small European principality of Monaco. It's the home of a famous casino and entertainment complex that has been in operation since the 1800s.*

## Due Monday 5/1 (the last day of class)

## Overview

All of these problems will give you additional practice using combinations of `while` and `for` loops, as well as functions.

This assignment introduces a new kind of program: **Monte Carlo simulation**, which is all about using randomized programs to answer questions that would be hard to answer with exact calculations. We'll use the Monte Carlo technique to simulate some games and estimate their winning probabilities.

Put your solutions in the workspace on repl.it. There are no automated tests for this project: each problem has only one answer, which you should simply print at the end of each simulation.

## Reading

Complete the **participation questions** for Chapter 7 on lists and dictionaries.

## Problems


<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Casino_de_Monaco_%2850158785856%29.jpg/2880px-Casino_de_Monaco_%2850158785856%29.jpg" width="50%" />

*The Place du Casino.*

### Baby Needs a New Pair of Shoes

Here's a simulation warm-up: What is the average value obtained by rolling two dice?

One way to solve this problem is to reason about set of possible outcomes obtained by rolling two dice and their underlying probabilities. Another way is to simply **simulate a large number of dice rolls** and calculate the average from the simulated results. With high probability, the simulated average should be a close approximation of the true average.

Fill in code for the program below and put your solution in `dice.py`. Use a for loop to call simulate 1000 times and add up the results of all the simulated die rolls. At the end of the program, calculate the average over all 1000 trials.

Your answer should be close to 7.

```
"""
Simulate the average of rolling two dice
"""

from random import seed, randint

def simulate():
    """
    Roll two dice and return their sum
    """

    # Fill in the body of this method
    # Generate two random die rolls and return their sum


### Main

seed(0)  # DON'T MODIFY THIS LINE

# Keep track of the sum of all trials
total = 0

# Use a for loop that runs for 1000 iterations
for trial in range(1000):

  # Call simulate() inside the loop to generate the sum
  # of two dice and add it into total


# Print the average of all 1000 simulations
print(total / 1000)
```

### Probability of Winning at Passe-Dix

Recall the passe-dix game:

- Roll three dice
- The player wins if the sum is **greater** than 10 and loses if the sum is **less than or equal** to 10 (we'll ignore the case of pushing if the sum is exactly 10 for this problem).

Use a Monte Carlo simulation program to estimate the odds of winning at passe-dix. Use the same strategy as the previous program, with a main loop that calls a `simulate` method 1000 times. In this case, the `simulate` method will return `True` if the player wins a round or `False` if the player did not win. The final output is the fraction of calls that resulted in a win for the player.

Your answer should be about 49%.

```
"""
Simulate passe-dix
"""

from random import seed, randint

def simulate():
    """
    Simulate three dice and return true if sum is > 10
    """

    # Fill in the rest of the method
    # Simulate three die rolls
    # Return True if their sum is > 10, False otherwise


### Main

seed(0)  # DON'T MODIFY THIS LINE

# Fill in the rest of the main program

# Again, use a loop that runs for 1000 iterations
#
# Call simulate() inside the loop and sum up the number
# of trials that result in True
#
# The final output is the fraction of successful trials
```

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
        point = total  # the sum becomes the point value

        # Loop until a result is achieved
        while True:

            # Roll two dice and add their sum

            # If the roll equals the point, return True

            # If the roll equals 7, return False

            # Any other outcome just continues the loop to try again
```

- Run 10000 trials. The answer should be about 49%.


### The Newton-Pepys Problem


<img src="https://cdn.aarp.net/content/dam/aarp/food/healthy-eating/2016/2016-05/1140-peeps-nation.imgcache.rev3aa6a5a0b7d521bbef63f0e833d97a8f.web.900.513.jpg" width="40%" />

Samuel Pepys (pronounced "Peeps") was a 17th Century British naval administrator, best known for the detailed diary he kept describing his life in the 1660's. In 1693 he
corresponded with Isaac Newton regarding a wager:

>Which of the following three propositions has the greatest chance of success?
>
>- Six fair dice are tossed independently and at least one six appears.
>- Twelve fair dice are tossed independently and at least two sixes appear.
>- Eighteen fair dice are tossed independently and at least three sixes appear.

What is the answer to Pepys' question? Write a simulation program to find the answer. Check the [Wikipedia page](https://en.wikipedia.org/wiki/Newton%E2%80%93Pepys_problem) for the solution and calculations for each case. The first proposition is the most likely to occur.

Tips:

Try writing three different simulate methods, one that simulates the first proposition of tossing 6 dice, a second for the case of tossing 12 dice, and a third for tossing 18 dice. Perform 1000 trials of each simulation and observe the one that achieves the greatest number of successes.

Notice that the problem is phrased as **at least** not **exactly**.

Python's lists have a built-in method called `count` that can check the number of occurrences of an item in the list. Suppose you want to generate a list of 6 die rolls and then count the number of 6's that occur.

```
rolls = []

for i in range(6):
    rolls.append(randint(1, 6))

num_6 = rolls.count(6)

# If num_6 >= 1, then proposition 1 has succeeded
```

There an even more compact way to do the list generation, using what Python calls "list comprehensions". A list comprehension is basically a loop that generates a list, but packed into the list declaration as a single line. The statement above is equivalent to:

```
rolls = [randint(1, 6) for i in range(6)]
```

This statement will call `randint(1, 6)` a total of six times and pack the results into one list. You can play around with using list comprehensions if you want to, or use the slightly longer code with the explicit loop.


