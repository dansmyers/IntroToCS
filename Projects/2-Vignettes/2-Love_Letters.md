# Strachey's Love Letter Algorithm

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/The_Love_Letter_E10722.jpg/1090px-The_Love_Letter_E10722.jpg" width="400px" />

*The Love Letter*, François Boucher (1750)

## Overview

Christopher Strachey was an early British computer programmer. Born in 1916, he attended Cambridge at the same time as Alan Turing, the father of computer science. Strachey did not initially excel in his studies and took an industry position after graduation where he then became interested in emerging computing technologies.

Strachey began programming in the 1950s. He wrote a program to play checkers that may have been the first video game and also created one of the first computer music programs (it played "God Save the Queen"). He went on to do pioneering work in a number of areas of computer science, including developing the concept of [time-sharing in operating systems](https://en.wikipedia.org/wiki/Time-sharing), which turned out to be a big deal. He finished his career as a professor at Oxford.

The Love Letter Algorithm dates from 1952. It was a program that could automatically compose love letters (for certain definitions of "love" and "letters") and perhaps the earliest example of computer-generated literature. [Wikipedia records the following example](https://en.wikipedia.org/wiki/Strachey_love_letter_algorithm),
> Darling Sweetheart,
>
>You are my avid fellow feeling. My affection curiously clings to your passionate wish. My liking yearns for your heart. You are my wistful sympathy: my tender liking.
>
>Yours beautifully
>
>M. U. C.

More details are in [this article](https://www.newyorker.com/tech/annals-of-technology/christopher-stracheys-nineteen-fifties-love-machine) by Siobhan Roberts. "M.U.C." stands for "Manchester University Computer", as in *the* computer, because the university only had one.

Write a program that can produce randomized love letters with the following format:

- A salutation, generated randomly.
- A paragraph of least three sentences. Decide on the general format of each sentence, then choose random adjectives, nouns, and other words to fill in the structure.
- A closing, again generated randomly.

It's not required, but I think it's more fun if your letters have a theme and some personality, rather than using generic romance words.

## AI Use

You can use AI freely to help you write this program.

- As in the last program, think about the complexity of the AI's code. There are many ways to make this program more complicated, which the AI will probably try unless you carefully exclude them. Don't turn in a solution that uses feature we haven't talked about yet.

- You get to make a lot of choices for this program, so make them! Don't outsource your creativity to the AI!

- Keep a log document where you record all of your prompts, responses, and your reflections and iterations.

## Making Choices

Use `randint` and `if-elif-else` statements to make your random choices. For example, to pick your salutation, you might do the following (with your own choices in place of mine):

```
### Construct the salutation

# Choose an adjective
r = randint(1, 3)
if r == 1:
  opening_adj = 'Incomprehensible'
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

## Automate

**After you've finished your version of the program** (not before), prompt an AI to generate a complete implementation of the Love Letter Algorithm, with no restrictions on the structure. Record your prompt and the AI output in your log document.

Verify that the AI's program works. If it doesn't, fix any errors manually, or prompt it to revise. Prompt it to make any changes that you want in the output.

Then consider the AI's output. How does it compare to yours? Give your thoughts on what the AI program is doing. If there are parts you don't understand yet, that's okay, just note that and try to think about them based on the context given by the rest of the code.

## Thoughts to Think

Once you've finished, think about the structure of this program. It's kind of repetitive, isn't it? Also, the `if`-`elif`-`else` structure, while convenient, doesn't really scale; it's hard to work with more than about five branches at a time. We're going to address these problems over the next few weeks:

- Functions and loops will allow us to avoid repeating nearly-identical blocks of code over and over again

- Lists will allow us to manage and select from arbitrarily-long sequences of data; for example, we could have a list with dozens of adjectives and select random items to fill the letter
