# Challenge Project: Personality Quiz

<img src="https://i.pinimg.com/originals/c8/67/d7/c867d7bed74dcd85220972edfc1a7cc7.jpg" width="30%" />

## Due 

## Introduction

Personality quizzes. Is there a better way to learn about yourself than answering nonsensical questions written by randos on the Internet? I think not! I've taken a bunch of these over the years and I've learned all kinds of things.

- Hogwarts house? (Slytherin, but I'd pretend to be Hufflepuff).
- Disney heroine? (Maid Marian from *Robin Hood*).
- [Myers-Briggs personality type](https://www.myersbriggs.org/my-mbti-personality-type/mbti-basics/the-16-mbti-types.htm)? (INTP).
- [Enneagram type](https://www.narrativeenneagram.org/tour-the-nine-types/)? (3, and far more useful than Myers-Briggs, in my opinion).
- [Pokémon type](https://www.buzzfeed.com/sarahtooley5/what-pokamon-type-are-you-248el1snke)? (Poison).
- [Minor villain from "Jojo's Bizarre Adventure"](https://www.buzzfeed.com/puppetmaster64/which-minor-jojo-villain-are-you-42nxcnqrfi)? (Steely Dan, and I didn't even have to make that up).

Buzzfeed is still the leading purveyor of these online quizzes, offering insight into, for example, how [your controversial anime opinions will reveal your true Hogwarts house](https://www.buzzfeed.com/shualien/tell-us-some-of-your-unpopular-anime-opinions-and-aailsw3wr0).

In this project, you're going to use your knowledge of culture, relationships, and Python to write a program that implements a Buzzfeed-style personality quiz. Your quiz can be about anything that you want. This program will let you practice writing a completely self-designed program that's a bit larger than anything we've done so far.

## Quiz Design

<img src="https://ahseeit.com//king-include/uploads/2021/05/43915181_326611507924503_5421316365027478799_n-7515047846.jpg" width="30%" />

There are a number of ways to implement online quizzes. We're going to use the approach described in [this article](https://www.buzzfeed.com/annakopsky/everything-you-need-to-know-to-make-a-buzzfeed-personality). First, determine the title and "hook" for your quiz. What's it going to be about? Then decide on 3-6 outcomes that will be the results the user sees at the end.

Each possible answer in your quiz will correspond to one of your 3-6 final outcomes. Each time the user answers a question, assign a point to the associated outcome. At the end of the quiz, pick the final outcome with the most total points.

## Example

<img src="https://critter.science/wp-content/uploads/2019/03/ts1b-1180x520.jpg" width="30%" />

*G'day, mate.*

Scott's favorite animals are snakes, so I'm going to use "Which deadly Australian snake are you?" as our example. Here are four options, [sourced from Wikipedia](https://en.wikipedia.org/wiki/Snakes_of_Australia):

- Tiger snake
- Taipan
- Death adder
- Bandy-bandy

At the beginning of the main part, create four variables, one for each outcome:

```
tiger_snake_score = 0
taipan_score = 0
death_adder_score = 0
bandy_bandy_score = 0
```

We can then print a question and a menu of answers:

```
What is your coloration?

1. Bands of red, brown, or black with a light-colored belly.
2. Dark tan
3. Sharply contrasting black and white rings
4. Darker bands with a yellow-orange belly
```

Read the user input using our standard technique, then assign a point to the snake that matches the user's answer:

```
choice = int(input('Enter your answer: '))

if choice == 1:
    death_adder_score += 1
elif choice == 2:
    taipan_score += 1
elif choice == 3:
    bandy_bandy_score += 1
else:
    tiger_snake_score += 1
```

Here, I'm using `+= 1` as a shortcut to add one to a variable.


## Code

```
"""
What deadly Australian snake are you?
"""

# Use functions for multiline outputs to keep the main part of the program
# free from big blocks of print statements

def print_question_one():
  print()
  print('What is your coloration?')
  print('1. Bands of red, brown, or black with a light-colored belly')
  print('2. Dark tan')
  print('3. Sharply contrasting black and white rings')
  print('4. Darker bands with a yellow-orange belly')
  print()


### Main

# Declare variables for each outcome
tiger_snake_score = 0
taipan_score = 0
death_adder_score = 0
bandy_bandy_score = 0

# Print the first question
print_question_one()

# Read the answer and assign a point to its associated outcome
choice = int(input('Enter your answer: '))

if choice == 1:
    death_adder_score += 1
elif choice == 2:
    taipan_score += 1
elif choice == 3:
    bandy_bandy_score += 1
else:
    tiger_snake_score += 1


# More questions would go here...


# Determine which outcome has the most points, then print out
# a result message
```

## More Guidelines

Put your entire quiz into one script named `quiz.py` and then upload it to Canvas at the assignment I'll create for you.

- Choose your own topic with 3-6 possible outcomes.
 
- Write at least four questions.
 
- Think about how to identify which question as the most points, including how to break ties.
 
- Use functions to wrap up the print statements for your questions and final output messages. Putting big chunks of text behind a function call keeps the main part of the program from getting overloaded with print statements (and also lets you practice writing your own functions).

