# Assignment 2: How to Variables

## Due Thursday, September 1

## Overview

This assignment will give you the chance to practice writing Python programs that use variables, user input, and formatted printing.

Complete the assignment on Replit, in the CMS 120 workspace. When you load the project, you'll see multiple files in the workspace. There is one `.py` file for each problem and `main.py`, which contains the autograded tests that will evaluate your solutions.

Put the solution for each problem into its associated file. You can run the tests in `main.py` by pressing the green "Run" button at the top of the page. The test script will run each one of your programs and compare the output your program produces to the expected output. If the outputs match, you'll receive credit for the problem. If they don't, the script will point out the first place where your output doesn't match what's expected. **Do not edit the test script in `main.py` under any circumstances**.

To get credit, you must pass at least 90% of the autograded tests and make a reasonable attempt at every problem. For this assignment, that means you must successfully complete every problem, but future assignments will have more tests, so you won't necessarily need to pass every one.

General tips:

- **Start early! Don't wait until the last minute!**

- Succeeding in this class is about **consistency and effort**. If your program doesn't work the first time, that's normal and expected. Just look carefully at the output, make some changes, and try again.

- **You can run the test script as many times as you need to**. There are no limits. Get in the habit of testing early and often.
 
- If you are not passing a test, think carefully about your output and the expected output. **Do not make random changes to your program!**

## Reading

Read **Chapter 2** of the ZyBook and complete the **participation questions**. The book also includes "challenge questions" that you don't need to complete.

Note: the ZyBook "challenge questions" are not the same as my challenge problems that count towards your grade. You will never need to do a so-called challenge question from the ZyBook (they aren't actually that challenging). I will start assigning the real challenge problems later in the semester.

## Problems

### McChocolate Potatoes

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
