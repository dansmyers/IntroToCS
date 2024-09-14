# Strachey's Love Letter Algorithm

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/The_Love_Letter_E10722.jpg/1090px-The_Love_Letter_E10722.jpg" width="400px" />

*The Love Letter*, François Boucher (1750)

## Overview

Christopher Strachey was an early British computer programmer. Born in 1916, he attended Cambridge at the same time as Alan Turing, the father of computer science. Strachey did not do well in his studies and took an industry position after graduation where he became interested in emerging computing technologies.

Strachey began programming in the 1950s. He wrote a program to play checkers that may have been the first video game. He also created the first computer music program (it played "God Save the Queen"). He went on to do pioneering work in a number of areas of computer science, including developing the concept of [time-sharing in operating systems](https://en.wikipedia.org/wiki/Time-sharing), which turned out to be a big deal.

The Love Letter Algorithm dates from 1952. It was a program that could automatically compose love letters, for certain definitions of "love" and "letters", and perhaps the earliest example of computer-generated literature. [Wikipedia records the following example](https://en.wikipedia.org/wiki/Strachey_love_letter_algorithm),
> Darling Sweetheart,
>
>You are my avid fellow feeling. My affection curiously clings to your passionate wish. My liking yearns for your heart. You are my wistful sympathy: my tender liking.
>
>Yours beautifully
>
>M. U. C.

Write a program that can produce randomized love letters with the following format:

- An opening, generated randomly.
- A paragraph of least three sentences. Decide on the general format of each sentence, then choose random adjectives, nouns, and other words to fill in the structure.
- A closing, again generated randomly.

## AI Use

You can use AI freely to help you write this program.

- As in the last program, think about the complexity of the AI's code. There are many ways to make this program more complicated and the AI will probably try to do them unless you carefully exclude them. Don't turn in a solution that uses feature we haven't talked about yet.

- You get to make a lot of choices for this program, so make them! Don't outsource your creativity to the AI!

- Keep a log document where you record all of your prompts, responses, and your reflections and iterations.

## Making Choices

Use `randint` and `if-elif-else` statements to make your random choices. For example, to pick your salutation, you might do the following:

```
### Construct the salutation

# Choose an adjective
r = randint(1, 3)
if r == 1:
  opening_adj = 'Darling'
elif r == 2:
  opening_adj = 'Whimsical'
else:
  opening_adj = 'Paradoxical'

# Choose a noun
r = randint(1, 2)
if r == 1:
  opening_noun = 'Moonbeam'
else:
  opening_noun = 'Floret'

# Print
print(f'{opening_adj} {opening_noun},')
print()  # blank line 
```

Use a similar approach for the sentences. Decide in advance on a format for the first sentence, with blanks that you'll fill in with randomly chosen words. You can pick your own choices. Repeat for at least three total sentences, each with its own format and at least three randomized words.

## Thoughts to Think

Once you've finished, think about the structure of this program. It's kind of repetitive, isn't it? Also, the `if`-`elif`-`else` structure, while convenient, doesn't really scale; it's hard to work with more than about five branches at a time. We're going to address these problems gradually:

- Functions and loops will allow us to avoid repeating nearly-identical blocks of code over and over again

- Lists will allow us to manage and select from arbitrarily-long sequences of data; for example, we could have a list with dozens of adjectives and select random items to fill the letter

