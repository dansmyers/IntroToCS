# Final Project

## Due December 10 (day after final exams end)

## Description

This is it, the final project.

**Make anything you want**, as long as it's awesome and uses the Python features that we've learned over the course of the semester. Most of you will probably want to make some sort of game, but note that isn't required. I have some ideas for you at the end of the document.

## Groups

**If you choose**, you may work in a group of up to three people to complete your project. If you do choose to work with others,

- You may write code collaboratively with other members of your group, but remember to pay attention to the guidelines below on acceptable use of resources.
- It's not required, but if you work in a group it would be cool to undertake a more ambitious project worthy of your combined efforts.

## Requirements

1. Awesomeness.

2. Uses basic features of Python: variables, loops, conditional statements, and functions. Almost any reasonably complex program is going to satisfy these requirements. If your program doesn't include most of these features then it might be too simple. **You must include at least one instance of each of these features**.
   
3. Uses at least one advanced data organization feature: a list, a class, or a dictionary. I'm not requiring any particular number of these, because the best choice depends on the nature of your program.
   
4. Demonstrates good programming style (indentation, variable names) and includes descriptive comments explaining what's happening in the program.

5. You may also create a project that uses front-end web development techniques instead of Python. If you do this, you have to include a combination of HTML, CSS, and JavaScript features, with some non-trivial interactive behavior. It's not enough to build a mostly static website.
   
## Grading

Complete your project in the workspace on repl.it. I'll run your program and look at the source code. I'll be checking:

1. Does it work? I want to see something that could be considered a complete working program, not an incomplete fragment. It's better to turn in a complete, working program that you know could be improved than an ambitious but unfinished one.

2. Does it use the features of Python that we've discussed? Follow the guidelines given above.

3. Does it follow good coding style, as we've used in class and in
  labs?

## Acceptable Use of Resources

It is acceptable to use the Internet to get ideas and figure out how to implement features you need for your projects. However, **the work you submit must be your own original creation**, or in the case of a group collaboration, your group's original creation. Copying another program and presenting it as your own is unacceptable and will result in automatic failure and a potential Honor Code violation.

**It is acceptable** to research solutions to programming problems and incorporate them into your code. For example, if you need to convert a string to a list, you could look up how to to do that and then use the solution you find. That's an acceptable use of documentation. You **don't** need to provide citations for basic language features or solutions like these.

## Tips

- **Start early**! Don't wait until the last minute!

- Start with the simplest idea that could work, get it to work, then build up from there. It's better to have a complete program that does
what it's supposed to do than an ambitious but incomplete idea. Develop incrementally and test as you go!

- Use our previous examples. They illustrate many different concepts that could be useful for your own programs.

## Ideas

### Web-Based Quiz

Prompt the user to answer a few question (look at the radio buttons from the meme generator), then trigger some JS code that gets the answers and produces an output message.

This requires a little bit of front-end work to put the page together, but it can all be done by copying and modifying our earlier examples.

### Digits of π

Do some research to learn how to write a program that can calculate the digits of π. Write your own Python implementation.

### Ancient Algorithms

Look up some ancient techniques for things like multiplication, division, square roots, and other math operations. Write a library of your own implementations.

### Data Projects

If you would prefer to answer a data question, you can find a data set, load it into Pandas, and produce a graph answering your question. Take a look at [this challenge project from the DTA class](https://github.com/dansmyers/DataScienceAndAnalytics/blob/master/Challenge-Projects/1-Make_a_Graph.md) for some tips. If you take this approach, you don't have to write a "report," but do provide a summary of the question, your data source, and an interpretation of the plot that answers the question.

### 24.a2 Game

If you completed the third challenge project, you might want to try making another game using the 24.a2 framework.

### Hangman

Classic word game. There are lots of different ways to implement it. Make sure that you're choosing the word from a random pool.

There are many versions of this and other traditional pen and paper games floating around on the Internet. **Do not submit someone else's code as you own**. Trust me: I will know. **I always know**.

### Pig

A classic game played with one die. The object is to be the first player to accumulate 100 total points. On your turn, roll the die.

- If you roll a 1, your turn ends immediately and you earn no points.

- If you roll any other number, add it to your points for this turn.

- You can then choose to either end your turn and add your accumulated points to your total score, or roll again to try and accumulate
more points for the turn.

- You can keep rolling as many times as you want to accumulate points before ending your turn, but if you roll a 1 your turn ends
immediately and you score no points for this turn. The strategy of Pig is trading off the risk of rolling a 1 vs. the benefit
of rolling repeatedly to get as many points as possible.
