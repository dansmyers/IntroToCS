#



## Overview


## Setup


## Submission


## Personality Quiz

<img src="https://i.pinimg.com/originals/c8/67/d7/c867d7bed74dcd85220972edfc1a7cc7.jpg" width="30%" />

### Introduction

Is there a better way to learn about yourself than answering nonsensical questions written by randos on the Internet? I think not! I've taken a bunch of these over the years and I've learned all kinds of things.

- Hogwarts house? (Slytherin, but I'd pretend to be Hufflepuff).
- Disney heroine? (Maid Marian from *Robin Hood*).
- [Myers-Briggs personality type](https://www.myersbriggs.org/my-mbti-personality-type/mbti-basics/the-16-mbti-types.htm)? (INTP).
- [Enneagram type](https://www.narrativeenneagram.org/tour-the-nine-types/)? (3, and far more useful than Myers-Briggs, in my opinion).

Buzzfeed is still the leading purveyor of these online quizzes, offering insight into, for example, [what kitchen appliance you are based on your food preferences](https://www.buzzfeed.com/catmjohnston/which-kitchen-appliance-are-you-based-on-your-food-8arc2wkfy8). (Microwave, apparently).

Use your knowledge of culture, relationships, and Python to write a program that implements a Buzzfeed-style personality quiz. Your quiz can be about anything that you want, as long as it's your own original implementation.

### AI use

You can use AI freely to help you with this question. Experiment with making your own prompts and using it to fix any problems you encounter. The main challenge is keeping the AI from writing code that's too complex:

1. Think about how AI can help you with this question. Generating the entire program may not actually be that efficient if you have to go back and make edits. Think about using AI selectively to help with particular questions that come up as you're coding.

2. You have to follow the program format I give you below. Don't let the AI make up a completely different approach.

3. I'll reject solutions that use major Python features we haven't talked about in class. In particular, `def` statements, loops, and lists or other data structures.

4. Keep a log of your interactions with AI. For each interaction, record the prompt, the AI's output, and your response to that output (how you evaluated and used it). I want to see evidence of critical engagement with the AI. If the AI's response is good, state how you know that it's good.

### Quiz design

There are a number of ways to implement online quizzes. We're going to use the approach described in [this article](https://www.buzzfeed.com/annakopsky/everything-you-need-to-know-to-make-a-buzzfeed-personality). First, determine the title and "hook" for your quiz. What's it going to be about? Then decide on 3-6 outcomes that will be the results the user sees at the end.

Each possible answer in your quiz will correspond to one of your 3-6 final outcomes. Each time the user answers a question, assign a point to the associated outcome. At the end of the quiz, pick the final outcome with the most total points.


### Starting code

Use the program below as a starting point. Create your own theme, choose 3-6 possible outcomes, then write **at least five** questions.

The final step determines the most popular choice and prints the associated output. Think about how you want to handle ties: You could break them arbitrarily by just selecting one outcome, or you could let a tie represent a distinct output.

```
"""
What X are you?
"""

# Declare variables for each outcome


# Print the first question


# Read the answer and assign a point to its associated variable


### Repeat for at least four more questions


# When you get to the end of the questions, determine which variable has the
# max score and use it to print the output message
#
# Think about how you want to handle ties

```

### Answer scoring

My son Scott likes snakes, so let's make a *Which deadly Australian snake are you?* quiz. There will be four outcomes, [sourced from Wikipedia](https://en.wikipedia.org/wiki/Snakes_of_Australia):

- Tiger snake
- Taipan
- Death adder
- Bandy-bandy

At the beginning of the program, create four variables, one for each outcome:

```
tiger_snake_score = 0
taipan_score = 0
death_adder_score = 0
bandy_bandy_score = 0
```

Each question offers the user a menu of answers, where each choice maps to one of the outcomes. For example,
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
elif choice == 4:
    tiger_snake_score += 1
else:
    print('That\'s not an option.')
    # Don't quit; continue without scoring a point
```
Notice that `+= 1` is a standard shortcut to add one to a variable. It's equivalent to writing
```
death_adder_score = death_adder_score + 1
```
The `else` block prints an error, but the program then continues without quitting. The user doesn't get a point for the incorrectly answered question.



## 

