# Assignment 6: Jeu Monégasque

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Monaco_Monte_Carlo_1.jpg/2560px-Monaco_Monte_Carlo_1.jpg" width="100%" />

*Monte Carlo is a district of the small European principality of Monaco. It's the home of a famous casino and entertainment complex that has been in operation since the 1800s.*

## Due 

## Overview

All of these problems will give you additional practice using combinations of `while` and `for` loops, as well as functions.

This assignment introduces a new kind of program: **Monte Carlo simulation**, which is all about using randomized programs to answer questions that would be hard answer with exact calculations. We'll use the Monte Carlo technique to simulate some games and estimate their winning probabilities.


## Submission


## Problems


<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Casino_de_Monaco_%2850158785856%29.jpg/2880px-Casino_de_Monaco_%2850158785856%29.jpg" width="100%" />

*The Place du Casino.*

### Baby Needs a New Pair of Shoes

What is the average value obtained by rolling two dice? One way to solve this problem is to reason about the underlying probabilities. Another way is to simply simulate a large number of dice rolls and calculate the average from the simulated results. With high probability, the simulated average should be a close approximation of the true average.

This type of program is called a Monte Carlo simulation, named after the famous Monte Carlo casino complex in the tiny European principality of Monaco.

Fill in code for the program below. Use a for loop to call simulate 1000 times and add up the results of all the simulated die rolls. At the end of the program, calculate the average over all 1000 trials.
