# Jeu Monégasque

## Due 

## Overview

All of these problems will give you additional practice using combinations of `while` and `for` loops, as well as functions.

This assignment introduces a new kind of program: **Monte Carlo simulation**, which is all about using randomized programs to answer questions that would be hard answer with exact calculations. We'll use the Monte Carlo technique to simulate some games and estimate their winning probabilities.


## Submission


## Problems

### Baby Needs a New Pair of Shoes

What is the average value obtained by rolling two dice? One way to solve this problem is to reason about the underlying probabilities. Another way is to simply simulate a large number of dice rolls and calculate the average from the simulated results. With high probability, the simulated average should be a close approximation of the true average.

This type of program is called a Monte Carlo simulation, named after the famous Monte Carlo casino complex in the tiny European principality of Monaco.

Fill in code for the program below. Use a for loop to call simulate 1000 times and add up the results of all the simulated die rolls. At the end of the program, calculate the average over all 1000 trials.
