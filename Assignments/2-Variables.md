# Assignment 2: How to Variables

## Due Wednesday, February 1

## Overview

This assignment will give you the chance to practice writing Python programs that use variables, user input, and formatted printing.

Complete the assignment on Replit in the workspace I'll create for you. When you load the project, you'll see multiple files in the workspace. There is one `.py` file for each problem and `main.py`, which contains the autograded tests that will evaluate your solutions.

Put the solution for each problem into its associated file. You can run the tests in `main.py` by pressing the green "Run" button at the top of the page. The test script will run each one of your programs and compare the output your program produces to the expected output. If the outputs match, you'll receive credit for the problem. If they don't, the script will point out the first place where your output doesn't match what's expected. **Do not edit the test script in `main.py` under any circumstances**.

To get credit, you must pass at least 90% of the autograded tests and make a reasonable attempt at every problem. For this assignment, that means you must successfully complete every problem, but future assignments will have more tests, so you won't necessarily need to pass every one.

General tips:

- **Start early! Don't wait until the last minute!**

- Succeeding in this class is about **consistency and effort**. If your program doesn't work the first time, that's normal and expected. Just look carefully at the output, make some changes, and try again.

- **You can run the test script as many times as you need to**. There are no limits. Get in the habit of testing early and often.
 
- If you are not passing a test, think carefully about your output and the expected output. **Do not make random changes to your program!**

## Reading

Read **Chapter 2** of the ZyBook and complete the **participation questions**. The book also includes "challenge questions" that you don't need to complete.


## General Tips

For all of these problems other than the McChocolate Potates one, read your inputs and print your outputs without printing any text for the user.

For example, instead of writing something like:
```
deg_f = int(input('Enter a temperature in degrees Fahrenheit: '))
```

You can just read the input directly:
```
def_f = int(input())
```

Similarly for the output, just print the final result to the appropriate number of decimal places. For example,
```
print('%.1f', deg_c)
```

These formats are easier for the automated tests to evaluate, since they don't have to parse numbers out of a string of text messages and you won't have to worry about matching any particular format for the input or output messages.

## Problems

### McChocolate Potatoes

<img src="http://del.h-cdn.co/assets/16/03/480x360/sd-aspect-1453239737-chocopotato-main-01.jpg" width="35%" />

The Japanese yen currently trades for about $.0091.

I'm a sucker for regional fast food items. It turns out that you can get chocolate fries at McDonald's in Japan (they are officially known as "McChocolate Potatoes"). Are they any good? Maybe not, but they cost only 330 yen as a side item.

What is the cost of a side of chocolate fries in dollars? Print your result to two decimal places.

Tip: you don't need to take user input for this problem. Just print the result to two decimal places.


### Temperature Conversion

A classic example.

To convert a temperature of *F* degrees Fahrenheit into Celsius, use

```
C = (F - 32) * (5 / 9)
```

Write a program that can read an **integer** number of degrees Fahrenheit from the terminal and report the corresponding number of degrees Celcius.
Output your results to **one decimal place**.

Tip:

Read your input without printing a prompt. For example,

```
deg_f = int(input())
```

### Furlongs


A furlong is an archaic unit of length defined to be one-eigth of a mile (660 feet).

Write a program that can read a length in feet and convert it to units of fulongs. Print your results to one decimal place.

You may assume that the user will enter a valid length.

Tip:

Assume that the input may be fractional. To read fractional input, use

```
user_input = input()
feet = float(user_input)
```

### £sd

The main unit of currency is Great Britain is the **pound sterling**, represented by the £ symbol. Similar to the U.S. dollar, each pound is divided into 100 pence. However, this straightforward system only went into effect in 1971. Prior to that date, the British used a different system descended from the ancient Romans.

The £sd system, as it was known, had three basic coins:
- The pound, which was the main unit, just as it is today.
- The shilling, with 20 shillings to a pound.
- The penny, with 12 pennies to the shilling. There were therefore 240 pennies in a pound.


The symbols for the three coins come from ancient Roman terms.
- £ stands for *libra*, the Roman word for balance and their equivalent of our one pound weight. This is also the origin of our abbreviation lb. for weights measured in pounds.
- d stands for *denarius*, a basic silver coin, 240 of which were traditionally struck from a pound of silver.
- s stands for *solidus*, a gold coin held to be the equivalent of 12 denarii.

The system owed its continuing popularity in Western Europe to Charlemagne in the 700s, who mandated that the silver penny would be the basic unit of currency in his realm and regulated its purity.

£sd coins are no longer legal tender, but can still be exchanged for their face value.

Write a program that can take in an integer number of shillings and pennies and return the number of modern pounds. For reference, each shilling is worth .05 pounds and each old penny is worth .0041667 pounds.

You can assume that the user will only enter positive integer values. Report your answers to two decimal places.


Tip: Use the `int` function to convert input to integer values. Don't use a prompt for the `input` functions.

```
shillings = int(input())
pennies = int(input())
```

### Binet's Formula

Recall the famous Fibonacci sequence, where each term is the sum of the previous two terms.

```
0, 1, 1, 2, 3, 5, 8, 13, 21, ...
```

Suppose you would like to calculate the Nth Fibonacci number. How could you do that? One way is to start at the base case and grind your way up through the sequence until you've calculated N total terms. 

It turns out there is a single formula that will calculate the terms of the Fibonacci sequence. This is weird and suprising, because it seems unlikely that such a highly structured sequence, where each term depends on all the previous terms, could be represented in closed form.

The result is known as Binet's formula and it says that the Nth Fibonacci number `F_n` is

<img src="https://latex.artofproblemsolving.com/8/6/d/86d486c560727727342090b432e23ba85ac098b1.png" width="30%"/>

Gnarly.

The number `(1 + sqrt(5)) / 2` is the famous golden ratio, the most aesthetically pleasing of all proportions. It's sometimes denoted by the Greek letter φ (phi) after the ancient architect and sculptor Phidias, who used it in planning the design of the Parthenon.

<img src="https://lp-cms-production.imgix.net/2019-09/ab57ac3775d90a72da514d158401bd47-parthenon.jpg" width="35%" />

*much columns  such proportions*

Write a program that reads an integer `n` from the user and prints the corresponding term in the Fibonacci sequence.

Tips:

You'll need the ability to take square roots and calculate powers. Use the built-in `**` operator to calculate powers. There is a built-in square root function that you can import into your program by adding the following line to the top of your code:

```
from math import sqrt
```

You can then call the functions like so

```
phi = (1 + sqrt(5)) / 2  # sqrt(5) calculates the square root of 5
phi_to_the_n = phi ** n  # Calculate phi to the power n
```
