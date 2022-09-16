# Assignment 3: The Compleat Gamester

This problem set will let you practice writing some simple text-based games that are based around random events like rolling dice. Along the way you'll get to practice

-Using the built-in `random` module
-More user input
-Testing for valid input
-Using conditional statements
-Using logical operations
-More formatted printing
-The modulus operator
-Integer division

These problems are all more challenging than the ones in the previous assignment.

The title of this assignment comes from an early English book on gaming, *The Compleat Gamester*, published in 1674 and attributed to Charles Cotton, a writer with a penchant for compleatness: He also contributed to a book called *The Compleat Angler* ("Being a difcourfe of FISH and FISHING not unworthy of the perufal of moft Anglers.")

## Reading

Complete the **participation questions** for Chapter 3 of the ZyBook.

## Don't Use Functions (For Now)

We will be talking about writing our own functions by the time this assignment is due. You DO NOT need to write any functions to complete this assignment: Focus on finishing the programs using the structure that I've given you and the examples we've done in class. The next assignment will be all about writing functions.

## General Tips

As before, pass the autograded tests given in `main.py` to receive full credit for the assignment.

- **Read the problem descriptions carefully**. They contain useful tips.

- You don't have to write the entire program in one go, from top to bottom. Develop incrementally and always start by understanding the high-level structure of the program.

- If you aren't sure what your program is doing, try adding `print` statements to check the values of your variables. You can see the output of your program when you run the tests.

The output for these programs is more complex that the previous assignments. The tests are written to give you a little flexibility (they ignore whitespace, new lines, capitalization, and basic punctuation), but your best bet is to look at the exepected output carefully and make sure that your programs' print statements are conforming to what's given as the expected result.

## Don't Get Stuck!

Here's a general rule for making progress on your programs: don't let yourself get stuck for too long. If you run into something you don't understand right away, spend a little time wrestling with it on your own (this is an important part of the learning process), but don't hesitate to seek out additional resources to break past things that are blocking you.

As a rough rule of thumb, if you've spent 30-60 minutes stuck on one issue (like a single bug or a test that you can't pass), look for additional help to move past it.

I'm always available to help you with any questions you have. There are also peer tutors available through the Tutoring and Writing Center.

It's acceptable to look at online resources as you're writing your code. For example, you might want to look up more examples of how to use a certain built-in function, or you might need pointers on debugging an error message that you haven't seen before.


## Problems

### More Modulus


Python supports a special operator, `%`, which is called the **modulus operator**. The mod operator calculates the remainder after division. For example,

```
11 % 3  is  2

13 % 4  is  1

8 % 2  is  0 (because 8 is evenly divisible by 2)

17 % 6  is  5
```

The mod operator can be used to check for divisibility. For example, suppose you want to test if an input value n is even. A number is even if it's evenly divisible by 2, so

```
if n % 2 == 0:
    # n is even
else:
    # n is odd
```

Write a program that reads an integer from the terminal and prints Even if the number is even or Odd if it's odd.

Tips:

- Remember to start your program with a docstring.
- Use `n = int(input())` to read an integer.


### Cho-Han

Cho-han is a traditional Japanese dice game. The rules are simple:

- The player bets if the sum of two six-sided dice will be odd or even.
- If the player's guess is correct, he wins. If not, he loses.

The game appears in Japanese movies set in historical periods, where it's played by Yakuza gangsters and wandering samurai.

Write a program for cho-han. Your program should prompt the user to choose an even or odd bet, then simulate the roll of two dice and announce if the player was correct.

```
Welcome to Cho-Han.
1. Even
2. Odd
Select a bet: 1
The dice are 1 and 5.
The sum is 6.
You win.
```

Check the user's input to make sure that it's either 1 or 2:

```
Welcome to Cho-Han.
1. Even
2. Odd
Select a bet: -1
You must enter 1 or 2.
```

Use `sys.exit()` to end the program immediately if the user gives you bad input.


#### Tips

- Python has a `random` module with a method named `randint`. To generate a single six-sided die roll use

```
first_die = randint(1, 6)  # Random integer in range 1 to 6, including both
```

To gain access to `randint`, put this line at the top of your program

```
from random import randint
```

- Remember that rolling two six-sided dice and adding their sum is not the same as generating a single random value in the range 1 to 12!

- You can print the sum of the two dice using `%d` format specifiers, like this (`%d` tells Python to print an integer value):

```
print('The dice are %d and %d.' % (die1, die2))
```

#### Seeds

Every random number generator has a special internal parameter called the **seed**. The seed value controls the sequence of random numbers, such that starting the same random number generator with the same seed always produces an identical sequence of pseudorandom values.

The autograded tests need a predictable random sequence to correctly check the output of your progam, so the first line of the starter code sets the seed of the RNG to 0. **Don't modify this line** or you won't be able to pass the tests.


### Passe-Dix

Passe-dix (French for "pass ten") is an ancient dice game. According to some early gambling books, it was allegedly the game played by Roman soldiers to divide the clothes of Jesus at the Crucifixion. The rules are simple: roll three dice and add their sum. The player wins if the sum is strictly greater than 10, loses if the sum is strictly less than 10, and draws ("pushes" in gambling terms) if the sum equals 10.

Write a program that implements passe-dix. To make the program more interesting, the first thing that you'll do is prompt the user to enter a seed that controls the random number generation.

Here is example output:

```
Enter a seed value: 1
The dice are 2, 5, and 1.
The sum is 8.
You lose.
```

The three possible outcomes are

```
You win.
You lose.
Push.
```

### Sic bo


Sic bo ("precious dice") is a dice game of Chinese origin, now available in many American casinos that cater to Asian gamers. The game is similar to craps: Players roll three dice and bet on the outcome. There are a wide variety of possible bets, but the two most common wagers in sic bo are "big" and "little".

- The big bet wins if the sum of the three dice is 11 to 17 (including both), but not three-of-a-kind
- The little bet wins if the sum of the three dice is 4 to 10 (including both), but not three-of-a-kind

Write a program for sic bo using the big and little bets. Again, to make things interesting, we're going to allow the user to input the seed value at the start of the program.

```
Welcome to Sic Bo.
Enter a seed value: 0
1. Big
2. Little
Choose a bet: 2
The three dice are 3, 5, and 1.
The sum is 9.
You win.
```


Tip

Both bets lose if the result is a triple, so you can test for that first, then move on to the test the sum if the result is not a triple. To test for a triple, you need the logical and of three comparisons

```
die1 == die2 and die2 == die3 and die1 == die3
```




